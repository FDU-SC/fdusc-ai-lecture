# Verified facts: Goodhart's Law and Zipf's Law

Compiled 2026-09-19 for a technical lecture on AI history.
Working dir: `/home/zecyel/slides/ch1`. All notes written under `research/scratch/cv-facts/notes/`.

**Method note.** Only `web_search` / `web_fetch` were used (bash has no network here). Primary
sources were preferred; where only secondary sources were reachable this is stated explicitly.
`web_fetch` cannot read PDFs (`unsupported content type "application/pdf"`), which blocked
several primary sources. Every failing fetch is logged in the FETCH FAILURES section.

---

# ITEM 1 — Goodhart's Law

## 1(a) The ORIGINAL formulation (monetary-policy context)

### The wording that is normally cited as "the original"

> "Any observed statistical regularity will tend to collapse once pressure is placed upon it for
> control purposes."

Locations found for this sentence:

1. **McIntyre, M. E.** (DAMTP, University of Cambridge), "GOODHART'S LAW", page dated
   *Copyright © Michael E. McIntyre 2000, last updated 17 October 2001*.
   URL: <http://www.damtp.cam.ac.uk/user/mem2//papers/LHCE/goodhart.html>
   (Note: only the **http://** `mem2//` URL worked; the https and non-`mem2` variants repeatedly
   failed — see FETCH FAILURES.) McIntyre writes:

   > "Professor Charles Goodhart FBA was Chief Adviser to the Bank of England. The Bank used to
   > have a web page about him at www.bankofengland.co.uk/cvs/goodhart.htm, giving his own
   > statement of the law, as published in his book *Monetary Theory and Practice*, page 96:
   > 'Any observed statistical regularity will tend to collapse once pressure is placed upon it
   > for control purposes.'"

   **This is important:** McIntyre (citing the Bank of England's own page) locates the sentence in
   **Goodhart's 1984 book *Monetary Theory and Practice*, p. 96** — i.e. in the **1984 reprint
   volume**, not necessarily in the 1975 conference paper.

2. **El-Mhamdi, E.-M. & Hoang, L.-N.**, "On Goodhart's law, with an application to value
   alignment", arXiv:2410.09638.
   URL: <https://arxiv.org/abs/2410.09638> (rendered: <https://ar5iv.labs.arxiv.org/html/2410.09638>)

   > "This quote by anthropologist Marilyn Strathern [Str97] is probably the most commonly known
   > rephrasing of Goodhart's law, which originally stated that 'any observed statistical
   > regularity will tend to collapse once pressure is placed upon it for control purposes'
   > [Goo75]."

   Here the bracket `[Goo75]` = Goodhart **1975**.

3. **Manheim, D. & Garrabrant, S.**, "Categorizing Variants of Goodhart's Law", arXiv:1803.04585.
   URL: <https://arxiv.org/abs/1803.04585> (rendered: <https://ar5iv.labs.arxiv.org/html/1803.04585>)
   Footnote 1:

   > "As a historical note, Goodhart's Law [1] as originally formulated states that 'any observed
   > statistical regularity will tend to collapse once pressure is placed upon it for control
   > purposes.'"

   Their reference [1]:
   > "Charles E. Goodhart *Problems of Monetary Management: The U.K. Experience* 1975. *Papers in
   > Monetary Economics*. Reserve Bank of Australia. I."

4. **Karwowski, J. et al.**, "Goodhart's Law in Reinforcement Learning", arXiv:2310.09144.
   URL: <https://arxiv.org/abs/2310.09144> (rendered: <https://ar5iv.labs.arxiv.org/html/2310.09144>)

   > "…an informal principle often stated as 'any observed statistical regularity will tend to
   > collapse once pressure is placed upon it for control purposes' (Goodhart 1984), or more
   > simply: 'when a measure becomes a target, it ceases to be a good measure'."

   and, in §1.1: "Goodhart's law was first introduced by [Goodhart 1984]."
   So this paper dates the original to **1984**, not 1975.

### "Papers in Monetary Economics, Volume I", RBA, 1975 — what the RBA itself says

The Reserve Bank of Australia's own retrospective bibliography (RDP 9013, Chiang & Power,
December 1990), "Conference Volumes" page, lists:

> "*Papers in Monetary Economics*. Vol. I and II. Sydney : Reserve Bank of Australia, **1976**.
> Revised version of seven papers presented at the Conference in Monetary Economics, Sydney,
> **July 1975**, and two additional papers.
> Vol. I papers: … Goodhart, C.A.E. *Problems of Monetary Management : The U.K. Experience*[36]"

