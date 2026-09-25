# GPU Rental Prices + Depreciation Research
Research date: 2026-09-16. Each figure tagged [PRIMARY] / [SECONDARY] / [VENDOR/DISPUTED].

## 1A. VENDOR PUBLISHED LIST PRICES (fetched live 2026-09-16)

### Lambda (lambda.ai/pricing) — on-demand list, self-serve, per-GPU/hour, no commitment [VENDOR/PRIMARY-published]
URL: https://lambda.ai/pricing (fetched 2026-09-16)
On-demand instances (8x/4x/2x/1x configs):
- NVIDIA B200 SXM6 180GB: $6.69 (8x) / $6.79 (4x) / $6.89 (2x) / $6.99 (1x) per GPU/hr
- NVIDIA H100 SXM 80GB: $3.99 (8x) / $4.09 (4x) / $4.19 (2x) / $4.29 (1x) per GPU/hr
- NVIDIA H100 PCIe 80GB: $3.29 (1x) per GPU/hr
- NVIDIA GH200 96GB: $2.29 per GPU/hr
- NVIDIA A100 SXM 80GB: $2.79; A100 SXM/PCIe 40GB: $1.99; A6000: $1.09; A10: $1.29; V100: $0.79
- NO H200 and NO GB200/GB300 listed on Lambda pricing page as of 2026-09-16 (H200 appears to have been dropped from the public price list).

Lambda 1-Click Clusters (reserved/committed, 2 weeks–1 year) [VENDOR list price]:
- NVIDIA HGX B200: 16 GPUs $9.86/GPU/hr; 64 GPUs $9.36; 256+ GPUs $8.87; 1 year+ = "Talk to our team"
- NVIDIA H100: 16 GPUs $6.16/GPU/hr; 64 GPUs $5.85; 256 GPUs $5.54; 1 year+ = "Talk to our team"

NOTE THE SPREAD: same vendor, H100 = $3.99/hr on-demand vs $5.54–$6.16/hr in the *reserved cluster* tier. Reserved cluster pricing is HIGHER than on-demand list on Lambda's own page — undermines naive "reserved is cheaper" narratives.

### RunPod (runpod.io/pricing) — page states "Updated September 13, 2026" [VENDOR/PRIMARY-published]
URL: https://www.runpod.io/pricing (fetched 2026-09-16)
Secure Cloud Pods (on-demand, per hour):
- B300 288GB HBM3e: $7.89/hr
- B200 180GB: $6.79/hr
- H200 141GB: $4.59/hr
- H100 NVL 94GB: $3.19/hr ; H100 PCIe 80GB: $2.89/hr ; H100 SXM 80GB: $3.49/hr
- A100 80GB (PCIe & SXM): $1.59/hr ; L40S 48GB: $1.09/hr ; RTX 5090: $0.99/hr
Serverless (per hour, per worker):
- B300 $9.98 ; B200 $8.64 ; H200 $5.93 ; H100 PRO $4.79 ; A100 $2.72
Clusters (no commitment, per hour): H200 SXM $4.31 ; A100 SXM $1.79 ; H100 SXM / B200 = "Contact sales"
Reserved Clusters (1/3/6/12mo): all "Contact sales" (no public rates).
NOTE: B300/GB300-class publicly rentable on RunPod at $7.89/hr (2026-09-13) — this is the key new-2026 datapoint.
NOTE: RunPod H100 SXM ($3.49) < Lambda H100 ($3.99–4.29); RunPod H200 ($4.59) is now priced BELOW H100 reserved-cluster rates at Lambda.

### Vast.ai — live supply/demand marketplace (spot-like) [VENDOR/MARKET]
URL: https://vast.ai/pricing (fetched 2026-09-16) — prices are JS-rendered; page advertises three tiers:
On-Demand (guaranteed uptime, per-second billing), Interruptible ("50%+ cheaper", preemptible), Reserved (1/3/6-month terms, "up to 50% off").
Exact live $/GPU-hr numbers NOT retrievable from static HTML — UNVERIFIED (need JS or API).

