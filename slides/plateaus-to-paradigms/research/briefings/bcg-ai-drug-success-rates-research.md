# BCG / AI-discovered drug clinical success rates — sourced research note

Research date: 2026-09-16. Scope: BCG analysis of AI-discovered drug Phase I/II success rates, exact numbers, and published critiques.

## 1. The "BCG analysis" is a journal paper, not a bcg.com report

**Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C.** "How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons." *Drug Discovery Today* 2024 Jun;29(6):104009. Epub 2024 Apr 30. doi:10.1016/j.drudis.2024.104009. PMID 38692505.

- PubMed record (retrieved OK): https://pubmed.ncbi.nlm.nih.gov/38692505/
- DOI: https://doi.org/10.1016/j.drudis.2024.104009
- Open-access copy (retrieved OK): https://zenodo.org/records/13137004

**Author affiliations confirm BCG authorship** (from the PubMed record): all five authors are affiliated with Boston Consulting Group (London / Amsterdam / Summit NJ); corresponding author e-mail `meier.chris@bcg.com`. Article type: Review. Open access (CC BY-NC-ND).

## 2. Exact numbers (verbatim from the abstract, retrieved from PubMed)

- **Phase I: 80–90% success rate** — "substantially higher than historic industry averages."
- **Phase II: ~40%** — "albeit on a limited sample size, comparable to historic industry averages."
- Claimed interpretation: "AI is highly capable of designing or identifying molecules with drug-like properties."

