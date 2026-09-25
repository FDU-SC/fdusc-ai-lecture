# Energy and Physical Constraints on AI Datacenters, 2023 – Sept 2026

Primary sources unless marked. Access notes: `pjm.com`, `eia.gov`, `ercot.com` unreachable from the research sandbox, so RTO figures rest on named secondary reporting of primary documents. LBNL PDFs were retrieved via OSTI after WAF blocks.

## 1. Datacenter electricity

| Source (date) | Figure |
|---|---|
| [IEA, *Energy and AI* (Apr 2025)](https://www.iea.org/reports/energy-and-ai/executive-summary) | **2024: 415 TWh = ~1.5%** of world electricity (US 45%, China 25%, Europe 15%; +12%/yr since 2017). **2030: ~945 TWh**; 2035 Base Case ~1,200 TWh, case range **700–1,700 TWh**. **~20% of planned projects at risk of delay**; transmission build 4–8 yrs; transformer/cable waits doubled in 3 yrs; 50% of US projects sit in existing clusters |
| **[IEA, *Key Questions on Energy and AI* (16 Apr 2026)](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary)** | **2025: 485 TWh → 2030: ~950 TWh = ~3% of global electricity.** DC demand **+17% in 2025**; AI-focused DCs **+50%**. Energy per AI task falling **≥10× annually**; but reasoning/video/agentic tasks cost **100s–1,000s× more per query**. Rack power density **×11 (2020–25)**, further **×4 by 2027**; load swings **>50% of rated capacity per second**; **~20–25 GW DC battery storage by 2030**; onsite gas must be **overbuilt 30–70%**; **~15–27 GW onsite gas by 2030**; HBM shortage through **≥2027** |
| [LBNL, *2024 US Data Center Energy Usage Report* (Dec 2024)](https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/) | **2023: 176 TWh = 4.4%** of US electricity (58 TWh in 2014); **2028: 325–580 TWh = 6.7–12%** |
| **[LBNL, *2025 Update*, LBNL-2001758, DOI 10.71468/P1RP4F (18 Jun 2026)](https://www.osti.gov/biblio/3374245)** | **2024: 192 TWh = 4.7%** (upward revision; prior years revised *down*). 2028 Reference Case **464 TWh**; **2030 Reference Case 649 TWh = 11.8%**, range **521–843 TWh = 9.5–15.3%**. DCs = **33% of US load growth 2024–30**; +14% 2023→24, **+22% 2024→25, +29% 2025→26**; **148 GW interconnection capacity needed by 2030** at 50% utilization = **+17.4 GW/yr** |

LBNL's 2026 revision **raises** the path above its 2024 Report and above IEA's US figure (**~430 TWh in 2030**), inside EPRI's 2026 range (**~390–800 TWh**). **No 2026 revision to IEA's global figure** beyond the 485/950 TWh restatement.

## 2. Interconnection queues

**[LBNL *Queued Up: 2026 Edition* (Jun 2026, data through end-2025)](https://emp.lbl.gov/sites/default/files/2026-06/Queued%20Up%202026%20Edition.pdf)** — **covers generation/storage only; large-load queues are explicitly excluded.**

- **~2,061 GW active** (1,312 GW generation + 749 GW storage), **−10% YoY**
- **Gas 253 GW, +86%** — the only growing resource; solar 773 GW (−19%), storage 749 GW (−16%), wind 220 GW (−19%)
- **>750 GW withdrew in 2025** vs ~600 GW new (second straight net outflow); **13% of capacity** (19% of projects) requesting 2000–2020 reached operation by end-2025; **75% withdrawn**
- Median **61 months** request→operation for 2025 projects (36 in 2015, 22 in 2008); **549 GW holds an executed IA but is not operating** (incl. 45 GW gas)

**ERCOT large-load queue** (requests only — duplicated and speculative): **~63 GW (Dec 2024) → >233 GW (Dec 2025, >70% datacenter) → ~410 GW (9 Apr 2026) → >438 GW (18 Jun 2026) → ~474 GW (Aug 2026)**. Of the Dec-2025 total **only 7.5 GW was energized (3.2%)**; ERCOT's own filing puts **realized peak at 49.8% of requested MW**. Its Apr-2026 preliminary forecast of **367,790 MW peak by 2032** is explicitly unadjusted. Actual ERCOT peak: **91.1 GW, 22 Jul 2026**.

**PJM capacity clearing prices** ($/MW-day): 2024/25 **$28.92** → 2025/26 **$269.92 (+833%)** → 2026/27 **$329.17** → 2027/28 **$333.44** → 2028/29 **$325.00 (−2.5%)**, clearing **6,831 MW short** (14.7% reserve margin vs 20%). FERC issued **show-cause orders on large-load interconnection to six RTOs, 18 Jun 2026**. Texas SB 6 (20 Jun 2025) sets the large-load threshold at **≥75 MW**.

## 3. Behind-the-meter gas

| Item | Figure | Date/source |
|---|---|---|
| xAI Memphis — **only permit issued** | **15 Solar SMT-130 turbines = up to 247 MW** | Shelby County Health Dept, [2 Jul 2025](https://techcrunch.com/2025/07/03/xai-gets-permits-for-15-natural-gas-generators-at-memphis-data-center/) |
| xAI Memphis — unpermitted fleet | **35 turbines / ~421 MW** (26/407 MW still running 15 Jun 2025) | [SELC/TechCrunch, 18 Jun 2025](https://techcrunch.com/2025/06/18/xai-is-facing-a-lawsuit-for-operating-over-400-mw-of-gas-turbines-without-permits/) |
| xAI Southaven MS | **69 temporary turbines ≈ 1,775 MW by Jul 2026**; permit for **41 permanent ≈ 1,200 MW** | Sci. American 9 Sep 2026 (secondary) |
| xAI compute draw | COLOSSUS I+II **~1.0 GW nameplate as of 31 Mar 2026**; **$399M litigation accrual** | [SpaceX S-1, 20 May 2026](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001181412) |
| **GE Vernova** gas backlog+slots | **50 GW (Q1'25) → 55 → 62 → 83 → 100 → 116 GW (Q2'26)**, guiding **≥125 GW by YE2026**; firm 53 GW + slots 63 GW; RPO **$119.0B → $176B**; output **20 GW annualized Q3'26, 24 GW 2028, 30 GW 2030** | SEC 8-Ks (CIK 0001996810) |
| Siemens Energy Q3 FY26 | Gas Services backlog **69 GW firm**; group backlog **€162B** | quarterly release |
| Orders / lead times | **846 units / 100.3 GW in 2025** vs 399/58.2 GW 2024; large turbine lead time **>5 yrs**; **~$2,000/kW → ~$3,000/kW in six months** | EPRI via [Utility Dive, 23 Mar 2026](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/) |
| **Meta–Entergy, Hyperion (Richland Parish, LA)** | **10 gas plants / 7.5 GW** = 3 approved in 2025 + **7 new** (announced 27 Mar 2026); **>$30% of Louisiana's entire grid capacity**; plus up to **2.5 GW renewables/storage**; cost **~$11bn**; **15-yr** contract terms; Louisiana PSC approval pending | [Fortune, 27 Mar 2026](https://fortune.com/2026/03/27/meta-hyperion-10-gas-power-plants-louisiana-entergy/) |
| Hyperion campus size | $10bn initial (Dec 2024), 2,250 acres + 1,400 acres added; **Blue Owl JV up to $27bn** total development cost (Oct 2025) | same |
| **Bloom Energy–Oracle** | MSA for **up to 2.8 GW** solid-oxide fuel cells; **1.2 GW already contracted**, deploying through 2027; Oracle received a **$400M warrant** (9 Apr 2026). On-site cells energize a DC in **90 days** without grid connection | [Nasdaq/Zacks, 14 Apr 2026](https://www.nasdaq.com/articles/oracle-taps-bloom-energy-power-ai-data-centers-hold-stock) |
| **Bloom Energy–Brookfield** | **$5bn framework, up to 1 GW** behind-the-meter (13 Oct 2025) → **raised to $25bn** (30 Jun 2026), a fivefold increase | [energynews.pro, 2 Jul 2026](https://energynews.pro/en/brookfield-and-bloom-energy-raise-their-energy-partnership-to-25-billion) |

## 4. Nuclear

| Deal | MW | Terms | Date | Delivery |
|---|---|---|---|---|
| Constellation–Microsoft **Crane (TMI-1)** | **835** | 20-yr PPA; **$1B DOE loan closed**; FERC CIR transfer (ER26-2028) | PPA [20 Sep 2024](https://www.sec.gov/Archives/edgar/data/1868275/000186827524000058/ceg-202409208kexh991.htm); DOE [18 Nov 2025](https://www.energy.gov/articles/energy-department-closes-loan-restart-nuclear-power-plant-pennsylvania) | **target moved EARLIER to 2027** |
| Talen–AWS Susquehanna | up to **1,920** | **17-yr, ~$18B to 2042**; ramp 840–1,200 MW by 2029 | [11 Jun 2025](https://www.sec.gov/Archives/edgar/data/1622536/000162828025030559/a20250611pressreleasebusin.htm) | 2029–32 |
| Vistra–AWS Comanche Peak | up to **1,200** | 20-yr | [6 Nov 2025](https://www.sec.gov/Archives/edgar/data/1692819/000119312525268033/d33941dex991.htm) | from 2027 |
| Vistra–Meta PJM | **>2,600** (2,176 operating + 433 uprates) | 20-yr | [9 Jan 2026](https://www.prnewswire.com/news-releases/vistra-and-meta-announce-agreements-to-support-nuclear-plants-in-pjm-and-add-new-nuclear-generation-to-the-grid-302656941.html) | **operating** |
| Constellation–Meta Clinton IL | **1,121** | 20-yr | [3 Jun 2025](https://www.constellationenergy.com/news/2025/constellation-meta-sign-20-year-deal-for-clean-reliable-nuclear-energy-in-illinois) | Jun 2027 |
| NextEra–Google Duane Arnold (restart) | **615** | 25-yr, full capacity | [28 Oct 2025](https://www.sec.gov/Archives/edgar/data/753308/000075330825000055/neeq32025exhibit99.htm) | 2029 |
| Meta RFP → Oklo / TerraPower | **1.2 GW / 2.8 GW** | Meta prepayment; 2 Natrium + rights to 6 | [9 Jan 2026](https://www.nasdaq.com/press-release/oklo-meta-announce-agreement-support-12-gw-nuclear-energy-development-southern-ohio) | 2030s |
| Fermi America, TX | **17 GW campus**, 4× AP1000 | COLA accepted Sept 2025 | [424B4, 1 Oct 2025](https://www.sec.gov/Archives/edgar/data/2071778/000121390025094424/ea0252333-11.htm) | COLA only |

**SMRs (company targets, not commitments).** [Kairos–Google](https://kairospower.com/updates/google-kairos-power-tva-collaborate-to-meet-americas-growing-energy-needs): **500 MW by 2035**, first unit **2030** (28→**50 MW**); new **Kairos–TVA PPA up to 50 MW** (18 Aug 2026). [X-energy–Amazon](https://x-energy.com/news/triso-x-advances-to-next-phase-of-construction-for-tx-1-fuel-fabrication-facility/): "up to **>5 GW by 2039**"; Xe-100 = 80 MW; pipeline **144 reactors / ~11.5 GWe**. [Oklo](https://www.sec.gov/Archives/edgar/data/1849056/000162828026054571/oklo-20260630.htm): **Switch 12 GW**, **Meta 2 GW**, **~14 GW pipeline** — Equinix/Diamondback/Prometheus are **non-binding LOIs, MW undisclosed**; **no COLA date**. TerraPower: **NRC construction permit 4 Mar 2026** (first commercial advanced-nuclear CP), **construction start 23 Apr 2026**, target 2030; Meta up to **8 Natrium / 2.8 GW baseload**, initial units **as early as 2032**. NuScale's TVA program is "discussions" — **unsigned**. Westinghouse: **6 AP1000s operating, 14 building, 5 contracted**; AP300 MW **UNVERIFIED**.

**Corrections to the brief:** (1) Crane's 2028 target **accelerated to 2027**, did not slip. (2) **No 2025 FERC "settlement"** in Talen/AWS — the amended ISA was **rejected 2–1 on 1 Nov 2024 (ER24-2172)**; the fix was a front-of-the-meter restructure. (3) **No Vistra–Comcast PPA exists** in Vistra PRs, SEC filings or EDGAR full-text — treat as nonexistent; Comanche Peak's counterparty is AWS. (4) The 1,920 MW figure dates from **11 Jun 2025**, not Mar 2024. (5) Fermi America has **no signed customer** and lost its CEO/CFO in May 2026. (6) The "1–4 GW" Meta RFP resolved into **~6.6 GW by 2035**.

## 5. Water

| Operator | Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| **Google** ([2026 Env. Report, 30 Jun 2026](https://sustainability.google/reports/google-2026-environmental-report/)) | Consumption, DCs+offices (M gal) | **6,352** | **8,135** | **10,869** (+34% YoY) |
| Google | Withdrawal / DC-only consumption (M gal) | — | — | **14,689 / 10,523** |
| **Microsoft** ([2025 Env. Report](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2025-Microsoft-Environmental-Sustainability-Report.pdf)) | Withdrawal / consumption (m³) | **12,951,000 / 7,844,000** | **10,377,000 / 5,807,000** | — |
| **Amazon** ([2025 Sustainability Report](https://sustainability.aboutamazon.com/2025-amazon-sustainability-report.pdf)) | DC withdrawal | — | — | **9.4 billion liters** |

The cited "Microsoft 7.84 M m³ (2023)" is **consumption, not withdrawal** (withdrawal: 12.95 M m³). Microsoft FY24 withdrawal WUE **0.30 L/kWh** (−39% vs 0.49 in 2021); Amazon WUE **0.25 (2021) → 0.12 (2025) L/kWh**; Google replenished **7,717 M gal in 2025 = 78%** of freshwater consumption. **Meta's absolute withdrawal is UNVERIFIED** (only >**1.6 bn gallons restored in 2024**). **LBNL's 2025 Update contains no water data.**

## 6. Per-query energy

| Source | Figure | Date |
|---|---|---|
| [Google, arXiv:2508.15734](https://arxiv.org/abs/2508.15734) | **0.24 Wh median Gemini text prompt** (0.14 accelerator + 0.06 CPU/DRAM + 0.02 idle + 0.02 PUE); **0.26 mL water**; 4,167 prompts/kWh; narrow-boundary variant 0.10 Wh | 21 Aug 2025 |
| Sam Altman | **0.34 Wh/prompt**, ~0.3 mL water; methodology undisclosed | **Jun 2025**, not Oct |
| [Epoch AI](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use) | **~0.3 Wh** typical; **2.5 Wh @10k input tokens; ~40 Wh @100k**; band 0.1–4 Wh | 7 Feb 2025 |
| [Luccioni et al., arXiv:2311.16863](https://arxiv.org/abs/2311.16863) | Measured, unbatched: **0.002 Wh** (classification) → **0.047 Wh** (text gen) → **2.907 Wh** (image gen) per inference | 28 Nov 2023 |
| BLOOM 176B, arXiv:2211.02001 | **~4 Wh/prompt** inference; training **24.7 tCO2eq** | 3 Nov 2022 |

Range: **~0.10–4 Wh/query (1×10⁻⁴–4×10⁻³ kWh)**, up to **~40 Wh** at 100k-token input; **0.002–11.5 Wh** across all measured tasks. Spread driven by measurement boundary (2.4×), batching (~17×), output length (~4×), modality (62×), hardware and PUE. Training: **Llama 3.1 405B = 11,390 tCO2eq** ([Meta model card, Jul 2024](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct)), 3.8×10²⁵ FLOPs — but **neither "8.9 GWh" nor "11.9 GWh" appears in Meta's disclosure; both are modeled arithmetic.** GPT-4's "~50 GWh" is a **SemiAnalysis estimate**; GPT-3 was **1,287 MWh** ([arXiv:2104.10350](https://arxiv.org/abs/2104.10350), 2021). **No frontier lab has published a measured 2025–26 training-run figure.**

## 7. Is power the binding constraint?

**Pro.** Huang, GTC 2025: *"Every single data centre in the future will be power-limited. We are now a power-limited industry."* Nadella, BG2Pod, Nov 2025: *"The biggest issue we are now having is not a compute glut, but it's power… It's not a supply issue of chips. It's actually the fact that I don't have warm shells to plug into… You may actually have a bunch of chips sitting in inventory that I can't plug in."* PJM cleared **6,831 MW short** for 2028/29; ERCOT realizes **49.8%** of requested load; Capgemini (Jan 2026) found **67% of 600+ utility executives call queue requests "phantom."**

**Counter-evidence.** PJM prices flattened at the cap then **fell 2.5%** (total auction cost +1.9%); NERC (19 May 2026) found **>58 GW of summer capacity added YoY that "has outpaced demand,"** with ERCOT and MISO shedding elevated-risk status; **Texas paused new large-load interconnections** pending a governor's audit; Grid Strategies estimates the datacenter portion of utility forecasts is **overstated by ~25 GW**; Microsoft dropped **~2 GW** of leases in early 2025. EPRI: *"The limiting factor does not appear to be turbine technology, but the manufacturing system itself."*
