# Claim #22 fact-check — "The second AI winter" (early 1990s)

Checked 2026-09-16. Environment note: `en.wikipedia.org`, `web.archive.org`, `dl.acm.org`, `ieeexplore.ieee.org`, `link.springer.com`, `nytimes.com` were **not reachable** from this sandbox, so Wikipedia's own "AI winter" text (the likely proximate source of the "1987–1993" dating) could not be read, and several paywalled papers could not be retrieved.

## VERDICT: CONTESTED — right in outline, wrong in several specific figures and in its framing

Core phenomenon is real and datable, but (a) "second AI winter" is not the term the standard history uses, (b) the periodization is "mid- to late 1980s" rather than "early 1990s," (c) the FGCS funding figure that circulates is roughly double the official one, and (d) the "1987 DARPA review / three-year funding cuts" trigger could not be verified.

---

## 1. Expert systems / symbolic AI industry

**Verified — contraction is real and documented, but mostly qualitatively.**

- Nilsson (standard history) on the company cohort: Teknowledge (first; Stanford faculty, used EMYCIN), Syntelligence, Production Systems Technologies (Forgy, 1983), **Aion Corporation**, Helix Expert System Ltd., Exsys, IntelliCorp, **Inference Corporation**, and IBM/Xerox/TI/DEC divisions. On the collapse: *"Because it was not too difficult for clients who wanted expert systems to develop their own versions (which were able to run on low-cost workstations and personal computers), many of the expert systems companies ceased to exist, were bought by larger companies, or had to reorient their businesses to provide additional or related services."*
  - Source: Nils J. Nilsson, *The Quest for Artificial Intelligence* (Cambridge UP, 2010), ch. 18.2.4 — full text https://ai.stanford.edu/~nilsson/QAI/qai.pdf
- Hirsch-Kreinsen (peer-reviewed, *AI & Society* 39:1641–1652, 2024): *"by the end of the 1980s at the latest, a situation emerged that is referred to as the AI crisis, or internationally as the second 'AI winter'... A large gap had emerged – and was impossible to overlook – between the expectations of many businesses and policymakers about the commercial usability of expert systems, and their actually realised benefits."* Consequences: *"a significant reduction in the amount of private-sector financing available... Another consequence was a dramatic cutback in AI-oriented research and development (R&D) capacities in many companies."*
  - https://doi.org/10.1007/s00146-023-01629-w ; open PDF https://eldorado.tu-dortmund.de/server/api/core/bitstreams/27544b5f-aacf-40e9-aed8-a43a48764160/content
- Computer History Museum oral history exists on exactly this question: "AI: Expert Systems Pioneer Meeting, day 2 session 7: Why did the expert systems industry decline?", 2018-05-15, 41-pp transcript, catalog 102781127 (Feigenbaum, Hendrix, Harmon, Lenat, Peter Hart, Reid Smith, Herb Schorr). Catalog abstract cites "business management approaches, company revenue models, the lack of expert systems standards, and the complexity of expert systems solutions."
  - https://www.computerhistory.org/collections/catalog/102781127/ (transcript PDF not retrieved)

**COULD NOT VERIFY:** any concrete expert-systems market size at peak or its rate of decline (no dollar figures from any source read); revenue drops, layoff counts, or stock-price collapses for IntelliCorp, Teknowledge, Inference, Aion. The obvious authority — "The Expert Systems Business: How It Grew and Died," *IEEE Annals of the History of Computing* (2022), https://ieeexplore.ieee.org/document/9707876 — is bot-blocked here; even its author/abstract could not be retrieved. **Treat all market-size numbers in claim #22 as unverified.**

## 2. LISP machine market collapse

