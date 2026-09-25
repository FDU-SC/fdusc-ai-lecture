# Lean / mathlib facts, 2024 – Sep 2026

Every URL below was fetched successfully unless explicitly marked NOT VERIFIED. Fetch date for all live pages: 2026-09-16.

## 1. mathlib4 statistics

- https://leanprover-community.github.io/mathlib_stats.html (fetched 2026-09-16): **136,850 definitions; 288,518 theorems; 772 contributors.** The page carries no measurement date of its own; figures are master-at-fetch-time.
- GitHub API https://api.github.com/repos/leanprover-community/mathlib4 (2026-09-16): **487,128 KB repo size; 4,134 stars; 1,688 forks; 3,359 open issues; created 2021-05-09; last push 2026-09-16T14:04:33Z; Apache-2.0.**
- Lines of code ≈ 2 million: "about 2 million lines … over 750 contributors" — https://mathlib-initiative.org/formal-frontier/ ; "approximately 2 million lines" — https://www.math.inc/sphere-packing . Contributor counts differ (750 vs 772) — different counting methods.
- Peer-reviewed: A. Kontorovich, "The Shape of Math To Come", *Proceedings of the ICM 2026, Vol. 2: Plenary Lectures*, pp. 102–123, online 2026-07-13, DOI **10.1137/25m1806764** (verified via https://api.crossref.org/works/10.1137/25m1806764).

## 2. Milestones

- **Liquid Tensor Experiment**: completed 15:46:13 EST Thursday 14 July 2022 (~18 months after Scholze's challenge), announced 2022-07-15 — https://leanprover-community.github.io/blog/posts/lte-final/ (outside the 2024–26 window).
- **FLT**: ImperialCollegeLondon/FLT is still self-described "Ongoing Lean formalisation" (GitHub API 2026-09-16: created 2023-11-19, 1,029 stars, 63 open issues, last push 2026-09-16). Anthropic's 2026 proof builds on it.
- **PFR**: the *mathematics* — Gowers, Green, Manners, Tao, "On a conjecture of Marton", *Annals of Mathematics*, DOI 10.4007/annals.2025.201.2.5, issued 2025-03-01 (Crossref). The *Lean formalization* (teorth/pfr, from arXiv 2311.05762): **no journal/DOI found** — treat as a non-peer-reviewed artifact.
- **Carleson**: 2025-05-27 all blueprint statements formalized, 143/179 results proven, 88 sorries; 2025-07-08 "all tasks … have been claimed" (endgame) — https://leanprover-community.github.io/archive/stream/442935-Carleson/topic/Milestones.html ; final blueprint dated 2026-09-16 — http://florisvandoorn.com/carleson/blueprint/
- **Sphere eversion**: van Doorn, Massot, Nash, "Formalising the h-Principle and Sphere Eversion", CPP '23, published 2023-01-11, pp. 121–134, DOI 10.1145/3573105.3575688. **No 2025 event exists** (the task premise appears wrong).
- **Sphere packing** (the real 2024–26 large project): launched Feb 2024 by Hariharan/Viazovska, made public 13 Jun 2025, AI-completed Feb 2026 (see §4).

## 3. Industry

- **AWS**: Lean powers verification-guided development of Cedar, the open-source authorization language — https://aws.amazon.com/blogs/opensource/lean-into-verified-software-development/ (page fetched; publication date NOT VERIFIED).
- **Lean FRO**: `leanprover.foundation` **DOES NOT RESOLVE** (getaddrinfo ENOTFOUND). Live site: https://lean-lang.org/fro/ ("© 2026 Lean FRO"); roadmap "The Lean FRO Year 4 – Part 1" — https://lean-lang.org/fro/roadmap/y4-1/
- **Funding**: $10M from XTX Markets founder Alex Gerko via Renaissance Philanthropy, 24 Jul 2025 — $5M Lean FRO, $5M Mathlib: https://www.renaissancephilanthropy.org/insights/lean-fro-and-mathlib-receive-10m-from-xtx-markets-founder-alex-gerko-to-further-advance-the-use-of-ai-for-mathematical-research and https://mathlib-initiative.org/formal-frontier/
- **Microsoft Research, Jane Street, Meta, Google, NVIDIA: NOT VERIFIED.**

## 4. AI formalization milestones 2025–26

- **Anthropic, "Formalizing Fermat's Last Theorem", 2026-09-04** — https://www.anthropic.com/research/formalizing-fermats-last-theorem : Claude, ~11 days, largely autonomous, 13M lines of Lean, 30,300 theorems proved (29,500 used in the final proof), proof root read `PROVED` at 02:00:57Z on 18 Aug 2026; uses only Lean's three standard axioms; a comparator confirmed the statement matches Mathlib's own FLT statement; Kevin Buzzard reviewed. Code: https://github.com/anthropics/fermats-last-theorem . Also: Vinogradov's Three Primes Theorem formalized in 3 days by agents on consumer plans; Prove2Me platform paper DOI 10.48550/arXiv.2608.28433.
- **Math, Inc "Gauss"**: completed Viazovska's sphere packing in dimensions 8 (5 days) and 24 (2 weeks), Feb 2026; 70k → ~200k lines (peak 500k); funded partly by DARPA expMath; maintainers verified definitions unmodified, standard axioms only, ran lean4checker — https://www.math.inc/sphere-packing and https://leanprover-community.github.io/blog/posts/SpherePacking-1/ (2026-03-02).
- **Harmonic's Aristotle** filled sphere-packing `sorry`s from late Oct 2025 (same blog post).
- **Caveat on machine-checked claims**: Lean bug #14684 (all stable versions ≤ 4.33.1, fixed in v4.34.0-rc1) let `native_decide` forge a fake FLT "proof"; explicitly not a kernel soundness issue and unrelated to Anthropic's proof — https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/

## COULD NOT VERIFY

- mathlib dependency count (lakefile fetch failed repeatedly).
- PFR formalization journal/DOI (none found in Crossref or search).
- Lean FRO founding date and initial funders.
- Exact Carleson completion date/announcement.
- amazon.science FRO investment post (repeated fetch timeouts); Sloan grant page (HTTP 403).
- Microsoft Research, Jane Street, Meta, Google (AlphaProof), NVIDIA Lean activity.
- "Sphere Eversion project (2025)" — no such milestone found; correct date is 2022 completion / CPP '23 paper.