**Sample size** (retrieved from https://www.quantumbiospace.ai/news/how-successful-are-ai-discovered-drugs-in-clinical-trials/):
- 300 AI-native biotechs active worldwide
- **67 drugs in clinical development** (vs 6,147 drugs in clinical development overall ⇒ ~1%)
- **24 AI-discovered targets**, of which only **3 to 9** were AI-discovered *novel* targets (0.05–0.1% of all clinical-stage drugs)
- Authors' projection: overall probability of a molecule advancing through all clinical phases rises from **5–10% to ~9–18%** ("near doubling of R&D productivity")

## 3. Critiques

### 3a. OPINION-CRITIQUE — Optibrium blog, Matt Segall (CEO), "Is AI improving drug discovery?"
URL (retrieved OK): https://optibrium.com/knowledge-base/blog-is-ai-improving-drug-discovery-how/

Key points:
- States the industry standard as **40–60%** for Phase I (vs BCG's 80–90%).
- "**Only ten candidates from these companies have reported results from Phase II trials. Four were successful**" ⇒ 40%, matching the industry norm.
- Warns the evidence base is small; "the number of candidates is small so far."
- Notes AI-native biotechs "benefitted from an unusually high number of computational experts supporting these projects. **This doesn't scale** across the broader pharma and biotech industries."
- Notes contemporaneous layoffs/restructuring among AI-native biotechs.

### 3b. OPINION-CRITIQUE — Derek Lowe, "In the Pipeline" blog, "AI Drugs So Far"
URL as quoted verbatim inside the Optibrium page: https://www.science.org/content/blog-post/ai-drugs-so-far

**NOT RETRIEVED** by me (science.org returns HTTP 403 / Cloudflare). Per Optibrium's quotation, Lowe noted that **of the 24 targets in the paper claimed to be "AI discovered," 23 had precedence in the literature for the therapeutic indication they were targeting.** This is the strongest published "not genuinely AI-discovered" critique I could source, but only second-hand.

### 3c. OPINION-CRITIQUE — attribution / survivorship-bias blog post
"How much of 'AI-discovered drugs succeed more' is evidence and how much is narrative: attribution, sample size and the survivorship trap" (2026-07-16)
URL: https://uthandonethemba.com/2026/07/16/ai-drug-part4-attribution-success-rate/
Title verified via search + HTTP 200 fetch, but the body is JS-rendered and returned no readable text. Content UNVERIFIED beyond the title.

### 3d. The paper's own caveat
The abstract itself concedes the Phase II result rests on "a limited sample size."

## 4. Follow-up / re-analysis (SECONDARY SOURCE — primary UNVERIFIED)

ic.work, "AI制药的成绩单:早期漂亮,Phase II原地踏步" (2026-08-16)
URL (retrieved OK): https://www.ic.work/article/ai-drug-discovery-phase-2-evidence-gap

Reports:
- A **2025 update** to the analysis: **9 newly completed Phase II programs, 3 succeeded, 6 failed or terminated ⇒ ~33% success**. Compared against BIO's 2011–2020 industry Phase II→Phase III transition rate of **28.9%** (from ~5,000 transitions): https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf
- A *Nature Reviews Drug Discovery* review by **Bender et al., 7 Aug 2026**, "Artificial intelligence in drug discovery — what it is, where we stand and the path forward": https://www.nature.com/articles/s41573-026-01496-2 — concludes evidence for clinically relevant impact is "disappointingly limited" (evidence *absent*, not evidence *of absence*).
- Notes methodological defects: single-digit sample, **no contemporaneous control arm**, and inconsistent company definitions of what counts as "AI-involved"; plus selection effect (only already-filtered molecules reach Phase II).
- Named clinical outcomes often lumped together as "AI drug failures": BenevolentAI **BEN-2293** (atopic dermatitis; missed primary efficacy endpoint — a genuine failure), Recursion **REC-994** (met primary safety endpoint, efficacy unclear), Exscientia **EXS21546** (terminated on portfolio review, not an efficacy failure).

Corroborating summary (retrieved OK): GIGAZINE English, 2026-09-08, "To what extent has AI-driven drug discovery actually progressed?" https://gigazine.net/gsc_news/en/20260908-ai-drug-discovery-reality — summarizes the same Bender et al. review: as of 2024 most AI-drug-company compounds were preclinical; only dozens in Phase I/II; very few in Phase III; "limited evidence" that AI delivers safe and effective drugs faster.

**IMPORTANT CAVEAT:** the 33% / 3-of-9 Phase II figure is reported only by ic.work. The Nature Biotechnology URL ic.work cites for it (https://www.nature.com/articles/s41587-025-02901-8) resolves in search to an **unrelated** article, "Drugmakers share data to feed voracious foundation models." So the primary source of the 2025 update numbers is **UNVERIFIED and appears mis-attributed**.

## 5. What I could NOT verify

- **No standalone bcg.com 2024 or 2025 publication** carrying these success-rate numbers could be found. bcg.com is reachable (a guessed URL returned a clean 404), but no matching article surfaced in any search.
- The **Wellcome Trust + Boston Consulting Group** report *"Unlocking the potential of AI in drug discovery"* (published 26 Jun 2023), cited as reference 11 of the Jayatunga paper: https://wellcome.org/reports/unlocking-potential-ai-drug-discovery — fetch returned **HTTP 202 with no content**. Not verified.
- **Derek Lowe's post** (science.org, HTTP 403) — content known only via Optibrium's quotation.
- **Bender et al. NRDD review** (nature.com redirects to idp.nature.com) — content known only via ic.work and GIGAZINE summaries.
- The Jayatunga paper's own **Phase I sample size** (how many molecules underpinned the 80–90%) was not obtainable: the Zenodo PDF preview returns no extractable text, and ScienceDirect returned HTTP 403.
- The paper's reference 14 is a relevant editorial I could not retrieve: "AI's potential to accelerate drug discovery needs a reality check," *Nature* 2023;622:217, doi:10.1038/d41586-023-03172-6.

## 6. Retrieval status of hosts

- Worked: pubmed.ncbi.nlm.nih.gov, zenodo.org (record page), optibrium.com, ic.work, gigazine.net, quantumbiospace.ai, ouci.dntb.gov.ua, cen.acs.org (truncated)
- Blocked: nature.com (redirect to idp.nature.com), science.org (403), sciencedirect.com (403), cell.com (403), biorxiv.org (429 Cloudflare), wellcome.org (202 empty)