and the footnote [36]:

> "This paper contains the first reference to what became known as 'Goodhart's Law'. For an
> account of the history of 'Goodhart's Law' see Paul Evans, 'Money, Output and Goodhart's Law :
> The U.S. Experience', *The Review of Economics and Statistics* Feb 1985, pp.1–8."

URL: <https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html>

**Verdict on 1975 vs. 1984 — what is verifiable and what is not:**

* The paper was **presented at a conference in Sydney in July 1975**; the **published volume is
  dated 1976 by the RBA's own bibliography**. Citations saying "1975" (conference year) and "1976"
  (publication year) both circulate. Manheim & Garrabrant give the page range as pp. 1–20 (their
  arXiv text) and the Wikipedia reference list gives "1975, p. 1-20" — but I could not inspect the
  RBA volume itself.
* The famous sentence is located **at page 96 of the 1984 book *Monetary Theory and Practice***
  by McIntyre, quoting the Bank of England. Several arXiv papers instead attribute the sentence
  to the 1975/1976 RBA paper.
* **I could NOT verify which is correct from a primary source.** The 1975/1976 RBA conference
  volume text and the 1984 Macmillan reprint text were both inaccessible (no PDF support, no
  library access). This is the single most important "could not verify" item in this file. The
  honest statement for a lecture is: *the sentence is universally quoted as Goodhart's, and is
  reliably documented as appearing at p. 96 of the 1984 reprint; whether it is literally in the
  1975/1976 conference version I could not confirm.*

### An alternative formulation recorded by the same provenance page

McIntyre also quotes *Pears Cyclopaedia*, 99th edition (1990–1, pp. G 27, G 31):

> "As soon as the government attempts to regulate any particular set of financial assets, these
> become unreliable as indicators of economic trends."

> "financial institutions can... easily devise new types of financial assets."

(URL as above.) Note the ellipsis is McIntyre's.

### A conflicting citation I could not check

A web_search result snippet from the European Central Bank's 2007 publication
*Monetary Policy: A Journey from Theory to Practice* reads: *"Thirty years ago, Charles Goodhart
(1981, page 116) formulated his famous law 'that any observed statistical regularity will ten…'"*
URL: <https://www.ecb.europa.eu/pub/pdf/other/monetarypolicyjourneytheorypractice2007en.pdf>
This PDF could not be fetched (unsupported content type), so the "1981, page 116" citation is
**unverified** and is recorded here only as a conflict to be aware of.

---

## 1(b) The popular form — who actually wrote it

### Full citation (verified)

**Strathern, Marilyn (1997). "‘Improving ratings’: audit in the British University system."**
*European Review*, **Vol. 5, No. 3, pp. 305–321**. Published **July 1997**. Publisher of record:
Cambridge University Press. ISSN 1062-7987 (print) / 1234-981X (electronic).

**DOI (verified via Crossref):**
`10.1002/(SICI)1234-981X(199707)5:3<305::AID-EURO184>3.0.CO;2-4`

* Crossref record (retrieved): <https://api.crossref.org/works/10.1002/(sici)1234-981x(199707)5:3%3C305::aid-euro184%3E3.0.co;2-4>
  Fields returned: `container-title: ["European Review"]`, `volume: 5`, `issue: 3`,
  `page: 305-321`, `published-print: 1997-07`, `publisher: Cambridge University Press (CUP)`,
  `prefix: 10.1017`, `author: Marilyn Strathern`, `ISSN: ["1062-7987","1234-981X"]`.
  Note the DOI prefix is **10.1002** (a Wiley-era SICI string) even though Crossref's publisher
  is CUP; the canonical resource Crossref gives is
  <https://www.cambridge.org/core/product/identifier/S1062798700002660/type/journal_article>.
* Cambridge Core landing page (abstract only; the fetched copy returned navigation chrome only):
  <https://www.cambridge.org/core/journals/european-review/article/abs/div-classtitleimproving-ratings-audit-in-the-british-university-systemdiv/FC2EE640C0C44E3DB87C29FB666E9AAB>
* So the lecturer's citation (**1997, European Review 5(3):305–321**) is **correct**. The DOI the
  lecturer should use is the 10.1002 SICI string above (there is no separate registered
  10.1017/S1062798700002660 DOI in Crossref; `S1062798700002660` is the Cambridge *product*
  identifier).

