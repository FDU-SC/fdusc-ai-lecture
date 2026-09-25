#!/usr/bin/env node
/**
 * Layout verification for this deck.
 *
 * Slidev will happily let content overflow the 980x552 canvas and clip it
 * silently, and matplotlib will happily let chart labels collide. Neither is
 * visible without opening the deck, so this script measures both:
 *
 *   1. every slide — is any content below the canvas edge?
 *   2. every chart  — do any two text labels overlap, or fall outside the frame?
 *
 * It builds the deck, serves dist/ on a scratch port, drives a headless
 * Chromium, and exits non-zero if anything fails.
 *
 * Usage:  node scripts/verify.mjs            # build, serve, check
 *         node scripts/verify.mjs --no-build # reuse the existing dist/
 */

import { chromium } from 'playwright-chromium'
import { spawn, execSync } from 'node:child_process'
import { createRequire } from 'node:module'
const require = createRequire(import.meta.url)
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'

const ROOT = path.resolve(import.meta.dirname, '..')
const BUILD = !process.argv.includes('--no-build')

// Pick a free port per run. A hard-coded port means a leftover server from a
// previous run keeps the number, this process fails to bind, and the browser
// silently measures the STALE build on that port — which reads as a content
// failure and wastes a debugging round. Verify the port is actually free.
async function freePort() {
  const net = require('node:net')
  for (let i = 0; i < 40; i++) {
    const p = 8800 + Math.floor(Math.random() * 900)
    // listen() is asynchronous: a port that is already taken does not throw
    // here, it emits 'error' on a later tick. So the probe has to await the
    // callback and the error event, or it always reports the port as free.
    const free = await new Promise(resolve => {
      const srv = net.createServer()
      srv.once('error', () => resolve(false))
      srv.listen(p, '127.0.0.1', () => srv.close(() => resolve(true)))
    })
    if (free) return p
  }
  throw new Error('no free port found')
}

// A slide fits if nothing reaches the bottom edge; charts may not have any two
// labels overlapping by more than this fraction of the smaller label's box.
const MIN_SLACK_PX = 8
const OVERLAP_TOLERANCE = 0.15

const die = (msg) => { console.error(`\n  ${msg}\n`); process.exit(1) }

// ------------------------------------------------------------------ slide count
/** Count slides the way Slidev does: `---` separators, plus `---`-delimited
 *  per-slide frontmatter which counts once rather than twice. */
function countSlides() {
  const fmRe = /^[A-Za-z_][\w-]*\s*:/
  const count = (text) => {
    const lines = text.split('\n')
    let i = 0
    if (lines[0]?.trim() === '---') {
      i = 1
      while (i < lines.length && lines[i].trim() !== '---') i++
      i++
    }
    const body = lines.slice(i)
    let n = 1
    for (let j = 0; j < body.length; j++) {
      if (body[j].trim() !== '---') continue
      let k = j + 1
      const fm = []
      while (k < body.length && body[k].trim() !== '---') fm.push(body[k++])
      const isFrontmatter = k < body.length && fm.length > 0 &&
        fm.every(l => fmRe.test(l) || !l.trim() || l.startsWith(' '))
      if (!isFrontmatter) n++
      else { n++; j = k }
    }
    return n
  }
  const pages = fs.readdirSync(path.join(ROOT, 'pages')).map(f => `pages/${f}`)
  const total = pages.reduce((a, f) => a + count(fs.readFileSync(path.join(ROOT, f), 'utf8')), 0)
  return total + 1 // + the title slide in slides.md
}

// ------------------------------------------------------------------ build + serve
// Build and serve under the SAME sub-path the workspace deploy uses. The site
// is on a custom domain, so a deck is deployed at /<deck>/.
//
// Building with the default base '/' and serving dist at the root makes every
// root-absolute URL resolve, so a path that is wrong for the deployed
// sub-path still works here and the bug stays invisible. That is exactly how
// every chart shipped 404: components/Chart.vue asked for `/charts/x.svg`
// while the deployed deck lives at /<workspace>/<deck>/.
const DECK = path.basename(ROOT)
const BASE = `/${DECK}/`

