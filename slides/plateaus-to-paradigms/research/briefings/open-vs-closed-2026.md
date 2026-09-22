# Open-Weight vs Closed Frontier AI: Verifiable Facts, Jan 2025 – Sep 2026

**Access caveat:** `huggingface.co`, `lmarena.ai`, `github.com`, `openai.com`, `mistral.ai` and `ai.meta.com` were **unreachable here**, so model-card-level verification (exact license strings) was **not possible**. Claims below are labeled `[primary]`, `[secondary]`, or `[could not verify]`.

## 1–2. Open-weight inventory: who leads, release dates, parameters, licenses, context

**Epoch AI's model database** (live-fetched primary aggregator) is the backbone. Its 29 May 2026 insight lists the strongest open-weight models. Its openness labels are the only license information obtained — **no per-model license file could be read** (see Unverified list):

| Model | Org | Release date | Epoch classification | ECI |
|---|---|---|---|---|
| Kimi K2.6 | Moonshot | 2026-04-20 | Open weights (unrestricted) | 151.60 |
| GLM-5.1 | Z.ai (Zhipu) | 2026-04-07 | open weights | 149.94 |
| Kimi K2.5 | Moonshot | 2026-01-27 | Open weights (unrestricted) | 148.22 |
| MiniMax-M2.5 | MiniMax | 2026-02-12 | Open weights (unrestricted) | 147.44 |
| GLM-5 | Z.ai | 2026-02-11 | Open weights (unrestricted) | 146.62 |
| DeepSeek-V3.2 (Thinking) | DeepSeek | 2025-12-01 | Open weights (unrestricted) | 146.46 |
| Qwen3-235B-A22B-Thinking-2507 | Alibaba | 2025-07-25 | Open weights (unrestricted) | 145.81 |
| Kimi K2 Thinking | Moonshot | 2025-11-06 | Open weights (**restricted** use) | 145.60 |
| GLM-4.7 | Z.ai | 2025-12-22 | Open weights (unrestricted) | 144.61 |
| DeepSeek-R1 (May 2025) | DeepSeek | 2025-05-28 | Open weights (unrestricted) | 142.19 |

