# Raw research notes: "scaling wall" debate 2025–2026
Collected 2026-09-16. Working notes (raw URLs + dates). See final brief for WELL ESTABLISHED / CONTESTED labelling.

## Topic 1 — scaling returns
- Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?" arXiv:2304.15004 (v1 2023-04-28, v2 2023-05-22). https://arxiv.org/abs/2304.15004 — emergent abilities an artifact of nonlinear/discontinuous metrics; smooth with linear metrics.
- Schaeffer, Levi, Kirsch, Guenais, Miranda, Obbad, Koyejo, "Evaluating the Robustness of Chinchilla Compute-Optimal Scaling" arXiv:2509.23963 (2025-09-28). https://arxiv.org/abs/2509.23963 — Chinchilla prescriptions survive perturbation; "renewed confidence in Chinchilla".
- Gundlach, Lynch, Thompson, "Meek Models Shall Inherit the Earth" arXiv:2507.07931 (2025-07-10), TAIG @ ICML 2025. https://arxiv.org/abs/2507.07931 — marginal capability returns to raw compute shrink substantially; capability convergence.
- DeepSeek-AI, "DeepSeek-R1" arXiv:2501.12948 (v1 2025-01-22; v2 2026-01-04); Nature 645:633-638 (2025). https://arxiv.org/abs/2501.12948 — pure RL incentivizes reasoning; no human-labeled reasoning trajectories.
- Schaipp, "How to Allocate Your Tokens? Scaling Laws with Training Steps and Batch Size" arXiv:2607.01487 (2026-07-01). https://arxiv.org/abs/2607.01487 — three-term scaling law; Chinchilla-form work continues.
- UNVERIFIED aggregators seen: agentmarketcap.ai, benchlm.ai, benchgecko.ai, jeffreypaine.com, quantumzeitgeist.com, futureagi.com, ainvest.com.

## Topic 2 — data exhaustion
Villalobos, Ho, Sevilla, Besiroglu, Heim, Hobbhahn, "Will we run out of data?" arXiv:2211.04325 (v1 2022-10-26; v2 2024-06-04). https://arxiv.org/abs/2211.04325 ; HTML https://arxiv.org/html/2211.04325v2 ; Epoch page https://epoch.ai/publications/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data
- Stock estimates (tokens), Table 1: Common Crawl 130T [100T,260T]; Indexed web 510T [130T,2100T]; Whole web 3100T [1900T,5200T]; Images 300T; Video 1350T.
- Median year stock fully utilized: **2028**; range **2026–2032** (earlier if overtrained). Effective stock ≈ **4e14 tokens (~400T)**, ≈5e28 FLOP for non-overtrained models.
- Dataset-size growth: **0.38 OOM/yr** (~2.4x/yr), 95% CI 0.27–0.48.
- Quality adjustment: only **10–40%** of deduplicated web data usable without compromising performance.
- Multi-epoch: effective dataset size gain up to 3x–15x (Muennighoff et al.), model anchors at **5x**.
- Avg plain text bytes/web page 7000 [6100,8200]; ~4 bytes/token [2,5]; Google index ~250B pages [100B,1200B].
- Token estimates based on cl100k_base.
- Counterargument lead: Rich Sutton "data scarcity mistake" (need primary verification).