if (BUILD) {
  console.log('building ...')
  execSync(`npx slidev build --out dist --base ${BASE}`, { cwd: ROOT, stdio: 'pipe' })
}
if (!fs.existsSync(path.join(ROOT, 'dist'))) die('no dist/ — run without --no-build first')

const PORT = await freePort()
// http-server has no way to mount dist at a sub-path, so serve a scratch
// parent directory in which the build appears under the deck's name.
const SERVE = fs.mkdtempSync(path.join(os.tmpdir(), 'deck-verify-'))
fs.symlinkSync(path.join(ROOT, 'dist'), path.join(SERVE, DECK), 'dir')
const server = spawn('npx', ['http-server', SERVE, '-p', String(PORT), '-c-1', '--silent'],
  { cwd: ROOT, stdio: 'ignore' })
process.on('exit', () => server.kill())
// Wait for the server to actually answer rather than sleeping a fixed amount:
// if it never binds, every later check fails with "no current slide", which
// says nothing about why.
const base0 = `http://127.0.0.1:${PORT}${BASE}`
let up = false
for (let i = 0; i < 40; i++) {
  try { const r = await fetch(base0 + '/'); if (r.ok) { up = true; break } } catch {}
  await new Promise(r => setTimeout(r, 250))
}
if (!up) die(`the preview server never came up on port ${PORT}`)

// ------------------------------------------------------------------ checks
const TOTAL = countSlides()
const charts = fs.readdirSync(path.join(ROOT, 'public/charts')).filter(f => f.endsWith('.svg'))
const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } })
const base = base0

let failures = 0