**Verified:**
- A **1987** contemporary source already describes the market eroding, not collapsing in one event: Jeffrey Stone, "The AAAI-86 Conference Exhibits," *AI Magazine* 8(1), Spring 1987, p. 49 — https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/574 (PDF /download/574/510). Quotes: *"The primary response of the traditional Lisp machine vendors to the erosion of their future markets has been the development of very large scale integration (VLSI) versions of their symbolic processors."* and, of Gold Hill's 80386 Hummingboard, *"The 386 is the last nail in the coffin for Lisp machine leader Symbolics."* It notes *"All that is left now for the Lisp machines is their powerful development environments"*, TI's Compact Lisp Machine for DARPA (spring 1987), Xerox's VLSI Common Lisp Processor program, and projects VLSI Lisp machines at $10k–$25k.
- **Symbolics**: "Symbolics Inc. Seeks Chapter 11 Protection," *Los Angeles Times*, **Feb. 2, 1993** — https://www.latimes.com/archives/la-xpm-1993-02-02-fi-1060-story.html (headline + date verified; body paywalled).
- **Xerox**: "COMPANY NEWS; Xerox Spins Off Intelligence Unit," *The New York Times*, **Aug. 24, 1988** — https://www.nytimes.com/1988/08/24/business/company-news-xerox-spins-off-intelligence-unit.html (headline + date verified via search only; NYT unreachable from sandbox).

**Assessment of the "collapsed around 1987–1988" dating:** consistent with the 1987 AI Magazine evidence of market erosion and the 1988 Xerox spin-off, but the terminal event for Symbolics is 1993 — i.e. a **gradual 1987–1993 decline**, not a single 1987 collapse.

**COULD NOT VERIFY:** LMI (Lisp Machines Inc.) 1987 bankruptcy/GigaMos disposition; TI Explorer introduction date and TI's exit date from the AI/Lisp business; Xerox Interlisp-D/1100 discontinuation and the "Envos" spin-off name; any Lisp-machine market revenue figures.

## 3. Japan's FGCS

**Verified (primary, official):**
- Launched **FY1982** (昭和57年度) by MITI; **ICOT** (Institute for New Generation Computer Technology) established as the promoting organization; ran **11 years**; **~¥54 billion (約540億円)** invested; ended **FY1992** (i.e. March 1993). Evaluation began Nov 1991, interim report June 1992.
  - ICOT 最終評価報告書 (Final Evaluation Report), primary: https://www.airc.aist.go.jp/aitec-icot/ICOT/Museum/FinalReport/node2.html
  - IPSJ Computer Museum: *"Approximately ¥54 billion was invested in the project over 11 years, and it came to an end in 1992."* PIM/p = 512 processors, PIM/m = 256. https://museum.ipsj.or.jp/en//computer/other/0002.html