### Nebius AI Cloud (nebius.com/prices) — on-demand AND preemptible list, per GPU-hour [VENDOR/PRIMARY-published]
URL: https://nebius.com/prices (fetched 2026-09-16). "Commitment discounts: pay up to 35% less than on-demand rates by reserving large-scale clusters for multiple months."
| GPU instance | Preemptible $/GPU-hr | On-demand $/GPU-hr |
|---|---|---|
| NVIDIA GB300 NVL72 | — | Contact us |
| NVIDIA HGX B300 | $4.30 | **$7.85** |
| NVIDIA GB200 NVL72 | — | Contact us |
| NVIDIA HGX B200 | $3.95 | **$7.15** |
| NVIDIA HGX H200 | $2.45 | **$4.50** |
| NVIDIA HGX H100 | $2.15 | **$3.85** |
| NVIDIA RTX PRO 6000 | $0.95 | $1.80 |
| NVIDIA L40S (Intel CPU) | from $0.90 | from $1.82 |
H100 preemptible/spot at $2.15/hr vs on-demand $3.85/hr = a 44% spot discount, published by the vendor.
KEY: H100 on-demand $3.85 (2026) is nowhere near the "$1.7-2.5/hr" claim — that claim matches only PREEMPTIBLE/spot tiers.

### AWS EC2 GPU instances — on-demand list, US regions [VENDOR/PRIMARY-published; aggregator cited]
Source: Vantage Instances (mirrors AWS Price List API), page footer "Updated 9/16/2026, 8:37:38 AM" — fetched 2026-09-16
| Instance | GPUs | On-demand $/hr | $/GPU-hr | Spot $/hr | Spot $/GPU-hr | 1-yr reserved $/hr | 1yr $/GPU-hr | Introduced |
|---|---|---|---|---|---|---|---|---|
| p5.48xlarge (H100 80GB) | 8 | $55.04 | **$6.88** | $20.789 | **$2.60** | $23.777 | **$2.97** | 2023-07-26 |
| p5e.48xlarge (H200 141GB) | 8 | $98.32 (AWS list; see note) | $12.29 | $26.795 | $3.35 | — | — | 2024-09-09 |
| p5en.48xlarge (H200) | 8 | $63.296 | **$7.91** | $27.121 | **$3.39** | — | — | 2024-12-02 |
| p6-b200.48xlarge (B200) | 8 | $113.9328 | **$14.24** | $42.094 | **$5.26** | — | — | 2025-05-15 |
| p6e-gb200.36xlarge (GB200) | 36 | N/A (Capacity Blocks / contact) | — | — | — | — | — | 2025-07-09 |
CAVEAT: Vantage's p5e.48xlarge page displays "$1.843 On Demand", which is internally inconsistent (its own spot figure is $26.795). AWS's actual us-east-1 list for p5e.48xlarge is $98.32/hr = $12.29/GPU-hr — treat the $1.843 as a SCRAPING ERROR / flagged. p5e and p5en figures need re-verification against AWS's own price JSON.
KEY: AWS on-demand $/GPU-hr is ~1.7-2.1x the neocloud list price for the same silicon (p5 H100 $6.88 vs Nebius H100 $3.85 vs RunPod $3.49 vs Lambda $3.99). AWS SPOT for H100 ($2.60/GPU-hr) is in the range of the "H100 fell to $2/hr" narrative — but that's spot, not on-demand.

## 2. MICHAEL BURRY — Nov 2025 DEPRECIATION CLAIMS

Source (reporting, verbatim quotes): CNBC, "'Big Short' investor Michael Burry accuses AI hyperscalers of artificially boosting earnings", published Tue **Nov 11 2025** 9:26 AM EST (updated 10:45 AM EST), by Yun Li. https://www.cnbc.com/2025/11/11/big-short-investor-michael-burry-accuses-ai-hyperscalers-of-artificially-boosting-earnings.html [SECONDARY — but quotes the X post verbatim]

