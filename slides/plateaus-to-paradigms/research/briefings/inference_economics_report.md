# Inference Economics, 2023 – September 2026

All prices are **USD per 1M tokens (input / output)**, list price for the first-party API unless noted. Prices verified live on **2026-09-16** from first-party pricing pages where reachable, cross-checked against [LiteLLM's dated model-price database](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json) and the [OpenRouter model API](https://openrouter.ai/api/v1/models) (both secondary but systematically maintained and date-stamped). Where a source is an aggregator or a vendor claim it is flagged.

## 1. Frontier API prices and the 10×–100× drops

| Model | Date | Input | Output | Source / note |
|---|---|---|---|---|
| GPT-4 (8K) | 2023-03-14 | $30 | $60 | [LiteLLM](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json) |
| GPT-4 Turbo | 2023-11-06 | $10 | $30 | LiteLLM |
| GPT-4o | 2024-05-13 | $5 | $15 | LiteLLM (`gpt-4o-2024-05-13`) |
| GPT-4o (2024-08-06 refresh) | 2024-08-06 | $2.50 | $10 | LiteLLM — **2× cut** |
| GPT-4o mini | 2024-07-18 | $0.15 | $0.60 | LiteLLM |
| o1-preview / o1 | 2024-09-12 / 2024-12-17 | $15 | $60 | LiteLLM |
| o1-pro | 2025-03-19 | $150 | $600 | LiteLLM — most expensive listing found |
| GPT-4.1 | 2025-04-14 | $2 | $8 | LiteLLM |
| o3 | 2025-04-16 → cut 2025-06-10 | $10→$2 | $40→$8 | [VentureBeat: "80% price drop for o3"](https://venturebeat.com/ai/openai-announces-80-price-drop-for-o3-its-most-powerful-reasoning-model) [SECONDARY] |
| o3-pro | 2025-06-10 | $20 | $80 | LiteLLM |
| GPT-5 | 2025-08-07 | $1.25 | $10 | LiteLLM; date from Azure's [model table](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/) |
| GPT-5.1 | 2025-11-13 | $1.25 | $10 | LiteLLM |
| GPT-5.2 / 5.2-pro | 2025-12-11 | $1.75 / $21 | $14 / $168 | [llm-stats](https://llm-stats.com/models/gpt-5.2-2025-12-11) |
| GPT-5.4 / 5.4-pro | 2026-03-05 | $2.50 / $30 | $15 / $180 | [llm-stats](https://llm-stats.com/models/gpt-5.4) |
| GPT-5.5 / 5.5-pro | 2026-04-23 | $5 / $30 | $30 / $180 | [llm-stats](https://llm-stats.com/models/gpt-5.5) |
| GPT-5.6 luna / sol / terra | 2026-07-09 | $0.20 / $2 / $2 | $1.20 / $10 / $12 | [llm-stats](https://llm-stats.com/models/gpt-5.6-luna); OpenRouter |

| Model | Date | Input | Output | Source |
|---|---|---|---|---|
| Claude 3 Opus | 2024-02-29 | $15 | $75 | LiteLLM (`claude-3-opus-20240229`) |
| Claude 3.5 Sonnet | 2024-06-20 | $3 | $15 | LiteLLM |
| Claude 3.7 Sonnet | 2025-02-19 | $3 | $15 | LiteLLM |
| Claude Sonnet 4 / Opus 4 | 2025-05-14 | $3 / $15 | $15 / $75 | LiteLLM model IDs |
| Claude Opus 4.1 | 2025-08-05 | $15 | $75 | LiteLLM |
| Claude Sonnet 4.5 | 2025-09-29 | $3 | $15 | LiteLLM |
| **Claude Opus 4.5** | 2025-11-01 | **$5** | **$25** | [Anthropic pricing](https://www.anthropic.com/pricing) — **3× cut vs Opus 4/4.1** |
| Claude Opus 4.6 / 4.7 / 4.8 | 2026-02-05 / 2026-04-16 / — | $5 | $25 | LiteLLM + Anthropic pricing |
| Claude Sonnet 5 | 2026-06-30 | $2 | $10 | [llm-stats](https://llm-stats.com/models/claude-sonnet-5) |
| Claude Opus 5 | 2026-07-24 | $5 | $25 | [llm-stats](https://llm-stats.com/models/claude-opus-5) |
| Claude Fable 5 / 5.1 | — | $10 | $50 | [Anthropic pricing](https://www.anthropic.com/pricing) (fetched 2026-09-16) |

Google (via [LiteLLM](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json); **Google's own pricing pages were unreachable from this network** — no first-party confirmation): Gemini 2.5 Pro **$1.25/$10**; Gemini 2.5 Flash **$0.30/$2.50**; Gemini 2.5 Flash-Lite **$0.10/$0.40**; Gemini 3 Pro **$2/$12** (preview); Gemini 3 Flash **$0.50/$3**; Gemini 3.1 Pro **$2/$12**; Gemini 3.5 Flash (2026-05-19) **$1.50/$9**; Gemini 3.6–3.8 Flash **$0.75/$3.75**. Gemini 1.5-series prices (2024) are **COULD NOT VERIFY** from a primary source here.

**Reasoning-token overhead.** Token *price* understates reasoning-model cost because reasoning models emit far more tokens per answer. The [Price of Progress](https://arxiv.org/abs/2511.23455) attributes part of the frontier-cost increase of **3×–18×/yr** explicitly to "larger reasoning demands," and SemiAnalysis measures reasoning-model inference at 4,610 tok/s/GPU (DeepSeek R1) vs 91,089 tok/s/GPU for a 2026 non-reasoning-class model — a ~20× throughput gap. **A precise published multiplier of reasoning tokens per query (e.g. "o1 burns Nx GPT-4o's tokens") was COULD NOT VERIFY in this session.**

**Where the 10×–100× drops happened.** GPT-4 → GPT-4o mini is **200×/100×** in 16 months ($30/$60 → $0.15/$0.60). GPT-4 → GPT-5 is **24×/6×**; GPT-4 → GPT-5.6 luna is **150×/50×**. The o3 80% cut (2025-06-10) is the largest single-day frontier cut found. Anthropic's Opus line cut **3×** on 2025-11-01 and has not fallen since. Notably, **the frontier has re-inflated since 2025**: OpenAI's top model went $1.25/$10 (GPT-5) → $1.75/$14 → $2.50/$15 → **$5/$30** (GPT-5.5), matching the [Price of Progress](https://arxiv.org/abs/2511.23455) finding that frontier *per-token* prices are rising.

## 2. Open / Chinese models and DeepSeek's disclosed costs

| Model | Date | Input | Output | Source |
|---|---|---|---|---|
| DeepSeek-V3 | 2024-12-26 | $0.27 | $1.10 | [LiteLLM](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json) (`deepseek/deepseek-v3`) |
| DeepSeek-R1 | 2025-01-20 | $0.55 | $2.19 | LiteLLM (`deepseek/deepseek-r1`) |
| DeepSeek-V3-0324 | 2025-03-25 | $0.25 | $1.00 | LiteLLM |
| DeepSeek-V3.2-Exp | 2025-09-29 | $0.27 | $0.41 | [DeepSeek changelog](https://api-docs.deepseek.com/updates) |
| DeepSeek-V4.1-Flash | 2026-09-10 | $0.15 off-peak / $0.30 peak | $0.60 / $1.20 | [DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek-V4-Pro | 2026-08-13 GA | $0.66 / $1.32 peak | $1.98 / $3.96 peak | [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing) — peak/off-peak effective 2026-08-16 |

Others (OpenRouter, 2026-09-16): Qwen3.8-Max-0902 **$2/$6**; Qwen3-Max **$0.78/$3.90**; Kimi K3 (2026-07-16) **$3/$15** ([Moonshot via LiteLLM](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json)); Kimi K2 **$0.57–0.60/$2.30–2.50**; GLM-5.3 **$1.40/$4.40**, GLM-5.3-Flash **$0.09/$0.30**; MiniMax M3 **$0.30/$1.20**; Llama 4 Maverick **$0.1875/$0.6525**, Llama 3.3 70B **$0.10/$0.32**.

**DeepSeek's training-cost disclosure — verified verbatim.** Table 1 of the [DeepSeek-V3 Technical Report (arXiv:2412.19437, submitted 2024-12-27)](https://arxiv.org/abs/2412.19437) gives H800 GPU-hours of **2,664K (pre-training) + 119K (context extension) + 5K (post-training) = 2,788K**, and in USD **$5.328M + $0.238M + $0.01M = $5.576M total**, "assuming the rental price of H800 is $2 per GPU hour." **The $294,000 figure for R1 is COULD NOT VERIFY** — it does not appear in the V3 report and I could not trace it to an official DeepSeek statement; treat it as an unverified third-party/analyst figure. **Criticism of the $5.576M number**: it is a marginal compute-rental figure that excludes R&D, ablation and failed runs, salaries, and the GPU capex itself; SemiAnalysis estimated DeepSeek held ~50,000 Hopper GPUs and ~$1.3B of GPU investment **[UNVERIFIED — could not re-source in this session]**. The $2/GPU-hour assumption is also the low end of 2024–25 market rates.

## 3. Inference vs training, and token volumes

**Google's disclosed inference token volume is the best-documented series in the industry** — and it is 330× in two years:

| Date | Google monthly tokens (all products + APIs) | Source |
|---|---|---|
| May 2024 | **9.7 trillion** | [Pichai, Google I/O 2025 keynote, May 2025](https://blog.google/innovation-and-ai/technology/ai/io-2025-keynote/) [PRIMARY] |
| May 2025 (I/O 2025) | **over 480 trillion** ("50 times more") | same — verbatim: *"This time last year, we were processing 9.7 trillion tokens a month across our products and APIs. Now, we're processing over 480 trillion — that's 50 times more."* |
| May 2026 (I/O 2026) | **over 3.2 quadrillion** (~7× YoY) | [CryptoBriefing, 2026-05-22](https://cryptobriefing.com/google-3-2-quadrillion-tokens-monthly/) and [Business Insider](https://www.businessinsider.com/ceo-sundar-pichai-google-ai-growth-io-conference-2026-5), both citing Pichai's I/O 2026 keynote [SECONDARY — blog.google transcript was unreachable from this network] |

Two-year growth = **~330×**; Google also disclosed **~19B tokens/minute via model APIs** and **>375 Cloud customers each processing >1 trillion tokens over the prior 12 months** (I/O 2026). **A "1.3 quadrillion/month" late-2025 figure is COULD NOT VERIFY — the 480T → 3.2Q step is the one the sources support.**

**Microsoft**: on its [FY25 Q3 call (2025-04-30)](https://tomasztunguz.com/earnings-microsoft-2025-04-30/) [SECONDARY, quoting the call] it said it "processed over 100t tokens this quarter, up 5x year over year, including a record 50t tokens last month alone." **A Microsoft "45 trillion tokens" figure is COULD NOT VERIFY** and may be a conflation of the 50T-in-one-month statement.

**Inference vs training split**: no hard, sourced percentage was verified. The direction is well attested — by CES 2026 the framing had shifted to "[AI compute sees a shift from training to inference](https://www.computerworld.com/article/4114579/ces-2026-ai-compute-sees-a-shift-from-training-to-inference.html)" [SECONDARY] — but **do not quote a percentage without a primary source**; be careful to distinguish compute (FLOPs), spend, and revenue shares, which differ by a lot.

## 4. Utilization, depreciation, and GPU rental prices

**Burry (2025-11-10/11).** Michael Burry posted on X that hyperscalers were "[u]nderstating depreciation by extending useful life of assets" and that chips on a "2-3 yr product cycle" should not get extended lives; he estimated **~$176B of understated depreciation**, but per [CNBC (2025-11-11)](https://www.cnbc.com/2025/11/11/big-short-investor-michael-burry-accuses-ai-hyperscalers-of-artificially-boosting-earnings.html) that figure covers **2026–2028, not 2023–2028** as commonly misquoted. He claimed Oracle's profits could be overstated ~27% and Meta's ~21% by 2028 [SECONDARY].

**The filings cut against the blanket claim — and this is the strongest available rebuttal** [PRIMARY, SEC]:
- **Alphabet**: extended servers/network equipment **4 → 6 years** in Jan 2023, worth **−$3.9B depreciation in FY2023** ([FY2023 10-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204424000022/goog-20231231.htm)); still **six years** in the [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000018/goog-20251231.htm). No subsequent extension.
- **Microsoft**: **4 → 6 years** in July 2022, worth **+$3.7B operating income in FY2023** ([FY2023 10-K](https://www.sec.gov/Archives/edgar/data/0000789019/000095017023035122/msft-20230630.htm)); the [FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm) discloses a **"two to six years"** range — a 2-year lower bound.
- **Meta**: extended to **5.5 years** in Jan 2025, worth **+$2.59B net income in 2025** ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/0001326801/000162828026003942/meta-20251231.htm)).
- **Amazon went the other way**: shortened a subset of servers **6 → 5 years** effective 2025-01-01, costing **+$1.4B depreciation and −$1.0B net income in 2025, "primarily impact[ing] our AWS segment"** ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000004/amzn-20251231.htm)).

**Rental prices (all fetched 2026-09-16)** — the "$8/hr → $2/hr" story is a **tier-mixing artifact**:

| Provider / tier | H100 | H200 | B200 | B300 |
|---|---|---|---|---|
| [Lambda](https://lambda.ai/pricing) on-demand | $3.99–4.29 | delisted | $6.69–6.99 | — |
| [RunPod](https://www.runpod.io/pricing) (page updated 2026-09-13) | $2.89–3.49 | $4.59 | $6.79 | **$7.89** |
| [Nebius](https://nebius.com/prices) on-demand / preemptible | $3.85 / **$2.15** | $4.50 / $2.45 | $7.15 / $3.95 | $7.85 / $4.30 |
| AWS p5/p6 (Vantage mirror of AWS Price List API) on-demand / spot | **$6.88** / $2.60 | $7.91 / $3.39 | **$14.24** / $5.26 | — |

So ~$2/GPU-hr H100 is real **only in spot/preemptible tiers**; hyperscaler on-demand H100 is still **$6.88**. SemiAnalysis's [AI Cloud TCO model](https://inferencex.semianalysis.com/chips/h100) prices H100 at **$1.17/GPU-hr** at hyperscaler volume and **$2.00** retail (H200 $1.22/$2.90; B200 $1.73/$3.70; GB200 NVL72 $1.86/$4.00; GB300 NVL72 $2.31/$5.00; MI300X $0.95/$1.30; MI355X $1.50/$2.90) [THIRD-PARTY]. **The original "$8/hr in 2023" anchor and any 2026 "H100 rents rose ~30%" report are COULD NOT VERIFY.** No Google TPU utilization figure or MFU percentage was verified.

## 5. Price-per-intelligence

Two independent estimates, both showing very fast decline in **cost to reach a fixed capability level**, while **frontier per-token prices rise**:

| Finding | Value | Source |
|---|---|---|
| Price to reach GPT-4's GPQA performance | **40×/yr** decline | [Epoch AI, 2025-03-12](https://epoch.ai/data-insights/llm-inference-price-trends) |
| Range across 6 benchmarks/thresholds | **9×–900×/yr**, median **50×/yr** | Epoch AI, 2025-03-12 |
| Median after dropping pre-2024 data | **200×/yr** | Epoch AI, 2025-03-12 |
| Frontier cost for a fixed benchmark level | **5×–10×/yr** decline | [arXiv:2511.23455](https://arxiv.org/abs/2511.23455) (v1 2025-11-28, v2 2026-03-23) |
| Algorithmic efficiency (open models, hardware-adjusted) | **~3×/yr** | same |
| Cost of running *frontier* models | **rising 3×–18×/yr** | same |
| GPQA-Diamond, top performance bin vs lowest bin | **31×/yr vs 1.7×/yr** | same |

The two sources agree on direction and disagree in magnitude (Epoch 50×/yr median vs 5–10×/yr) because Epoch measures the cheapest model above a threshold while the paper measures the frontier Pareto bin — **say which you mean**. Both use [Artificial Analysis](https://artificialanalysis.ai/) price snapshots.

## 6. Inference hardware economics

SemiAnalysis **InferenceX** — measured $/M tokens at hyperscaler GPU pricing, re-benchmarked continuously (all values 2026-09-16) [THIRD-PARTY]:

| Model | Cheapest platform | $/M tokens | Fastest tok/s/GPU |
|---|---|---|---|
| DeepSeek V4.1 Flash | GB200 NVL72 | **$0.006** | 91,089 (B300) |
| DeepSeek V4 Pro | B200 | $0.011 | 57,850 (B300) |
| gpt-oss-120b | B200 | $0.011 | 44,489 (B200) |
| Qwen3.5 | B300 | $0.036 | 17,277 (B300) |
| Kimi K3 | GB300 NVL72 | $0.038 | 16,762 (GB300) |
| MiniMax M2.7 | GB200 NVL72 | $0.041 | 13,707 (GB300) |
| GLM-5.3 | MI355X | $0.061 | 6,779 (MI355X) |
| DeepSeek R1 | B200 | $0.10 | 4,610 (B200) |

**GB300 vs MI355X head-to-heads** ([InferenceX comparisons](https://inferencex.semianalysis.com/compare/deepseek-r1-gb300-vs-mi355x), 2026-09-16): GB300 NVL72 delivers **+148% tok/s/chip and is 61% more cost-efficient than MI355X on DeepSeek R1**; **+197% / +93% on DeepSeek V4.1 Flash**; **+336% / +183% on GLM-5.3**. **But MI355X wins on DeepSeek V4 Pro vs GB200 NVL72 (+313% tok/s/chip, +412% cost-efficiency for AMD)** — the sign flips by model, which is the honest headline. Other measured points: **GB300 NVL72 vs GB200 NVL72 on DeepSeek-V4-Pro FP4 at 27 tok/s/user = $0.12/M vs $0.28/M (2.31× cheaper)**, but at peak they **tie at ~$0.07/M** (GB300's 20% per-GPU-hour TCO premium eats the throughput gain) ([InferenceX, measured 2026-05-22](https://inferencex.semianalysis.com/blog/gb300-nvl72-vs-gb200-nvl72-dsv4-pro-vllm-fp4)); **B200 NVFP4 vs H100 FP8 on MiniMax-M2.5 at 110 tok/s/user = $0.09 vs $0.74/M (8.2×)**; **TPUv7 Ironwood $0.181/M vs B200 $0.222 and B300 $0.276 at 100 tok/s/user** ([TPU InferenceX](https://inferencex.semianalysis.com/blog/tpu-inferencex-full-steam)); **speculative decoding (MTP) alone moved DeepSeek-R1 FP4 from $0.251/M to $0.057/M** ([InferenceX v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper)).

**Vendor claims, flagged:** at GTC 2026 NVIDIA claimed GB300 NVL72 (FP4, MTP) gives **50× higher tokens-per-watt and 35× lower cost-per-token than Hopper FP8** — available to me only second-hand via [AMD's rebuttal (2026-03-18)](https://www.amd.com/en/developer/resources/technical-articles/2026/the-many-aspects-of-inference-performance.html) [VENDOR, definition unverified]. AMD counter-claims MI355X is cheaper per token than GB300 at 60+ TPS/user with FP8 and no MTP [VENDOR; AMD's figures are chart images with no extractable numbers]. **Both vendors cite the same InferenceX benchmark against each other, each picking its own operating point** — that is itself the most useful slide in this section.