### The sentence as printed

> "When a measure becomes a target, it ceases to be a good measure."

Three independent secondary sources quote it with a page number:

1. **McIntyre (DAMTP, Cambridge)** — URL above:
   > "Professor Marilyn Strathern FBA, following Hoskin (1996, see below), has re-stated
   > Goodhart's Law more succinctly and more generally: 'When a measure becomes a target, it
   > ceases to be a good measure.'"
2. **FORRT glossary** ("Goodhart's Law") — URL: <https://forrt.org/glossary/english/goodhart_s_law/>
   > "In relation to examination performance, Strathern (1997) stated that 'when a measure becomes
   > a target, it ceases to be a good measure' (p. 308)."
   FORRT also gives the DOI (the same 10.1002 SICI string).
3. **Reagle, J.**, "Measure, manage, manipulate", 17 Dec 2014 —
   URL: <https://reagle.org/joseph/pelican/2014/measure-manage-manipulate.html>
   > "…in Marilyn Strathern's words, states 'When a measure becomes a target it ceases to be a good
   > measure' (Strathern, 1997: 308)."

**Punctuation caveat:** McIntyre and FORRT print a comma after "target"; Reagle omits it. Since the
printed article is paywalled and I could not read the page image, I **cannot certify the exact
punctuation of the printed sentence**. The page number (**308**) rests on FORRT and Reagle.

### Whom Strathern herself credits — NOT Goodhart directly

This is the key correction to the lecturer's belief. The evidence says Strathern took the phrasing
from **Keith Hoskin (1996)**, and that *Hoskin* is the one who attached it to Goodhart's law:

1. **McIntyre** (URL above):
   > "Professor Marilyn Strathern FBA, **following Hoskin (1996, see below)**, has re-stated
   > Goodhart's Law more succinctly and more generally: 'When a measure becomes a target, it
   > ceases to be a good measure.'"

   McIntyre's bibliography for Hoskin:
   > "Keith Hoskin (1996) (*The 'awful idea of accountability': inscribing people into the
   > measurement of objects*), in R. Munro and J. Mouritsen (eds.), *Accountability: Power, ethos
   > and the technologies of managing*, London, International Thomson Business Press, 265-282."

2. **Wikipedia** (via the Everything.Explained.Today mirror; the live Wikipedia was unreachable —
   see FETCH FAILURES) — URL: <https://everything.explained.today/Goodhart%27s_law/>
   > "Later writers generalized Goodhart's point about monetary policy into a more general adage
   > about measures and targets in accounting and evaluation systems. In a book chapter published
   > in 1996, Keith Hoskin wrote: […quote block not rendered by the mirror…] In a 1997 paper on the
   > misuse of accountability models in education, anthropologist Marilyn Strathern **cited Hoskins
   > expressing Goodhart's Law as** 'When a measure becomes a target, it ceases to be a good
   > measure', and linked the sentiment to the history of accountability stretching back into
   > Britain in the 1800s: […quote block not rendered…]"

3. **Majka, A. & El-Mhamdi, E.-M.**, "The Strong, Weak and Benign Goodhart's law",
   arXiv:2505.23445 — URL: <https://arxiv.org/abs/2505.23445> (rendered:
   <https://ar5iv.labs.arxiv.org/html/2505.23445>)
   > "From Charles Goodhart's remark in the context of monetary economics [5] to its reformulation
   > by **Keith Hoskin** [9] and its popularisation by **Marylin Strathern** [16], Goodhart's law
   > remained unformalised."

   (This paper's reference list was beyond the fetch truncation point, so the exact Hoskin [9]
   entry could not be read; the attribution sentence above is verbatim from the retrieved body.)

**IMPORTANT — what I could NOT verify:** I could **not** obtain the full text of Strathern (1997),
so I could **not** quote a verbatim sentence in which Strathern herself attributes the formulation
to Goodhart. The task asked to quote "that attribution … verbatim, if present". On the best
available evidence, her attribution runs through **Hoskin (1996)** rather than directly to
Goodhart, so the lecturer's premise ("Strathern … attributed the idea/formulation to Goodhart")
is **probably inaccurate as stated**. The primary text is needed to settle it. (The Hoskin chapter
PDF exists at <https://gwern.net/doc/statistics/decision/1996-hoskin.pdf> but PDFs cannot be
fetched here; the HTML variant 404s.)

