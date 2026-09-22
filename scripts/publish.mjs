#!/usr/bin/env node
// Publish a notes-free copy of this workspace to GitHub.
//
// The local working copy keeps its presenter notes — those are the speaker's
// script, and they are the reason the deck is worth giving. What must not
// leave this machine is a copy of them in a public repository.
//
// So this script does not strip anything in place. It copies the workspace to
// a temporary directory, deletes every HTML comment from the deck sources
// there, and pushes that with a *fresh* history. A fresh history matters: if
// the notes had ever been committed, stripping the working tree would still
// leave them recoverable with `git log -p`.
//
//   node scripts/publish.mjs --dry-run     # build the copy, report, stop
//   node scripts/publish.mjs               # build the copy and push
//
// Environment:
//   REMOTE   git remote to push to (defaults to the FDU-SC repo over SSH)
//   BRANCH   branch to push (defaults to main)

import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'

const ROOT = path.resolve(import.meta.dirname, '..')
const REMOTE = process.env.REMOTE ?? 'git@github.com:fdu-sc/fdusc-ai-lecture.git'
const BRANCH = process.env.BRANCH ?? 'main'
const DRY = process.argv.includes('--dry-run')

// never copied into the publish tree
const SKIP = new Set(['.git', 'node_modules', 'dist', '_gh-pages', '.DS_Store'])

const run = (cmd, args, cwd) =>
  execFileSync(cmd, args, { cwd, stdio: ['ignore', 'pipe', 'pipe'] }).toString()

function copyTree(from, to) {
  fs.mkdirSync(to, { recursive: true })
  for (const entry of fs.readdirSync(from, { withFileTypes: true })) {
    if (SKIP.has(entry.name)) continue
    const src = path.join(from, entry.name)
    const dst = path.join(to, entry.name)
    if (entry.isDirectory()) copyTree(src, dst)
    else if (entry.isFile()) fs.copyFileSync(src, dst)
  }
}

// A presenter note is an HTML comment. Every comment in this deck is one — the
// deck's own verification asserts that, so there is nothing else to preserve.
const NOTE = /<!--[\s\S]*?-->[ \t]*\n?/g

function stripNotes(file) {
  const before = fs.readFileSync(file, 'utf8')
  const count = (before.match(NOTE) ?? []).length
  if (!count) return { count: 0, chars: 0 }
  const after = before.replace(NOTE, '').replace(/\n{3,}/g, '\n\n').trimEnd() + '\n'
  fs.writeFileSync(file, after)
  return { count, chars: before.length - after.length }
}

function deckSources(tree) {
  const slidesDir = path.join(tree, 'slides')
  const out = []
  for (const deck of fs.readdirSync(slidesDir)) {
    const dir = path.join(slidesDir, deck)
    if (!fs.statSync(dir).isDirectory()) continue
    const entry = path.join(dir, 'slides.md')
    if (fs.existsSync(entry)) out.push(entry)
    const pages = path.join(dir, 'pages')
    if (fs.existsSync(pages)) {
      for (const f of fs.readdirSync(pages)) {
        if (f.endsWith('.md')) out.push(path.join(pages, f))
      }
    }
  }
  return out
}

// ---- build the publish tree
const tree = fs.mkdtempSync(path.join(os.tmpdir(), 'fdusc-publish-'))
console.log(`publish tree: ${tree}`)
copyTree(ROOT, tree)

let notes = 0
let bytes = 0
for (const file of deckSources(tree)) {
  const r = stripNotes(file)
  notes += r.count
  bytes += r.chars
}
console.log(`stripped ${notes} presenter notes (${(bytes / 1024).toFixed(0)} KB) from ${deckSources(tree).length} files`)

// belt and braces: nothing may remain that looks like a note
const leftover = deckSources(tree).filter(f => fs.readFileSync(f, 'utf8').includes('<!--'))
if (leftover.length) {
  console.error('refusing to publish: comments survived in\n  ' + leftover.join('\n  '))
  process.exit(1)
}

if (DRY) {
  console.log('\n--dry-run: not pushing. Inspect the tree above, then re-run without the flag.')
  process.exit(0)
}

// ---- fresh history, so the notes are not recoverable from the remote
run('git', ['init', '-q', '-b', BRANCH], tree)
run('git', ['add', '-A'], tree)
run('git', ['-c', 'user.name=Zecyel', '-c', 'user.email=zecyel@users.noreply.github.com',
            'commit', '-q', '-m', 'Publish from the local working copy'], tree)
run('git', ['remote', 'add', 'origin', REMOTE], tree)
run('git', ['push', '--force', 'origin', `${BRANCH}:${BRANCH}`], tree)
console.log(`\npushed ${run('git', ['rev-list', '--count', 'HEAD'], tree).trim()} commit(s) to ${REMOTE} (${BRANCH})`)
