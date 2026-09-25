# FDU-SC AI Lecture

Slide decks from the Fudan University supercomputing team's AI lecture series,
as a [Slidev](https://sli.dev) workspace.

## Decks

| Deck | Title | Slides | Author |
| --- | --- | --- | --- |
| [`plateaus-to-paradigms`](slides/plateaus-to-paradigms/) | *From Plateaus to Paradigms: A History of AI and Our Future* | 88 | Zecyel |
| [`theory-of-computation`](slides/theory-of-computation/) | *Theory of Computation: From Lambda Calculus to Computer Application Practice* | 41 | Zecyel |
| [`competition-101`](slides/competition-101/) | 关于竞赛这件事 —— 给判据，不给结论 | 16 | Zecyel |

## Running it

```bash
pnpm install
pnpm dev       # the workspace preview app
pnpm build     # builds every deck plus the preview app into dist/
```

To run a single deck with its own dev server instead of the workspace shell:

```bash
cd slides/plateaus-to-paradigms
pnpm dev
```

## Layout

```
.
├── package.json              workspace scripts (dev / preview / build)
├── pnpm-workspace.yaml       slides/* are packages
├── slidev-workspace.yaml     baseUrl for the deployed site
├── .github/workflows/        builds and deploys to GitHub Pages
├── scripts/publish.mjs       publishes a notes-free copy
└── slides/
    └── plateaus-to-paradigms/
```

Each deck is a normal Slidev project: `slides.md`, plus `pages/`, `public/`,
`components/`, `style.css` and its own `package.json` where a deck needs them.

`theory-of-computation` is a single-file deck, migrated from
[AIxMath/Lecture-TOC](https://github.com/AIxMath/Lecture-TOC), which is MIT
licensed — the licence is kept alongside it at
`slides/theory-of-computation/LICENSE`. Its cover background was an external
link to `aixmath.org` that now 404s; the image is vendored into the deck's
`public/` so the deck is self-contained.

The deployed site is <https://slides.fdu.sc/>, with a
preview page listing every deck at the root and each deck under its own path.

`competition-101` is a Chinese deck, and the only one whose typography needed
its own `style.css`: seriph's defaults are tuned for Latin (17.6px body, ~1.36
line-height), which is too small and too tight for Chinese. It sets 19.2px /
1.75 and pins the CJK font explicitly rather than relying on fallback, so the
layout is reproducible rather than machine-dependent. Its figures also set
matplotlib's font family — the default DejaVu Sans has no CJK glyphs, so a
chart would otherwise export as tofu boxes, *and* the tight bounding box would
be computed from the wrong glyph widths.

`slidev-workspace.yaml` sets `baseUrl: "/"`, because the site is served from
a custom domain (`slides.fdu.sc`) and decks therefore live at `/<deck>/`
rather than at `/<repo>/<deck>/`. Setting it back to a repository prefix is
the one change that would break every asset on the deployed site — the charts
404'd that way once already, for the same underlying reason.

It also means `dist/` cannot be served from a bare local root; mirror the
deployed layout instead:

```bash
mkdir -p /tmp/serve && ln -sfn "$PWD/dist" /tmp/serve/fdusc-ai-lecture
cd /tmp/serve && npx http-server . -p 8080
# open http://127.0.0.1:8080/fdusc-ai-lecture/
```

## Presenter notes

The published decks carry no speaker notes. The working copy they are
published from does, and `scripts/publish.mjs` strips them into a temporary
tree and pushes that with a fresh history, so they are not recoverable from
this repository — not from the working tree and not from an old commit.
