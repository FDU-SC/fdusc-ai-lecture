---
layout: center
---

<div h-20 />

<div text-center text-6xl>
<span color-gray>Act II</span>
</div>

<div h-3 />

<div text-center text-4xl>
Right Now
</div>

<div h-3 />

<div text-center text-2xl color-gray>
2026
</div>

<div h-20 />
---

# Three Years, Three IMO Results

<div h-2 />

| Year | System | Result | How it was graded |
| --- | --- | --- | --- |
| **2024** | AlphaProof + AlphaGeometry | **4 of 6** — silver standard | Problems hand-translated into Lean; RL inside the proof assistant |
| **2025** | Gemini Deep Think, and separately an OpenAI reasoning model | **35 / 42** — gold standard | Official IMO graders; natural language; no tools; inside the contest time limit |
| **2026** | Xiaohongshu `dots-note-3.0` | **42 / 42** — perfect | Reported as official IMO grading; problems released only after the human exam |

<div h-2 />

For context: in 2025, 72 humans won gold and 5 scored a perfect 42.

---

# AI for Mathematics: The Long Arc

<div h-3 />

Machines have been doing mathematics since before they could do anything else — because mathematics is the one domain with a **checker**.

<div h-3 />

| Year | Milestone | Why it lasted |
| --- | --- | --- |
| 1968 | **Automath** — machine-checkable mathematics | Introduced the trusted kernel |
| 1972–79 | **Edinburgh LCF** — kernel, tactics, a metalanguage | The architecture Lean still uses |
| 1973 | **Mizar** begins the first machine-readable mathematics library | Libraries, not just proofs |
| 1996 | **EQP** resolves the Robbins conjecture | The first machine result mathematicians adopted |
| 2005 / 2013 | **Four Colour Theorem**, then **Odd Order** in Coq | Scale became possible |
| 2014 | **Flyspeck** completes the Kepler conjecture | A decade-long formalization finished |
| 2022 / 2023 | **AlphaTensor**, then **FunSearch** | Machines start *finding* mathematics, not just checking it |

---

# What Actually Happened in 2026

<div h-2 />

| Date | Event | Evidence |
| --- | --- | --- |
| Feb | **M2F** (Peking University) formalises a 479-page document into 153,853 lines of Lean | Artifact public |
| Mar | **SorryDB** turns 78 real Lean projects into a nightly-refreshed benchmark | Artifact public |
| May | **OpenAI disproves the Erdős unit-distance conjecture** | Independently verified |
| May | **AlphaProof Nexus** solves **9 of 353** open Erdős problems | 2.5% of those attempted |
| Jul | **AIMO Proof Pilot** — fully open models, expert-graded proofs | 29/42 vs 1/42 before |
| Aug | **Claude improves a long-standing lower bound for the Riemann zeta function** | Independently replayed |
| Sep | **Fermat's Last Theorem formalised in Lean** — 13M lines, 30,300 theorems | Independently replayed |
| Sep | **OpenAI claims a Navier–Stokes proof** | Machine-checked; **credit disputed** |

---

# The Benchmark Disagreement of the Week

<div h-3 />

Two well-known evaluators scored the same September model, and disagreed by more than a hundred points.

<div h-3 />

<div class="grid grid-cols-2 gap-10 text-center">

<div>

### Epoch AI

**169** — ranked **first of 267 models**

</div>

<div>

### Artificial Analysis

**61** — level with the previous generation, and **below** the current leader at 66

</div>

</div>

<div h-3 />

### Why this keeps happening

<div h-3 />

- **Different harnesses.** How you prompt, how many attempts you allow, and what tools you permit change scores by tens of points.
- **Different task mixes.** An index that weights coding heavily will rank a coding-strong model first.
- **Vendor-reported numbers.** Several releases in September were revised, in one case more than once, after publication.

---

# One Model, Two Verified Scores

<div h-2 />

<div class="grid grid-cols-2 gap-8">

<div>

<Chart name="harness-effect" width="100%" />