## Topic 3 — energy
- IEA, *Energy and AI* (published 2025-04-10). Primary site www.iea.org repeatedly timed out from this session. Figures reproduced by Peking University Energy Research Institute, 2025-04-21, citing IEA executive summary: https://energy.pku.edu.cn/xsdt/sznyyw/d123q/xnyyw202508/64bdec556620445292f6f21510e8d5a4.htm
  - 2024: data centres ≈ **1.5% of global electricity demand = 415 TWh**
  - 2030: more than double to ≈ **945 TWh** (slightly above Japan's current total electricity consumption)
  - US largest share of growth, then China; data centres ≈ 1/10 of global electricity demand growth to 2030
  - Emissions: 180 Mt today → **300 Mt by 2035** (base case); **500 Mt** (high-emissions scenario)
  - Emerging/developing economies ex-China: 50% of internet users, <10% of data centre capacity
- IEA, *Key Questions on Energy and AI* (April 2026). Report URL: https://www.iea.org/reports/key-questions-on-energy-and-ai (not reachable this session). Figures via Crown Publications / Electricity+Control, 2026-07-16: https://www.crown.co.za/latest-news/electricity-control-latest-news/37355-the-link-between-energy-and-ai
  - Capex of five large tech firms > **$400bn in 2025**, +**75%** expected in 2026
  - Data-centre electricity demand **+17% in 2025**; AI-focused data centres faster; vs **3%** growth in global electricity demand
  - Power consumption per AI task declining; "efficiency improving at a rate unprecedented in energy history"
  - Data-centre electricity consumption **set to double by 2030**; AI-focused power use **to triple**
  - Bottlenecks: gas turbine + transformer supply chains, advanced chips/IT components; planning/regulatory systems strained → grid connection delays
  - Tech sector ≈ **40%** of all corporate renewables PPAs signed in 2025
  - SMR conditional offtake pipeline **25 GW end-2024 → 45 GW** (mid-2026)
  - On-site gas generation mainly US; batteries becoming critical; new IEA government/industry platform announced
  - Quote: Fatih Birol, IEA Executive Director.

## Topic 4 — people
- **Ilya Sutskever**: Dwarkesh Podcast, "We're moving from the age of scaling to the age of research" — 2025-11-26, https://www.dwarkesh.com/p/ilya-sutskever-2 (fetch timed out). Secondary: Business Insider 2025-11 https://www.businessinsider.com/openai-cofounder-ilya-sutskever-scaling-ai-age-of-research-dwarkesh-2025-11 . NOTE: this is **Nov 2025, not 2026**.
- **Yann LeCun**: left Meta 2025; founded AMI. Reuters 2026-03-10: "Ex-Meta AI chief Yann LeCun's AMI raises $1.03 billion for alternative AI approach" https://www.reuters.com/business/ex-meta-ai-chief-yann-lecuns-ami-raises-103-billion-alternative-ai-approach-2026-03-10/ (fetch failed; headline + date from search index). Also AIwire/HPCwire 2026-03-11 https://www.hpcwire.com/aiwire/2026/03/11/yann-lecuns-ami-secures-1b-seed-to-develop-ai-world-models/ ; Sifted https://sifted.eu/articles/yann-lecun-ami-labs-meta-funding-round-nvidia
- **Demis Hassabis**: 20VC podcast ep. published **2026-04-07/08**: "Why LLMs Will Not Commoditise & We Have Not Hit Scaling Laws". Transcript excerpt: "The returns are still very substantial, although they're a bit less than they were, obviously, at the start of all of this scaling... Those labs that have capability to invent new algorithmic ideas are gonna start having bigger advantage over the next few years. The last set of ideas are sort of, you know, all the juices being rung out of them." Source: signalcast.app AI summary/transcript (third-party; flag). AGI within 5 years; 10x industrial revolution at 10x speed.
- **Andrej Karpathy**: Sequoia AI Ascent 2026 talk, "Software 3.0 / from vibe coding to agentic engineering" (~May 2026). lifeboat.com 2026/05 https://lifeboat.com/blog/2026/05/andrej-karpathy-from-vibe-coding-to-agentic-engineering . Needs primary.
- **Sam Altman**: 2026 — "AI Was Held Back By A Generation Of Scientists Who Didn't Believe Scaling Would Work" (officechai, fetch timed out); mixed-news "Sam Altman hits back at AI skeptics who called LLMs a dead end, as science-focused GPT 5.6 launch looms". Also fireside with Chollet at ARC-AGI-3 launch (2026-03-25, Y Combinator HQ).
- **François Chollet**: ARC Prize cofounder + Ndea. Chollet–Altman fireside at ARC-AGI-3 launch 2026-03-25. Fast Company ~2026-03-26 "A top AI researcher explains the limitations of current models" (403).

## Topic 5 — ARC-AGI
Official blog index: https://arcprize.org/blog
- **2026-03-25** "Announcing ARC-AGI-3" https://arcprize.org/blog/arc-agi-3-launch — hundreds of interactive turn-based environments, thousands of levels; no instructions/rules/goals. **Humans 100%, frontier AI 0.51%.** ARC Prize 2026 = $2M+; launch event at Y Combinator HQ with Chollet + Altman fireside. Technical paper: https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf (arXiv 2603.24621).
- **2026-04-14** "Measuring Human Performance on ARC-AGI-3" https://arcprize.org/blog/arc-agi-3-human-dataset
- **2026-05-01** "Analyzing GPT-5.5 & Opus 4.7 with ARC-AGI-3" https://arcprize.org/blog/arc-agi-3-gpt-5-5-opus-4-7-analysis — semi-private scores: **GPT-5.5 0.43%**, **Opus 4.7 0.18%** (standard harness). 135 environments. >1,000,000 games played. Three failure modes: (1) true local effect / false world model; (2) wrong level of abstraction from training data (Tetris/Frogger/Sokoban analogies hijack action selection); (3) solved the level, didn't learn the game.
- **2026-07-06** "ARC Prize 2026: ARC-AGI-3 Milestone Prize #1" https://arcprize.org/blog/arc-prize-2026-milestone-1 — $37.5K milestone through 2026-06-30. 1st Tufa Labs "The Duck" (Qwen 3.6 27B FP8, agent-writes-code REPL); 2nd Reki (Gemma-4-31B VLM-as-policy); 3rd Md Boktiar Mahbub Murad "forge". 2nd/final milestone ends **2026-09-30**.
- **2026-09-03** "OpenAI's GPT-6 Astra on ARC-AGI-3" https://arcprize.org/blog/astra — **GPT-6 Astra 62.7% for $26K (Standard harness, Semi-Private)**; **99.9% for $19K (Provider Adapter harness)**. Action efficiency: fewer actions than human baseline on **96.0%** of levels, **51.7% fewer actions/level on average**. Human baseline from ~500 general-public participants (paid $115/90-min session + $5/game). Astra builds custom algebraic notation + game-specific software libraries. ARC Prize explicitly does NOT claim AGI; ARC-AGI-3 scope "tightly bounded", deterministic, closed-ended. Reviewers incl. Chollet, Knoop, Mazur, Bond, Smith. PRO-LONG harness paper arXiv 2607.20064.
- **ARC-AGI-2**: dataset = 1000 train / 120 public eval / 120 semi-private / 120 private; 85% target. https://arcprize.org/arc-agi/2
- **2025-12-05** "ARC Prize 2025 Results & Analysis" https://arcprize.org/blog/arc-prize-2025-results-analysis
  - Kaggle 1st NVARC **24.03%** ARC-AGI-2 private, $0.20/task; 2nd the ARChitects 16.53%; 3rd MindsAI 12.64%
  - Top verified commercial model: **Opus 4.5 (Thinking, 64k) 37.6%, $2.20/task**
  - Top verified refinement: **Poetiq on Gemini 3 Pro 54%, $30/task** (baseline Gemini 3 Pro 31%, $0.81/task)
  - 1,455 teams / 15,154 entries; 90 papers. Grand Prize unclaimed.
  - ARC Prize states ARC-AGI-1/2 may be being "overfit" via training-data knowledge coverage (Gemini 3 Deep Think used correct ARC color mappings unprompted).
- **ARC Prize 2026 key dates** https://arcprize.org/competitions/2026 — starts 2026-03-25; ARC-AGI-3 Milestone #1 2026-06-30; Milestone #2 2026-09-30; submissions due 2026-11-02; papers 2026-11-08; results **2026-12-04**. $2M, 3 tracks (ARC-AGI-3, ARC-AGI-2, Paper). Internet access unavailable during Kaggle eval; solutions must be open source.
- Note: /leaderboard is JS-rendered; raw HTML gave no numeric rows. Aggregate numbers above come from official blog posts.

## Cross-cutting / to-verify
- Epoch AI 2025–2026 data-stock updates: NOT yet located.
- Synthetic data counterarguments (Phi-4, Nemotron, "textbook quality"): NOT yet located.
- Inference-time compute scaling primary sources beyond R1: o1/o3 ARC numbers exist on 2024-12-20 and 2025-04-22 ARC blog posts.
