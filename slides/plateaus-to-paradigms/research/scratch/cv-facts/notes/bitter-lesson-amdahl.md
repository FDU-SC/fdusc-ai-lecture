# Verified facts: "The Bitter Lesson" (Sutton) and Amdahl's law

Compiled: 2026-09-19 (workspace date). Tools used: `web_search`, `web_fetch` only (no shell network).
Every quote below is copied from a page I actually fetched; the fetching URL is named next to it.

---

# ITEM 1 — "The Bitter Lesson", Rich Sutton

## 1(a) Publication date and original venue

| Fact | Value | Source actually fetched |
|---|---|---|
| Title | "The Bitter Lesson" | <http://www.incompleteideas.net/IncIdeas/BitterLesson.html> (HTTP 200) |
| Author as printed | "Rich Sutton" | same page |
| Date as printed on the page | **March 13, 2019** (heading rendered as `### March 13, 2019`) | same page |
| Canonical URL | **<http://www.incompleteideas.net/IncIdeas/BitterLesson.html>** | HTTP 200 |

Both of these returned the identical page text and the identical "March 13, 2019" dateline:

* <http://www.incompleteideas.net/IncIdeas/BitterLesson.html> — HTTP 200 ✅
* <http://incompleteideas.net/IncIdeas/BitterLesson.html> — HTTP 200 ✅

**sutton.cs.ualberta.ca: COULD NOT VERIFY.** `sutton.cs.ualberta.ca` does **not resolve**
(`getaddrinfo ENOTFOUND`, 2 attempts, both http:// and https://). I could not retrieve any
primary page or archive capture naming it as the original host, because every archive/mirror
endpoint I tried was unreachable from this environment (see FETCH FAILURES). I therefore
**cannot confirm** that `sutton.cs.ualberta.ca/IncIdeas/BitterLesson.html` was ever the
original location, and I cannot confirm it is a valid URL today. The only host I verified
serving the essay is `incompleteideas.net`.

**HTTPS caveat:** `https://www.incompleteideas.net/...` and `https://incompleteideas.net/...`
both failed to fetch (3 attempts). Only the **http://** form worked. Do not print an https://
canonical link without re-checking from a different network.

## 1(b) Verbatim quotes (from the fetched page)

**(i) Opening thesis sentence** (the very first sentence of the essay):

> "The biggest lesson that can be read from 70 years of AI research is that general methods
> that leverage computation are ultimately the most effective, and by a large margin."

**(ii) Closing sentence** (the last sentence on the page):

> "Building in our discoveries only makes it harder to see how the discovering process can be
> done."

**(iii) The "opposing approach" line** — this is item 4) of the numbered list, in one long
sentence:

> "The bitter lesson is based on the historical observations that 1) AI researchers have often
> tried to build knowledge into their agents, 2) this always helps in the short term, and is
> personally satisfying to the researcher, but 3) in the long run it plateaus and even inhibits
> further progress, and 4) breakthrough progress eventually arrives by an opposing approach
> based on scaling computation by search and learning."

**(iv) The "general methods / general purpose methods" formulation** (there are two; both are
often conflated, so give both):

Opening (same sentence as (i)):
> "The biggest lesson that can be read from 70 years of AI research is that general methods
> that leverage computation are ultimately the most effective, and by a large margin."

Later section:
> "One thing that should be learned from the bitter lesson is the great power of general
> purpose methods, of methods that continue to scale with increased computation even as the
> available computation becomes very great. The two methods that seem to scale arbitrarily in
> this way are search and learning."

**(v) Related line worth having for a lecture** (the "only thing that matters" formulation):

> "Seeking an improvement that makes a difference in the shorter term, researchers seek to
> leverage their human knowledge of the domain, but the only thing that matters in the long run
> is the leveraging of computation."

**(vi) Typographic quirk on the original page (use with care).** As rendered by the fetch tool,
the chess paragraph reads:

> "They said that ``brute force" search may have won this time, but it was not a general
> strategy, and anyway it was not how people played chess."

i.e. the source appears to contain **two literal backticks** (``) rather than a curly opening
quote, a LaTeX-ism. I am flagging this as *observed through the text-decoding fetch*, not as a
byte-level inspection of the HTML — verify before putting it on a slide verbatim.

## 1(c) Misquotes / paraphrase drift to watch for

The task asked me to note commonly misquoted versions *if I happened to see them*. What I
actually observed while fetching:

