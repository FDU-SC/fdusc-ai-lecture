# AI Compute, Hardware, Datacenters and Energy: Hard Numbers, 2023 – September 2026

Research brief for a September 2026 university HPC lecture. All figures retrieved **2026-09-16** unless stated. Announced plans and delivered reality are separated throughout. Items that could not be verified against a primary source are listed in §9 and must not be put on a slide as fact.

---

## 1. Hardware spec table

Rack-level numbers are vendor spec-sheet values (sparse where NVIDIA footnotes say so); they are **not** measured application throughput.

| Chip / system | Announced | Shipping | Memory (per GPU) | Mem BW (per GPU) | Dense FP4 / FP8 | TDP | Source |
|---|---|---|---|---|---|---|---|
| H100 SXM | Mar 2022 (Hopper) | 2022–23 | 80 GB HBM3 | 3.35 TB/s | — / 1,979 TFLOPS FP8 (sparse) | up to 700 W | [NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/) |
| H200 | 13 Nov 2023 | Q2 2024 | 141 GB HBM3e | 4.8 TB/s | — / 1,979 TFLOPS FP8 | up to 700 W | [NVIDIA H200](https://www.nvidia.com/en-us/data-center/h200/) |
| B200 (Blackwell) | 18 Mar 2024 (GTC) | Nov 2024 | 180 GB HBM3e (192 GB widely quoted) | 8 TB/s | 9 PFLOPS / 4.5 PFLOPS | ~1,000 W | [DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/) |
| GB200 NVL72 | 18 Mar 2024 | 2024 H2–2025 | 13.4 TB/rack | 576 TB/s/rack | 720 / 360 PFLOPS | ~120 kW/rack | [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) |
| GB300 / Blackwell Ultra NVL72 | 18 Mar 2025 (GTC) | Sept 2025 | 20 TB/rack (288 GB HBM3e/GPU) | 576 TB/s/rack | 1,080 / 720 PFLOPS | ~135 kW/rack (est., see §9) | [NVIDIA GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/) |
| **Rubin (Vera Rubin NVL72)** | CES **Jan 2026**; full production Jan 2026 | 2026 H2 | 288 GB HBM4 → **20.7 TB/rack** | **22 TB/s** (HGX page); 19.2 TB/s (NVL72 page) | 35 / 17.5 PFLOPS per GPU; 2,520 / 1,260 PFLOPS per rack | n/d | [Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/), [HGX](https://www.nvidia.com/en-us/data-center/hgx/) |
| Rubin CPX | 9 Sept 2025 | 2026 | 128 GB GDDR7 | n/d | ~30 PFLOPS FP4 (trade press) | n/d | [WCCFTech](https://wccftech.com/nvidia-rubin-cpx-gpu-128-gb-gddr7-30-exaflops-ai-compute/) *(secondary)* |
| **NVIDIA Groq 3 LPX** | GTC **16 Mar 2026** | full production **24 Aug 2026**, online "later this year" | 500 MB on-die SRAM | — | LPU, decode-only | n/d | [CNBC 24 Aug 2026](https://www.cnbc.com/2026/08/24/nvidia-says-groq-racks-will-be-online-this-year-after-20-billion-deal.html) |
| Google TPU v5p | Dec 2023 | 2024 | — | 4,800 Gbps ICI | 8,960-chip pods, ~4.45 EF | — | [Introl](https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations) *(secondary)* |
| Google Trillium (v6e) | May 2024 | 2024 | 32 GB HBM | 2× v5e | 4.7× v5e peak | — | same |
| **Google Ironwood (v7)** | 9 Apr 2025 (Cloud Next) | Nov 2025 | 192 GB HBM3e (6× Trillium) | n/d | **4,614 TFLOPS** peak/chip; **9,216-chip pod = 42.5 EF**; 2× perf/W vs Trillium | ~600 W | [9to5Google](https://9to5google.com/2025/04/09/google-ironwood-tpu/), [Introl](https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations) |
| AMD MI355X | June 2025 | 2025 H2 | 288 GB HBM3e | 8 TB/s | 10,066 / 5,033 TFLOPS | 1,400 W | [InferenceX](https://inferencex.semianalysis.com/chips/mi355x) *(third-party)* |
| **AMD MI455X (Helios)** | **23 Jul 2026** page launch | ramp Aug 2026 | **432 GB HBM4** | **23.3 TB/s** | **40.3 PFLOPS MXFP4** / 20.1 FP8 | n/d (DLC) | [AMD MI455X](https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html) |
| AMD Helios rack | 2026 | 2026–27 | 72 GPUs, 31 TB HBM4 | 1.7 PB/s/rack | 2.9 EFLOPS claimed | — | [ServeTheHome Hot Chips 2026](https://www.servethehome.com/amd-helios-mi400-system-architecture-at-hot-chips-2026/) |
| AWS Trainium3 / Trn3 UltraServer | 2 Dec 2025 (re:Invent) | GA Dec 2025 | 144 GB HBM3e | 4.9 TB/s | 2.52 PFLOPS FP8/chip; 362 PFLOPS per 144-chip UltraServer | — | [AWS](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/) |
| Huawei CloudMatrix 384 (384× Ascend 910C) | Apr 2025 | 2025 | 3.6× GB200 NVL72 aggregate | 2.1× GB200 | 300 PFLOPS dense BF16 (≈2× GB200 NVL72) | **4.1× GB200 NVL72 power; 2.5× worse perf/W** | [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72) |

Two spec conflicts worth naming on a slide: (a) NVIDIA's own pages give Rubin at **22 TB/s** (HGX NVL8, 176 TB/s ÷ 8) and **19.2 TB/s** (Vera Rubin NVL72); AMD's comparison table cites 22.0 TB/s. (b) NVIDIA's HGX B300 (144 PFLOPS sparse FP4 for 8 GPUs = 18/GPU) is 10 % below the GB300 NVL72's implied 20 PFLOPS/GPU.

**Chinese accelerators.** Huawei's advantage is systems, not silicon: Ascend 910C is ~⅓ of a Blackwell per chip, and CM384 compensates with 5× the chips ([SemiAnalysis, Apr 2025](https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72)). Yield and fab constraints are the binding limits — SemiAnalysis notes the 910C uses Korean HBM and TSMC wafers. The export-control picture inverted in 2026: the US approved H200 sales to China in **January 2026**, but shipments stalled on unresolved terms, and **DeepSeek launched V4 on 24 April 2026 explicitly optimized for Huawei Ascend**, with Huawei stating its chips were used in part of V4's training ([Reuters via Emirates247, 2026-04-24](https://www.emirates247.com/technology/deepseek-launches-v4-ai-model-optimized-for-huawei-ascend-chips-challenging-nvidia-dominance/1081)).

---

## 2. Capex and megawatts

Cash capex for property and equipment, $B, from SEC XBRL company facts (excludes finance-lease additions):

| Company | 2023 | 2024 | 2025 | 2026 H1 | 2026 guidance |
|---|---|---|---|---|---|
| Microsoft (FY) | 31.9 (FY23) | **44.5** (FY24) | **64.6** (FY25) | 49.3 (H1 FY26) | **~$190B CY26**, ~$25B of it component-price inflation |
| Alphabet | 32.3 | 52.5 | **91.4** | **80.6** | **$195–205B FY26** (raised) |
| Amazon | 52.7 | 83.0 | **131.8** | **98.4** | **~$220B** (raised from ~$200B) |
| Meta | 27.0 | 37.3 | **69.7** | **49.1** | **$130–145B** (raised twice) |
| Oracle (FY) | 6.9 (FY24) | 21.2 (FY25) | — | — | **55.7 (FY26)**, +162 % YoY |

Microsoft including finance leases: **$37.5B in Q2 FY26** (+66 % YoY), **$31.9B Q3 FY26** ([Nasdaq](https://www.nasdaq.com/articles/microsoft-plans-190-billion-capital-spending-year-wednesday-shows-whether-azure-keeping)). Alphabet's Q2 2026 free cash flow was **–$5.9B**, its first negative quarter. Dell'Oro: 2025 worldwide datacenter capex **+57 %**, top-4 US CSPs **+76 %**; 2026 to surpass **$1 trillion** ([Dell'Oro, 2026-03-17](https://www.delloro.com/news/data-center-capex-surges-57-percent-in-2025-as-ai-deployments-accelerate/)).

**Announced vs delivered — OpenAI is the sharpest case.** Roughly **35+ GW** has been announced across Stargate (10 GW), Oracle (4.5 GW), NVIDIA (10 GW), AMD (6 GW) and Broadcom (10 GW). Verifiably **operational as of April 2026: ≈0.3 GW**, all of it at Abilene, Texas ([Epoch AI, 2026-04-17](https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand)). Stargate's "$500B over four years" is explicitly an *intention*; the OpenAI–NVIDIA 10 GW/$100B deal is a **non-binding LOI** with no evidence the first 1 GW was delivered; the AMD warrant's first tranche had not vested as of Aug 2026. In 2026 OpenAI **dropped the Abilene expansion** (Mar), **paused Stargate UK** (Apr), and shifted toward leasing.

xAI: Colossus 1 online **2 Sept 2024** with **100,000 H100s**; by Sept 2025 SemiAnalysis counted **~200k H100/H200 + ~30k GB200 at ~300 MW**; a third building took the site toward a claimed **~2 GW**. Satellite analysis disputes the 1 GW claim, finding only **~350 MW of cooling capacity** ([Yahoo Finance](https://finance.yahoo.com/news/elon-musks-xai-colossus-2-180014348.html)). A widely circulated "555,000 GPUs" figure is internally inconsistent and should not be used.

Anthropic: **up to 1 million TPUs** and "well over a gigawatt online in 2026" with Google (2025-10-23); **$30B** Azure commitment with NVIDIA up to $10B (2025-11-18); **$50B** Fluidstack US program (2025-11-12); Project Rainier, **~500k Trainium2**, ~$8B (Oct 2024). Meta Hyperion was expanded to **5 GW and >$50B** ([Reuters, 2026-07-13](https://www.reuters.com/business/meta-expands-louisiana-data-center-5-gigawatts-compute-capacity-2026-07-13/)).

---

## 3. Timeline of key compute events

| Date | Event | Why it matters |
|---|---|---|
| 2023-11-13 | H200 announced: 141 GB HBM3e, 4.8 TB/s | Memory capacity becomes the headline spec, not FLOPs |
| 2024-03-18 | Blackwell/GB200 NVL72 announced | Rack becomes the unit of compute; 72-GPU NVLink domain |
| 2024-09-02 | xAI Colossus online, 100k H100 | First 100k-GPU single cluster |
| 2024-09-20 | Constellation–Microsoft TMI/Crane PPA, 835 MW, 20 yr | Nuclear restart as AI power strategy |
| 2024-12-27 | DeepSeek-V3 report: **2.788M H800 GPU-hrs, $5.576M** | Publishes a frontier training cost; resets cost expectations |
| 2025-01-21 | Stargate announced, "$500B over four years" | Gigawatt-scale private buildout framing |
| 2025-01-27 | DeepSeek triggers ~$600B single-day NVIDIA market-cap loss | Inference-cost shock |
| 2025-04-09 | Google Ironwood TPU: 4,614 TFLOPS, 192 GB, 42.5 EF pods | TPU becomes a credible frontier alternative |
| 2025-04-10 | Huawei CloudMatrix 384 | China matches GB200 at 4.1× the power |
| 2025-09-22/23 | OpenAI–NVIDIA 10 GW/$100B LOI; OpenAI–Oracle 4.5 GW/$300B | Circular-financing critique crystallises |
| 2025-10-06 | OpenAI–AMD 6 GW, warrant up to 160M shares | Second-source GPU supply |
| 2025-10-23 | Anthropic–Google: up to 1M TPUs | TPU scale-out beyond Google |
| 2025-11-10 | Burry alleges ~$176B understated depreciation **2026–28** | Utilization/depreciation debate goes mainstream |
| 2025-12-02 | AWS Trainium3 GA | Third credible non-NVIDIA training chip at scale |
| 2026-01-07 | **Rubin in full production** (CES) | Annual cadence sustained |
| 2026-03-16 | NVIDIA GTC: 7 chips, Groq 3 LPX, $1T order outlook through 2027 | Inference-optimized heterogeneous racks |
| 2026-04-16 | IEA *Key Questions on Energy and AI* | Power becomes the official constraint |
| 2026-04-24 | DeepSeek V4 optimized for Huawei Ascend | Frontier Chinese model on domestic silicon |
| 2026-06-23 | **LineShine (China) takes TOP500 #1** at 2,198.40 PFlop/s, CPU-only | Reverses the "China absent" narrative; not an AI machine |
| 2026-08-24 | NVIDIA Groq 3 LPX in full production (Groq assets bought for **$20B** in Dec 2025) | Largest NVIDIA acquisition; decode-phase specialization |
| 2026-09-01 | **NAIRR becomes permanent**: NSF 5-yr, $35M, SDSC-led | US academic AI compute gets a standing program |
| 2026-09-14 | Nasdaq –0.6 % after Amodei essay urging to "pace the frontier" | Bubble anxiety, but no crash |

---

## 4. Cluster-scale training runs

Epoch AI's Notable AI Models database ([CSV](https://epoch.ai/data/notable_ai_models.csv), retrieved 2026-09-16) is the best single source; confidence flags are Epoch's.

| Model | Date | Training compute (FLOP) | Hardware | Qty | Time | Cost (2023 USD) | Conf. |
|---|---|---|---|---|---|---|---|
| GPT-4 | 2023-03 | 2.1e25 | A100 SXM4 40 GB | 25,000 | 2,280 h | $37.3M | Likely |
| Gemini 1.0 Ultra | 2023-12 | 5.0e25 | TPU v4 | 57,000 | 2,400 h | $30.7M | Speculative |
| Llama 3.1 405B | 2024-07 | 3.8e25 | H100 SXM5 | 16,384 | 2,142 h | $52.9M | Confident |
| DeepSeek-V3 | 2024-12 | 3.3e24 | H800 | 2,048 | — (MFU 0.195) | **$5.576M** | Confident |
| DeepSeek-R1 | 2025-01 | 3.5e24 | — | — | — | $6.77M | Confident |
| Grok 3 | 2025-02 | 3.5e26 | H100 SXM5 | 80,000 | 2,160 h | $217.8M | Likely |
| GPT-4.5 | 2025-02 | 3.8e26 | — | — | 3,000 h | $366.0M | Likely |
| Llama 4 Behemoth | 2025-04 | 5.18e25 | H100 SXM5 | 32,000 | — | $44.6M | Likely |
| **Grok 4** | 2025-07 | **5.0e26** | — | 200,000 | — | $387.8M | Speculative |
| GPT-5 | 2025-08 | 6.6e25 | — | — | — | — | Speculative |
| Gemini 3 Pro | 2025-11 | no estimate | TPU v7 Ironwood | — | — | — | Unknown |
| DeepSeek-V4-Pro | 2026-04 | 9.7e24 | (Huawei Ascend, partial) | — | — | — | Likely |

**The most important slide-ready fact here is a gap:** Grok 4 (July 2025, 5e26 FLOPs, speculative) remains the highest-compute entry in Epoch's database. **No 2026 model has a published or credibly estimated training-compute figure.** Every 2026 frontier release (Gemini 3.x, GPT-5.5/5.6, Claude Opus 5, DeepSeek V4) is listed with compute blank or "Unknown". Disclosed compute transparency effectively ended in 2025 — state this rather than implying the numbers stopped growing.

**Interconnect.** Meta's Llama 4 work is the best-documented 100k-GPU scale-out: Meta open-sourced its transport stack (NCCLX) for **>100k GPU** training with **30× cross-datacenter long-tail latency** tolerance ([SDxCentral](https://www.sdxcentral.com/news/meta-open-sources-transport-stack-to-scale-ai-training-to-over-100k-gpus/)). Google's competitive edge is optical: **Apollo optical circuit switching** on a 3D-torus ICI, with **13,824 optical ports across 48 OCS units** wiring a full v5p superpod ([Introl](https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations) — secondary). NVIDIA's scale-out is Quantum-X800 InfiniBand or Spectrum-X Ethernet, with **ConnectX-9 SuperNICs** on Vera Rubin. Ethernet-with-RoCE (Broadcom Tomahawk 6, 102.4 Tbps, first with co-packaged optics, [Broadcom, 2025](https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024)) is now the credible alternative to InfiniBand at hyperscale.

---

## 5. Energy and physical constraints

| Source | Figure |
|---|---|
| [IEA, *Energy and AI*, Apr 2025](https://www.iea.org/reports/energy-and-ai/executive-summary) | 2024: **415 TWh ≈ 1.5 %** of world electricity (US 45 %, China 25 %, Europe 15 %); **2030: ~945 TWh**; **~20 % of planned projects at risk of delay** |
| [IEA, *Key Questions on Energy and AI*, 16 Apr 2026](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary) | 2025: **485 TWh → 2030 ~950 TWh ≈ 3 %** of global electricity. Datacenter demand **+17 % in 2025**, AI-focused DCs **+50 %**. Rack density **×11 (2020–25)**, further **×4 by 2027** |
| [LBNL 2024 Report, Dec 2024](https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/) | 2023: **176 TWh = 4.4 %** of US electricity; 2028: **325–580 TWh = 6.7–12 %** |
| [LBNL 2025 Update, 18 Jun 2026](https://www.osti.gov/biblio/3374245) | 2024: **192 TWh = 4.7 %**; 2030 Reference **649 TWh = 11.8 %** (range 521–843) |
| [LBNL *Queued Up 2026*, Jun 2026](https://emp.lbl.gov/sites/default/files/2026-06/Queued%20Up%202026%20Edition.pdf) | ~2,061 GW active; **gas 253 GW, +86 %** the only growing resource; median **61 months** request→operation; **>750 GW withdrew in 2025**. **Excludes large loads** — do not cite for datacenter queues |

**ERCOT's large-load queue is the headline number and the headline warning:** requests went **~63 GW (Dec 2024) → >233 GW (Dec 2025, >70 % datacenter) → ~474 GW (Aug 2026)**, but only **7.5 GW was actually energized (3.2 %)** and ERCOT's own filing puts realized peak at **49.8 % of requested MW**. PJM capacity prices went **$28.92/MW-day (2024/25) → $269.92 (2025/26) → $333.44 (2027/28)**, then **–2.5 %** for 2028/29 while clearing **6,831 MW short**.

**Nuclear:** Constellation–Microsoft Crane/TMI **835 MW, 20-yr, restart target moved *earlier* to 2027** ($1B DOE loan closed 18 Nov 2025 — [DOE](https://www.energy.gov/articles/energy-department-closes-loan-restart-nuclear-power-plant-pennsylvania)); Talen–AWS Susquehanna up to **1,920 MW, ~$18B to 2042**; Vistra–Meta **>2,600 MW** (Jan 2026, *operating* today); Meta RFP resolved into **~6.6 GW by 2035** with Oklo (1.2 GW) and TerraPower (2.8 GW) — **2030s delivery, not 2026 capacity**.

**Gas:** GE Vernova's gas backlog plus slots went **50 GW (Q1 2025) → 116 GW (Q2 2026)**, guiding ≥125 GW by YE2026; large-turbine lead times **>5 years** and prices **~$2,000/kW → ~$3,000/kW in six months**. Bloom Energy: **up to 2.8 GW** MSA with Oracle (1.2 GW contracted) and a Brookfield framework raised from **$5B to $25B** on 30 Jun 2026. Meta–Entergy Hyperion: **10 gas plants / 7.5 GW**, >30 % of Louisiana's grid capacity — note that the widely quoted "7 plants / 7 GW" is only the *new* tranche.

**Per-query energy (measured, not modelled):** Google measured a **0.24 Wh median Gemini text prompt** and **0.26 mL water** ([arXiv:2508.15734](https://arxiv.org/abs/2508.15734), 21 Aug 2025). Epoch AI gives **~0.3 Wh typical, 2.5 Wh at 10k input tokens, ~40 Wh at 100k** ([Epoch, 2025-02-07](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use)). Measured range across tasks is **0.002–11.5 Wh**. Training energy is much less well attested: **no frontier lab has published a measured 2025–26 training-run figure**, and the circulating Llama 3 "8.9 GWh"/"11.9 GWh" numbers do not appear in Meta's disclosure (which reports only **11,390 tCO2eq**).

**Is power binding?** Nadella, Nov 2025: *"It's not a supply issue of chips. It's actually the fact that I don't have warm shells to plug into."* Counter-evidence: PJM's 2028/29 price fell 2.5 %; NERC (19 May 2026) found **>58 GW of summer capacity added YoY that "has outpaced demand"**; Capgemini (Jan 2026) found **67 % of utility executives call queue requests "phantom."** Both directions are defensible — the honest slide is that *announced* demand is hugely inflated while *energized* demand is genuinely constrained.

---

## 6. Where university HPC sits in 2026

| # | System | Site | Rmax (PFlop/s) | Source |
|---|---|---|---|---|
| 1 | **LineShine** (CPU-only) | NSC Shenzhen, **China** | **2,198.40** | [TOP500 June 2026](https://top500.org/lists/top500/list/2026/06/?page=1) |
| 2 | El Capitan | LLNL | 1,809.00 | same |
| 3 | Frontier | ORNL | 1,353.00 | same |
| 5 | JUPITER Booster | EuroHPC/FZJ | 1,000.00 | same |
| **13** | **Isambard-AI phase 2** | **Univ. of Bristol** | **216.50** | same |

**The top university-owned system in the world is #13, at 1/10th of #1.** No US university-owned system ranks above #66 (Texas A&M VISION, 34.82 PFlop/s). GPU counts make the gap starker: Purdue's Gautschi-AI has **160 H100s** ([Purdue, 2024-12-10](https://www.rcac.purdue.edu/news/6937)); Bristol's Isambard-AI has **5,448 GH200** (£225M, launched 17 Jul 2025); TACC's NSF-funded Horizon will have **4,000 GPUs** and 360 PFlop/s when it enters production **Fall 2026** ([TACC](https://tacc.utexas.edu/systems/horizon/)). Frontier industry clusters run **100,000+**. That is a 60×–1,000× accelerator-count gap.

**Programs and money.** NAIRR's Task Force recommended **$2.6B over six years** (Jan 2023); the pilot (Jan 2024) was a two-year, ~**$3.77 exaFLOPS** federated demo that expired Jan 2026; on **1 Sept 2026** NSF made it permanent with a **5-year, $35M** cooperative agreement to SDSC with TACC (award 2616251). The pilot served **~900 research teams across all 50 states**. New money: **State and Regional AI Infrastructure Hubs, ~$100M across ~10 awards of $4–12M** (proposals due 4 Nov 2026). EuroHPC: **"at least €8.2B for 2021–27"**, **19 AI Factories + 13 Antennas** selected across three batches, and an **AI Gigafactories** call (30 Jul 2026, deadline 12 Nov 2026) of up to **7 gigafactories** with a **€1B** Union contribution covering ≤17 % of CAPEX toward up to €5.8B total. China aggregates **>3.5 million CPU cores and >250,000 GPU cards** through its National Supercomputing Internet, with >1.7M registered users (Sept 2026).

**The gap is not primarily a TOP500 gap** — it is a GPU-count and training-compute gap. Industry produced **~90 % of notable AI models in 2024, up from 60 % in 2023** (Stanford AI Index 2025), and training compute for notable models doubles roughly every five months.

---

## 7. Inference economics

**Price per million tokens collapsed, then partially re-inflated.** GPT-4 launched at **$30/$60** (2023-03-14); GPT-4o mini at **$0.15/$0.60** (2024-07-18) — **200×/100×** in 16 months. o3 was cut **80 %** on 2025-06-10 ($10/$40 → $2/$8). But OpenAI's frontier went **$1.25/$10 (GPT-5) → $1.75/$14 (GPT-5.2) → $2.50/$15 (GPT-5.4) → $5/$30 (GPT-5.5)**, matching the finding that **frontier per-token prices are rising 3×–18 %/yr** ([arXiv:2511.23455](https://arxiv.org/abs/2511.23455), v1 2025-11-28). Anthropic cut Opus **3×** to **$5/$25** on 2025-11-01 and has held there. DeepSeek V4.1-Flash sits at **$0.15/$0.60 off-peak** ([DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)). *Source caveat: most prices verified via [LiteLLM's dated database](https://raw.githubusercontent.com/BerriAI/litellm/model_prices_and_context_window.json) and OpenRouter, because openai.com and google.com were unreachable from the research environment.*

**Cost per unit of capability is falling much faster than price per token.** Epoch AI measures the price to reach GPT-4's GPQA performance falling **40×/yr** (median **50×/yr** across six benchmarks; **200×/yr** after dropping pre-2024 data) ([Epoch, 2025-03-12](https://epoch.ai/data-insights/llm-inference-price-trends)). The Price of Progress paper finds a more conservative **5×–10×/yr** for a fixed frontier level. **The two disagree because they measure different things** — cheapest-model-above-a-threshold vs frontier Pareto bin. Say which you mean.

**Volume.** Google's disclosed token series is the best-documented in the industry: **9.7 trillion/month (May 2024) → 480 trillion (I/O 2025) → 3.2 quadrillion (I/O 2026)**, ~**330×** in two years ([Pichai, I/O 2025 keynote](https://blog.google/innovation-and-ai/technology/ai/io-2025-keynote/); I/O 2026 via [Business Insider](https://www.businessinsider.com/ceo-sundar-pichai-google-ai-growth-io-conference-2026-5)). Microsoft disclosed **>100 trillion tokens in FY25 Q3, up 5× YoY, with a record 50T in one month**.

**Utilization / depreciation debate.** Burry's claim (10 Nov 2025) is **~$176B of understated depreciation over 2026–2028** — *not* 2023–2028, as commonly misquoted ([CNBC, 2025-11-11](https://www.cnbc.com/2025/11/11/big-short-investor-michael-burry-accuses-ai-hyperscalers-of-artificially-boosting-earnings.html)). SEC filings partly rebut it: Alphabet moved 4→6 years in Jan 2023 and has not moved since; Microsoft is at "two to six years"; Meta extended to 5.5 years in Jan 2025; **Amazon shortened servers 6→5 years effective 2025-01-01, taking +$1.4B depreciation and −$1.0B net income** ([Amazon FY2025 10-K](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000004/amzn-20251231.htm)) — i.e. at least one hyperscaler moved the *other* way.

**Rental prices.** The "$8/hr → $2/hr H100" story is a tier-mixing artifact: ~$2/GPU-hr exists only in **spot/preemptible** tiers (Nebius $2.15, AWS p5 spot $2.60), while on-demand H100 is still **$3.85–6.88** and B300 rents at **$7.89** (RunPod, page updated 2026-09-13). SemiAnalysis TCO: H100 **$1.17** hyperscaler / **$2.00** retail; GB300 NVL72 **$2.31/$5.00** ([InferenceX](https://inferencex.semianalysis.com/chips/h100)). Measured inference cost is highly model- and platform-specific: DeepSeek V4.1 Flash on GB200 NVL72 reaches **$0.006/M tokens**, DeepSeek R1 on B200 **$0.10/M**; **the GB300-vs-MI355X ranking flips by model** (GB300 wins on R1 and GLM-5.3; MI355X beats GB200 on V4 Pro by +313 % tok/s/chip) — a useful caution against single-number comparisons.

---

## 8. Bubble: the specific numbers

Goldman Sachs, *Top of Mind* #129, "Too Much Spend, Too Little Benefit" (Jim Covello), **2024-06-27**. Sequoia's David Cahn, "$200B Question" (Sept 2023) and the larger follow-up. MIT NANDA, *GenAI Divide* (Aug 2025): **95 % of enterprise GenAI pilots fail** — publicly contested on methodology. Capital Economics models an S&P 8,250 end-2026 then a **>20 % drop by end-2027**. BofA: five stocks = **27 %** of S&P 500 growth; tech = **50 %**.

**As of 2026-09-16 the bubble has not burst.** On 14 Sept 2026 the Nasdaq fell **147 points (–0.6 %) to 26,186**, NVIDIA **–3.4 %**, Micron **–5.3 %**, after Dario Amodei published an essay urging the industry to "pace the frontier," echoed by Musk and Altman — with indices still near record highs. Verified pauses/delays: Microsoft slowed datacenter leases (TD Cowen, Feb 2025), the Abilene expansion was dropped (Mar 2026), Stargate UK paused (Apr 2026). **No 2026 cancellation with a quantified write-down was verified.** CBRE's H1 2026 report nevertheless finds North American demand still outpacing supply despite record construction.

---

## 9. Unverified / do-not-cite

- **xAI Colossus 2 "2 GW" and "555,000 GPUs"** — company claims contradicted by satellite cooling-capacity analysis (~350 MW). Present both sides or omit.
- **OpenAI–Microsoft "$250B / 2.5 GW"** — the 2.5 GW figure is unverified; the $250B Azure increment is documented.
- **Bloom Energy datacenter MW/$** — company-level figures obtained only via secondary sources.
- **Llama 3 405B "8.9 GWh" / "11.9 GWh"** — not in Meta's disclosure; modelled arithmetic, not measurement. GPT-4's "~50 GWh" is a SemiAnalysis estimate.
- **DeepSeek R1 "$294,000"** — does not appear in the V3 report or any traced DeepSeek source.
- **Meta absolute water withdrawal; PJM/MISO primary large-load queue GW; Westinghouse AP300 MW; Google TPU utilization or any MFU percentage; a published inference:training spend split; the DeepSeek "$1.3B of GPUs / 50,000 Hopper" figure.**
- **Google 2024 Gemini 1.5 pricing; the "1.3 quadrillion tokens/month late-2025" figure; the H100 "$8/hr in 2023" anchor.**
- **GB300 NVL72 rack TDP** — the ~135 kW figure is an industry estimate, not an NVIDIA spec-sheet value.
- **Epoch's training-compute figures for Grok 4 (5e26) and Gemini 1.0 Ultra (5e25) carry "Speculative" confidence**; GPT-4's 2.1e25 and 25,000 A100s is "Likely," not confirmed by OpenAI.
- Several primary domains (openai.com, google.com, x.ai, reuters.com, sec.gov www) were unreachable from the research environment; those figures rest on dated mirrors and are flagged inline.
