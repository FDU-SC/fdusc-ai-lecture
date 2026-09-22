# Research: InferenceX / Inference Hardware Economics

_Scraped 2026-09-16. All figures quoted verbatim from source; flags: [VENDOR] = self-reported by NVIDIA/AMD, [THIRD-PARTY] = SemiAnalysis/MLPerf, [UNVERIFIED] = could not confirm._

## 1. InferenceX (SemiAnalysis) — live ranking pages

Source: sitemap `https://inferencex.semianalysis.com/sitemap.xml` (2,442 `<loc>`, downloaded 2026-09-16).
Page path breakdown: 338 `/compare`, 338 `/compare-per-dollar`, 168 `/glossary`, 97 `/run`, 65 `/compare-spec-decode`,
41 `/compare-precision`, 33 `/blog`, 27 `/rankings`, 22 `/chips`, 14 `/inference`, 14 `/agentx`, 13 `/historical`,
13 `/calculator`, 13 `/model`, 5 `/profit-estimator-per-gigawatt`, 5 `/profit-estimator`.
_(Each path is duplicated under `/zh/` — 1,221 Chinese URLs.)_

**Method note:** the ranking pages are client-rendered React, BUT the headline figures are present in
`<meta name="description">` / `og:description` server-side. Extracted 2026-09-16 with:
`curl -sL -m 25 "URL" | grep -oE '<meta name="description" content="[^"]*"'`
The raw HTML also contains the winner figures inline (e.g. 14x `$0.038` on the Kimi K3 page), but the
full ranked table is not in the server HTML. [THIRD-PARTY]

### 1a. Cheapest $/million tokens — headline winners (as of 2026-09-16)