1. **A re-typeset copy silently rewrites the numbered list into prose.** The GitHub copy at
   <https://raw.githubusercontent.com/jonathangittins/pm-ai-toolkit/refs/heads/main/frameworks/bitter-lesson.md>
   (HTTP 200; secondary source, not primary) lists under "Key Quotes":
   > "The bitter lesson is based on the historical observations that AI researchers have often
   > tried to build knowledge into their agents. This always helps in the short term, and is
   > personally satisfying to the researcher, but in the long run it plateaus and even inhibits
   > further progress."

   This is **not** the original wording: the original keeps the "1) … 2) … 3) … 4) …" list and
   omits the word "that" before "this" (original: "…into their agents, 2) this always helps…").
   It also silently drops clause 4) (the "opposing approach" clause). Good example of a
   plausible-looking quote that is not verbatim. That same copy does, however, carry the correct
   date ("March 13, 2019") and names `http://www.incompleteideas.net/IncIdeas/BitterLesson.html`
   as its source.

2. **General cautions (patterns to check in your own deck, not claims about a specific source):**
   - Quoting only "…general methods that leverage computation are ultimately the most effective"
     and **dropping ", and by a large margin."** The trailing clause is part of the sentence.
   - Using the later "general purpose methods" sentence as if it were the opening thesis
     sentence — they are two different sentences (see 1(b)(iv)).
   - Rendering the essay's dashes as em-dashes/en-dashes. On the page they decode as `---`
     (another LaTeX-ism), e.g. "knowledge of words, of phonemes, of the human vocal tract, etc."
     is preceded by `---`.
   - Citing the date as just "2019" or "April 2019". The page's own dateline is **March 13, 2019**.

I did **not** find (and therefore do not assert) any documented catalogue of misquotations of
this essay. No such source was retrievable.

---

# ITEM 2 — Amdahl's law

## 2(a) The formulation

Standard closed form, in the notation used by the request:

```
S = 1 / ((1 - p) + p/s)
```

Symbol definitions (verbatim from the source's definition list, then the mapping):

| Symbol | Meaning | Source |
|---|---|---|
| `S` (Speedup) | "Maximum theoretical performance improvement" | <https://www.tutorialspoint.com/article/what-is-amdahl-s-law> (HTTP 200) |
| `p` | "Fraction of the system that can be improved (0 ≤ p ≤ 1)" — i.e. the parallelizable/improved fraction | same |
| `s` | "Speedup factor applied to the improvable portion" — i.e. the speedup of the improved part (for parallel hardware, the number of processors/cores N) | same |
| `(1 - p)` | "Fraction that remains unimproved (the bottleneck)" — the serial fraction | same |

**Limiting form.** As `s → ∞` (unbounded parallel resources), the `p/s` term vanishes and

```
lim (s→∞) S = 1 / (1 - p)
```

so the serial fraction alone caps the achievable speedup. A second, independent reference
states the same limit in the equivalent per-part notation: with serial time `F_s` and parallel
time `F_p`, `S = 1 / (F_s + F_p/N)` and `lim(N→∞) S = 1 / F_s`, i.e. "As the number of cores
increases, the serial portion dominates the execution time" —
see Cornell Virtual Workshop, *Amdahl's Law*,
<https://cvw.cac.cornell.edu/parallel/efficiency/amdahls-law> (HTTP 200, fetched on the 3rd
attempt after two EAI_AGAIN DNS failures). Mapping: `p ≡ F_p`, `(1-p) ≡ F_s`, `s ≡ N`.

*Reference quality note:* the closed form above is quoted from a general-audience technical
article (tutorialspoint), because ACM/IEEE/Wikipedia/ScienceDirect all blocked this fetcher
(403) and Wikipedia resolved to a non-public IP. The Cornell Center for Advanced Computing
page is the stronger citation for the physics and the limit; **use Cornell as the citation of
record and the closed form as the textbook identity it is.** I could not read the 1967 paper's
body (see 2(c)), so **I cannot state from evidence whether the 1967 paper itself prints this
closed form**; do not claim either way on a slide.

## 2(b) The 1967 citation — VERIFIED

Your proposed citation is **correct**, with one wording precision noted below.

