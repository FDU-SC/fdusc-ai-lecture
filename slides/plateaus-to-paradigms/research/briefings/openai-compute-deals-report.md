# OpenAI Compute & Datacenter Deals, Jan 2025 – Sep 16 2026: Announced vs. Delivered

**Method note.** openai.com returns HTTP 403 to this tool and nvidianews.nvidia.com/blogs.nvidia.com fail DNS here, so NVIDIA/OpenAI text is verified via verbatim press-release reprints (StorageNewsletter, TechPowerUp) and via SoftBank/Microsoft/AMD/Crusoe IR pages, which serve the same releases. SEC.gov blocks automated fetches (403); AMD filings were read via ir.amd.com. Figures below are labelled **[PRIMARY]**, **[REPORTED]** (credible secondary), or **UNVERIFIED**.

## 1. Stargate: claimed vs. committed

**[PRIMARY]** [SoftBank/OpenAI release, Jan 22 2025](https://group.softbank/en/news/press/20250122) (DC dateline Jan 21): Stargate "**intends to invest $500 billion over the next four years**"; "**We will begin deploying $100 billion immediately**." Initial equity funders: SoftBank, OpenAI, Oracle, MGX. SoftBank = financial responsibility, OpenAI = operational; Masayoshi Son chairman. Tech partners: Arm, Microsoft, NVIDIA, Oracle, OpenAI.

Key point: **$500B is stated intent, not committed capital.** No tranche schedule, no signed customer contracts, and the word "intends" carries the claim. **No primary source committing $500B of actual capital was found.** Entity structure beyond "a new company" was never detailed in the release; I found **no** primary disclosure of a "Stargate LLC" capital table or of the $100B having been funded.

**[PRIMARY]** [SoftBank/OpenAI/Oracle, Sep 24 2025](https://group.softbank/en/news/press/20250924) (Sep 23 dateline) escalated: five new sites plus Abilene and CoreWeave projects = "**nearly 7 gigawatts of planned capacity and over $400 billion in investment over the next three years**," on a "clear path to securing the full $500 billion, **10-gigawatt** commitment… by the end of 2025, ahead of schedule."

## 2. Stargate sites

**[PRIMARY]** site list: [OpenAI/SoftBank, Sep 23 2025](https://group.softbank/en/news/press/20250924) and [Michigan, Oct 30 2025](https://www.reuters.com/5f374b32b07b/technology/openai-oracle-related-digital-announce-new-stargate-data-center-michigan-2025-10-30/). **Capacity figures below are [REPORTED] third-party estimates from [Epoch AI, Apr 17 2026](https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand)** — not company statements, and not the same as energized load.

| Site | Current (GW) | Projected (GW) | Constr. began | Proj. complete | Power |
|---|---|---|---|---|---|
| Abilene, TX (Crusoe/Oracle) | **0.3** | **1.2** | Q2 2024 | Q4 2026 | on-site gas + grid |
| Shackelford County, TX (Vantage) | 0 | **2.0** | Q3 2025 | Q4 2028 | on-site gas |
| Doña Ana County, NM (STACK "Project Jupiter") | 0 | **2.2** | Q4 2025 | Q4 2028 | 2× gas microgrids |
| Milam County, TX (SB Energy) | 0 | **1.2** | Q3 2025 | Q4 2028 | on-site |
| Port Washington, WI (Vantage "Lighthouse") | 0 | **1.3** | Q1 2026 | Q4 2028 | grid (70% renewables) |
| Saline Twp., MI (Related Digital "The Barn") | 0 | **1.4** | Q4 2025 | Q4 2028 | grid |
| Lordstown, OH (SB Energy) | 0 | **<0.3** | Q4 2025 | unknown | grid |

**Totals: >9 GW planned; ~0.3 GW operational as of Apr 17 2026.** SoftBank owns hardware at Milam County and Ohio; Oracle elsewhere.

- **Abilene delivered reality:** **[PRIMARY]** "Oracle began delivering the first NVIDIA GB200 racks in **June**" (2025) ([SoftBank, Sep 24 2025](https://group.softbank/en/news/press/20250924)). 4 of 8 buildings operational; 0.3 GW ≈ 250,000 H100-equivalents, 1.2 GW ≈ 1.0M ([Epoch AI](https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand)). **[REPORTED]** 450,000 GB200 GPUs planned ([DCD](https://www.datacenterdynamics.com/en/news/openai-and-oracle-to-deploy-450000-gb200-gpus-at-stargate-abilene-data-center/)); Oracle ~$40B GB200 purchase ([Benzinga/FT, May 2025](https://cdn2.benzinga.com/markets/equities/25/05/45599854/oracle-to-spend-40-billion-on-nvidia-gb200-chips-for-openais-texas-data-center-report)).
- **Michigan:** announced Oct 30 2025 at **1 GW** ([Reuters](https://www.reuters.com/5f374b32b07b/technology/openai-oracle-related-digital-announce-new-stargate-data-center-michigan-2025-10-30/)), **$7B** ([Bridge Michigan](https://bridgemi.com/michigan-environment-watch/dte-consumers-advance-plans-for-power-hungry-data-centers-in-michigan/)). Epoch later estimates 1.4 GW. **UNVERIFIED:** the "$16B Related Digital financing" figure (single trade-press source).

## 3. OpenAI–Oracle $300B / 4.5 GW

**[PRIMARY]** [SoftBank, Sep 24 2025](https://group.softbank/en/news/press/20250924): "In **July**, OpenAI and Oracle entered an agreement to develop **up to 4.5 gigawatts** of additional Stargate capacity… a partnership that **exceeds $300 billion** between the two companies over the **next five years**." **[REPORTED]** first surfaced via WSJ on **Sep 10 2025** ([PYMNTS citing WSJ](https://www.pymnts.com/news/artificial-intelligence/2025/oracle-and-openai-strike-300-billion-cloud-agreement-for-ai-infrastructure/)). **There is no standalone Oracle press release for this deal.**

## 4–6. Silicon deals: announced vs. status

| Deal | Announced | Announced terms | Status as of Sep 2026 |
|---|---|---|---|
| **NVIDIA** | Sep 22 2025 | **Letter of intent**; "**at least 10 GW**"; "up to **$100B**… progressively as each gigawatt is deployed"; **first 1 GW in 2H 2026** on Vera Rubin ([reprint](https://www.storagenewsletter.com/2025/09/24/openai-and-nvidia-announce-strategic-partnership-to-deploy-10-gigawatts-of-nvidia-systems/)) | **[REPORTED]** investment cut **$100B → $30B** ([Business Standard, Feb 20 2026](https://www.business-standard.com/technology/tech-news/nvidia-30bn-openai-investment-after-shelving-100bn-deal-126022000503_1.html); [eWEEK](https://www.eweek.com/news/nvidia-openai-30b-plan/)). **No evidence found that the first 1 GW was delivered.** |
| **AMD** | Oct 6 2025 | **6 GW**; first **1 GW** MI450 in **2H 2026**; warrant for **up to 160,000,000 shares** ([AMD IR, PRIMARY](https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)) | **[PRIMARY]** May 5 2026: "**begun sampling** MI450… on track to **ramp** Helios production shipments in 2H"; "initial volume in Q3, significant ramp in Q4" ([Q1'26 call](https://www.fool.com/earnings/call-transcripts/2026/05/06/amd-amd-q1-2026-earnings-call-transcript/)). Aug 4 2026 8-K: Helios launched, "**begins to ramp**" ([EX-99.1](https://ir.amd.com/financial-information/sec-filings/content/0000002488-26-000121/q22026991.htm)). **No warrant tranche vesting disclosed.** |
| **Broadcom** | Oct 13 2025 | **10 GW** of OpenAI-designed accelerators; "**signed a term sheet**" (not definitive) ([reprint](https://www.techpowerup.com/341833/openai-teams-up-with-broadcom-to-deploy-10-gigawatts-of-ai-accelerators)) | **[PRIMARY]** Q3 FY26 call: "**shipped Jalapeno**, OpenAI's first-generation custom accelerator"; **1.3 GW planned for 2027**; "line of sight" for **>5 GW in 2028** — i.e. ~6.3 GW visible vs 10 GW announced. XPV vehicle (Apollo/Blackstone) targets "more than 20 GW" for OpenAI+Anthropic by end-2028 ([transcript](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)). |

**AMD warrant %:** the release states no percentage. 160M ÷ the ~1.66B diluted shares AMD guided for Q2 2026 = **≈9.6%** (*my computation*, matching the ~10% press figure).

## 7. Microsoft (Oct 28 2025) and AWS (Nov 3 2025)

- **[PRIMARY]** OpenAI's deal counsel: "OpenAI has agreed to purchase an **incremental $250 billion of Azure services**, and Microsoft will no longer have a **right of first refusal** to be OpenAI's compute provider" ([Sullivan & Cromwell, Oct 30 2025](https://www.sullcrom.com/About/News-and-Events/Highlights/2025/October/OpenAI-Microsoft-Reach-Deal-Next-Chapter-Landmark-Partnership)). **$250B Azure is CONFIRMED.** Microsoft 10-Q subsequent-event note exists ([SEC](https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/R26.htm)) but was unfetchable.
- **[REPORTED]** Microsoft ~27% stake, ~$135B ([Silicon Republic](https://www.siliconrepublic.com/business/microsoft-openai-27pc-135bn-nonprofit-130bn-corporate-restructuring)).
- **"2.5 GW" is UNVERIFIED.** No primary or reliable secondary source ties a 2.5 GW figure to the restructuring. Do not use it.
- **New:** [Microsoft blog, Apr 27 2026](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/) — amended agreement: OpenAI may serve **all** products on any cloud; Microsoft IP licence **non-exclusive** through **2032**; Microsoft **stops paying** revenue share to OpenAI; OpenAI→Microsoft revenue share runs **through 2030, subject to a total cap**. **No dollar or GW figures.**
- **[REPORTED]** AWS: **$38B**, "hundreds of thousands" of NVIDIA GPUs ([Reuters, Nov 3 2025](https://www.reuters.com/business/retail-consumer/openai-amazon-strike-38-billion-agreement-chatgpt-maker-use-aws-2025-11-03/)). **Contract term UNVERIFIED** (the widely repeated "seven-year" was not confirmed in a primary source).

## 8. 2026 reality check — reversals

- **Abilene expansion dropped, Mar 6 2026:** Oracle and OpenAI ended plans to expand the flagship site (planned 2.1 GW); Microsoft/Crusoe took the adjacent **900 MW** campus instead ([Reuters](https://www.reuters.com/business/oracle-openai-end-plans-expand-texas-data-center-site-bloomberg-news-reports-2026-03-06/); [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-06/oracle-and-openai-end-plans-to-expand-flagship-data-center); [Crusoe](https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure)).
- **Stargate UK paused, Apr 9 2026** over energy costs and regulation ([CNBC](https://www.cnbc.com/2026/04/09/openai-halts-uk-stargate-project.html)).
- **New Ohio deal, Jul 26 2026:** NVIDIA in talks to guarantee **~$250B** financing for a **10 GW** OpenAI campus (SB Energy developer, former uranium-enrichment site ~50 miles south of Columbus); **first phase ~800 MW in 2028**; total cost incl. chips could exceed **$500B**; **terms not final and could be scrapped** ([Reuters](https://www.reuters.com/business/media-telecom/nvidia-talks-with-openai-guarantee-250-billion-financing-data-center-wsj-reports-2026-07-26/)).

**Bottom line:** of roughly **35+ GW** announced across Stargate (10 GW), Oracle (4.5 GW), NVIDIA (10 GW), AMD (6 GW) and Broadcom (10 GW), **≈0.3 GW was verifiably operational as of Apr 2026**, all at Abilene. Every 2026 datapoint shows announced capacity revised down, delayed, or reassigned.