### How the popular form differs from the original

* It is **not** a wording difference *from Strathern* — the popular form is, near enough, exactly
  the sentence quoted by McIntyre/FORRT/Reagle (modulo one comma).
* It **is** a difference *from Goodhart*. Goodhart's own sentence is
  "Any observed statistical regularity will tend to collapse once pressure is placed upon it for
  control purposes." The "measure / target" phrasing is a 1990s reformulation (Hoskin 1996,
  popularised by Strathern 1997) of the idea behind Goodhart's law — markedly shorter and stated
  for measures/targets in general rather than for monetary aggregates under control.

---

## 1(c) Is the popular form misattributed to Goodhart himself?

**Yes — the popular form is routinely presented as Goodhart's own words / as "Goodhart's law".**

* **Karwowski et al., arXiv:2310.09144** (URL above) states Goodhart's law "is an informal
  principle often stated as 'any observed statistical regularity …' (Goodhart 1984), **or more
  simply: 'when a measure becomes a target, it ceases to be a good measure'**" — the simpler
  sentence is folded into Goodhart's law with no mention of Strathern or Hoskin.
* The **Wikipedia article's own lead** (via the mirror above) makes the same collapse:
  > "Goodhart's law is an adage that has been stated as, 'When a measure becomes a target, it
  > ceases to be a good measure'. It is named after British economist Charles Goodhart…"
  with reference [1] pointing only at Goodhart (1975), *Papers in Monetary Economics*, RBA.
* Against this, **El-Mhamdi & Hoang (arXiv:2410.09638)** are explicit that the sentence belongs to
  Strathern — "'When a measure becomes a target, it ceases to be a good measure'. **This quote by
  anthropologist Marilyn Strathern [Str97]** …" — and **Majka & El-Mhamdi (arXiv:2505.23445)**
  call it Hoskin's reformulation, Strathern's popularisation.

No source was found that says in so many words "this is frequently misattributed to Goodhart",
but the misattribution pattern is directly evidenced by the sources above.

---

# ITEM 2 — Zipf's Law

## 2(a) Formulation and origin

**Formulation (verified, peer-reviewed secondary source):**

> "The *r*th most frequent word has a frequency *f*(*r*) that scales according to
> **f(r) ∝ 1/r^α** for **α ≈ 1** (Zipf, 1936, 1949)."

and Mandelbrot's generalisation:

> "f(r) ∝ 1/(r+β)^α for α ≈ 1 and β ≈ 2.7"

Source: **Piantadosi, S. T. (2014). "Zipf's word frequency law in natural language: A critical
review and future directions." *Psychonomic Bulletin & Review* 21(5):1112–1130.**
DOI: 10.3758/s13423-014-0585-6.
URL: <https://pmc.ncbi.nlm.nih.gov/articles/PMC4176592/>

Same source, on the qualitative shape (verbatim):

> "…there are few very high-frequency words that account for most of the tokens in text (e.g.,
> 'a,' 'the,' 'I,' etc.) and many low-frequency words (e.g., 'accordion,' 'catamaran,' 'ravioli')."

**Original books (bibliographic identity, not text-verified):**

* Zipf, G. K. (1935). *The Psycho-Biology of Language: An Introduction to Dynamic Philology*.
  Boston: Houghton Mifflin. — HathiTrust has a full-view text-only copy:
  <https://babel.hathitrust.org/cgi/ssd?id=mdp.39015008812839> (fetch failed; see FETCH FAILURES).
  **Caveat:** Piantadosi cites this book as **"Zipf, 1936"**, and the 1935/1936 dating varies in
  the literature (1935 Houghton Mifflin first edition; a 1936 London reprint also exists). Do not
  state a single year without noting this.
* Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort: An Introduction to Human
  Ecology*. Cambridge, MA: Addison-Wesley. — Internet Archive copy:
  <https://archive.org/details/humanbehaviorpri00zipf> (fetch failed).

**Could not verify:** I could **not** fetch either book's text, so I have **no verbatim sentence
from Zipf himself**. The formulation above is quoted from Piantadosi's review, which is a reliable
secondary source. For a slide, cite the books bibliographically and Piantadosi (or the PMC page)
for the equation.

## 2(b) Relevance to tokenizers / long-tail data — which paper actually says it?

**Verdict: the Zipf/long-tail connection is ABSENT from every part of the three named papers that
I could retrieve. I found no sentence in any of them citing Zipf's law or the long tail.**

