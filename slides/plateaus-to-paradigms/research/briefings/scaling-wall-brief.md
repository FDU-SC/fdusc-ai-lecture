# The "Scaling Wall" Debate, 2025–2026 — Research Brief
Compiled 2026-09-16. All claims carry a URL and a date. Labelled **WELL ESTABLISHED** (multiple independent primary sources agree) vs **CONTESTED** (credible sources disagree, or single-source).

**Source-quality caveat up front.** Primary sources were reachable for arXiv, arcprize.org, epoch.ai, the-decoder.com, fastcompanyme.com, crown.co.za and energy.pku.edu.cn. **www.iea.org timed out on every attempt** (5 tries, incl. `/reports/energy-and-ai`, `/executive-summary`, `/news/...`, `/reports/key-questions-on-energy-and-ai`), so all IEA figures below come from secondary sources that reproduce the IEA numbers and name the reports. `arcprize.org/leaderboard` renders its table client-side, so no numeric rows could be extracted from raw HTML — all ARC numbers below come from official ARC Prize blog posts. Items seen only on aggregator/SEO domains are marked **UNVERIFIED**.

---

## 1. Are returns to pretraining scale diminishing?

### 1a. What is genuinely established

**WELL ESTABLISHED — scaling-law *form* has survived scrutiny, but the *marginal capability* return per unit compute is sub-linear.**
- Rylan Schaeffer et al., "Evaluating the Robustness of Chinchilla Compute-Optimal Scaling," arXiv:2509.23963, **2025-09-28** — deliberately perturbed Chinchilla's model parameters four structured ways; key results "withstand sizable perturbations," concluding "renewed confidence in Chinchilla as a durable guide." [https://arxiv.org/abs/2509.23963](https://arxiv.org/abs/2509.23963)
- Hans Gundlach, Jayson Lynch, Neil Thompson, "Meek Models Shall Inherit the Earth," arXiv:2507.07931, **2025-07-10** (TAIG @ ICML 2025) — "under a fixed-distribution next-token objective, the marginal capability returns to raw compute shrink substantially"; diminishing returns are argued to be strong enough that even exponentially-faster-scaling labs "will eventually have little advantage in capabilities." [https://arxiv.org/abs/2507.07931](https://arxiv.org/abs/2507.07931)

**WELL ESTABLISHED — "emergent abilities" are largely a metric artifact.** Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?" arXiv:2304.15004 (**v1 2023-04-28, v2 2023-05-22**) — nonlinear/discontinuous metrics manufacture apparent emergence; linear/continuous metrics produce smooth change. Verified in three ways (InstructGPT/GPT-3, BIG-Bench meta-analysis, vision tasks). [https://arxiv.org/abs/2304.15004](https://arxiv.org/abs/2304.15004)
*Note: this cuts against the "sharp wall" narrative as much as against naive emergence — it implies smooth, predictable returns, which is itself an anti-discontinuity result.*

**WELL ESTABLISHED — a second scaling axis (inference-time compute) is real and large.**
- DeepSeek-AI, "DeepSeek-R1," arXiv:2501.12948 (**v1 2025-01-22; v2 2026-01-04**), published *Nature* **645:633–638 (2025)**. Pure RL "incentivizes" reasoning with no human-labeled reasoning trajectories; emergent self-reflection/verification/strategy adaptation. [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948)

**WELL ESTABLISHED — frontier capability progress did *not* visibly stall in 2026.**
- Epoch Capabilities Index (ECI), which pools 50+ benchmarks: GPT-6 Astra set a new record at **169**, vs prior high **163** (Claude Fable 5.1), 162 (GPT-5.6 Sol and Claude Opus 5). [https://epoch.ai/eci](https://epoch.ai/eci); table reproduced in THE DECODER, **2026-09-04** [https://the-decoder.com/benchmarks-disagree-on-gpt-6-astra-but-its-human-beating-efficiency-on-arc-agi-3-pulls-chollets-agi-forecast-forward/](https://the-decoder.com/benchmarks-disagree-on-gpt-6-astra-but-its-human-beating-efficiency-on-arc-agi-3-pulls-chollets-agi-forecast-forward/)
- Epoch AI, "Global AI computing capacity is doubling every 7 months," Data Insight, **2026-01-09** — the compute input to scaling is still compounding fast. [https://epoch.ai/data-insights/ai-chip-production](https://epoch.ai/data-insights/ai-chip-production)

**WELL ESTABLISHED — scaling is not a single number; benchmark choice determines the verdict.**
- As of **2026-09-04**, two independent aggregators disagreed about the *same model*: Epoch ECI put Astra first (169), while Artificial Analysis' Intelligence Index rated Astra at **61**, exactly level with its predecessor Sol and **behind** Claude Fable 5.1 (66). Astra lost ~80 Elo on GDPval-AA v2 and regressed on banking support, SciCode and long-context reasoning. THE DECODER, 2026-09-04 (URL above).
- Epoch's own analysis found Astra's ECI jump was "still consistent with the existing trajectory of AI progress" — i.e. *not* a discontinuity. Reported in Fast Company Middle East, **2026-09-16** [https://fastcompanyme.com/technology/openai-says-the-agi-era-has-begun-ai-researchers-arent-so-sure/](https://fastcompanyme.com/technology/openai-says-the-agi-era-has-begun-ai-researchers-arent-so-sure/) citing Epoch AI's post at [https://x.com/EpochAIResearch/status/2095602754282783108](https://x.com/EpochAIResearch/status/2095604282783108)

### 1b. What is contested

**CONTESTED — whether the *next* doubling of pretraining compute still buys frontier capability.** Position holders, all 2026:
- **Altman (pro-scaling):** "Betting against LLMs scaling at this point feels quite misguided to me." At Stanford, **2026-06-21**; he also said LLMs are "capable of figuring out new knowledge" but on very long-horizon high-judgment tasks "seem much worse than people." [https://the-decoder.com/sam-altman-says-a-whole-generation-of-researchers-held-ai-back-by-underestimating-what-scaling-could-do/](https://the-decoder.com/sam-altman-says-a-whole-generation-of-researchers-held-ai-back-by-underestimating-what-scaling-could-do/) (primary: Stanford Online, [https://www.youtube.com/watch?v=F_7M4Hc-usM](https://www.youtube.com/watch?v=F_7M4Hc-usM) @ t=1556)
- **Hassabis (qualified):** "The returns are still very substantial, although they're a bit less than they were… The last set of ideas are sort of, you know, all the juices being rung out of them." 20VC podcast, **2026-04-07/08** — episode title explicitly asserts "We Have Not Hit Scaling Laws." Transcript via signalcast.app (third-party AI summary/transcript; episode existence and title corroborated by the 20VC feed listing) [https://www.signalcast.app/episode/20vc-20-minute-vc/20vc-deepminds-demis-hassabis-on-why-agi-is-bigger-than-the-industrial-revolution-why-llms-will-not-](https://www.signalcast.app/episode/20vc-20-minute-vc/20vc-deepminds-demis-hassabis-on-why-agi-is-bigger-than-the-industrial-revolution-why-llms-will-not-)
- **Gary Marcus (anti):** "We are nowhere near AGI… That's just marketing by people who either don't know the original definitions or are deliberately lowering the bar." Fast Company ME, **2026-09-16** (URL above).
- **Gundlach/Lynch/Thompson (arXiv 2507.07931):** convergence, not divergence — the strongest formal statement of the diminishing-returns case.

**CONTESTED — the "Chinchilla is not enough" framing.** No paper titled or substantively arguing "Chinchilla scaling laws are not enough" was located in 2025–2026 despite repeated searches. What *does* exist is (a) the robustness paper above *defending* Chinchilla, and (b) continued Chinchilla-form work, e.g. Fabian Schaipp, "How to Allocate Your Tokens? Scaling Laws with Training Steps and Batch Size," arXiv:2607.01487, **2026-07-01**, which fits a three-term law separating training steps from batch size. [https://arxiv.org/abs/2607.01487](https://arxiv.org/abs/2607.01487) **Treat "Chinchilla is not enough" as a framing in commentary, not an established paper title.**

---

## 2. Data exhaustion / "peak data"

### 2a. The canonical numbers (verified directly from the paper)

Villalobos, Ho, Sevilla, Besiroglu, Heim, Hobbhahn, "Will we run out of data? Limits of LLM scaling based on human-generated data," **arXiv:2211.04325, v1 2022-10-26, v2 2024-06-04**. [https://arxiv.org/abs/2211.04325](https://arxiv.org/abs/2211.04325) · full text [https://arxiv.org/html/2211.04325v2](https://arxiv.org/html/2211.04325v2) · Epoch page [https://epoch.ai/publications/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data](https://epoch.ai/publications/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data)

**Exhaustion dates (the exact projections):**
- **Median year the stock of public human text is fully utilised: 2028.**
- **Range: 2026–2032**, "or slightly earlier if models are overtrained."
- At that point models train on ≈ **4×10¹⁴ tokens (~400T)**, corresponding to ≈ **5×10²⁸ FLOP** for non-overtrained models.

**Stock of high-quality language data (Table 1, in tokens):**

| Estimate | Median | 95% CI |
|---|---|---|
| Common Crawl | 130T | [100T, 260T] |
| Indexed web | **510T** | [130T, 2100T] |
| Whole web | **3100T** | [1900T, 5200T] |
| Images (token-equivalent) | 300T | n/a |
| Video (token-equivalent) | 1350T | n/a |

**Supporting parameters (all from the paper):** dataset sizes grew **0.38 OOM/yr (~2.4×/yr)**, 95% CI 0.27–0.48; quality filtering leaves only **10–40%** of deduplicated web data usable without compromising performance; multi-epoch training raises effective dataset size up to 3–15× (Muennighoff et al.), and the authors **anchor at 5×**; average plain-text bytes per page **7000** [6100, 8200]; **~4 bytes/token** [2, 5]; Google index **~250B pages** [100B, 1200B]; tokenisation via cl100k_base.

**WELL ESTABLISHED (arithmetic check):** the paper's own framing is often misreported. 510T tokens is the *raw indexed web*; the *effective* stock after quality filtering and repetition adjustments is ~400T. The widely repeated "we run out in 2028" is the **median**, with a 2026–2032 band — the 2026 end is already inside the window as of this brief's date.

### 2b. Synthetic data as counterargument

**WELL ESTABLISHED — synthetic data can substitute for organic web text at small-to-mid scale, and can exceed the teacher.**
- "Phi-4 Technical Report," arXiv:2412.08905, **2024-12-12** — 14B model, "training recipe centrally focused on data quality," "strategically incorporates synthetic data throughout the training process," and "substantially surpasses its teacher model [GPT-4] on STEM-focused QA capabilities, giving evidence that our data-generation and post-training techniques go beyond distillation." [https://arxiv.org/abs/2412.08905](https://arxiv.org/abs/2412.08905)
- "Nemotron-4 340B Technical Report," arXiv:2406.11704 (**v1 2024-06-17, v2 2024-08-06**) — "over **98% of data used in our model alignment process is synthetically generated**"; generation pipeline open-sourced. [https://arxiv.org/abs/2406.11704](https://arxiv.org/abs/2406.11704)
- Villalobos et al. themselves list synthetic data generation, transfer learning from data-rich domains, and data-efficiency improvements as the escape routes (abstract, arXiv:2211.04325).

**CONTESTED — whether synthetic data removes the ceiling or merely moves it.** The Villalobos paper treats synthetic data as a *mitigation*, not a refutation; it does not revise the stock estimate to include synthetic tokens. **No 2025–2026 Epoch AI publication revising the 510T / 3100T / 2028 figures was located.** Searching Epoch's Data Insights index (**fetched 2026-09-16**) returned no data-stock update among featured items (top items: AI chip production 2026-01-09; CVE severity spike 2026-07-02; LLM inference prices 2025-03-12). [https://epoch.ai/data-insights](https://epoch.ai/data-insights) **Flag: the absence of a revision is a negative finding from a non-exhaustive index, not proof none exists.**

**UNVERIFIED.** Claims circulating that a "Stanford report" warns of peak data, and that "the compute bottleneck is not the problem anymore, the data bottleneck is," were seen only on aggregator domains (ainvest.com, sbbit.jp, longtermwiki.com) and were not traced to a primary report. A "Rich Sutton data-scarcity-mistake" counterargument was seen only on a secondary handbook site and **could not be verified against a Sutton primary source**.

---

## 3. Energy and compute constraints, 2025–2026

### 3a. IEA *Energy and AI* (April 2025)

Published **2025-04-10**. Figures below reproduced verbatim from Peking University Energy Research Institute's summary of the IEA executive summary, **2025-04-21** (primary iea.org unreachable). [https://energy.pku.edu.cn/xsdt/sznyyw/d123q/xnyyw202508/64bdec556620445292f6f21510e8d5a4.htm](https://energy.pku.edu.cn/xsdt/sznyyw/d123q/xnyyw202508/64bdec556620445292f6f21510e8d5a4.htm)

- **2024: data centres ≈ 1.5% of global electricity demand = 415 TWh.**
- **2030: more than doubles to ≈ 945 TWh** — "slightly more than Japan's current total electricity consumption."
- US accounts for the largest share of growth, then China.
- To 2030, data centres ≈ **one-tenth of global electricity demand growth** — *less* than industrial motors, air conditioning or EVs.
- Emissions: **180 Mt today → 300 Mt by 2035** (base case); **500 Mt** in the high-emissions scenario.
- Emerging/developing economies outside China: **50% of global internet users but <10% of data-centre capacity.**

### 3b. IEA *Key Questions on Energy and AI* (April 2026, the update)

Report at [https://www.iea.org/reports/key-questions-on-energy-and-ai](https://www.iea.org/reports/key-questions-on-energy-and-ai) (unreachable this session). Figures via Crown Publications / *Electricity + Control*, **2026-07-16**, which quotes the report directly. [https://www.crown.co.za/latest-news/electricity-control-latest-news/37355-the-link-between-energy-and-ai](https://www.crown.co.za/latest-news/electricity-control-latest-news/37355-the-link-between-energy-and-ai)

- Capex of five large tech companies **> $400bn in 2025**, set to rise a further **75% in 2026**.
- **Data-centre electricity demand +17% in 2025**; AI-focused data centres grew faster; vs **3%** growth in *global* electricity demand.
- **Power consumption per AI task is declining** — efficiency improving "at a rate unprecedented in energy history." But usage breadth and energy-intensive uses (AI agents) are rising.
- **Data-centre electricity consumption set to double by 2030; AI-focused power use to triple.**
- **Physical bottlenecks are now binding:** gas-turbine and transformer supply chains, advanced chips/IT components; "the swelling pipeline of data centre projects is straining planning and regulatory systems, **holding up grid connections** and other necessary approvals."
- Tech sector ≈ **40% of all corporate renewables PPAs signed in 2025**; now a major driver of nuclear and advanced geothermal.
- **SMR conditional offtake pipeline: 25 GW at end-2024 → 45 GW today** (mid-2026).
- Constrained by slow grid connections, developers are advancing on-site natural-gas generation, mainly in the US; IEA satellite tracking shows most such projects "remain in their early stages." Batteries becoming critical because AI data centres have "rapid and large swings in demand."
- Proven AI applications could cut energy-intensive firms' energy costs by **3–10 percentage points**; lack of digital skills and data availability are the key adoption barriers.
- IEA launching a new government/industry platform on energy and AI. Quote from Executive Director **Fatih Birol**.

**WELL ESTABLISHED (cross-source):** both IEA reports agree on direction (doubling by 2030) and on grid interconnection being a real, near-term constraint. **CONTESTED:** the *rate* — the 2026 report's "triple for AI-focused" and "+17% in 2025" are single-source (Crown/ IEA 2026) and could not be cross-checked against iea.org. **UNVERIFIED:** a "17% growth" figure also appeared on axis-intelligence.com, an aggregator; it is the same number, so it likely propagates from the IEA report, but the aggregator adds no independent support.

---

## 4. What the named people actually said in 2026

### Ilya Sutskever
**CONTESTED/IMPORTANT DATE CORRECTION.** The famous "pretraining as we know it will end / age of scaling → age of research" material is **November 2025, not 2026**. Dwarkesh Podcast, "Ilya Sutskever — We're moving from the age of scaling to the age of research," episode page [https://www.dwarkesh.com/p/ilya-sutskever-2](https://www.dwarkesh.com/p/ilya-sutskever-2) (**page repeatedly timed out; not read directly**). Date **2025-11-26** per a dated transcript mirror [https://eikon.moom.cn/portal/zh/kb/articles/2025-11-26-ilya-sutskever-we-re-moving-from-the-age-of-scaling-to-the-age-of-research](https://eikon.moom.cn/portal/zh/kb/articles/2025-11-26-ilya-sutskever-we-re-moving-from-the-age-of-scaling-to-the-age-of-research); corroborated by Business Insider, **2025-11** [https://www.businessinsider.com/openai-cofounder-ilya-sutskever-scaling-ai-age-of-research-dwarkesh-2025-11](https://www.businessinsider.com/openai-cofounder-ilya-sutskever-scaling-ai-age-of-research-dwarkesh-2025-11). **No verified 2026 Sutskever statement was found.** Treat any "Sutskever 2026" citation as likely a mis-dated reference to this Nov-2025 interview.

### Yann LeCun
- Left Meta in 2025; founded **AMI**. Reuters, **2026-03-10**: "Ex-Meta AI chief Yann LeCun's AMI raises **$1.03 billion** for alternative AI approach." [https://www.reuters.com/business/ex-meta-ai-chief-yann-lecuns-ami-raises-103-billion-alternative-ai-approach-2026-03-10/](https://www.reuters.com/business/ex-meta-ai-chief-yann-lecuns-ami-raises-103-billion-alternative-ai-approach-2026-03-10/) (Reuters page did not load this session; headline + date from the search index and corroborated by AIwire/HPCwire **2026-03-11** [https://www.hpcwire.com/aiwire/2026/03/11/yann-lecuns-ami-secures-1b-seed-to-develop-ai-world-models/](https://www.hpcwire.com/aiwire/2026/03/11/yann-lecuns-ami-secures-1b-seed-to-develop-ai-world-models/) and Sifted [https://sifted.eu/articles/yann-lecun-ami-labs-meta-funding-round-nvidia](https://sifted.eu/articles/yann-lecun-ami-labs-meta-funding-round-nvidia)).
- **CONTESTED:** LeCun's "LLMs are a dead end" position is attested in 2026 indirectly — Altman, at Stanford **2026-06-21**, "responded to critics like Yann LeCun, who has called LLMs a dead end," and said "some people tie their identity to a position and can't let go." [https://the-decoder.com/sam-altman-says-a-whole-generation-of-researchers-held-ai-back-by-underestimating-what-scaling-could-do/](https://the-decoder.com/sam-altman-says-a-whole-generation-of-researchers-held-ai-back-by-underestimating-what-scaling-could-do/). **A direct, dated 2026 LeCun quotation on LLM limits was NOT obtained from a primary source** — flag any such quote as unverified unless the parent can reach LeCun's own posts/talks.

### Andrej Karpathy
- Talk "**From Vibe Coding to Agentic Engineering**," **May 2026** — one year after coining "vibe coding"; themes: agentic engineering as "the more serious discipline taking shape on top of vibe coding"; LLMs "not as animals but as **ghosts**: jagged, statistical, summoned entities that require a new kind of taste and judgment to direct"; **Software 3.0**; "the limits of verifiability"; "you can outsource your thinking but never your understanding."
- Source: Lifeboat News summary, **2026-05-09**, linking the primary talk video [https://lifeboat.com/blog/2026/05/andrej-karpathy-from-vibe-coding-to-agentic-engineering](https://lifeboat.com/blog/2026/05/andrej-karpathy-from-vibe-coding-to-agentic-engineering) → [https://www.youtube.com/watch?v=96jN2OCOfLs](https://www.youtube.com/watch?v=96jN2OCOfLs). Searches also surfaced a Sequoia "AI Ascent 2026" attribution and a "Training Data" podcast episode with the same title.
- **UNVERIFIED:** exact talk date, venue and the "summoning ghosts" quote's verbatim wording — no primary transcript was read. **No 2026 Karpathy statement on *progress rates* / scaling returns was located**; his 2026 material is about software practice, not the scaling wall. Do not attribute a scaling-wall position to him on this evidence.

### Demis Hassabis
- 20VC, **2026-04-07/08**: AGI "within five years" with high probability; AGI framed as "10 times the industrial revolution at 10 times the speed"; **"We Have Not Hit Scaling Laws"** (episode title); returns "still very substantial" but lower than at the start; labs able to "invent new algorithmic ideas" will gain advantage over the next few years because "the last set of ideas are sort of… all the juices being rung out of them." Critical missing capabilities named: **continual learning** and **long-horizon hierarchical planning**. (URL above; transcript via third-party signalcast.app — treat wording as indicative.)

### Sam Altman
- **2026-06-21**, Stanford: "Betting against LLMs scaling at this point feels quite misguided to me"; a whole generation of researchers "held the field back" by being too confident about what scaling *couldn't* do; yet on very long-horizon, high-judgment tasks LLMs "seem much worse than people." (URL above.)
- **March 2026:** spoke in a fireside with **François Chollet** at the ARC-AGI-3 launch, Y Combinator HQ, **2026-03-25** — announced on the ARC Prize launch post [https://arcprize.org/blog/arc-agi-3-launch](https://arcprize.org/blog/arc-agi-3-launch).
- **July 2026:** reported as claiming we are already "in the Singularity" — cited as ABC News by Fast Company ME, **2026-09-16** [https://abcnews.com/Business/openai-ceo-sam-altman-claims-ai-singularity-arrived/story?id=135120342](https://abcnews.com/Business/openai-ceo-sam-altman-claims-ai-singularity-arrived/story?id=135120342) (not independently fetched).
- **CONTESTED — no candid admission of a scaling plateau was found.** Reports of Altman being *candid about limits* are limited to the long-horizon-judgment concession above. A widely-circulated claim that Altman said a whole generation of researchers held AI back appears in both the-decoder (fetched, dated) and officechai (fetch timed out) — the the-decoder version is the reliable one. **UNVERIFIED:** a "parts of new AI clouds are unsustainably stupid" / "would delay IPO if RSI" item was seen only on sohu.com and non-English aggregators.

### François Chollet (also see §5)
- **2026-09-16**, by email to Fast Company: ARC-AGI-3 "doesn't represent the finish line… because it tests a non-exhaustive set of attributes at very small scales. The real world features much longer time horizons for continual learning compared to ARC 3 games (**decades vs minutes**), much larger world modeling complexity, much greater goal ambiguity, more greater exploration spaces, etc. So solving the benchmark is **a strong sign of progress** (as prior systems did not exhibit these attributes), but it is **not proof of AGI**, and that was never the point." [https://fastcompanyme.com/technology/openai-says-the-agi-era-has-begun-ai-researchers-arent-so-sure/](https://fastcompanyme.com/technology/openai-says-the-agi-era-has-begun-ai-researchers-arent-so-sure/)

---

## 5. ARC-AGI-3 status as of September 2026

### 5a. What ARC-AGI-3 is
**WELL ESTABLISHED.** Announced **2026-03-25**. "Our first **Interactive Reasoning Benchmark**… a set of novel, video-game-like environments where agents must perceive, explore, plan, and act across long horizons." Hidden hold-out set prevents memorisation; rewards on-the-fly learning, efficient exploration, and setting your own goals when the objective isn't stated. **100% human-solvable**; scoring includes a **skill-acquisition / action-efficiency** metric comparing AI against a measured human baseline.
- Launch post [https://arcprize.org/blog/arc-agi-3-launch](https://arcprize.org/blog/arc-agi-3-launch) · benchmark page [https://arcprize.org/arc-agi/3](https://arcprize.org/arc-agi/3) · technical paper [https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf) (arXiv:2603.24621) · human-baseline post **2026-04-14** [https://arcprize.org/blog/arc-agi-3-human-dataset](https://arcprize.org/blog/arc-agi-3-human-dataset)
- Scale: **135 novel environments** per the ARC Prize analysis post (2026-05-01). **>1,000,000 games** played by 2026-05-01.

### 5b. Leaderboard trajectory (the headline finding)

| Date | System | ARC-AGI-3 (Semi-Private) | Cost | Source |
|---|---|---|---|---|
| 2026-03-25 | "Frontier AI" (launch-day best) | **0.51%** (humans 100%) | — | [launch post](https://arcprize.org/blog/arc-agi-3-launch) |
| 2026-05-01 | GPT-5.5 | **0.43%** | — | [analysis post](https://arcprize.org/blog/arc-agi-3-gpt-5-5-opus-4-7-analysis) |
| 2026-05-01 | Claude Opus 4.7 | **0.18%** | — | same |
| 2026-09-03 | Claude Opus 5 | **30.16%** | — | THE DECODER 2026-09-04 |
| 2026-09-03 | GPT-5.6 Sol | **7.78%** | — | same |
| 2026-09-03 | **GPT-6 Astra (max)** | **62.7%** | **$26,098** | [ARC Prize, 2026-09-03](https://arcprize.org/blog/astra) |
| 2026-09-03 | **GPT-6 Astra (high), OpenAI Provider Adapter harness** | **99.9%** | **$18,817** | same |

**WELL ESTABLISHED — GPT-6 Astra leads ARC-AGI-3, with a caveat that matters.** ARC Prize, "OpenAI's GPT-6 Astra on ARC-AGI-3," **2026-09-03**: Astra (max) 62.7% for $26K under the **Standard harness** (model keeps only its own visible notes); Astra (high) **99.9%** for $19K under the **Provider Adapter harness** (preserves opaque reasoning state and compacts long conversations). Full reasoning-effort sweep (Standard): max 62.7%/$26,098; xhigh 59.3%/$37,317; high 54.8%/$40,705; medium 38.6%/$48,090; **low 17.5%/$38,166**; **none 35.2%/$49,791**. Note the non-monotonicity: "low" scores *below* "none." [https://arcprize.org/blog/astra](https://arcprize.org/blog/astra)
- **Higher reasoning effort costs *less*** because Astra solves games in fewer actions → fewer calls/tokens.
- **Action efficiency: Astra (max, Provider Adapter) used fewer actions than the human baseline on 96.0% of levels, and 51.7% fewer actions per level on average.** Human baseline from ~500 unscreened general-public participants, paid $115 per 90-minute session plus $5 per game solved.
- Astra developed a **self-invented algebraic shorthand DSL** for game state (e.g. `L8: hub q2 (8↓). Lengths: 14=1…`, `extend8 to3; retract10 to2; shorten8 to1`, `Controls: 9−=(39,4), rotate=(49,18)`), and in the third-party **PRO-LONG** harness wrote game-specific libraries (`maze_solver.py`, `combat_solver.py`, `patrol_solver.py`, `sync_state.py`). No sandbox-escape attempts observed.
- **CONTESTED — harness comparability.** ARC Prize states only the 62.7% Standard-harness number "allowed a fair comparison between vendors"; Provider Adapter runs were ~**3.66× faster** and used **49% fewer tokens** across the 167 game-reasoning pairs both harnesses solved. This is a live dispute: THE DECODER (2026-09-04) notes the same harness disagreement already arose with GPT-5.6 Sol. [https://the-decoder.com/openai-claims-gpt-5-6-sol-beats-opus-5-on-arc-agi-3-with-its-latest-api-and-two-additional-settings/](https://the-decoder.com/openai-claims-gpt-5-6-sol-beats-opus-5-on-arc-agi-3-with-its-latest-api-and-two-additional-settings/)
- **WELL ESTABLISHED — ARC Prize explicitly does not claim AGI.** "Astra represents a noticeable step-function change in frontier model capabilities… while we believe Astra represents meaningful progress towards generalization, we are not claiming that it is AGI." ARC-AGI-3 "has a tightly bounded scope… deterministic, closed-ended mechanics and goals. It does not represent the complexity and open-endedness of the real world."

### 5c. ARC-AGI-2 state — and why "solved" depends on which leaderboard
**WELL ESTABLISHED (ARC Prize official).**
- Benchmark structure: 1000 training / 120 public eval / 120 semi-private / 120 private; grand-prize target **85%**; all tasks solved pass@2 by ≥2 humans; calibration via 400+ participants in San Diego, early 2025. [https://arcprize.org/arc-agi/2](https://arcprize.org/arc-agi/2)
- **As of 2025-12-05** the **Grand Prize remained unclaimed**: top *Kaggle* score on ARC-AGI-2 private was **24.03%** (NVARC, $0.20/task); top **verified commercial model** was **Claude Opus 4.5 (Thinking, 64k) at 37.6% ($2.20/task)**; top **verified model refinement** was **Poetiq on Gemini 3 Pro at 54% ($30/task)** vs a Gemini 3 Pro baseline of 31% ($0.81/task). 1,455 teams / 15,154 entries; 90 papers. [https://arcprize.org/blog/arc-prize-2025-results-analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis)
- **As of 2026-09-04** (third-party table, THE DECODER): ARC-AGI-2 — Astra **95.0%**, Sol 92.5%, Fable 5.1 90.0%, Opus 5 90.4%; ARC-AGI-1 — Astra 98.5% (xhigh; 97.5% at max), others 97.5% each, and **"ARC-AGI-1 is now considered largely saturated."**
- **CONTESTED — has ARC-AGI-2 been "solved"?** Two different questions are being conflated: (i) *capability* — verified commercial systems are now well above the 85% grand-prize threshold; (ii) *the prize* — the ARC Prize 2026 Grand Prize requires an **open-source** solution under Kaggle compute constraints with **no internet access during evaluation**, and as of the last official statement (2025-12-05) no open solution had cleared it. ARC Prize's 2026 page guarantees the ARC-AGI-2 grand prize will be awarded to the best open-source solution. [https://arcprize.org/competitions/2026](https://arcprize.org/competitions/2026) **The 95.0% figure could not be confirmed against arcprize.org's own leaderboard table** (client-side rendered).
- **WELL ESTABLISHED and important:** ARC Prize itself believes ARC-AGI-1/2 are being **"overfit" through training-data coverage** — "either incidentally or intentionally, we cannot tell." Evidence: Gemini 3 Deep Think's reasoning used correct ARC colour mappings unprompted, though the verification harness never mentions ARC or its colour format. [https://arcprize.org/blog/arc-prize-2025-results-analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis)

### 5d. ARC Prize 2026 competition status
**WELL ESTABLISHED.** $2M+, three tracks (ARC-AGI-3, ARC-AGI-2, Paper Track). Key dates: competition started **2026-03-25**; ARC-AGI-3 Milestone #1 **2026-06-30**; **Milestone #2 2026-09-30** (open now); **submissions due 2026-11-02**; papers due 2026-11-08; **results announced 2026-12-04**. All prize-eligible solutions must be open source (CC0/MIT-0 or compatible); no internet during Kaggle evaluation. [https://arcprize.org/competitions/2026](https://arcprize.org/competitions/2026)
- **Milestone #1 results (announced 2026-07-06, $37.5K):** 1st **Tufa Labs "The Duck"** (small open-source LLM writing/running Python in a live REPL; runs **Qwen 3.6 27B FP8** locally; "infinite play via eviction" of oldest messages; team reports gains came from multimodality and better base models, and that hand-crafted tools *hurt*); 2nd **Reki** (vision-LLM-as-policy; **Gemma-4-31B** local; JSON action per step + reflection memory + numpy click heuristic); 3rd **Md Boktiar Mahbub Murad "forge"** (same paradigm, profile-driven framework; top run disabled all extra machinery). [https://arcprize.org/blog/arc-prize-2026-milestone-1](https://arcprize.org/blog/arc-prize-2026-milestone-1)
- **ARC-AGI-4:** in development since ARC-AGI-3's release, targeted **Q1 2027**; intended to probe **recursive self-improvement and open-ended innovation**. ARC Prize, via THE DECODER, 2026-09-04 (URL above); also [https://arcprize.org/blog/astra](https://arcprize.org/blog/astra) ("actively exploring the questions that should shape the next generation of benchmarks, including how to evaluate recursive self-improvement and open-ended innovation").

### 5e. Has Chollet changed his view on LLM capability? — **He moved his timeline, not his thesis.**
**WELL ESTABLISHED (direct quote):** Chollet, **2026-09-04**, on X ([https://x.com/fchollet/status/2095598451115614371](https://x.com/fchollet/status/2095598451115614371), quoted by THE DECODER): Astra shows "highly efficient, on-the-fly symbolic world modeling for each game and level," going so far as "developing its own shorthand DSL to represent in-game situations," which is "essentially a game-specific algebraic notation." The key line: **"Astra exhibits symbolic modeling behaviors we had only previously seen with sophisticated harnesses, so harness capabilities are increasingly shifting into the model itself."**
- Timeline revision: at ARC-AGI-3's release he answered a saturation question with "**about a year**"; Astra arrived **"about twice as fast"** as expected. Asked whether his earlier **2030** AGI forecast still held, he replied: **"Sooner, because progress is happening faster than I expected."** THE DECODER, 2026-09-04 (URL above).
- But his **thesis is unchanged**: benchmark success "is not proof of AGI, and that was never the point" (Fast Company ME, 2026-09-16, URL above). Years earlier he framed the endpoint as: "You'll know AGI is here when the exercise of creating tasks that are easy for regular humans but hard for AI becomes simply impossible" (quoted by ARC Prize, 2025-12-05).
- **CONTESTED:** a French aggregator headline claims Astra "pulls Chollet's AGI forecast forward" toward an earlier date; the *direction* is corroborated by Chollet's own "Sooner" reply, but **no specific revised year was stated by Chollet** in any source read here. Do not attribute a numeric new forecast to him.
- **UNVERIFIED:** a widely-syndicated item that ARC-AGI-4 will test "invention" comes from 36kr/C114 aggregation; the Q1-2027 date and the "recursive self-improvement / open innovation" framing are corroborated by THE DECODER and ARC Prize's own post, so the substance holds even though the aggregator framing does not add support.

### 5f. The 2026 AGI-claim fight around Astra (context for the scaling debate)
**WELL ESTABLISHED as statements made, even where the claims themselves are contested:**
- **Greg Brockman** (OpenAI president), at the GPT-6 Astra launch, **early September 2026**: declared the "AGI era" had begun. **Jensen Huang** tweeted "AGI has arrived" ([https://x.com/JensenHuang/status/2096700264569090384](https://x.com/JensenHuang/status/2096700264569090384)) — he had already made the claim in **March 2026** (Forbes, 2026-03-23). All via Fast Company ME, 2026-09-16.
- Rebuttals in the same piece: **Gary Marcus** — "We are nowhere near AGI"; he notes Astra should be *decisively* outperforming rivals if it were AGI. **Andy Konwinski** — "These systems can't yet think on their own for long… They're really good at coding, but most of the world's value doesn't come from software engineers," and "Nobody has a definition of AGI that's worth its weight, so who cares whether it's 'here'?" **Ben Goertzel** — Astra is "superhuman at some things and subhuman at others… comparing it to a human being ends up being complicated rather than a simple yes or no"; missing: self-modeling, lifelong memory, and goal coordination. OpenAI's current AGI definition is "highly autonomous systems that outperform humans at most economically valuable work." All Fast Company ME, 2026-09-16.

---

## 6. Where the disagreement actually sits (synthesis, no new claims)

1. **Everyone credible agrees raw pretraining returns are sub-linear.** The fight is over *how* sub-linear, and whether it matters: Gundlach et al. (arXiv:2507.07931) say convergence; Hassabis says "substantial but less," with algorithm invention as the differentiator; Altman says betting against scaling is "misguided."
2. **The disagreement is increasingly about *which axis*.** Inference-time compute (DeepSeek-R1, arXiv:2501.12948; the o-series lineage) moved the frontier while pretraining returns flattened — so "scaling is dead" and "scaling is alive" can both be true on different axes, and the AI-press verdict flips depending on whether the benchmark is ARC-AGI-3 (62.7% vs 0.43% five months earlier) or the Artificial Analysis Index (61 vs 66).
3. **Data: the projection window (2026–2032, median 2028) is now, but nobody has observed a hard stop.** Synthetic data is a demonstrated partial substitute (Phi-4, Nemotron-4), and the 2025–2026 record shows labs routing around the constraint via RL on verifiable tasks and test-time compute rather than more tokens.
4. **Energy is a *rate* constraint, not a *ceiling*.** Both IEA reports describe grid interconnection, transformers and turbines as the binding near-term frictions; the 2026 report adds that per-task efficiency is improving fast enough that demand growth is a function of adoption breadth, not of per-query cost.
5. **Benchmark validity is itself now contested terrain.** ARC Prize publicly suspects ARC-AGI-1/2 are contaminated by training-data coverage, and the ARC-AGI-3 harness dispute (62.7% vs 99.9% for the same model) shows the measurement apparatus can swing a result by 37 points. Any claim of the form "model X proves/disproves the scaling wall" inherits that uncertainty.

---

## 7. Explicit verification gaps

| Item | Status |
|---|---|
| iea.org primary report text | **Not reachable** (all URLs timed out, 5 attempts). IEA figures are second-hand. |
| arcprize.org/leaderboard numeric rows | **Not extractable** (client-side rendered). Numbers come from ARC Prize blog posts. |
| dwarkesh.com Sutskever transcript | **Not reachable.** Date (2025-11-26) from a dated mirror + Business Insider. |
| Epoch AI 2025–2026 revision of the 510T/3100T/2028 data-stock figures | **Not found.** Absence in a non-exhaustive index is not proof of absence. |
| Direct 2026 LeCun quotation | **Not obtained** from a primary source. |
| Karpathy talk exact date/venue; verbatim "summoning ghosts" | **Not confirmed** from primary. |
| 2026 Sutskever statement | **None found.** The famous interview is Nov 2025. |
| "Chinchilla scaling laws are not enough" as a paper | **Not found as a paper title or argument.** |
| Rich Sutton "data scarcity mistake" | **Not verified.** |
| Sources treated as unreliable aggregators/SEO and excluded from load-bearing claims | benchlm.ai, benchgecko.ai, agentmarketcap.ai, theagiclock.com, bedda.tech, securing.ai, lumevalley.com, aihot.virxact.com, remio.ai, threatclaw.ai, lefilia.fr, cryptobriefing.com, aidailypost.com, ainvest.com, axis-intelligence.com, quantumzeitgeist.com, jeffreypaine.com, aitechsuite.com, sumnify.io, kucoin/htx news, aibase.com, 163.com, sohu.com, toutiao.com |