- The X post was made **Monday Nov 10, 2025** (CNBC: "In a post Monday on X").
- Exact quote: "Understating depreciation by extending useful life of assets artificially boosts earnings - one of the more common frauds of the modern era."
- Exact quote: "Massively ramping capex through purchase of Nvidia chips/servers on a 2-3 yr product cycle should not result in the extension of useful lives of compute equipment. Yet this is exactly what all the hyperscalers have done."
- **$176 BILLION** estimated understated depreciation — CNBC: "Burry estimated that from **2026 through 2028**, the accounting maneuver would understate depreciation by about $176 billion." ⚠️ CORRECTION: the widely repeated "2023-2028" framing is WRONG per CNBC — Burry's window was **2026-2028**. Flag as [DISPUTED] where the 2023-2028 range is cited.
- Useful life: he says Nvidia chips/servers run a **2-3 year product cycle**; hyperscalers use 5-6 years. [SECONDARY]
- Oracle: profits "could be overstated by roughly **27%**" by 2028. Meta: "roughly **21%**" by 2028. [SECONDARY]
- He said "more detail" was coming **Nov 25, 2025** ("stay tuned").
- Context (same CNBC piece): Burry's Q3 filing showed put options notional **~$187M against Nvidia** and **~$912M against Palantir** as of **Sept 30, 2025**. Strike prices/expiries not disclosed. Palantir CEO Alex Karp called the wagers "super weird" and "bats--- crazy."

- Substack check 2026-09-16: `https://www.cassandra-unchained.com/` and `/archive` did NOT serve Burry content — the domain currently serves an unrelated site ("Humanity's Last Exam"). Direct Substack posts from Burry's "Cassandra Unchained" are therefore UNVERIFIED as of 2026-09-16 (domain appears to have lapsed/been repurposed, or the newsletter was renamed). Need the canonical Substack URL confirmed from a secondary source.

## 4. DISCLOSED DEPRECIATION SCHEDULES — verbatim from SEC filings (fetched 2026-09-16) [PRIMARY]

### Alphabet — 10-K for FY2025, filed 2026-02-05 (period 2025-12-31) [PRIMARY]
URL: https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000018/goog-20251231.htm
Verbatim: "We depreciate data center and office buildings over periods of seven to 40 years. **We depreciate servers and network equipment generally over a period of six years.** We depreciate corporate and other assets over periods of two to 25 years."
=> Alphabet: **6 years** for servers and network equipment, current as of the FY2025 10-K.
(Historical 4→5 yr change in 2023 and 5→6 yr change effective Jan 1 2025: see section 4b below.)

### Amazon — 10-K for FY2025, filed 2026-02-06 (period 2025-12-31) [PRIMARY]
URL: https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000004/amzn-20251231.htm
Verbatim: "We review the useful lives of equipment on an ongoing basis. **Effective January 1, 2025 we changed our estimate of the useful lives of a subset of our servers and networking equipment from six years to five years.** The shorter useful lives are due to the increased pace of technology development, particularly in the area of artificial intelligence and machine learning."
Footnote (1) to the Property-and-equipment table, verbatim: "**Effective January 1, 2024, we changed our estimate of the useful lives for our servers from five to six years, and effective January 1, 2025, we changed our estimate of the useful lives of a subset of our servers and networking equipment from six to five years.**"
Table as of Dec 31 2025: "Servers and networking equipment — **Five to six years**"; Buildings "Lesser of forty years or the remaining life of the underlying building"; Heavy equipment "Ten to thirteen years"; Other equipment "Three to ten years".
⚠️ CORRECTION to the prompt: Amazon's 5→6 yr server extension was effective **January 1, 2024**, not 2022. The Jan 1 2025 change was a REDUCTION 6→5 for a *subset* only, so the disclosed range is now "five to six years".

### Microsoft — 10-K for FY2026, filed 2026-07-29 (period 2026-06-30) [PRIMARY]
URL: https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm
Verbatim: "The estimated useful lives of our property and equipment are generally as follows: software developed or acquired for internal use, **three years**; **servers and network equipment, two to six years**; buildings and improvements, five to 15 years; leasehold improvements, three to 15 years; and furniture and equipment, one to 10 years."
=> Microsoft: **2 to 6 years** range for servers and network equipment (upper bound 6 years), unchanged as of FY2026 10-K. Microsoft is the only one of the four disclosing a *2-year* lower bound — directly relevant to the Burry debate.