| Field | Verified value | Source |
|---|---|---|
| Author | **Gene M. Amdahl** | Crossref `author.given = "Gene M."`, `family = "Amdahl"`: <https://api.crossref.org/works/10.1145/1465482.1465560> (HTTP 200) |
| Title | **"Validity of the single processor approach to achieving large scale computing capabilities"** | Crossref + Semantic Scholar + Mendeley (all fetched) |
| Venue (Crossref `container-title`) | "Proceedings of the April 18-20, 1967, spring joint computer conference on - AFIPS '67 (Spring)" | Crossref |
| Event | "the April 18-20, 1967, spring joint computer conference", **Atlantic City, New Jersey**, acronym **AFIPS '67 (Spring)**, conference number 30, sponsor AFIPS | Crossref `event` object |
| Year | **1967** | Crossref `issued` = 1967; Semantic Scholar `year` = 1967 |
| Pages | **483–485** | Mendeley: "AFIPS Conference Proceedings - 1967 Spring Joint Computer Conference, AFIPS 1967 (1967) **483-485**" — <https://www.mendeley.com/catalogue/c768709b-5f5e-3d6d-9917-9f4adddb2a6e/> (HTTP 200); Semantic Scholar also returns `"pages": "483-485"` |
| DOI | **10.1145/1465482.1465560** ✅ (your guess is correct) | Crossref (HTTP 200), Semantic Scholar (`externalIds.DOI`), Mendeley |
| URL | <https://doi.org/10.1145/1465482.1465560> | DOI resolves; note the ACM DL landing page returns **HTTP 403** to this fetcher |

Machine-readable corroboration actually fetched:

* Crossref: <https://api.crossref.org/works/10.1145/1465482.1465560> (HTTP 200) —
  `"title": ["Validity of the single processor approach to achieving large scale computing capabilities"]`,
  `"author": [{"given":"Gene M.","family":"Amdahl"}]`, `"DOI":"10.1145/1465482.1465560"`,
  `"type":"proceedings-article"`, `"published-print":{"date-parts":[[1967]]}`, `"page":"483"`,
  `"is-referenced-by-count":2039`.
* Semantic Scholar: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/1465482.1465560?fields=...`
  (HTTP 200) — `"venue":"AFIPS '67 (Spring)"`, `"year":1967`, `"journal":{"pages":"483-485"}`,
  `"openAccessPdf":{"status":"CLOSED"}`.

**Precision note on the venue wording** you supplied — "AFIPS Spring Joint Computer Conference,
1967, published in AFIPS '67 (Spring) Proceedings, pages 483-485" — is accurate but the
proceedings' formal container title (per Crossref) is *"Proceedings of the April 18-20, 1967,
spring joint computer conference on - AFIPS '67 (Spring)"*. Also note Crossref records only the
first page (`"page":"483"`); the **483–485** range comes from Mendeley/Semantic Scholar.
A search-result snippet (from `sciprofiles.com`, **which returned HTTP 403 when fetched, so this
is UNVERIFIED**) additionally gave "AFIPS Conference Proceedings, Vol. 30 (Atlantic City, N.J.,
Apr. 18–20), AFIPS Press, Reston, Va., 1967, pp. 483–485". **I could not independently confirm
"Vol. 30" or "AFIPS Press, Reston, Va."** — treat as unverified.

## 2(c) Verbatim sentence from the paper

**I could not access the body of the paper.** It is paywalled and closed access
(Semantic Scholar reports `openAccessPdf.status = "CLOSED"` and notes the publisher elided the
abstract). Every route to the full text failed — see FETCH FAILURES. **I have not invented any
quote from the body, and you should not use any "quote" from the paper's body that is not
traced to the PDF itself.**

What I *can* give verbatim is the paper's **abstract**, as reproduced by Mendeley (Scopus-sourced
metadata) at <https://www.mendeley.com/catalogue/c768709b-5f5e-3d6d-9917-9f4adddb2a6e/>
(HTTP 200). Labelled clearly because it is a **secondary reproduction of the primary abstract**,
not the PDF itself:

> "For over a decade prophets have voiced the contention that the organization of a single
> computer has reached its limits and that truly significant advances can be made only by
> interconnection of a multiplicity of computers in such a manner as to permit cooperative
> solution. Variously the proper direction has been pointed out as general purpose computers
> with a generalized interconnection of memories, or as specialized computers with geometrically
> related memory interconnections and controlled by one or more instruction streams."

**Provenance discrepancy worth knowing:** the QuoteKG quote database
(<https://quotekg.l3s.uni-hannover.de/resource/Mention897346>, HTTP 200, sourced to
`en.wikiquote.org/wiki/Gene_Amdahl`) carries the *same two sentences* but appends a third:
"Demonstration is made of the continued validity of the single processor approach and of the
weaknesses of the multiple processor approach in terms of application to real problems and
their attendant irregularities." Mendeley/Scopus's abstract **stops after two sentences**, so I
**cannot verify** whether that third sentence is the paper's, another part of the front matter,
or an editorial addition. Do not quote it as the abstract without checking the PDF.

## 2(d) Amdahl's law vs. Gustafson's law

In one or two sentences: **Amdahl's law assumes a fixed problem size** and asks how much faster
that same job runs as processors are added — the classic **strong scaling** view, whose speedup
is bounded by `1/(1-p)`. **Gustafson's law assumes a fixed run time** and asks how much *more*
work can be done as processors are added — **weak scaling / scaled speedup** — giving a speedup
that grows linearly with the number of processors `N`, `S = F_s + N·F_p = N + (1-N)·F_s`.
The unparallelizable portion limits both, but "it is more detrimental when the problem size
cannot scale with the number of cores." — Cornell Virtual Workshop, *Amdahl's Law*,
<https://cvw.cac.cornell.edu/parallel/efficiency/amdahls-law> (HTTP 200); strong vs. weak
scaling definitions also at <https://cvw.cac.cornell.edu/parallel/efficiency/scaling> (HTTP 200).

Gustafson 1988 citation, verified from Crossref
(<https://api.crossref.org/works/10.1145/42411.42415>, HTTP 200):

* **John L. Gustafson**, "**Reevaluating Amdahl's law**", *Communications of the ACM*,
  **vol. 31, no. 5, pp. 532–533, May 1988**, DOI **10.1145/42411.42415**,
  URL <https://doi.org/10.1145/42411.42415>. Affiliation recorded: Sandia National Laboratory,
  Albuquerque, NM. (Note the title is capitalised "Reevaluating Amdahl's law" in Crossref.)

---

# COULD NOT VERIFY

1. **That `sutton.cs.ualberta.ca` was ever the original host of "The Bitter Lesson".** The
   hostname does not resolve today (ENOTFOUND) and I could not reach any archive to check
   historical captures. I verified only `incompleteideas.net`.
2. **The essay's https:// URL.** Only `http://` fetched successfully (both with and without
   `www`). Three attempts on the https forms failed.