| Paper | Zipf mentioned? | "long tail"? | Text retrieved |
|---|---|---|---|
| Sennrich, Haddow & Birch (2016), "Neural Machine Translation of Rare Words with Subword Units", arXiv:1508.07909 / ACL P16-1162 | **No** in retrieved text | **No** | Body through §4.2 (Table 2) only; truncated **before** §5 Analysis, §6, and references |
| Kudo (2018), "Subword Regularization", arXiv:1804.10959 | **No** in retrieved text | **No** | Body through §5.1 only; truncated before the rest of §5, §6, references |
| Kudo & Richardson (2018), "SentencePiece", arXiv:1808.06226 | **No** — retrieved text **includes the complete reference list** | **No** | Complete paper incl. references |

URLs used:
* <https://ar5iv.labs.arxiv.org/html/1508.07909> (also tried `…v5`, identical truncation point)
* <https://ar5iv.labs.arxiv.org/html/1804.10959> (also tried `…v3`)
* <https://ar5iv.labs.arxiv.org/html/1808.06226>

What these papers *do* say (verbatim, and this is the honest substitute for a Zipf quote):

* Sennrich et al. (2016), §1: "However, the translation of rare words is an open problem. The
  vocabulary of neural models is typically limited to 30 000–50 000 words, but translation is an
  open-vocabulary problem…" and "We show that open-vocabulary neural machine translation is
  possible by encoding (rare) words via subword units."
* Sennrich et al. (2016), §3.1: "A simple method to manipulate the trade-off between vocabulary
  size and text size is to use shortlists of unsegmented words, using subword units only for rare
  words."
* Kudo (2018), §1: "limiting vocabulary size increases the amount of unknown words, which makes the
  translation inaccurate especially in an open vocabulary setting."
* Kudo & Richardson (2018), §3.2: "Existing subword segmentation tools train subword models from
  pre-tokenized sentences."