// 1. slide overflow, measured in BOTH colour schemes.
//
// The deck is presented in dark mode, and figures are swapped by CSS on the
// `.dark` class. So a slide that fits in light mode can still break in dark —
// and a chart that renders in light mode can be the invisible variant in dark.
// Both passes are mandatory.
async function checkSlides(mode) {
  await page.evaluate(dark => {
    document.documentElement.classList.toggle('dark', dark)
  }, mode === 'dark')
  await page.waitForTimeout(300)

  let localFailures = 0
  console.log(`\nslides, ${mode} mode (${TOTAL})`)
  await page.goto(`${base}/#/1`, { waitUntil: 'networkidle' })
  await page.waitForTimeout(900)
  if (await page.evaluate(() => document.querySelectorAll('.slidev-page').length) === 0) {
    const errs = []
    page.on('requestfailed', r => errs.push(r.url()))
    die('the deck did not mount: no .slidev-page elements. ' +
        'Most likely the build references a base path this server does not serve ' +
        '(check slidev-workspace.yaml baseUrl against how dist/ is being served).')
  }
  await page.evaluate(dark => {
    document.documentElement.classList.toggle('dark', dark)
  }, mode === 'dark')

  for (let i = 1; i <= TOTAL; i++) {
    await page.evaluate(n => { window.location.hash = '#/' + n }, i)
    await page.waitForTimeout(420)
    const r = await page.evaluate(dark => {
      document.documentElement.classList.toggle('dark', dark)
      const cur = [...document.querySelectorAll('.slidev-page')]
        .find(e => getComputedStyle(e).display === 'block')
      if (!cur) return { err: 'no current slide' }
      const lay = cur.querySelector('.slidev-layout') || cur.firstElementChild
      const cb = cur.getBoundingClientRect()
      const scale = cb.height / cur.clientHeight
      let low = -Infinity, where = ''
      lay.querySelectorAll('*').forEach(el => {
        if (el.children.length) return
        const bb = el.getBoundingClientRect()
        if (bb.width && bb.height && bb.bottom > low) {
          low = bb.bottom
          where = `${el.tagName} ${(el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 46)}`
        }
      })

      // every chart <img> in this slide must load, and in a themed slide exactly
      // one variant of each figure must be visible
      const imgs = [...cur.querySelectorAll('img')]
      const broken = imgs.filter(im => !(im.complete && im.naturalWidth > 0)).length
      const badSrc = imgs.filter(im => !(im.complete && im.naturalWidth > 0))
        .map(im => im.getAttribute('src')).slice(0, 3)
      const themed = cur.querySelectorAll('.chart-swap')
      let swapBad = 0
      const swapWhy = []
      themed.forEach(sw => {
        const shown = [...sw.querySelectorAll('img')]
          .filter(im => getComputedStyle(im).display !== 'none')
        // not just "exactly one" — it must be the variant matching the mode,
        // otherwise a dark-mode talk shows the invisible light figure
        const want = dark ? '-dark' : ''
        const got = shown.map(im => (im.getAttribute('src') || '')).join(',')
        const ok = shown.length === 1 && got.endsWith(`${want}.svg`)
        if (!ok) { swapBad++; swapWhy.push(`want${want || '-light'} got[${got}] n=${shown.length}`) }
      })

      // Text that paints on top of other text. The theme hard-codes several
      // line-heights in rem, so a large font can sit in a line box far smaller
      // than its glyphs and collide with the line below while the boxes look
      // fine. Comparing per-line client rects catches that. Multi-line inline
      // elements need getClientRects(), not getBoundingClientRect(), or one
      // <em> spanning two lines looks like a collision with everything.
      const items = []
      for (const el of cur.querySelectorAll('h1,h2,h3,h4,span,li,td,th,p,blockquote,strong,em,code')) {
        if (el.children.length) continue
        const t = (el.textContent || '').trim()
        if (t.length < 2) continue
        for (const rc of el.getClientRects()) {
          if (rc.width > 3 && rc.height > 3) items.push({ t, el, rc })
        }
      }
      const overlaps = []
      if (items.length <= 500) {
        for (let a = 0; a < items.length; a++) for (let k = a + 1; k < items.length; k++) {
          const A = items[a], B = items[k]
          if (A.el === B.el || A.el.contains(B.el) || B.el.contains(A.el)) continue
          const ox = Math.min(A.rc.right, B.rc.right) - Math.max(A.rc.left, B.rc.left)
          const oy = Math.min(A.rc.bottom, B.rc.bottom) - Math.max(A.rc.top, B.rc.top)
          if (ox <= 3 || oy <= 1) continue
          const sm = Math.min(A.rc.width * A.rc.height, B.rc.width * B.rc.height)
          if (sm > 0 && (ox * oy) / sm > 0.05) {
            overlaps.push(`"${A.t.slice(0, 22)}" over "${B.t.slice(0, 22)}" (${oy.toFixed(0)}px)`)
          }
        }
      }

      return {
        title: cur.querySelector('h1')?.innerText.replace(/\s+/g, ' ').slice(0, 46) || '(divider)',
        clipped: cur.scrollHeight - cur.clientHeight,
        slack: Math.round((cb.bottom - low) / scale),
        brokenImg: broken > 0,
        badSrc,
        swapBad,
        swapWhy,
        where,
        overlaps: [...new Set(overlaps)].slice(0, 3),
      }
    }, mode === 'dark')
    if (r.err) { console.log(`  XX ${i}: ${r.err}`); localFailures++; continue }
    const textOverlap = mode === 'light' && r.overlaps.length > 0
    const bad = r.clipped > 6 || r.slack < MIN_SLACK_PX || r.brokenImg || r.swapBad > 0 || textOverlap
    if (bad) {
      localFailures++
      console.log(`  XX ${String(i).padStart(2)}  clipped=${r.clipped} slack=${r.slack}` +
        `${r.brokenImg ? ' IMAGE-FAILED' : ''}${r.swapBad ? ` SWAP-BAD(${r.swapBad})` : ''}` +
        `${textOverlap ? ' TEXT-OVERLAP' : ''}  ${r.title}`)
      if (r.swapWhy && r.swapWhy.length) console.log(`        swap: ${r.swapWhy.join(' | ')}`)
      if (r.badSrc && r.badSrc.length) console.log(`        broken img src: ${r.badSrc.join(' | ')}`)
      if (textOverlap) r.overlaps.forEach(o => console.log(`        overlap: ${o}`))
      console.log(`        bottom-most: ${r.where}`)
    }
  }
  if (!localFailures) console.log(`  ok — all ${TOTAL} slides fit, figures swapped correctly` +
    (mode === 'light' ? ', no text overlaps' : ''))
  return localFailures
}

failures += await checkSlides('light')
failures += await checkSlides('dark')