Source: [Epoch AI, "Open models lag state-of-the-art closed models by 4 months," 29 May 2026](https://epoch.ai/data-insights/open-closed-eci-gap). Also in that table: **Gemma 4 31B IT** (Google, 2026-04-02, *restricted-use* open weights) and **gpt-oss-120b** (OpenAI, 2025-08-05, unrestricted).

**September 2026 state**, from the [DeepInfra](https://deepinfra.com/models/text-generation) hosting catalogue (fresh primary for *availability*, not licensing): **Kimi K3** — Moonshot's "2.8T-parameter open-weight multimodal reasoning model," 1M context; **DeepSeek-V4-Pro** (MoE, **1.6T total / 49B active**, 1M context; official build `DeepSeek-V4-Pro-0813`); **DeepSeek-V4-Flash** (284B/13B, 1M); **DeepSeek-V4.1-Flash** (multimodal MoE, **552B** backbone, 1M); **GLM-5.3 / 5.3-Flash / 5.2**; **Qwen3.8-2.4T-A95B**; **Nemotron-3-Ultra-550B-A55B** and **Nemotron-3-Super-120B-A12B**; **Seed-1.8** (ByteDance). Qwen3-Max and Qwen3-Max-Thinking are hosted-only, i.e. **closed**.

**Qwen3.8** is the best-verified 2026 open release `[secondary, two independent outlets]`: weights opened **12–13 Aug 2026** ([IT之家](https://m.ithome.com/html/989001.htm); [36kr/智东西](https://eu.36kr.com/zh/p/3937078710631810), both 2026-08-13). **2.4T total / 95B active**, 512 experts per MoE layer (10 routed + 1 shared), native **262,144** context extensible to **1,010,000**. First time Qwen open-weighted a *Max*-tier model; hosted **Qwen3.8-Max** shipped 3 Aug 2026. Primary links listed: `modelscope.cn/models/Qwen/Qwen3.8-2.4T-A95B`, `huggingface.co/Qwen/Qwen3.8-2.4T-A95B` (neither reachable here).

**Meta has exited open weights.** Muse Spark, unveiled **April 2026** by Meta Superintelligence Labs, is **cloud-only — no weight downloads or self-hosting**; Llama development is effectively halted with only maintenance promised ([DigitalToday, 2026-05-01](https://www.digitaltoday.co.kr/en/view/52444/meta-open-source-llama-effectively-abandoned-what-are-developers-alternatives), citing The News Stack). Epoch independently classifies **Muse Spark (2026-04-08) as "API access"** — closed. Llama had ~1.2B downloads a year earlier; Andrew Ng called the withdrawal "a big loss to the developer community." **Mistral, Phi and OLMo 3:** `[could not verify]` any 2026 release.

## 3. The measured open–closed gap

Epoch AI's time series is the cleanest quantitative measure:

- **Nov 2024** — "the best open model today is on par with closed models in performance and training compute, but with a lag of about **one year**" ([Epoch report, 2024-11-04](https://epoch.ai/publications/open-models-report)).
- **Oct 2025** — "Open-weight models lag state-of-the-art by around **3 months** on average… an average ECI gap of around **7 points**, similar to the gap between o3 and GPT-5" ([Epoch, 2025-10-30](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models)).
- **May 2026** — "Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of **four months**… The average ECI gap was **8 points**, similar to the gap between GPT-5 and GPT-5.5" ([Epoch, 2026-05-29](https://epoch.ai/data-insights/open-closed-eci-gap)).

So the lag **shrank from ~12 months to ~3, then widened slightly to ~4**. In the May 2026 table, best open (Kimi K2.6, 151.60) vs best closed (**GPT-5.5 Pro xhigh, 159.35**, 2026-04-23) is **~7.8 ECI points**; Claude Opus 4.7 sat at 156.18.

**Benchmark deltas, late 2026** — from Qwen's own published comparisons `[secondary]`: Qwen3.8-Max scored **PaperBench 93.0** and **OSWorld-Verified 86.1**, but trailed on **TerminalBench 2.1 (86.6 vs GPT-5.6 Sol 88.8)**, **SWE-bench Pro (67.7 vs Claude Fable 5's 80.0 and Opus 4.8's 69.2)** and **VideoMME v2 (68.3 vs 71.1)**. A Sept 2026 arXiv paper finds that on public tool-calling benchmarks "open-weight models now approach or even surpass closed-source frontier models in aggregate accuracy," with calibration the residual gap ([arXiv 2609.00949, 2026-09-01](http://arxiv.org/abs/2609.00949)).

**LMArena: `[could not verify]`** — `lmarena.ai` was unreachable and no authoritative rank snapshot was obtained (see Unverified list).

## 4. 2026 lab and policy positions

**US AI Action Plan** — verified verbatim from the primary PDF ([whitehouse.gov](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf), July 2025; announcement [2025-07-23](https://www.whitehouse.gov/articles/2025/07/white-house-unveils-americas-ai-action-plan/)). Pillar I has a dedicated section, **"Encourage Open-Source and Open-Weight AI"**: such models "have unique value for innovation because startups can use them flexibly without being dependent on a closed model provider"; they benefit governments "that have sensitive data that they cannot send to closed model vendors"; "we need to ensure America has leading open models founded on American values"; and "while the decision of whether and how to release an open or closed model is fundamentally up to the developer, the Federal government should create a supportive environment for open models." Actions: improving compute-market access for startups/academics, and **NTIA convening stakeholders to drive SME adoption of open-weight models**. The same document directs NIST/CAISI to publish evaluations of Chinese frontier models "for alignment with Chinese Communist Party talking points and censorship."

**2026 policy turn:** the **American AI Exports Program** (`aiexports.gov`) — ITA call for proposals 10 Apr 2026, 78 applications by July 2026 — explicitly **bars consortia from using open-weight models from "countries of concern," i.e. DeepSeek, Qwen and Kimi**, and requires ≥51% US-made hardware value ([GPPi, 2026-08-20](https://gppi.net/2026/08/20/what-the-american-ai-exports-program-means-for-europe)). GPPi also reports export controls "recently imposed (and later lifted) on Anthropic's most advanced models," plus live Washington debate on restricting **US companies' use of Chinese open-weight models**.

## 5. Cost and distillation

Per-million-token list prices, **16 Sep 2026** ([DeepInfra](https://deepinfra.com/models/text-generation), input/output): **DeepSeek-V4-Flash-0731 $0.06 / $0.18**; V4.1-Flash $0.20 / $0.60; V4-Pro-0813 $1.30 / $2.60; GLM-5.3-Flash $0.075 / $0.25; GLM-5.3 $0.90 / $3.00; Qwen3.8-2.4T-A95B $2.00 / $6.00; Kimi K3 $2.85 / $14.25. Artificial Analysis puts closed leaders far higher on cost-per-task (**Claude Fable 5.1 (max) $7.63**, GPT-6 Astra (max) $3.26) ([AA](https://artificialanalysis.ai/leaderboards/models)).

Sharpest single datapoint: on **OpenDesign Arena (10 Sep 2026)**, DeepSeek V4.1 Flash scored **81.2 vs GPT-6 Astra's 82.7 (~98%)** at **$0.023 vs $1.61 per finished design — ~1.4% of cost** — and 5.3 vs 11.1 minutes; Claude Fable 5.1 scored 80.3 at $3.66 ([DigitalToday, 2026-09-11](https://www.digitaltoday.co.kr/en/view/102509/deepseek-v4-1-flash-nears-gpt-6-astra-performance-at-1-4-percent-of-cost), citing Decrypt). Epoch earlier estimated DeepSeek-R1 "rivals OpenAI's o1 at **30x lower cost**" ([Epoch, 2025-01-31](https://epoch.ai/topics/open-models)).

**Open weights feeding other models:** Salesforce **Koa** was built by RL post-training of the open-weight **Nemotron-3-Super-120B** ([arXiv 2609.15066, 2026-09-14](http://arxiv.org/abs/2609.15066)).

## Unverified / low-confidence

- **LMArena ranks and Elo deltas — not verified.** No primary leaderboard snapshot obtained. The circulating "closed models outperform open-weight by 29 Elo points in 2026" claim appears only on an exchange news-flash page ([KuCoin](https://www.kucoin.com/news/flash/closed-ai-models-outperform-open-weight-models-by-29-elo-points-in-2026)) — **SEO-grade, do not cite.** The "Mozilla report: China's open weights just 4 months behind" ([Yahoo Tech](https://tech.yahoo.com/ai/meta-ai/articles/chinas-open-weight-ai-models-101500311.html)) is secondary and its primary report was unretrievable.
- **Licenses — not verified at model-card level.** Only Epoch's coarse labels ("unrestricted" vs "restricted use") are sourced. A headline claims DeepSeek's V4 vision weights ship under **MIT** ([iheima](http://www.iheima.com/article-401716.html)); the body was unretrievable — **unconfirmed**.
- **OpenAI/Anthropic distillation accusations against DeepSeek (Jan 2025)** — `[could not verify]`; sources gave headlines only (itc.ua returned HTTP 403), no evidentiary findings.
- **AA Intelligence Index for the best *open* model, Sept 2026** — not captured (open-weight rows truncated by the fetch). Closed leaders were Fable 5.1 and GPT-6 Astra at **53**.
- **"ATLAS Act"** and the **"American Innovation and Online Choice Act"** as open-weight legislation — `[could not verify]`; no primary source found.
- **Mistral (Large 3, Magistral, Devstral), Microsoft Phi, Ai2 OLMo 3, Gemma 4 details, Seed-OSS** — `[could not verify]` 2026 status.
- Anthropic model export controls and China's World AI Cooperation Organization — **secondary only** (GPPi).
- SEO/spam-grade 2026 "release" pages (orcarouter.ai, benchlm.ai, llm-stats.com, fastino.ai, swfte.com) were **excluded**.