3. **The body text of Amdahl (1967).** Paywalled/closed; no quote from the body is provided.
   Only the abstract is quoted, and only via a secondary reproduction (Mendeley/Scopus).
4. **Whether the 1967 paper prints the closed form `S = 1/((1-p)+p/s)`.** I could not read it.
5. **The third sentence** sometimes attached to the Amdahl abstract ("Demonstration is made of
   the continued validity…"). Present in QuoteKG/Wikiquote, absent from Mendeley/Scopus.
6. **"AFIPS Conference Proceedings, Vol. 30" / "AFIPS Press, Reston, Va."** — seen only in a
   search-result snippet from a page that returned HTTP 403. Unverified.
7. **Any catalogue of documented misquotations of "The Bitter Lesson".** None found/retrievable.
8. **A primary or textbook-quality page for the closed-form formula** in the exact `p`/`s`
   notation. ACM, IEEE-adjacent, ScienceDirect, Wikipedia, O'Reilly and GlobalSpec all blocked
   this fetcher. Cornell (formula + limit, different symbol names) and tutorialspoint (exact
   `p`/`s` form) are what I could actually read.

# FETCH FAILURES

Recorded per the task instruction. "attempts" = number of times that exact URL was retried.

**Network / DNS level**
| URL | Result | Attempts |
|---|---|---|
| `http://sutton.cs.ualberta.ca/IncIdeas/BitterLesson.html` | `getaddrinfo ENOTFOUND` | 2 |
| `https://sutton.cs.ualberta.ca/IncIdeas/BitterLesson.html` | `getaddrinfo ENOTFOUND` | 1 |
| `https://cvw.cac.cornell.edu/parallel/efficiency/amdahls-law` | `getaddrinfo EAI_AGAIN` | 2 (succeeded on 3rd) |
| `https://www.argmin.net/p/all-our-games-turn-into-calvinball` | `getaddrinfo EAI_AGAIN` | 1 |
| `http://timetravel.mementoweb.org/api/json/20190401/http://sutton.cs.ualberta.ca/...` | `getaddrinfo ENOTFOUND` | 1 |
| `https://en.wikipedia.org/wiki/Amdahl%27s_law` | "resolves to a non-public IP address" (blocked) | 1 |
| `<https://r.jina.ai/...>` (PDF→text proxy) and `https://r.jina.ai/https://example.com` | `TypeError: fetch failed` — **domain entirely unreachable** | 4 |
| `https://archive.org/advancedsearch.php?...` | `TypeError: fetch failed` | 3 |
| `https://archive.org/wayback/available?...` (x2 URLs) | `TypeError: fetch failed` | 2 |
| `https://web.archive.org/cdx/search/cdx?...` (x2 URLs) | `TypeError: fetch failed` | 4 |
| `https://openlibrary.org/search.json?...` | `TypeError: fetch failed` | 2 |
| `https://en.wikiquote.org/wiki/Gene_Amdahl` | `TypeError: fetch failed` | 1 |
| `https://www.incompleteideas.net/IncIdeas/BitterLesson.html` | `TypeError: fetch failed` | 2 |
| `https://incompleteideas.net/IncIdeas/BitterLesson.html` | `TypeError: fetch failed` | 1 |

**HTTP 403 / anti-bot**
| URL | Result | Attempts |
|---|---|---|
| `https://dl.acm.org/doi/10.1145/1465482.1465560` | HTTP 403 (Cloudflare interstitial) | 1 |
| `https://dl.acm.org/doi/abs/10.1145/1465482.1465560` | HTTP 403 | 1 |
| `https://acm-prod.literatumonline.com/doi/10.1145/1465482.1465560` | HTTP 403 | 1 |
| `https://sciprofiles.com/publication/view/6a5f35c5fa91807ebf5eaaedc572c093` | HTTP 403 Access Denied | 1 |
| `https://cacm.acm.org/opinion/the-sweeter-lesson/` | HTTP 403 (Cloudflare block) | 1 |
| `https://www.oreilly.com/library/view/intel-threading-building/9780596514808/ch02s03s01s03.html` | HTTP 403 | 1 |
| `https://www.sciencedirect.com/topics/computer-science/amdahls-law` | HTTP 403 / no content | 1 |
| `https://www.globalspec.com/reference/14698/160210/chapter-7-1-4-amdahl-s-law` | HTTP 403 security check | 1 |
| `https://dblp.org/rec/conf/afips/Amdahl67.html` | HTTP 200 but Anubis anti-bot challenge, no content | 1 |
| `https://api.crossref.org/works/10.1145/42411.42415` | HTTP 200 ✅ (Gustafson — control, not a failure) | 1 |

**Redirects / content type**
| URL | Result | Attempts |
|---|---|---|
| `https://doi.org/10.1145/1465482.1465560` | cross-origin redirect to `portal.acm.org` not followed | 1 |
| `http://portal.acm.org/citation.cfm?id=1465560` | cross-origin redirect not followed | 1 |
| `https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/Conc/Amdahl-04785615.pdf` | `unsupported content type "application/pdf"` | 1 |
| `https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15213-f98/lectures/class23.pdf` | `unsupported content type "application/pdf"` | 1 |

**Search-tool failures** (`web_search` returned `TypeError: fetch failed` on the
`api.deepseek.com/anthropic/v1/messages` endpoint): 4 separate search calls failed and were
retried; all eventually returned results on retry, except the final taskade/argmin query pair
which partially failed. No search result was used without fetching the underlying URL where a
quotable claim was involved.

## Successfully fetched URLs (the evidence base)

* <http://www.incompleteideas.net/IncIdeas/BitterLesson.html> (HTTP 200) — primary text
* <http://incompleteideas.net/IncIdeas/BitterLesson.html> (HTTP 200) — identical primary text
* <https://api.crossref.org/works/10.1145/1465482.1465560> (HTTP 200) — Amdahl metadata
* <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/1465482.1465560?fields=title,authors,year,venue,publicationVenue,externalIds,journal,abstract> (HTTP 200)
* <https://www.mendeley.com/catalogue/c768709b-5f5e-3d6d-9917-9f4adddb2a6e/> (HTTP 200) — Amdahl abstract + pages 483-485
* <https://api.crossref.org/works/10.1145/42411.42415> (HTTP 200) — Gustafson 1988 metadata
* <https://cvw.cac.cornell.edu/parallel/efficiency/amdahls-law> (HTTP 200) — formula, limit, Gustafson
* <https://cvw.cac.cornell.edu/parallel/efficiency/scaling> (HTTP 200) — strong vs. weak scaling
* <https://www.tutorialspoint.com/article/what-is-amdahl-s-law> (HTTP 200) — exact `p`/`s` form
* <https://raw.githubusercontent.com/jonathangittins/pm-ai-toolkit/refs/heads/main/frameworks/bitter-lesson.md> (HTTP 200) — secondary copy, used as a misquote specimen
* <https://quotekg.l3s.uni-hannover.de/resource/Mention897346> (HTTP 200) — abstract-provenance discrepancy
* <https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c21/c21s1/> (HTTP 200) — no usable formula text (slides only)
* <https://studylib.es/doc/8909569/amdahl> (HTTP 200) — no usable paper text