### Meta — 10-K for FY2025, filed 2026-01-29 (period 2025-12-31) [PRIMARY]
URL: https://www.sec.gov/Archives/edgar/data/0001326801/000162828026003942/meta-20251231.htm
Verbatim: "**In January 2025, we completed an assessment of the useful lives of property and equipment, which resulted in an increase in the estimated useful lives of most servers and network assets to 5.5 years, effective January 1, 2025.**"
Dollar impact, verbatim: "Based on the servers and network assets placed in service as of December 31, 2024, the financial impact of this change in estimate included **a reduction in depreciation expense of $2.92 billion and an increase in net income of $2.59 billion, or $1.00 per diluted share, for the year ended December 31, 2025.**"
Table as of Dec 31 2025: "Servers and network assets — **Five to 5.5 years**"; Buildings 25–30 years; Equipment and other 1–25 years; Finance lease ROU assets 5–20 years.
=> Meta: **5 to 5.5 years**; the 5.5-yr extension was an INCREASE and it was material: +$2.59B net income in 2025 (+$1.00/sh).


### Amazon — dollar impact of the Jan 1 2025 6→5 yr reduction [PRIMARY]
Verbatim: "The effect of this change in estimate for the year ended December 31, 2025, based on servers and networking equipment that were included in 'Property and equipment, net' as of December 31, 2024 and those acquired during the year ended December 31, 2025, was **an increase in depreciation and amortization expense of $1.4 billion and a reduction in net income of $1.0 billion, or $0.10 per basic share and $0.10 per diluted share, which primarily impacted our AWS segment.**"
=> Amazon SHORTENED the life and took a real $1.4B D&A hit in 2025, hitting AWS specifically. This is the strongest single fact against the "hyperscalers are all extending lives to inflate earnings" claim.


## 4b. WHEN EACH COMPANY CHANGED THE SCHEDULE (SEC filings, retrieved 2026-09-16) [PRIMARY]

### Alphabet — ONE change: 4 yrs → 6 yrs, effective FY2023 (announced January 2023) [PRIMARY]
FY2023 10-K (filed 2024-01-31): https://www.sec.gov/Archives/edgar/data/0001652044/000165204424000022/goog-20231231.htm
Verbatim: "In January 2023, we completed an assessment of the useful lives of our servers and network equipment, resulting in a change in the estimated useful life of our servers and certain network equipment **to six years**. The effect of this change was **a reduction in depreciation expense of $3.9 billion for the year ended December 31, 2023**, recognized primarily in cost of revenues and R&D expenses."
"Change in Accounting Estimate — In January 2023, we completed an assessment of the useful lives of our servers and network equipment resulting in a change in the estimated useful life of our servers and certain network equipment to six years. This change in accounting estimate was **effective beginning fiscal year 2023**."
=> Alphabet: **4 years → 6 years**, one step, January 2023. ⚠️ CORRECTION: there was NO separate 4→5 yr step in 2023 and NO 5→6 yr step in 2025. Alphabet's FY2025 10-K (2026-02-05) still discloses **six years**, unchanged. The prompt's "6 years (2023)" is CORRECT; a "2025 5→6" change is UNVERIFIED/does not appear in the filings.
Dollar impact: **−$3.9B depreciation expense in FY2023** (i.e. +$3.9B pre-tax benefit).

### Microsoft — 4 yrs → 6 yrs, effective FY2023 (assessment completed July 2022) [PRIMARY]
FY2023 10-K (filed 2023-07-27): https://www.sec.gov/Archives/edgar/data/0000789019/000095017023035122/msft-20230630.htm
Verbatim: "In July 2022, we completed an assessment of the useful lives of our server and network equipment. Due to investments in software that increased efficiencies in how we operate our server and network equipment, as well as advances in technology, we determined we should **increase the estimated useful lives of both server and network equipment from four years to six years**. This change in accounting estimate was **effective beginning fiscal year 2023**. Based on the carrying amount of server and network equipment included in property and equipment, net as of June 30, 2022, the effect of this change in estimate for fiscal year 2023 was **an increase in operating income of $3.7 billion and net income of $3.0 billion, or $0.40 per both basic and diluted share.**"
=> Microsoft: **4 → 6 years**, July 2022 (FY2023). FY2026 10-K still says "servers and network equipment, **two to six years**".
Note also Microsoft's FY2023 depreciation expense FELL to $11.0B from $12.6B in FY2022 explicitly "due to the change in estimated useful lives of our server and network equipment."

