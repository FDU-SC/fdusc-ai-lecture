# FDU-SC AI Lecture

Slide decks from the Fudan University supercomputing team's AI lecture series,
as a [Slidev](https://sli.dev) workspace.

## Decks

| Deck | Title | Slides |
| --- | --- | --- |
| [`plateaus-to-paradigms`](slides/plateaus-to-paradigms/) | *From Plateaus to Paradigms: A History of AI and Our Future* | 88 |

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

Each deck is a normal Slidev project: `slides.md` plus `pages/`, `public/`,
`components/`, `style.css` and its own `package.json`.

The deployed site is <https://fdu-sc.github.io/fdusc-ai-lecture/>, with a
preview page listing every deck at the root and each deck under its own path.

## Figures

Every chart in the deck is generated, not drawn.
`slides/plateaus-to-paradigms/scripts/make_charts.py` rebuilds all of them, in
both a light and a dark variant, from the data inlined in that script. Most are
computed rather than sketched — gradient descent is actually run, the
bias-variance curve is an actual experiment, the Hopfield panel is an actual
network settling, and the roofline uses real H100 specifications.

## Checks

`slides/plateaus-to-paradigms/scripts/verify.mjs` drives a headless browser
and fails on: content that overflows the slide canvas, chart labels that
collide or fall outside the frame, the wrong figure variant showing in dark
mode, text painted on top of other text, a `---` glued to the end of a line
(which silently merges two slides), and any slide carrying two presenter-note
comments where Slidev keeps only the last.

```bash
cd slides/plateaus-to-paradigms
node scripts/verify.mjs
```

## Presenter notes

The published decks carry no speaker notes. The working copy they are
published from does, and `scripts/publish.mjs` strips them into a temporary
tree and pushes that with a fresh history, so they are not recoverable from
this repository — not from the working tree and not from an old commit.