- **Yes, it was extended into a follow-on**: ICOT's own report states a "研究基盤化プロジェクト" (research-infrastructure project) started **FY1993 for 2 years**; Nilsson likewise: *"In 1993, the project was extended for two years to disseminate FGCS technology."*
- Nilsson on outcome: ten-year plan was 3 + 4 + 3 years; total ten-year budget **¥54.2 billion ≈ $380 million** at the 1990 exchange rate (citing Shunichi Uchida's slides). *"Many observers think that most of the results of the FGCS project are now of historical interest only. The software developed did not find notable applications."*

**Fix needed in claim #22:** the widely repeated "**$850 million**" figure for FGCS is **not supported** by ICOT's own final report or IPSJ (~¥54bn ≈ **$380M**). Also "ended 1992" needs the qualifier that it was extended two years as a follow-on. The "failure" judgment has support (Nilsson: results "of historical interest only"), but it is a judgment, not an official verdict — ICOT's own final report claims international-contribution success.

## 4. DARPA / Strategic Computing

**Verified:**
- SCI written up **October 1983**; funds approved at **$50 million for FY1984**; *"It was to become a billion-dollar program – the largest computer research and development program ever undertaken by the U.S. government up to that time."* *"During the decade from 1983 to 1993 DARPA spent just over $1 billion on SC."*
- The cut mechanism is documented but is **personnel/programmatic, not a named "1987 review"**: *"Jacob Schwartz, who was skeptical about some AI approaches, became the ISTO director in September 1987. He promptly canceled some AI programs and failed to renew others."* DARPA **cancelled the ALV program in April 1988**. In 1991 ISTO split into SISTO and CSTO, "effectively ending attempts to couple basic research with applications." Per Roland, SCI "was never mentioned in public documents or reports after 1989. It vanished from the DARPA budget in 1993."
- The only hard funding numbers found: *"According to Alex Roland, between 1987 and 1989, DARPA's budget for basic AI and Strategic Computing research fell from $47 million to $31 million."*
  - All above: Nilsson, *Quest for Artificial Intelligence*, ch. 23 (https://ai.stanford.edu/~nilsson/QAI/qai.pdf), citing Alex Roland with Philip Shiman, *Strategic Computing: DARPA and the Quest for Machine Intelligence, 1983–1993* (MIT Press, 2002).

**COULD NOT VERIFY:** a specific "**1987 DARPA review**" as the AI-winter trigger, and the "**three-year** funding cuts" formulation. Nothing retrieved supports that specific causal story. The verifiable version is: an SCI that peaked and was cut from 1987 onward (Schwartz, Sept 1987; $47M→$31M by 1989), with the program disappearing from the budget by 1993. Note also that $47M→$31M is the *basic AI + SCI research* line, not the whole SCI budget — do not describe it as "DARPA cut AI funding by a third" without that scope.

## 5. Severity vs. the first winter (1974–1980)

**Verified first-winter facts (Nilsson, ch. 16, 19):**
- **Mansfield Amendment**, passed **Nov 19, 1969**, Defense Procurement Authorization Act of 1970 (PL 91-121): DoD basic research restricted to projects "with a direct and apparent relationship to a specific military function or operation." ARPA renamed DARPA **March 23, 1972**.
- **Lighthill Report** (UK Science Research Council), "Artificial Intelligence: A General Survey": *"In no part of the field have the discoveries made so far produced the major impact that was then [around 1960] promised."* Nilsson: *"Lighthill's report resulted in a substantial curtailment of AI research in the United Kingdom"* (casualties included FREDDY the robot and Donald Michie's Edinburgh work; Michie called it "an outrage").
- **George Heilmeier** became DARPA Director in **1975**; one casualty of his tenure was the speech-understanding (SUR) program; Nilsson: *"DARPA's shift to shorter term applied research, together with the Lighthill report and criticisms from various onlookers, posed difficulties for basic AI research during the next few years. **Nevertheless, counter to Lighthill's assessment, many AI techniques did begin to find application to real problems, launching a period of expansion in AI applications work.**"*
- Lighthill primary text landing page (not text-extracted): https://mlanthology.org/misc/1973/lighthill1973misc-artificial/

**Assessment:** the standard histories do **not** present the early-1990s episode as unambiguously more severe than 1974–1980, and Nilsson's own account of the *first* winter already notes that applications work expanded during it. His account of the second is that it was survivable and brief (see §6).

**COULD NOT VERIFY:** any quantitative severity comparison (federal AI R&D funding series, AI PhD production/Taulbee data, publication counts).

## 6. Historiographic accuracy — what standard histories actually say

- **Nilsson (2010) never uses the label "second AI winter."** His section is titled `24.4 The "AI Winter"` — with quotation marks — and he dates the downturn to the **mid- to late 1980s**, not the early 1990s:
  > "During the early 1980s, many AI sponsors, in government and in industry, had greatly inflated expectations of what AI could do... The failure to deliver systems matching these unrealistic hopes, together with the accumulating critical commentary that I have already mentioned, combined **in the mid- to late 1980s** to bring on what came to be called an 'AI winter.'"
- **The term predates the downturn.** At the **1984 AAAI** national convention, a panel titled "The 'Dark Ages' of AI – Can We Avoid Them or Survive Them?" was chaired by Drew McDermott (Yale), who said: *"I think it is important that we take steps to make sure the 'AI Winter' doesn't happen – by disciplining ourselves and educating the public."* So "AI winter" was insider shorthand by 1984 — the narrative was partly constructed *in advance* of the contraction.
- **Nilsson's severity verdict is explicitly mild:**
  > "During the late 1980s, membership in the AAAI gradually fell. By 1996, it had leveled off to between 4,000 and 5,000 members. Advertising in the AI Magazine dropped also – as did participation by government and industry in AI conference exhibits. Several AI companies closed their doors, and AI research at some of the larger computer hardware and software companies was terminated... **But the winter endured only for a season – a season not of hibernation but of renewed efforts to carry on.** Several new ideas were explored, and older ones were strengthened with added powers."
- **Hirsch-Kreinsen (2024, peer-reviewed) explicitly rejects an all-crisis reading of the 1990s:**
  > "The following stage of development covered the period from the 1990s until well into the 2000s. **It would be wrong to view this solely as a crisis phase; rather it was a long phase of AI consolidation**, especially in Germany."
  He adds that in this stage "there were also few promises and expectations that were as far-reaching as before," and that topics shifted to "classic machine learning methods such as Bayesian statistics, and also a revitalisation of the connectionist AI concepts... i.e. neural networks" — i.e. **the field shifted rather than stopped**.
- **"Second AI winter" is used by some scholarly sources, with loose dating.** Klarmann, "Artificial Intelligence Narratives" (arXiv:2103.11961, 2021) — https://arxiv.org/abs/2103.11961 — writes: *"Most references differentiate in two major AI winters... The second AI winter (**around 1987**) is associated with the formation of a bubble that formed after first successes of expert systems were presented and hundreds of companies with extravagant promises emerged. The winter started after it was realized that the capabilities of these expert systems were limited."* Note "around 1987," not "1987–1993."

**COULD NOT VERIFY:** direct quotes or positions from Daniel Crevier, Pamela McCorduck (*Machines Who Think*, 2nd ed. 2004), Herbert Simon, or John McCarthy on the "second winter" — none of these texts were retrievable here. Also could not read Wikipedia's "AI winter" article (network-blocked), which is the likely source of the specific "1987–1993" periodization, so **the precise provenance of that date range is unverified.**

---

## Required fixes to claim #22 (if stated as fact)

1. Do not present "the second AI winter" as settled periodization. The standard history (Nilsson) uses `"AI Winter"` in scare quotes and dates it to the **mid-to-late 1980s**; the 1987–1993 range is a looser popular framing.
2. Replace "expert systems market collapse" with the documented mechanism: clients could build their own systems on cheap workstations/PCs, so many expert-systems firms "ceased to exist, were bought by larger companies, or had to reorient their businesses." **No market-size figure is verified.**
3. Symbolics: verified **Chapter 11, Feb 1993** — pair with 1987–88 evidence of market erosion for a *gradual* 1987–1993 collapse, not a single 1987 event.
4. FGCS: **FY1982–FY1992, ~¥54bn ≈ $380M, ICOT**, extended **2 years from FY1993** as a follow-on. The circulating "$850 million" is unsupported by ICOT's own final report.
5. DARPA: SCI 1983–1993, ~$1bn total, $50M in FY1984 — verified. The 1987 cut is real but is **Schwartz's Sept-1987 ISTO cancellations plus $47M→$31M (1987→1989) in basic AI + SCI research**; the "1987 DARPA review / three-year funding cuts" trigger is **unverified**.
6. Severity: say the second winter was **milder and/or differently shaped** — Nilsson: "the winter endured only for a season"; Hirsch-Kreinsen: viewing the 1990s "solely as a crisis phase" "would be wrong." Claiming it was as severe as 1974–1980 is not supported by the sources retrieved.

## URL list relied on

- https://ai.stanford.edu/~nilsson/QAI/qai.pdf — Nilsson, *The Quest for Artificial Intelligence* (Cambridge UP, 2010)
- https://doi.org/10.1007/s00146-023-01629-w — Hirsch-Kreinsen, *AI & Society* 39:1641–1652 (2024)
- https://eldorado.tu-dortmund.de/server/api/core/bitstreams/27544b5f-aacf-40e9-aed8-a43a48764160/content — open PDF of the above
- https://www.airc.aist.go.jp/aitec-icot/ICOT/Museum/FinalReport/node2.html — ICOT Final Evaluation Report (primary, Japanese)
- https://museum.ipsj.or.jp/en//computer/other/0002.html — IPSJ Computer Museum on FGCS
- https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/574 — Stone, *AI Magazine* 8(1), 1987 (PDF at /download/574/510)
- https://www.latimes.com/archives/la-xpm-1993-02-02-fi-1060-story.html — Symbolics Chapter 11, Feb 2, 1993
- https://www.nytimes.com/1988/08/24/business/company-news-xerox-spins-off-intelligence-unit.html — Xerox spin-off, Aug 24, 1988
- https://www.computerhistory.org/collections/catalog/102781127/ — CHM Expert Systems Pioneer Meeting transcript (2018)
- https://arxiv.org/abs/2103.11961 — Klarmann, "Artificial Intelligence Narratives" (2021)
- https://mlanthology.org/misc/1973/lighthill1973misc-artificial/ — Lighthill Report (1973) landing page
- https://ieeexplore.ieee.org/document/9707876 — *IEEE Annals* 2022, "The Expert Systems Business: How It Grew and Died" (NOT retrievable; cited as the outstanding authority)