| Model | Cheapest platform | $/M tokens | Platforms ranked | URL |
|---|---|---|---|---|
| DeepSeek V4.1 Flash | GB200 NVL72 | $0.006 | 4 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-deepseek-v41-flash) |
| DeepSeek V4 Pro | B200 | $0.011 | 4 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-deepseek-v4) |
| gpt-oss-120b | B200 | $0.011 | 2 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-gptoss-120b) |
| Qwen3.5 | B300 | $0.036 | 5 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-qwen-3-5) |
| Kimi K3 | GB300 NVL72 | $0.038 | 5 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-kimi-k3) |
| MiniMax M2.7 | GB200 NVL72 | $0.041 | 5 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-minimax-m27) |
| GLM-5.3 | MI355X | $0.061 | 1 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-glm-5-3) |
| Llama 3.3 70B | B200 | $0.078 | 2 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-llama-3-3-70b) |
| DeepSeek R1 | B200 | $0.10 | 5 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-deepseek-r1) |
| Kimi K2.6 | GB200 NVL72 | $0.11 | 5 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-kimi-k26) |
| GLM-5 | B200 | $0.17 | 5 | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-glm-5-1) |
| MiniMax M3 | _not stated_ | — | — | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-minimax-m3) |
| Qwen3.8-Flash-Next | _not stated_ | — | — | [link](https://inferencex.semianalysis.com/rankings/cheapest-gpu-for-qwen-3-8-flash-next) |

Note on semantics: "hyperscaler GPU pricing" is the cost basis ("measured $ per million tokens at hyperscaler GPU pricing").

### 1b. Fastest tokens/s per GPU — headline winners (as of 2026-09-16)

| Model | Fastest platform | tok/s/GPU | Platforms ranked | URL |
|---|---|---|---|---|
| DeepSeek V4.1 Flash | B300 | 91,089 | 4 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-deepseek-v41-flash) |
| DeepSeek V4 Pro | B300 | 57,850 | 4 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-deepseek-v4) |
| gpt-oss-120b | B200 | 44,489 | 2 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-gptoss-120b) |
| Qwen3.5 | B300 | 17,277 | 5 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-qwen-3-5) |
| Kimi K3 | GB300 NVL72 | 16,762 | 5 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-kimi-k3) |
| MiniMax M2.7 | GB300 NVL72 | 13,707 | 5 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-minimax-m27) |
| GLM-5.3 | MI355X | 6,779 | 1 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-glm-5-3) |
| Llama 3.3 70B | B200 | 6,127 | 2 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-llama-3-3-70b) |
| Kimi K2.6 | GB300 NVL72 | 5,601 | 5 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-kimi-k26) |
| DeepSeek R1 | B200 | 4,610 | 5 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-deepseek-r1) |
| GLM-5 | B300 | 2,988 | 5 | [link](https://inferencex.semianalysis.com/rankings/fastest-gpu-for-glm-5-1) |

## 2. SemiAnalysis "AI Cloud TCO model" cloud pricing — $/GPU-hour (from /chips/ FAQ JSON-LD)

These are the cost basis behind every InferenceX perf-per-dollar page. Quoted from the `FAQPage` JSON-LD
embedded server-side in each `/chips/<part>` page: *"The SemiAnalysis AI Cloud TCO model rates X at about
$A/hr when owned at large hyperscaler volume and $B/hr at the retail tier."* [THIRD-PARTY]

| Chip | Hyperscaler-volume TCO $/hr | Retail tier $/hr | URL |
|---|---|---|---|
| H100 SXM | **$1.17** | $2.00 | [chips/h100](https://inferencex.semianalysis.com/chips/h100) |
| H200 SXM | **$1.22** | $2.90 | [chips/h200](https://inferencex.semianalysis.com/chips/h200) |
| B200 | **$1.73** | $3.70 | [chips/b200](https://inferencex.semianalysis.com/chips/b200) |
| B300 | **$2.26** | $4.25 | [chips/b300](https://inferencex.semianalysis.com/chips/b300) |
| GB200 NVL72 (per GPU) | **$1.86** | $4.00 | [chips/gb200-nvl72](https://inferencex.semianalysis.com/chips/gb200-nvl72) |
| GB300 NVL72 (per GPU) | **$2.31** | $5.00 | [chips/gb300-nvl72](https://inferencex.semianalysis.com/chips/gb300-nvl72) |
| MI300X | **$0.95** | $1.30 | [chips/mi300x](https://inferencex.semianalysis.com/chips/mi300x) |
| MI325X | **$1.10** | $1.60 | [chips/mi325x](https://inferencex.semianalysis.com/chips/mi325x) |
| MI355X | **$1.50** | $2.90 | [chips/mi355x](https://inferencex.semianalysis.com/chips/mi355x) |

**Implied per-GPU-hour cost ratio (hyperscaler tier):** GB300 NVL72 $2.31 is **1.33x** B200 ($1.73),
**1.24x** GB200 NVL72 ($1.86), and **1.54x** MI355X ($1.50). MI355X is the cheapest per-GPU-hour
Blackwell-class part in the model.

### Alternative TCO figures quoted in SemiAnalysis blog prose (different scenarios, do not mix with the above)
- Vera Rubin NVL72 **$3.57 per GPU-hour** vs GB200 NVL72 **$1.84** and GB300 NVL72 **$2.36** —
  "operator ownership scenario (not rental prices)", all-in TCO ÷ renormalized output throughput
  ([vera-rubin-nvl72-vs-gb200-nvl72-inference](https://inferencex.semianalysis.com/blog/vera-rubin-nvl72-vs-gb200-nvl72-inference), 2026)
- GB200 NVL72 **$2.21** vs B200 **$1.95 per GPU-hour** — a "13% per-GPU TCO premium" for GB200 NVL72
  ([gb200-nvl72-vs-b200-disagg-deepseek-r1-fp4-dynamo-trt](https://inferencex.semianalysis.com/blog/gb200-nvl72-vs-b200-disagg-deepseek-r1-fp4-dynamo-trt))
- TPUv7 Ironwood costed at **$1.03 per chip-hour** ("Google internal TCO") vs B200 and B300
  ([tpu-inferencex-full-steam](https://inferencex.semianalysis.com/blog/tpu-inferencex-full-steam))

**Caveat:** the /chips/ $/hr model numbers and the blog-prose $/GPU-hour numbers are *different scenarios*
(hyperscaler purchase vs operator ownership, per-GPU vs whole-rack amortization) and SemiAnalysis does not
reconcile them across posts. Do not average them.

## 3. GB300 NVL72 vs GB200 NVL72 on DeepSeek-V4-Pro 1.6T FP4 — full measured table [THIRD-PARTY]

URL: [blog/gb300-nvl72-vs-gb200-nvl72-dsv4-pro-vllm-fp4](https://inferencex.semianalysis.com/blog/gb300-nvl72-vs-gb200-nvl72-dsv4-pro-vllm-fp4)
Setup: DSv4-Pro FP4, ISL 8192 / OSL 1024, NVL72, Dynamo vLLM, disaggregated prefill/decode, no speculative
decoding, **measured on InferenceX 2026-05-22** (GHA run 26306422380).
Cost formula: `TCO_$/GPU/hr × 1e6 / (3600 × tput_per_gpu)`; **GB200 NVL72 = $2.21/GPU/hr, GB300 NVL72 = $2.65/GPU/hr**
per the SemiAnalysis AI Cloud TCO Model (= a **20% per-GPU TCO premium** for GB300).

### Matched-interactivity Pareto comparison (interpolated) — the headline result
| tok/s/user | GB200 tok/s/GPU | GB300 tok/s/GPU | GB300/GB200 tput | GB200 $/M tok | GB300 $/M tok | GB200/GB300 cost |
|---|---|---|---|---|---|---|
| 16 | 8,835 | 10,608 | 1.20x | $0.07 | $0.07 | 1.00x |
| 18 | 8,366 | 10,094 | 1.21x | $0.07 | $0.07 | 1.01x |
| 20 | 7,283 | 9,401 | 1.29x | $0.08 | $0.08 | 1.07x |
| 22 | 5,650 | 8,562 | 1.52x | $0.11 | $0.08 | 1.31x |
| 25 | 2,846 | 7,208 | 2.53x | $0.21 | $0.10 | 2.11x |
| **27** | **2,189** | **6,182** | **2.83x** | **$0.28** | **$0.12** | **2.31x** |

**Headline: GB300 NVL72 is 2.31x cheaper per million tokens than GB200 NVL72 at 27 tok/s/user, and up to 2.83x
more throughput per GPU.** At peak the two are essentially tied on cost: GB200 peak **8,933 tok/s/GPU at 15.3
tok/s/user = $0.07/M**; GB300 peak **11,056 tok/s/GPU at 13.1 tok/s/user = $0.07/M** ("essentially tied
($0.069 vs $0.067) because GB300's 20% TCO premium eats most of the 1.24x throughput lift").

### Raw frontier points — GB200 NVL72 (Dynamo vLLM)
| Conc | Prefill | Decode | tok/s/GPU | tok/s/user | TPOT ms | $/M tok |
|---|---|---|---|---|---|---|
| 1 | 8 GPU TP=8 | 8 GPU EP=1 | 32.8 | 74.13 | 13.26 | $18.72 |
| 256 | 8 GPU TP=8 | 32 GPU EP=1 | 1,613.8 | 32.69 | 30.83 | $0.38 |
| 512 | 8 GPU TP=8 | 32 GPU EP=1 | 2,004.5 | 28.31 | 35.46 | $0.31 |
| 256 | 8 GPU TP=8 | 8 GPU EP=8 | 3,148.0 | 24.42 | 41.23 | $0.20 |
| 512 | 8 GPU TP=8 | 8 GPU EP=8 | 5,336.2 | 21.26 | 47.43 | $0.10 |
| 1024 | 8 GPU TP=8 | 8 GPU EP=8 | 6,036.2 | 21.60 | 46.42 | $0.10 |
| 4096 | 16 GPU TP=8 | 8 GPU EP=8 | 8,153.1 | 18.51 | 54.34 | $0.08 |
| 4096 | 24 GPU TP=8 | 8 GPU EP=8 | 8,933.0 | 15.26 | 66.26 | $0.07 |

### Raw frontier points — GB300 NVL72 (Dynamo vLLM)
| Conc | Prefill | Decode | tok/s/GPU | tok/s/user | TPOT ms | $/M tok |
|---|---|---|---|---|---|---|
| 18 | 4 GPU TP=4 | 68 GPU EP=1 | 138.8 | 73.43 | 13.58 | $5.31 |
| 192 | 4 GPU TP=4 | 24 GPU EP=1 | 1,920.0 | 36.78 | 27.44 | $0.38 |
| 3072 | 28 GPU TP=8 | 32 GPU EP=16 | 6,812.0 | 25.91 | 38.77 | $0.11 |
| 4096 | 16 GPU TP=8 | 8 GPU EP=8 | 10,214.0 | 17.58 | 57.12 | $0.07 |
| 4096 | 20 GPU TP=8 | 8 GPU EP=8 | 10,853.1 | 14.74 | 69.17 | $0.07 |
| 4096 | 24 GPU TP=8 | 8 GPU EP=8 | 11,055.6 | 13.12 | 77.83 | $0.07 |

**Mechanism (quoted):** "At 1.6T params, DSv4-Pro's FP4 weights alone are about 800 GB... GB300's 1.5x HBM
capacity (288 vs 192 GB/GPU) holds the same model on the same shape with hundreds of GB of headroom to spare."
Also: NVLink 5 scale-up = 900 GB/s per GPU uni-di / 1.8 TB/s bi-di; scale-out RoCEv2/IB = 50 GB/s per GPU
uni-di — **18x slower**, which is why wide EP needs the rack-scale NVLink island.

## 4. Cross-platform $/million-token measurements from InferenceX blog posts [THIRD-PARTY]

**IMPORTANT — two different TCO vintages.** The `/chips/` pages (§2) and the May-2026 blog posts use
*different* $/GPU/hr sets. Blog-era set: **H100 $1.30, H200 $1.41, B200 $1.95, GB200 NVL72 $2.21,
GB300 NVL72 $2.65, MI355X $1.48 per GPU-hour.** All blog posts cite "the SemiAnalysis AI Cloud TCO Model"
with formula `$/M tok = TCO_$/GPU/hr × 1e6 / (3600 × tput_per_gpu)` (non-disagg) or
`TCO_$/GPU/hr / (3600 × tput_per_gpu / 1e6)` (same thing). Where an article quotes two $/GPU/hr values in a
table it is comparing the two SKUs in that article, not contradicting §2.

### 4a. Head-to-head iso-interactivity $/M-token results

| Model / workload | Winning SKU | Losing SKU | Ratio | Date measured | URL |
|---|---|---|---|---|---|
| DeepSeek-V4-Pro FP4 8K/1K, at 27 tok/s/user | GB300 NVL72 **$0.12/M** (6,182 tok/s/GPU) | GB200 NVL72 **$0.28/M** (2,189 tok/s/GPU) | GB300 **2.31x** cheaper | 2026-05-22 | [link](https://inferencex.semianalysis.com/blog/gb300-nvl72-vs-gb200-nvl72-dsv4-pro-vllm-fp4) |
| DeepSeek-V4-Pro, peak throughput | GB200 **$0.07/M** @ 8,933 tok/s/GPU, 15.3 tok/s/user | GB300 **$0.07/M** @ 11,056 tok/s/GPU, 13.1 tok/s/user | tied ($0.069 vs $0.067) | 2026-05-22 | [link](https://inferencex.semianalysis.com/blog/gb300-nvl72-vs-gb200-nvl72-dsv4-pro-vllm-fp4) |
| GLM-5 8K/1K at 80 tok/s/user | B200 NVFP4 **$0.29/M** | H200 FP8 **$1.06/M** | B200 **3.65x** better perf/$ | 2026-05-25 (SGLang v0.5.12) | [link](https://inferencex.semianalysis.com/blog/b200-glm5-nvfp4-vs-h200-fp8-3-6x-perf-per-dollar) |
| GLM-5, whole H200 range 25–84 tok/s/user | B200 NVFP4 | H200 FP8 | 3.24x–3.65x band | 2026-05-25 | [link](https://inferencex.semianalysis.com/blog/b200-glm5-nvfp4-vs-h200-fp8-3-6x-perf-per-dollar) |
| MiniMax-M2.5 8K/1K at 110 tok/s/user | B200 NVFP4 **$0.09/M** | H100 FP8 **$0.74/M** | B200 **8.2x** | 2026-05-22 (vLLM) | [link](https://inferencex.semianalysis.com/blog/b200-minimax-m2-5-vllm-nvfp4-vs-h100-fp8-perf-per-dollar) |
| MiniMax-M2.5 at 22 tok/s/user | B200 NVFP4 **$0.031/M** | H100 FP8 **$0.12/M** | 4.0x (low end) | 2026-05-22 | [link](https://inferencex.semianalysis.com/blog/b200-minimax-m2-5-vllm-nvfp4-vs-h100-fp8-perf-per-dollar) |
| Kimi K2.5/K2.6 8K/1K at 32 tok/s/user | B200 NVFP4 **$0.140/M** | H200 INT4 **$0.413/M** | **2.95x** (66% reduction) | 2026-05-19 | [link](https://inferencex.semianalysis.com/blog/b200-nvfp4-vs-h200-int4-kimi-k2-vllm-perf-per-dollar) |
| Kimi K2.5/K2.6, 30–90 tok/s/user band | B200 NVFP4 | H200 INT4 | 2.71x–2.95x | 2026-05-19 | [link](https://inferencex.semianalysis.com/blog/b200-nvfp4-vs-h200-int4-kimi-k2-vllm-perf-per-dollar) |
| Kimi K2.5/K2.6 at 40 tok/s/user, INT4→NVFP4 on same B200 | B200 NVFP4 **$0.154/M** | B200 INT4 **$0.397/M** | 2.45x–2.74x | 2026-05-19 | [link](https://inferencex.semianalysis.com/blog/b200-nvfp4-vs-h200-int4-kimi-k2-vllm-perf-per-dollar) |
| GLM-5 FP8 8K/1K at 18 tok/s/user, with MTP | **MI355X $0.22/M** | B200 $0.30/M | MI355X **1.41x** cheaper (40%) | 2026-05-20 (SGLang v0.12) | [link](https://inferencex.semianalysis.com/blog/mi355x-glm5-fp8-sglang-40-cheaper-than-b200) |
| GLM-5 FP8 at 10 tok/s/user, no MTP | MI355X $0.23/M | B200 $0.31/M | 1.36x | 2026-05-20 | [link](https://inferencex.semianalysis.com/blog/mi355x-glm5-fp8-sglang-40-cheaper-than-b200) |
| TPUv7 Ironwood FP8, 100 tok/s/user | **TPU $0.181/M** | B200 $0.222/M; B300 $0.276/M | 19% < B200, 34% < B300 | 2026 (Official Preview) | [link](https://inferencex.semianalysis.com/blog/tpu-inferencex-full-steam) |
| TPUv7 Ironwood, 20 s median response | TPU **$0.098/M** | B200 $0.106/M; B300 $0.132/M | 8% < B200, 25% < B300 | 2026 | [link](https://inferencex.semianalysis.com/blog/tpu-inferencex-full-steam) |
| TPUv7 vs NVIDIA at conc 256 (TPU TCO $1.03/chip-hr) | TPU perf/$ | B200 / B300 | +76.7% vs B200, +130.2% vs B300 (but TTFT 5.41 s vs 3.75 s / 2.40 s) | 2026 | [link](https://inferencex.semianalysis.com/blog/tpu-inferencex-full-steam) |

### 4b. Effect of MTP / speculative decoding (same silicon, same article)
- DeepSeek-R1-0528 FP4, 8k/1k: **$0.251/M total tokens → $0.057/M with MTP** enabled
  ([inferencex-v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper), 2026).
- DeepSeek R1 FP4 8k/1k, GB300 Dynamo TRT at 150 tok/s/user: **~$2.35/M baseline → ~$0.11/M with MTP = ~21x**
  (same URL).
- DeepSeek R1 0528 FP4 on B200 + TRT-LLM: **~$0.56/M output tokens at 50 tok/s/user → ~$4/M output tokens at
  125 tok/s/user** ("2.5x speed for a ~7x price increase") (same URL).

### 4c. Other exact tok/s/GPU and $/M figures worth keeping
- **GB200 NVL72 vs B200 on Kimi K2.5**, 8k/1k NVFP4, Dynamo vLLM wide EP: peak throughput **4,021 → 12,587
  tok/s/GPU** (3.1x) at Decode EP 16
  ([gb200-nvl72-kimi-k2-5-vllm-wide-ep-3x-vs-b200](https://inferencex.semianalysis.com/blog/gb200-nvl72-kimi-k2-5-vllm-wide-ep-3x-vs-b200)).
- **GB200 NVL72 vs B200 on DeepSeek R1 670B** FP4, Dynamo TRT, disagg: up to **4.4x more per-GPU throughput at
  125 tok/s/user** (72-GPU NVLink enables wide EP=32)
  ([gb200-nvl72-vs-b200-disagg-deepseek-r1-fp4-dynamo-trt](https://inferencex.semianalysis.com/blog/gb200-nvl72-vs-b200-disagg-deepseek-r1-fp4-dynamo-trt)).
- **GB300 NVL72 vs GB200 NVL72, DeepSeek-V4-Pro**: up to **2.83x throughput per GPU**, up to **2.31x perf/$**, GB300 adds 50% HBM.
- **DeepSeekV4 1.6T on GB300 with MTP: $0.156 per million output tokens at 50 tok/s/user** (8k in / 1k out)
  ([deepseekv4-16t-day-0-to-day-43-performance](https://inferencex.semianalysis.com/blog/deepseekv4-16t-day-0-to-day-43-performance)).
- **Vera Rubin NVL72: $4.18 per million output tokens at 350 tok/s/user** — the only SKU able to serve past
  300 tok/s/user (GB200 stops at 250, GB300 at 300)
  ([vera-rubin-nvl72-vs-gb200-nvl72-inference](https://inferencex.semianalysis.com/blog/vera-rubin-nvl72-vs-gb200-nvl72-inference)).
- **MI355X DeepSeek-V4-Pro on SGLang: 110.5x throughput/GPU in 26 days, 20 → 2,256 tok/s/GPU**, 8K/1K, via
  TileLang + sparse MLA + FP4; MI355X TCO held at $1.48/GPU/hr the whole time
  ([mi355x-deepseek-v4-pro-sglang-110x-in-26-days](https://inferencex.semianalysis.com/blog/mi355x-deepseek-v4-pro-sglang-110x-in-26-days)).
- **MI355X Qwen3.5 397B-A17B FP8 SGLang: 1.3k → 6.4k tok/s/GPU (19x) in 3 months** at $1.48/GPU/hr
  ([mi355x-qwen3-5-sglang-v0-5-12-up-to-17x](https://inferencex.semianalysis.com/blog/mi355x-qwen3-5-sglang-v0-5-12-up-to-17x)).
- **B200 SGLang 0.5.6 DeepSeek R1 FP4: 508 → 907 tok/s/GPU** on the same 16-GPU B200 pool (1.8x)
  ([sglang-0-5-6-b200-deepseek-r1-fp4-up-to-1-8x](https://inferencex.semianalysis.com/blog/sglang-0-5-6-b200-deepseek-r1-fp4-up-to-1-8x)).
- **B300 FP4 = 12x performance/$ of H100** on Qwen3.5 397B AgentX, 256k truncated agentic trace replay
  ([qwen3-5-397b-agentx-b300-fp4-vs-h100](https://inferencex.semianalysis.com/blog/qwen3-5-397b-agentx-b300-fp4-vs-h100)).
- **NVIDIA >20x better than AMD on Qwen3.5 397B at 90 tok/s/user, SGLang-vs-SGLang**
  ([qwen3-5-397b-agentx-nvidia-vs-amd-sglang](https://inferencex.semianalysis.com/blog/qwen3-5-397b-agentx-nvidia-vs-amd-sglang)).
- **NVIDIA up to 5x cheaper per token at 150 tok/s/user on GLM 5.3 AgentX** — "a gap so large that free
  competitor hardware would still leave NVIDIA cheaper per token"
  ([glm-5-3-agentx-nvidia-vs-amd-sglang-150-toks](https://inferencex.semianalysis.com/blog/glm-5-3-agentx-nvidia-vs-amd-sglang-150-toks)).
- **MI355X ATOM beats GB300 NVL72 on part of the curve** on GLM 5.3 and on Kimi K3 (between 40 and 60 s
  end-to-end latency)
  ([kimi-k3-agentx-mi355x-atom-vs-gb300-nvl72](https://inferencex.semianalysis.com/blog/kimi-k3-agentx-mi355x-atom-vs-gb300-nvl72)).
- **MI355X Kimi K2.5 on vLLM: 7.7x throughput, up to 15x interactivity in 25 days** (vLLM PR #35850, AITER MLA dispatch)
  ([mi355x-kimi-k2-5-vllm-aiter-7x-speedup](https://inferencex.semianalysis.com/blog/mi355x-kimi-k2-5-vllm-aiter-7x-speedup)).
- **B200 vs B300 AgentX on DeepSeek V4 Pro**: TCO-normalized throughput close, but **91% HBM KV cache hit
  rate on B300 vs 73% on B200**, KV working set **43M tokens (B300) vs 22M (B200)**
  ([deepseek-v4-pro-agentx-b200-vs-b300-kv-working-set](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-b200-vs-b300-kv-working-set)).
- **DeepSeek V4 Pro AgentX, MI355X SGLang vs B200 vLLM**: MI355X matched B200 on perf/$ until **August 21,
  2026**, when vLLM optimizations from Inferact and NVIDIA put B200 ahead
  ([deepseek-v4-pro-agentx-mi355x-vs-b200-august](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-mi355x-vs-b200-august)).
- **OpenRouter market pricing (2026)**: Crusoe serves at 36 tok/s/user at **$1.35/M input, $5.40/M output**;
  Nebius AI Studio (Fast) serves DeepSeek FP4 at 167 tok/s/user at **$2/M input, $6/M output**
  ([inferencex-v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper)).
  SemiAnalysis' implied cost for Crusoe: "no more than $0.226/M input and $2.955/M output" → up to 83% gross
  margin on input, 45% on output.
- **Kimi K3 provider floor on OpenRouter as of 30 July 2026: $3/M input, $15/M output** — all providers
  ([kimi-k3-the-manos-the-mythos-the](https://inferencex.semianalysis.com/blog/kimi-k3-the-manos-the-mythos-the)).
- **AgentX 1.0 dataset**: 8,000+ sessions, 3.4M requests, **610 billion tokens**, >**$3M USD in spend**,
  1M+ context, 95%+ KV cache hit rate
  ([agentx-inferencexv3-does-cuda-moat](https://inferencex.semianalysis.com/blog/agentx-inferencexv3-does-cuda-moat)).

### 4d. Hardware specs quoted by InferenceX /chips/ pages [THIRD-PARTY compilation of vendor specs]
| Chip | HBM | BW | Dense FP4 | Notes |
|---|---|---|---|---|
| H100 SXM | 80 GB HBM3 | 3.35 TB/s | — (FP8 only) | NVLink 4.0 |
| H200 SXM | 141 GB HBM3e | 4.8 TB/s | — (FP8 only) | 1,979 FP8 dense TFLOP/s; NVLink 4.0, 450 GB/s uni-di |
| B200 | 180 GB HBM3e | 8 TB/s | 9,000 TFLOP/s | NVLink 5.0, 900 GB/s uni-di; 4,500 FP8 dense TFLOP/s |
| B300 (Blackwell Ultra) | 268 GB usable HBM3e | — | 13,500 TFLOP/s | 800 Gbit/s scale-out |
| GB200 NVL72 | 186 GB HBM3e/chip | — | — | 72 chips/NVLink domain, 900 GB/s scale-up |
| GB300 NVL72 | 278 GB HBM3e/chip (20 TB/rack) | — | 15,000 TFLOP/s/chip | 72 Blackwell Ultra chips |
| MI300X | 192 GB HBM3 | 5.3 TB/s | — | 2,615 dense FP8 TFLOP/s, full-mesh Infinity Fabric |
| MI325X | 256 GB HBM3e | 6 TB/s | — | 2,615 dense FP8 TFLOP/s |
| MI355X | 288 GB HBM3e | 8 TB/s | 10,066 TFLOP/s | first AMD chip with FP4 |

Cross-check from [b200-nvfp4-vs-h200-int4-kimi-k2](https://inferencex.semianalysis.com/blog/b200-nvfp4-vs-h200-int4-kimi-k2-vllm-perf-per-dollar):
"B200 has **2.27x H200's FP8 dense throughput (4,500 vs 1,979 TFLOP/s)**, **1.67x its HBM bandwidth (8 vs 4.8
TB/s)**, and **2.00x its NVLink scale-up bandwidth (900 vs 450 GB/s uni-di)**" and "B200's 1.38x TCO penalty
($1.95 vs $1.41 per GPU/hr)". Also **GB300 NVL72 HBM = 288 GB/GPU** and **GB200 = 192 GB/GPU** (from the DSv4
post), vs the /chips/ pages' 278 / 186 GB — the /chips/ numbers are *usable* capacity.

## 5. VENDOR CLAIMS — NVIDIA (via AMD rebuttal) and AMD

### 5a. NVIDIA GTC 2026 claim [VENDOR]
Quoted verbatim by AMD in its rebuttal, published **Mar 18, 2026**
([AMD: The Many Aspects of Inference Performance](https://www.amd.com/en/developer/resources/technical-articles/2026/the-many-aspects-of-inference-performance.html)):

> "At GTC 2026, NVIDIA showed an inference performance comparison based on benchmarking data from
> SemiAnalysis 'InferenceX', showing **GB300 NVL72 (FP4, MTP) delivering 50X higher tokens-per-watt and 35X
> lower cost-per-token than last-generation Hopper (FP8)** and shows the 'competition' in-between."

NVIDIA's GTC cost-per-million-token benchmark is characterized by AMD as using **FP4, MTP=3, and March 7
data on DeepSeek 1k/1k — "each choice favors NVIDIA's result."** AMD notes NVIDIA used MTP=3 while "AMD
defaults to MTP=1 at this time."
**I could not retrieve NVIDIA's own slide or blog post directly** — the GTC 2026 "GB NVL72 Inference King"
claim is only available here second-hand through AMD. Treat the 50x / 35x numbers as [VENDOR] and
[UNVERIFIED] as to exact workload definition.

### 5b. AMD counter-claims [VENDOR], all sourced to SemiAnalysis InferenceX™ chart images
Same URL, Mar 18, 2026. **The underlying figures are in chart IMAGES — no numeric values are in the page
text, so these are qualitative only and carry no exact $ figure.**
- DeepSeek R1 **FP8, no MTP**: "On equal footing, MTP off and FP8 for both, **MI355X cost-per-token is
  materially lower than GB300 NVL72 at high concurrency, 60+ TPS/user**" (Figure 1, InferenceX Mar 7, 2026).
- "To illustrate the impact of software optimization on cost per token: since February, **MI355X GPU cost per
  token has dropped significantly, while GB300 NVL72 remains higher and unchanged**" at 100 TPS/user
  (Figure 2, InferenceX Mar 13, 2026).
- DeepSeek R1 **FP4, no MTP**: "**MI355X SGLang is already ahead of GB300 SGLang at 80+ TPS/user on
  unoptimized FP4**" (Figure 3, InferenceX Mar 13, 2026).
- "Rack scale is coming in 2H with **AMD Helios (MI450)**... planned for 2H 2026."
- AMD's framing of InferenceX: "an **independent** inference benchmarking framework that tests NVIDIA and
  AMD GPUs across a very broad universe of configurations."

**Note for the deck:** AMD is citing SemiAnalysis InferenceX against NVIDIA while NVIDIA cited the *same*
benchmark against AMD — both at GTC 2026. This is the cleanest evidence that InferenceX is being used as a
neutral arbiter by both vendors, but each side cherry-picks the operating point (MTP on/off, FP4 vs FP8,
interactivity band).

## 6. MLPerf Inference — NVIDIA submissions [VENDOR-reported, MLPerf-verified where Closed division]

### MLPerf Inference v5.0 (results retrieved 2025-04-02; blog by NVIDIA)
URL: [NVIDIA Blackwell Delivers Massive Performance Leaps in MLPerf Inference v5.0](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/)
(accessed 2026-09-16). MLPerf entries cited: 5.0-0058, 5.0-0060 (GB200 NVL72); 5.0-0056, 5.0-0060 (B200/H200).

| Claim | Value | Model | Hardware | Flag |
|---|---|---|---|---|
| Per-GPU perf gain vs H200 8-GPU (server mode) | **3.4x** | Llama 3.1 405B | GB200 NVL72 vs 8x H200 | [VENDOR] |
| Per-GPU perf gain vs H200 8-GPU (offline) | **2.8x** | Llama 3.1 405B | GB200 NVL72 vs 8x H200 | [VENDOR] |
| System-level throughput gain vs H200 8-GPU | **up to 30x** | Llama 3.1 405B | GB200 NVL72 ("9x more GPUs on a single NVLink domain") | [VENDOR] |
| Throughput vs 8x H200 | **3.1x** | Llama 2 70B Interactive (450 ms TTFT / 40 ms TPOT = 25 tok/s/user) | 8x B200 | [VENDOR] |
| Raw throughput (unverified result) | **869,203 tokens/second** | Llama 2 70B (v4.1 benchmark) | GB200 NVL72 | [VENDOR]/[UNVERIFIED] |

Caveats NVIDIA itself states: "**Per-GPU performance is not a primary metric of MLPerf Inference v5.0 and is
derived by dividing reported throughput by accelerator count.**" The 869,203 tok/s figure is explicitly
labelled "an **unverified** result"; the reviewed results are MLPerf Closed/Data Center.
NVIDIA also claims MoE models run "**10x faster performance and 1/10 the token cost**" on GB200 NVL72
(link from the same post) — [VENDOR], no URL resolved.

**Timing note:** MLPerf Inference v5.0 (April 2025) predates GB300. I did **not** locate an NVIDIA MLPerf blog
covering GB300 NVL72 / Blackwell Ultra in this session (two plausible URLs returned HTTP 404: the
"GB300 NVL72 ... era of AI reasoning" and "Blackwell Ultra ... MLPerf Inference v5.1" slugs).

## 7. InferenceX v2 announcement — the flagship SemiAnalysis inference-economics post [THIRD-PARTY]

URL: [blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper)
**SemiAnalysis · February 16, 2026 · 47 min read** · tags: benchmark, gpu, inference, announcement.
(GitHub stars shown on page: 1,706.) This is the "formerly InferenceMAX" relaunch post.

### Hard numbers
- **GB300 NVL72: "up to 100x on FP8 vs FP4 compared to even a strong H100 disagg+wideEP+MTP baseline and
  65x on FP8 vs FP8."**
- **"On H100 vs GB200 NVL72, we see up to 55x realized performance difference at 75 tok/s/user."**
- **"At a fixed interactivity level of 60 tok/s/user, each GB200 NVL GPU produces slightly less than triple
  the number of tokens/s than each B200 does."**
- **"At 130 tok/s/user, the GB200 NVL72 has nearly no advantage and is even more expensive on a $/Million
  tokens basis."** — because at low batch the workload fits inside a single 8-GPU HGX NVLink domain and the
  NVL72 scale-out advantage disappears.
- Benchmark scale: **"close to 1000 GPUs"** across all GPU SKUs NVIDIA produced over four years; NVIDIA
  provided the GB300 NVL72 systems and validated configs, but SemiAnalysis states the benchmarking was
  independent.
- Interconnect: **NVLink domain inside NVL72 = 72 GPUs at 900 GB/s uni-directional per GPU**, "roughly 7-10x
  the bandwidth of the InfiniBand/Ethernet based scale-out network"; IB/RoCEv2 = **400-800 Gbit/s per GPU
  uni-directional (50-100 GB/s)**. All NVIDIA testing on InfiniBand clusters.
- **AMD FP4 composability gap (Feb 2026):** "Despite the MI355X being competitive in FP8 disagg, its FP4
  performance suffers from composability issues... In a 1k1k scenario, the MI355X (MoRI SGLang) with MTP
  barely manages to beat the B200 (Dynamo SGLang) without MTP." MI355X matches B200-without-MTP only in the
  **~60 to ~120 tok/s/user** band. AMD's official MI355X container was still a fork of vLLM 0.10.1.
- **B200 SGLang throughput per GPU doubled at some interactivity levels between Oct 2025 and Feb 2026.**
- MI355X + MoRI: **throughput per GPU +more than 20% in the 20-45 tok/s/user range** over ~1 month.
- NVIDIA share of the stack: "TensorRT LLM already serves **billions of tokens per hour** globally across
  providers like TogetherAI."

### Inference provider unit economics (the "Unpacking Inference Providers' Unit Economics" section)
- OpenRouter list of providers serving **DeepSeek R1 0528 FP8** with cost/M input+output and interactivity:
  "Disregarding Chutes, the **middle of the pack provider serves at an interactivity of around 35 tok/s/user**."
- Crusoe: **36 tok/s/user at $1.35/M input, $5.40/M output** → SemiAnalysis estimate "they incur a cost of
  *no more than* **$0.226/M input tokens and $2.955/M output tokens** for a profit margin of up to **83% gross
  margin on input tokens and 45% gross margin on output tokens** (depreciation counted in COGS)."
- Nebius AI Studio (Fast): DeepSeek FP4 at **167 tok/s/user at $2/M input, $6/M output**.
- MTP economics: DeepSeek-R1-0528 FP4, 8k/1k, **$0.251/M total tokens → $0.057/M with MTP**.
- B200 + TRT-LLM, DeepSeek R1 0528 FP4: **~$0.56/M output tokens at 50 tok/s/user → ~$4/M output tokens at
  125 tok/s/user** ("2.5x speed increase for a ~7x price increase").
- GB300 Dynamo TRT, DeepSeek R1 FP4 8k/1k at 150 tok/s/user: **~$2.35/M baseline → ~$0.11/M with MTP = ~21x**.
- Anthropic "fast mode" is used as the real-world analogue of this speed-for-price trade.

## 8. NVIDIA's own InferenceMAX / InferenceX post [VENDOR — NVIDIA]

URL: [NVIDIA Blackwell Raises Bar in New InferenceMAX Benchmarks](https://blogs.nvidia.com/blog/blackwell-inferencemax-benchmark-results/)
(blogs.nvidia.com, accessed 2026-09-16). NVIDIA describes InferenceMAX v1 as "a new benchmark from
SemiAnalysis released Monday" and "the first **independent** benchmark to measure total cost of compute across
diverse models and real-world scenarios."

| Claim | Value | Model / hardware | Flag |
|---|---|---|---|
| Cost per million tokens reduction vs previous generation | **15x** | NVIDIA Blackwell | [VENDOR] |
| AI-factory ROI | **$5M investment in GB200 NVL72 → $75M in DSR1 token revenue = 15x ROI** | GB200 NVL72, DeepSeek R1 | [VENDOR] |
| Lowest cost per token | **2 cents per million tokens** ("5x lower cost per token in just 2 months" via software optimization) | B200 on gpt-oss | [VENDOR] |
| Peak throughput | **60,000 tokens/second per GPU** and **1,000 tokens/second per user** | B200, gpt-oss, TensorRT-LLM | [VENDOR] |
| MoE efficiency | **10x throughput per megawatt** vs previous generation | Blackwell | [VENDOR] |
| NVLink Switch bandwidth | **1,800 GB/s bidirectional** | B200 system | [VENDOR] |
| Software-only gains | "more than **doubled** Blackwell performance since launch using software alone" | Blackwell | [VENDOR] |

**Cross-vendor reconciliation of the "cost per million tokens" headline:** NVIDIA says **15x** lower vs
previous generation (B200/Blackwell vs Hopper). AMD's rebuttal of the GTC 2026 version of this claim says
NVIDIA showed **35x lower cost-per-token and 50x higher tokens-per-watt** for GB300 NVL72 (FP4, MTP) vs Hopper
(FP8). InferenceX v2 (SemiAnalysis, Feb 16 2026) independently measures **"up to 100x on FP8 vs FP4 compared
to even a strong H100 disagg+wideEP+MTP baseline and 65x on FP8 vs FP8"** for GB300 NVL72, and **"up to 55x
realized performance difference at 75 tok/s/user"** for H100 vs GB200 NVL72.
**These 15x / 35x / 50x / 55x / 65x / 100x numbers are all "X vs Hopper" claims at different operating
points, precisions and MTP settings — they are not interchangeable.** Treat every "Xx vs Hopper" figure as
[VENDOR] unless it comes from InferenceX's own post.

## 9. GB300 NVL72 vs MI355X — the requested headline comparison [THIRD-PARTY]

The `/compare-per-dollar/...` pages are described as "verified, reproducible cost-per-million-token results...
normalized by **hyperscaler TCO**" — and they use the **/chips/ TCO set: GB300 NVL72 = $2.31/GPU/hr,
MI355X = $1.50/GPU/hr** (both appear verbatim in the page HTML). **This is the cleanest GB300-vs-MI355X
dollar comparison on the site.**

### Kimi K3 2.8T — GB300 NVL72 vs MI355X
URL: [compare-per-dollar/kimi-k3-gb300-vs-mi355x](https://inferencex.semianalysis.com/compare-per-dollar/kimi-k3-gb300-vs-mi355x)
`curve_date: 2026-09-15`, GHA run [34873998796](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/34873998796/attempts/1), curve workflow run id 2470.
Interactivity band measured: **19–132 tok/s/user**. Quoted narrative verbatim:

| tok/s/user | GB300 NVL72 $/M tok | MI355X $/M tok | GB300 advantage |
|---|---|---|---|
| 47 | **$0.04** | $0.07 | GB300 cheaper by **89%** |
| 75 | **$0.05** | $0.13 | GB300 delivers **149% more tokens per dollar** |
| 104 | **$0.07** | $0.23 | GB300 **229% more cost-efficient** |

Table values as rendered in HTML: GB300 **$0.038** vs MI355X **$0.071**; GB300 **$0.052** vs MI355X
**$0.131**; GB300 **$0.068** vs MI355X **$0.225**. (Article notes "Numbers reflect the default
agentic-trace" configuration — i.e. AgentX agentic trace replay, not a synthetic 8k/1k workload.)
Note the $0.038 here matches the Kimi K3 cheapest-GPU ranking headline (§1a) — **GB300 NVL72 at $0.038/M on
Kimi K3 is the single best-documented GB300 number on the site.**

Also confirmed on this page: GB300 NVL72 list TCO **$2.31/GPU/hr** and MI355X **$1.50/GPU/hr**.

## 10. ⭐ THE APPLES-TO-APPLES TABLE — `/run/<model>-on-<gpu>` pages [THIRD-PARTY]

**This is the single best source for "$/million-token and tokens/sec/GPU for GB300 NVL72 vs MI355X vs GB200
vs B200 vs H100 for a specific model."** Every `/run/` page has a server-side meta description of the exact form:
*"Measured: <MODEL> sustains **<N> tokens/s per GPU** on **<GPU>** at **50 tokens/s per user**, **$<X> per
million tokens at hyperscaler pricing**. Live data from **<K> benchmarked configs**."*
All values below are **at a fixed 50 tokens/s/user**, **hyperscaler pricing**, extracted 2026-09-16.
URL pattern: `https://inferencex.semianalysis.com/run/<model>-on-<gpu>`.

| Model | GPU | tok/s/GPU | $/M tokens | Configs benchmarked | URL |
|---|---|---|---|---|---|
| **Kimi K3** | **GB300 NVL72** | **16,762** | **$0.038** | 11 | [link](https://inferencex.semianalysis.com/run/kimi-k3-on-gb300-nvl72) |
| Kimi K3 | B300 | 6,083 | $0.10 | 11 | [link](https://inferencex.semianalysis.com/run/kimi-k3-on-b300) |
| Kimi K3 | MI355X | 5,542 | $0.075 | 19 | [link](https://inferencex.semianalysis.com/run/kimi-k3-on-mi355x) |
| Kimi K3 | B200 | 4,598 | $0.10 | 7 | [link](https://inferencex.semianalysis.com/run/kimi-k3-on-b200) |
| Kimi K3 | GB200 NVL72 | 4,579 | $0.11 | 13 | [link](https://inferencex.semianalysis.com/run/kimi-k3-on-gb200-nvl72) |
| **DeepSeek V4 Pro** | **B300** | **57,850** | **$0.011** | 173 | [link](https://inferencex.semianalysis.com/run/deepseek-v4-on-b300) |
| DeepSeek V4 Pro | GB300 NVL72 | 56,468 | $0.011 | 104 | [link](https://inferencex.semianalysis.com/run/deepseek-v4-on-gb300-nvl72) |
| DeepSeek V4 Pro | B200 | 45,291 | $0.011 | 170 | [link](https://inferencex.semianalysis.com/run/deepseek-v4-on-b200) |
| DeepSeek V4 Pro | MI355X | 20,322 | $0.021 | 231 | [link](https://inferencex.semianalysis.com/run/deepseek-v4-on-mi355x) |
| **DeepSeek V4.1 Flash** | **B300** | **91,089** | **$0.007** | 8 | [link](https://inferencex.semianalysis.com/run/deepseek-v41-flash-on-b300) |
| DeepSeek V4.1 Flash | GB300 NVL72 | 85,620 | $0.007 | 8 | [link](https://inferencex.semianalysis.com/run/deepseek-v41-flash-on-gb300-nvl72) |
| DeepSeek V4.1 Flash | GB200 NVL72 | 82,863 | **$0.006** | 8 | [link](https://inferencex.semianalysis.com/run/deepseek-v41-flash-on-gb200-nvl72) |
| DeepSeek V4.1 Flash | MI355X | 39,386 | $0.011 | 6 | [link](https://inferencex.semianalysis.com/run/deepseek-v41-flash-on-mi355x) |
| DeepSeek V4.1 Flash | H200 | 20,515 | $0.017 | 8 | [link](https://inferencex.semianalysis.com/run/deepseek-v41-flash-on-h200) |
| **Qwen3.5** | **B300** | **17,277** | **$0.036** | 178 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-b300) |
| Qwen3.5 | MI355X | 8,170 | $0.051 | 235 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-mi355x) |
| Qwen3.5 | B200 | 6,499 | $0.074 | 207 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-b200) |
| Qwen3.5 | GB300 NVL72 | 4,819 | $0.13 | 75 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-gb300-nvl72) |
| Qwen3.5 | GB200 NVL72 | 3,565 | $0.14 | 45 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-gb200-nvl72) |
| Qwen3.5 | H200 | 1,810 | $0.19 | 43 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-h200) |
| Qwen3.5 | H100 | 1,689 | $0.19 | 35 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-h100) |
| Qwen3.5 | MI325X | 707 | $0.43 | 82 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-mi325x) |
| Qwen3.5 | MI300X | 583 | $0.45 | 40 | [link](https://inferencex.semianalysis.com/run/qwen-3-5-on-mi300x) |
| **DeepSeek R1** | **B200** | **4,610** | **$0.10** | 350 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-b200) |
| DeepSeek R1 | GB200 NVL72 | 2,697 | $0.19 | 125 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-gb200-nvl72) |
| DeepSeek R1 | GB300 NVL72 | 2,438 | $0.26 | 126 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-gb300-nvl72) |
| DeepSeek R1 | MI355X | 1,608 | $0.26 | 307 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-mi355x) |
| DeepSeek R1 | H200 | 1,235 | $0.27 | 161 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-h200) |
| DeepSeek R1 | B300 | 1,779 | $0.35 | 129 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-b300) |
| DeepSeek R1 | MI325X | 312 | $0.98 | 25 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-mi325x) |
| DeepSeek R1 | MI300X | 240 | $1.10 | 15 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-mi300x) |
| DeepSeek R1 | H100 | **74.2** | **$4.38** | 72 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-h100) |
| **gpt-oss-120b** | **B200** | **44,489** | **$0.011** | 98 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-b200) |
| gpt-oss-120b | MI355X | 38,497 | $0.011 | 57 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi355x) |
| gpt-oss-120b | H200 | 9,319 | $0.036 | 101 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-h200) |
| gpt-oss-120b | H100 | 8,973 | $0.036 | 43 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100) |
| gpt-oss-120b | MI300X | 8,067 | $0.033 | 52 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi300x) |
| gpt-oss-120b | MI325X | 4,782 | $0.064 | 44 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi325x) |
| **MiniMax M2.7** | **GB300 NVL72** | **13,707** | **$0.047** | 74 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-gb300-nvl72) |
| MiniMax M2.7 | GB200 NVL72 | 12,515 | **$0.041** | 72 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-gb200-nvl72) |
| MiniMax M2.7 | B300 | 12,253 | $0.051 | 138 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-b300) |
| MiniMax M2.7 | B200 | 11,606 | $0.041 | 142 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-b200) |
| MiniMax M2.7 | MI355X | 7,692 | $0.054 | 172 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-mi355x) |
| MiniMax M2.7 | H200 | 2,523 | $0.13 | 24 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-h200) |
| MiniMax M2.7 | H100 | 1,692 | $0.19 | 17 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-h100) |
| MiniMax M2.7 | MI300X | 1,380 | $0.19 | 30 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-mi300x) |
| MiniMax M2.7 | MI325X | 2,035 | $0.15 | 35 | [link](https://inferencex.semianalysis.com/run/minimax-m27-on-mi325x) |
| **Kimi K2.6** | **GB300 NVL72** | **5,601** | **$0.11** | 40 | [link](https://inferencex.semianalysis.com/run/kimi-k26-on-gb300-nvl72) |
| Kimi K2.6 | GB200 NVL72 | 4,594 | **$0.11** | 42 | [link](https://inferencex.semianalysis.com/run/kimi-k26-on-gb200-nvl72) |
| Kimi K2.6 | B200 | 3,449 | $0.14 | 90 | [link](https://inferencex.semianalysis.com/run/kimi-k26-on-b200) |
| Kimi K2.6 | MI355X | 2,831 | $0.15 | 105 | [link](https://inferencex.semianalysis.com/run/kimi-k26-on-mi355x) |
| Kimi K2.6 | B300 | 3,504 | $0.18 | 56 | [link](https://inferencex.semianalysis.com/run/kimi-k26-on-b300) |
| **GLM-5** | **B200** | **2,792** | **$0.17** | 87 | [link](https://inferencex.semianalysis.com/run/glm-5-1-on-b200) |
| GLM-5 | B300 | 2,988 | $0.21 | 58 | [link](https://inferencex.semianalysis.com/run/glm-5-1-on-b300) |
| GLM-5 | GB200 NVL72 | 1,553 | $0.33 | 102 | [link](https://inferencex.semianalysis.com/run/glm-5-1-on-gb200-nvl72) |
| GLM-5 | GB300 NVL72 | 1,482 | $0.43 | 111 | [link](https://inferencex.semianalysis.com/run/glm-5-1-on-gb300-nvl72) |
| GLM-5 | MI355X | 967 | $0.43 | 109 | [link](https://inferencex.semianalysis.com/run/glm-5-1-on-mi355x) |
| GLM-5 | H200 | 572 | $0.59 | 25 | [link](https://inferencex.semianalysis.com/run/glm-5-1-on-h200) |
| **GLM-5.3** | **MI355X** | **6,779** | **$0.061** | 22 | [link](https://inferencex.semianalysis.com/run/glm-5-3-on-mi355x) |
| **Llama 3.3 70B** | **B200** | **6,127** | **$0.078** | 264 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-b200) |
| Llama 3.3 70B | MI355X | 2,878 | $0.14 | 120 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-mi355x) |
| Llama 3.3 70B | H200 | 2,099 | $0.16 | 132 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h200) |
| Llama 3.3 70B | MI325X | 1,494 | $0.20 | 60 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-mi325x) |
| Llama 3.3 70B | H100 | 1,496 | $0.22 | 45 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h100) |
| Llama 3.3 70B | MI300X | 1,482 | $0.18 | 60 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-mi300x) |
| Qwen3.8-Flash-Next | H200 | 16,353 | $0.021 | 5 | [link](https://inferencex.semianalysis.com/run/qwen-3-8-flash-next-on-h200) |
| Qwen3.8-Flash-Next | H100 | 4,974 | $0.065 | 5 | [link](https://inferencex.semianalysis.com/run/qwen-3-8-flash-next-on-h100) |

**Reading notes:**
- These are **all at 50 tok/s/user**, so cross-model/cross-GPU comparison is apples-to-apples *within a row set*.
- **B300 beats GB300 NVL72 on several models at this operating point** (DeepSeek V4 Pro 57,850 vs 56,468 tok/s/GPU;
  DeepSeek V4.1 Flash 91,089 vs 85,620; Qwen3.5 17,277 vs 4,819; MiniMax M2.7 12,253 vs 13,707 → GB300 wins there).
  This is consistent with the §3 finding that NVL72's advantage is not at the throughput peak.
- **GB300 NVL72 is dramatically best on Kimi K3** (16,762 tok/s/GPU, $0.038/M — 3.0x the tok/s/GPU of MI355X
  and 33% cheaper) but **worst-in-class on GLM-5** ($0.43/M, 1,482 tok/s/GPU, behind B200's $0.17).
- Some `/run/` pages have **no numeric meta description** (client-only): DeepSeek V4 Pro on GB200 NVL72 / H200 /
  MI300X / MI325X, DeepSeek V4.1 Flash on B200 / H100, GLM-5 on MI325X, GLM-5.3 on B200 / B300 / GB200 NVL72 /
  GB300 NVL72 / H200 / MI325X, gpt-oss-120b on GB200 NVL72, Kimi K2.6 on H200 / MI300X / MI325X, Kimi K3 on H200,
  MiniMax M3 on all GPUs, Qwen3.8-Flash-Next on B200 / B300. **These are the genuinely unreadable ones.**