// 3a. malformed frontmatter fences. A `---` glued onto the previous line (e.g.
//     `layout: center---`) is not a fence, so the slide boundary disappears and
//     two slides silently merge into one — the slide count then looks plausible
//     while the deck is wrong. Cheap to check, expensive to notice.
{
  const pageFiles = fs.readdirSync(path.join(ROOT, 'pages')).map(f => `pages/${f}`)
  let bad = 0
  for (const f of [...pageFiles, 'slides.md']) {
    fs.readFileSync(path.join(ROOT, f), 'utf8').split('\n').forEach((line, i) => {
      const t = line.trimEnd()
      if (t.endsWith('---') && t !== '---' && !t.startsWith('|')) {
        bad++
        console.log(`  XX ${f}:${i + 1}: fence glued to content -> ${JSON.stringify(t.slice(-30))}`)
      }
    })
  }
  console.log(`\nslide boundaries`)
  console.log(bad ? '' : '  ok — every fence is its own line')
  failures += bad
}

// 3b. presenter notes: Slidev uses only the LAST comment in a slide, so two
//    adjacent comments silently drop the first one.
{
  const pageFiles = fs.readdirSync(path.join(ROOT, 'pages')).map(f => `pages/${f}`)
  let bad = 0
  for (const f of pageFiles) {
    const text = fs.readFileSync(path.join(ROOT, f), 'utf8')
    text.split(/\n---\n/).forEach((s, idx) => {
      const n = (s.match(/<!--/g) || []).length
      if (n > 1) {
        bad++
        console.log(`  XX ${f} slide ${idx + 1}: ${n} separate comment blocks ` +
          '(Slidev keeps only the last as the note)')
      }
    })
  }
  console.log(`\npresenter notes`)
  console.log(bad ? '' : '  ok — one note per slide, none silently dropped')
  failures += bad
}


// 2. chart-internal text collisions
console.log(`\ncharts (${charts.length})`)
for (const f of charts) {
  await page.goto(`${base}/charts/${f}`, { waitUntil: 'networkidle' })
  await page.waitForTimeout(150)
  const r = await page.evaluate((tol) => {
    const svg = document.querySelector('svg')
    if (!svg) return { err: 'no svg root' }
    const root = svg.getBoundingClientRect()
    // getBoundingClientRect, not getBBox: matplotlib positions each label in its
    // own <g transform>, so getBBox returns pre-transform coordinates and any
    // cross-label comparison would be meaningless.
    const texts = [...svg.querySelectorAll('text')].map(t => {
      const bb = t.getBoundingClientRect()
      return { s: (t.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 28),
               x: bb.x, y: bb.y, w: bb.width, h: bb.height }
    }).filter(t => t.w > 0.5 && t.h > 0.5 && t.s)
    const hits = []
    for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
      const a = texts[i], c = texts[j]
      const ix = Math.max(0, Math.min(a.x + a.w, c.x + c.w) - Math.max(a.x, c.x))
      const iy = Math.max(0, Math.min(a.y + a.h, c.y + c.h) - Math.max(a.y, c.y))
      const smaller = Math.min(a.w * a.h, c.w * c.h)
      if (smaller > 0 && (ix * iy) / smaller > tol) {
        hits.push(`"${a.s}" ∩ "${c.s}" ${(100 * ix * iy / smaller).toFixed(0)}%`)
      }
    }
    const outside = texts.filter(t =>
      t.x < root.x - 2 || t.y < root.y - 2 ||
      t.x + t.w > root.right + 2 || t.y + t.h > root.bottom + 2).map(t => t.s)
    return { n: texts.length, hits, outside }
  }, OVERLAP_TOLERANCE)
  if (r.err) { console.log(`  XX ${f}: ${r.err}`); failures++; continue }
  if (r.hits.length || r.outside.length) {
    failures++
    console.log(`  XX ${f}  labels=${r.n}`)
    r.hits.slice(0, 6).forEach(h => console.log(`        overlap: ${h}`))
    r.outside.slice(0, 4).forEach(s => console.log(`        outside frame: ${s}`))
  } else {
    console.log(`  ok ${f.padEnd(28)} labels=${String(r.n).padStart(3)}`)
  }
}

await browser.close()
server.kill()
console.log(failures ? `\nFAILED: ${failures} problem(s)\n` : '\nAll checks passed.\n')
process.exit(failures ? 1 : 0)