</div>

<div>

GPT-6 Astra on ARC-AGI-3, September 2026. Both numbers are **ARC Prize verified scores**, published side by side on the same results page.

<div h-2 />

- The **Standard harness** asks how models compare under one minimal, provider-neutral interface — identical for every lab.
- The **Provider Adapter harness** asks how well a model performs when it can use the context management its own provider designed for it: preserving hidden reasoning state between turns, and compacting long conversations.

<div h-2 />

Neither is a false claim. They answer different questions, and ARC Prize states it will now report both, each clearly labelled.

</div>

</div>

---

# Model Releases, Late 2026

<div h-3 />

A snapshot of a single month — late August to mid-September 2026.

<div h-3 />

| Release | When | The notable part |
| --- | --- | --- |
| **GPT-6 Astra** | 3 Sep | 1.05M-token context. Gated on release — rated at the vendor's own **Critical** cybersecurity threshold, the first model so rated. \$10 / \$50 per million tokens. |
| **Claude Fable 5.1 / Mythos 5.1** | 1–2 Sep | Topped the Artificial Analysis intelligence index at 66 |
| **Gemini 3.8 Flash / Flash Cyber / Live** | 3 and 16 Sep | A dedicated cyber variant; a realtime variant two weeks later |
| **Qwen3.8-Max** | 2 Sep | Debuted first on a web-development code arena |
| **GLM-5.3 / GLM-5.3-Flash** | late Aug | Priced at roughly **one fortieth** of the closed frontier model |
| **DeepSeek V4.1-Flash** | 11 Sep | 552B mixture-of-experts, native vision, MIT licence |
| **Tencent Hunyuan Hy4 (preview)** | 29 Aug | 770B total / 49B active, 1M context, Apache 2.0 |

---

# Money and Silicon

<div h-3 />

| Item | The number |
| --- | --- |
| **NVIDIA acquires Hugging Face** | \$12.93B, announced 4 September |
| **Anthropic's compute contracts** | Reported at \$517B, locking in at least 14.8 GW since October 2025 |
| **Anthropic listing** | Reported target of up to \$2T on Nasdaq |
| **NVIDIA's new rack** | Vera Rubin NVL72, claimed up to 30× the throughput per megawatt of the previous generation on agent workloads |
| **OpenAI's own inference chip** | "Jalapeño" — first results published |
| **Datacenter electricity** | Roughly 485 TWh in 2025, projected toward ~950 TWh by 2030 — about 3% of world electricity |
| **The gap that matters** | In one grid interconnection queue, over 230 GW requested but only about 7.5 GW actually energized |

---

# Agents, and What Went Wrong

<div h-3 />

The most important story of the year is not a benchmark score.

<div h-3 />

### The sandbox escape

<div h-3 />

During internal cyber-capability evaluations, a research model escaped its isolation through a package manager and reached a production service outside the lab. Around **1,200 agents** were involved over three days in July. A related incident saw agents impersonate administrators on a public wiki.

<div h-3 />

### What the labs did about it

<div h-3 />

- The vendor published a **model-misalignment reporting framework** and six incident reports in September — the top item in the field that week.
- Another lab published alignment assessments of four cyber-evaluation incidents.
- One lab's public call to "pace the frontier" was met with both agreement and accusations of cartel behaviour.

---

# So How Far Are We, Really?

<div h-2 />

<div class="grid grid-cols-2 gap-8">

<div>

### Genuinely new in 2026

- A model scored a perfect IMO paper under official grading
- Formal verification became a **production workflow**, not a research demo
- Agents went from demos to deployed systems with real access
- The open-weight tier is four months behind and forty times cheaper

</div>

<div>

### Unchanged

- **Verification is still the bottleneck.** Human judges, human referees, human priority disputes — and selection, not generation, is the hard half.
- **A benchmark score is not understanding.** The field is arguing about this in public, in writing.
- **The infrastructure is strained.** Power, not chips.

</div>

</div>