**Claiming that Sennrich et al. (2016) or Kudo (2018) "cite Zipf's law" is NOT supported by the
text I could retrieve.** Two caveats, stated plainly: (i) for Sennrich 2016 and Kudo 2018 the fetch
was truncated before the closing sections/bibliography, so I cannot rule out a mention there; (ii)
`web_fetch` cannot read PDFs, so I could not use the ACL Anthology PDFs
(<https://aclanthology.org/P16-1162.pdf>) as a cross-check. Anyone repeating a "they cite Zipf"
claim should verify §5/§6/references directly.

**A citable source that DOES connect Zipf to tokenization:**

**He, Y., Zeng, Q. & Jiang, M. (2025). "Pre-trained Models Perform the Best When Token
Distributions Follow Zipf's Law." *Proceedings of EMNLP 2025*, pp. 28009–28021.**
DOI: 10.18653/v1/2025.emnlp-main.1421. URL: <https://aclanthology.org/2025.emnlp-main.1421/>
Abstract (verbatim):

> "In this work, we propose a principled method for determining the vocabulary size by analyzing
> token frequency distributions through Zipf's law. We show that downstream task performance
> correlates with how closely token distributions follow power-law behavior, and that aligning with
> Zipfian scaling improves both model efficiency and effectiveness. Extensive experiments across
> NLP, genomics, and chemistry demonstrate that models consistently achieve peak performance when
> the token distribution closely adheres to Zipf's law…"

**A weaker but genuine Zipf→NLP link (not tokenization):** El-Mhamdi & Hoang (arXiv:2410.09638,
URL above) argue that long-tail distributions "are argued to be ubiquitous, in natural language
processing [Zip49], scale-free networks [DMS00] and economics [BHS10]" — i.e. Zipf 1949 is cited
for heavy tails in NLP, but not for subword tokenization.

---

# COULD NOT VERIFY

1. **Whether the famous Goodhart sentence is literally in the 1975/1976 RBA conference paper.**
   McIntyre (quoting the Bank of England) ties it to *Monetary Theory and Practice* **p. 96**
   (the 1984 reprint); several arXiv papers tie it to the 1975 paper. Neither primary text was
   accessible. **The 1975-vs-1984 question therefore remains open.**
2. **The exact page and punctuation of Strathern's sentence in print.** Secondary sources say
   p. 308; comma placement differs between them. Full text paywalled.
3. **Strathern's own verbatim attribution sentence.** Could not be read. Best evidence: she cites
   **Hoskin (1996)**, not Goodhart directly.
4. **The verbatim sentence in Hoskin (1996).** PDF at <https://gwern.net/doc/statistics/decision/1996-hoskin.pdf>
   is unreadable by the fetch tool; HTML variant returns 404.
5. **Any verbatim text from Zipf (1935) or Zipf (1949).** HathiTrust / Internet Archive copies
   could not be fetched.
6. **Whether Sennrich et al. (2016) §5/§6/references or Kudo (2018) §5.2/§6/references mention
   Zipf.** Fetch truncation; PDFs unreadable.
7. **The ECB's "Goodhart (1981, page 116)" citation.** PDF unreadable.
8. **The Goodhart 1975 paper's page range / exact title punctuation.** Sources give pp. 1–20
   (Wikipedia ref list, Manheim & Garrabrant) and cite the title variously as
   "Problems of Monetary Management: The U.K. Experience" and "…The UK Experience".
9. **Exact author order / reference entries [9] and [16] in arXiv:2505.23445** (Hoskin and
   Strathern) — reference list was past the truncation point.

---

# FETCH FAILURES (recorded, with retry counts where >1)

**Blocked by DNS "non-public IP" (Wikipedia domains):**
* <https://en.wikipedia.org/wiki/Goodhart%27s_law> — ≥3 attempts
* <https://en.m.wikipedia.org/wiki/Goodhart%27s_law>
* <https://en.wikipedia.org/w/index.php?title=Goodhart%27s_law&action=raw>
* <https://en.wikipedia.org/api/rest_v1/page/html/Goodhart%27s_law>
* <https://pt.wikipedia.org/wiki/Lei_de_Goodhart>

**archive.org / Wayback (all "fetch failed", ≥2 attempts each):**
* <https://web.archive.org/web/20241006203510/http://www.damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html>
* <https://web.archive.org/web/20241006203510if_/http://www.damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html>
* <https://web.archive.org/web/20220816173929/https://en.wikipedia.org/wiki/Goodhart%27s_law> — ≥4 attempts
* <https://web.archive.org/web/20220816173929id_/https://en.wikipedia.org/wiki/Goodhart%27s_law>
* <https://web.archive.org/web/2023/https://en.wikipedia.org/wiki/Goodhart's_law>
* <https://web.archive.org/web/2024/http://www.damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html>
* <http://web.archive.org/web/20220816173929/https://en.wikipedia.org/wiki/Goodhart%27s_law>
* <https://web.archive.org/cdx/search/cdx?url=damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html&output=json>
* <http://archive.org/wayback/available?url=damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html>
* <https://archive.org/details/humanbehaviorpri00zipf>

**DAMTP Cambridge (only the `http://…mem2//…` form eventually succeeded):**
* <https://www.damtp.cam.ac.uk/user/mem2//papers/LHCE/goodhart.html> — many failures, then **success over http**
* <https://www.damtp.cam.ac.uk/user/mem2/papers/LHCE/goodhart.html>
* <https://www.damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html>
* <https://damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html>
* <http://www.damtp.cam.ac.uk/user/mem/papers/LHCE/goodhart.html>

**PDF — "unsupported content type application/pdf":**
* <https://www.ecb.europa.eu/pub/pdf/other/monetarypolicyjourneytheorypractice2007en.pdf>
* <https://lnu.edu.ua/wp-content/uploads/2017/06/dis_kostiuchenko.pdf>
* <https://gwern.net/doc/statistics/decision/1996-hoskin.pdf> (listed by search; not fetchable)

**HTTP errors / blocked:**
* <https://www.scilit.com/publications/4230e592501f72cf5495dd9ab4e2c040> — 403
* <https://www.cambridge.org/core/journals/european-review/article/abs/…/FC2EE640C0C44E3DB87C29FB666E9AAB> — 200 but content truncated to nav chrome (no abstract)
* <https://www.semanticscholar.org/paper/…5a984f47f4a20af09b6b1cdd42f47fe32cff97d8> — 202, empty body
* <https://www.academia.edu/76823011/Goodharts_Law_its_origins_meaning_and_implications_for_monetary_policy> — 403
* <https://www.nature.com/nature-index/news/measure-for-measure> — cross-origin redirect to idp.nature.com
* <https://committees.parliament.uk/writtenevidence/153851/html/> — 403 (Cloudflare interstitial)
* <https://www.tandfonline.com/doi/full/10.1080/02560046.2019.1690534> — 403 (Cloudflare interstitial)
* <https://wiki-gateway.eudic.net/wikipedia_en/Goodhart's_law.html> — 403
* <https://kids.kiddle.co/Goodhart%27s_law> — 404
* <https://gwern.net/doc/statistics/decision/1996-hoskin> — 404
* <https://brs.website.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html> — ENOTFOUND (the `www.rba.gov.au` variant worked)

**Wikipedia mirrors that failed ("fetch failed"):**
* <https://www.wikiwand.com/en/articles/Goodhart%27s_law> (and `/en/Goodhart%27s_law`)
* <https://infogalactic.com/info/Goodhart%27s_law>
* <https://alchetron.com/Goodhart%27s-law>
* <https://www.thefullwiki.org/Goodhart%27s_law>
* <https://wikipedia.moesalih.com/Goodhart%27s_law> — ENOTFOUND

**Text-extraction / CORS proxies (all failed; used to try to read the McIntyre page and PDFs):**
* <https://r.jina.ai/https://arxiv.org/pdf/1508.07909>
* <https://r.jina.ai/https://arxiv.org/pdf/1804.10959>
* <https://r.jina.ai/http://cyberlibris.typepad.com/blog/files/Goodharts_Law.pdf>
* <https://r.jina.ai/https://example.com>
* <https://api.allorigins.win/raw?url=…> — 500 / 520
* <https://api.codetabs.com/v1/proxy?quest=…> — 522 (twice)

**Google Books API (repeated "fetch failed"):**
* <https://www.googleapis.com/books/v1/volumes?q=%22when+a+measure+becomes+a+target%22>
* <https://www.googleapis.com/books/v1/volumes?q=%22it+ceases+to+be+a+good+measure%22>
* <https://www.googleapis.com/books/v1/volumes?q=%22Improving+ratings%22+Strathern>

**Other:**
* <https://api.wikimedia.org/core/v1/wikipedia/en/page/Goodhart%27s_law> and `…/html` — "fetch failed"
* <https://babel.hathitrust.org/cgi/ssd?id=mdp.39015008812839;page=ssd;view=plaintext;seq=294;num=262>
* <https://www.arxiv-vanity.com/papers/1508.07909/> and `…/1804.10959/` — cross-origin redirect to ar5iv

---

# SOURCE LIST (everything actually used)

1. McIntyre, M. E., "GOODHART'S LAW", DAMTP, University of Cambridge, 2000/2001 —
   <http://www.damtp.cam.ac.uk/user/mem2//papers/LHCE/goodhart.html>
2. Reserve Bank of Australia, RDP 9013 (Chiang & Power, Dec 1990), "Conference Volumes" —
   <https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html>
3. El-Mhamdi & Hoang, arXiv:2410.09638 — <https://arxiv.org/abs/2410.09638>
4. Manheim & Garrabrant, arXiv:1803.04585 — <https://arxiv.org/abs/1803.04585>
5. Karwowski et al., arXiv:2310.09144 — <https://arxiv.org/abs/2310.09144>
6. Majka & El-Mhamdi, arXiv:2505.23445 — <https://arxiv.org/abs/2505.23445>
7. Crossref record for Strathern 1997 —
   <https://api.crossref.org/works/10.1002/(sici)1234-981x(199707)5:3%3C305::aid-euro184%3E3.0.co;2-4>
8. FORRT glossary, "Goodhart's Law" — <https://forrt.org/glossary/english/goodhart_s_law/>
9. Reagle, J., "Measure, manage, manipulate" — <https://reagle.org/joseph/pelican/2014/measure-manage-manipulate.html>
10. Everything.Explained.Today mirror of Wikipedia "Goodhart's law" —
    <https://everything.explained.today/Goodhart%27s_law/>
11. Piantadosi (2014), *Psychon. Bull. Rev.* 21(5):1112–1130 —
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC4176592/>
12. Sennrich, Haddow & Birch, arXiv:1508.07909 — <https://ar5iv.labs.arxiv.org/html/1508.07909>
13. Kudo, arXiv:1804.10959 — <https://ar5iv.labs.arxiv.org/html/1804.10959>
14. Kudo & Richardson, arXiv:1808.06226 — <https://ar5iv.labs.arxiv.org/html/1808.06226>
15. He, Zeng & Jiang, EMNLP 2025 — <https://aclanthology.org/2025.emnlp-main.1421/>
