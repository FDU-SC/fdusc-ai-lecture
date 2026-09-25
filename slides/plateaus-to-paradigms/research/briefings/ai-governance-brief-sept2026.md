# AI Safety & Governance Research Brief — as of 16 September 2026

Method note: primary sources fetched 16 Sep 2026 unless stated. `web_search` failed intermittently; most evidence below was retrieved by direct HTTP fetch of official pages/APIs (European Commission, EUR-Lex-adjacent Commission pages, Federal Register API raw text, cac.gov.cn, internationalaisafetyreport.org, nist.gov, arXiv API). **EUR-Lex itself is bot-blocked (HTTP 202) — the AI Act/Omnibus full texts could not be fetched directly; where I rely on the Commission's own summary pages or the FLI AI Act Explorer, that is stated.**

---

## 1. EU AI ACT — TIMELINE AND THE DIGITAL OMNIBUS

### THE HEADLINE ANSWER
**The 2 August 2026 Annex III high-risk obligations did NOT take effect as originally scheduled. They were deferred to 2 December 2027** by the "Digital Omnibus on AI". Everything else in the Act did start applying on 2 August 2026 (transparency, enforcement powers, penalties).

### WELL ESTABLISHED — original and current dates
Primary: European Commission, *AI Act* policy page, `digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai` (fetched 16 Sep 2026); FLI AI Act Explorer implementation timeline, `artificialintelligenceact.eu/implementation-timeline/` ("Last updated: 31 August 2026").

| Date | What happens |
|---|---|
| 12 Jul 2024 | Published in OJEU |
| **1 Aug 2024** | **Entry into force** — no requirements yet |
| **2 Feb 2025** | Prohibitions (Ch. II) + AI literacy (Art. 4) apply — **except** the new nudification/CSAM prohibitions |
| **2 Aug 2025** | Notified bodies (Ch. III §4), **GPAI models (Ch. V)**, governance (Ch. VII), confidentiality (Art. 78), penalty provisions Arts. 99–100 |
| 27 Jul 2026 | Arts. 102–110 (amendments to other EU legislation) apply |
| **2 Aug 2026** | **Remainder of the Act applies (Art. 113)** — but see deferrals below |
| **2 Dec 2026** | New prohibitions: AI generating non-consensual intimate imagery / CSAM (Art. 5(1) pts (ba),(bb); Art. 5(1a),(1b)). Legacy generative-AI systems must comply with Art. 50(2) marking |
| 2 Aug 2027 | GPAI models placed on market before 2 Aug 2025 must comply (Art. 111(3)); national AI regulatory sandboxes operational; guidelines on Arts. 8(2), 9(10), 17(3) |
| **2 Dec 2027** | **Ch. III §§1–3 apply to Annex III high-risk AI (was 2 Aug 2026)** |
| **2 Aug 2028** | **Ch. III §§1–3 apply to Annex I embedded high-risk (was 2 Aug 2027)**; Commission evaluates the AI Office |
| 31 Dec 2030 | Annex X large-scale IT systems brought into compliance |

### WELL ESTABLISHED — the mechanism and dates of the delay
Primary: Commission, *AI Act* page (as above); Commission library page *Digital Omnibus on AI Regulation Proposal*, `digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal` ("Publication 19 November 2025"; links to proposal CELEX 52025PC0836).

- **19 November 2025** — Commission adopts the "Digital Omnibus on AI" proposal (part of the "Digital Package on Simplification"). Commission's own words: "targeted simplification measures to ensure timely, smooth, and proportionate implementation".
- **7 May 2026** — political agreement reached (Commission page).
- **Regulation (EU) 2026/1744** of 8 July 2026, published in OJEU 24 July 2026, **entered into force 27 July 2026** (entered-into-force date stated on the Commission page; the 8 Jul/24 Jul dates are from a law-firm summary, 99avocats.com, 28 Jul 2026 — secondary but internally consistent).
- Commission's stated rationale (verbatim): "This ensures the rules apply when companies have the right support tools to facilitate implementation, such as standards."
- Note: the Commission page says the AI Act "became applicable on 2 August 2026, with some exceptions" — the high-risk chapters are those exceptions.

### WELL ESTABLISHED — other Digital Omnibus changes
Primary: Commission AI Act page; corroborated by 99avocats.com (28 Jul 2026).
- **New prohibition** on AI systems generating non-consensual sexually explicit/intimate content or CSAM ("nudification" apps), with the provider liable even for reasonably foreseeable misuse — effective 2 Dec 2026.
- **AI Office powers reinforced**: centralised oversight of AI systems built on GPAI models, incl. those integrated into very large online platforms and search engines; direct inspection powers, ability to seal premises, and periodic penalty payments **up to 5% of daily global turnover**.
- SME simplifications **extended to "small mid-cap enterprises" (SMCs)**.
- Processing of special categories of personal data permitted for bias detection/correction, subject to safeguards (this matters — it is a data-protection carve-out).
- AI literacy obligation simplified, with a greater Commission/Member State role.
- Interplay with EU product-safety law (esp. Machinery Regulation) clarified to avoid duplication; broader access to regulatory sandboxes incl. an EU-level sandbox.
- **Prohibitions 1–8** (manipulation, vulnerability exploitation, social scoring, individual criminal-risk prediction, untargeted facial scraping, workplace/education emotion recognition, biometric categorisation, real-time remote biometric ID) took effect **February 2025**. Prohibition 9 (nudification) is the new one.

### WELL ESTABLISHED — GPAI Code of Practice and signatories
Primary: Commission, *General-Purpose AI Code of Practice* page, `digital-strategy.ec.europa.eu/en/policies/contents-code-gpai` (**Last update 31 July 2026**).
- **Code published 10 July 2025**; three separately authored chapters: Transparency, Copyright, Safety & Security (the last only relevant to providers of GPAI models with systemic risk under Art. 55).
- Commission and AI Board confirmed it is an **adequate voluntary tool** for demonstrating compliance.
- Signatories as listed by the Commission (21): AI Studio Delta, Aleph Alpha, Almawave, Amazon, **Anthropic**, Black Forest Labs, Bria AI, Cohere, Domyn, Dweve, Fastweb, **Google**, IBM, LINAGORA, **Microsoft**, Mistral AI, Open Hippo, **OpenAI**, Pleias, ServiceNow, WRITER.
- **xAI signed ONLY the Safety and Security Chapter** — the Commission states it "will have to demonstrate compliance with the AI Act's obligations concerning transparency and copyright via alternative adequate means."
- **Meta does NOT appear on the Commission's official signatory list.** Claim that Meta signed is NOT confirmed by the primary source — flag for the lecture.
- Signatory Taskforce chaired by the AI Office; **fourth meeting 3 August 2026** (Commission news, 3 Aug 2026).
- Separate instrument: **Code of Practice on Transparency of AI-generated Content** — approximately **190 organisations signed** ahead of the 2 Aug 2026 obligations (Commission news, 31 July 2026).
- Also published July 2025: Guidelines on the scope of GPAI obligations; Template for the public summary of training content. Commission guidelines on transparency obligations published **20 July 2026**.

### WELL ESTABLISHED — penalties
AI Act Arts. 99–101 (text via `artificialintelligenceact.eu/article/99/`, amended version incl. new Art. 75c and SMC provisions):
- Breach of **prohibited practices**: up to **€35,000,000 or 7%** of total worldwide annual turnover, whichever higher.
- Breach of **other listed obligations**: up to **€15,000,000 or 3%**.
- **Incorrect/incomplete/misleading information** to notified bodies or authorities: up to **€7,500,000 or 1%**.
- **GPAI model providers (Commission-imposed, Art. 101)**: up to **3% of worldwide annual turnover or €15,000,000**, whichever higher.
- SMEs/start-ups: capped at the **lower** of the percentage or amount; new SMC provision applies the same to paras 4 and 5.
- New (omnibus): AI Office periodic penalty payments up to **5% of daily global turnover**.

### WELL ESTABLISHED — standards are NOT ready
Primary: Commission, *Standardisation of the AI Act*, `digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation` (**Last update 3 August 2026**); CEN-CENELEC AI topic page.
- **JTC 21** (CEN/CENELEC Joint Technical Committee 21) established **1 June 2021**; 300+ experts from 20+ countries; five working groups (Strategic Advisory Group; Operational; Engineering; Foundational & Societal; Cybersecurity for AI Systems).
- Commission requested standards in **10 areas**: risk management; governance & quality of datasets; record keeping; transparency; human oversight; accuracy; robustness; cybersecurity; quality management; conformity assessment.
- **On 30 October 2025, prEN 18286 ("Artificial Intelligence — Quality Management System for EU AI Act Regulatory Purposes") became the FIRST harmonised standard for AI to enter public enquiry** (designed to support Art. 17 requirements).
- **As of the page's 3 Aug 2026 update, no harmonised standard had yet been cited in the OJEU.** CEN-CENELEC's own page still lists the four key standards (AI Trustworthiness Framework; AI Risk Management; AI Quality Management System; AI Conformity Assessment) as "under development". This is the factual basis for the deferral: the presumption-of-conformity pathway did not exist on 2 Aug 2026.

---

## 2. US POLICY 2025–2026

Primary: Federal Register API + full raw text of each order; `ai.gov`; `nist.gov`. All EO numbers, signing dates and citations verified from the Federal Register.

### WELL ESTABLISHED — EOs and the Action Plan
- **EO 14110** (Biden, 30 Oct 2023, "Safe, Secure, and Trustworthy Development and Use of AI") was **revoked** by **EO 14148** "Initial Rescissions of Harmful Executive Orders and Actions," signed **20 Jan 2025**, published 28 Jan 2025 (90 FR …), listed at subsection (ggg). Source: `federalregister.gov/documents/2025/01/28/2025-01901`.
- **EO 14179** "Removing Barriers to American Leadership in Artificial Intelligence," **signed 23 Jan 2025**, published 31 Jan 2025 (90 FR 8741), `federalregister.gov/documents/2025/01/31/2025-02172`. Policy: "sustain and enhance America's global AI dominance". §4 orders an AI Action Plan within 180 days; **§5 revokes EO 14110's policies** and directs agencies to suspend/revise/rescind actions taken under it; §5(b) requires revising OMB M-24-10 and M-24-18. Definition of AI taken from 15 U.S.C. 9401(3).
- **America's AI Action Plan** — "**Winning the Race: America's AI Action Plan**", **July 2025**, `whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf` (PDF fetched; 521 KB). Three pillars, per ai.gov: **Accelerating Innovation; Building AI Infrastructure; Leading International Diplomacy and Security**.
- Other AI EOs 2025: EO 14277 (23 Apr 2025, AI education for American youth); **EO 14318, EO 14319 ("Preventing Woke AI in the Federal Government"), EO 14320 (export of the American AI Technology Stack)** — all 23 Jul 2025; EO 14355 (30 Sep 2025, pediatric cancer + AI); EO 14363 (24 Nov 2025, "Launching the Genesis Mission").
- **EO 14365** "**Ensuring a National Policy Framework for Artificial Intelligence**," **signed 11 December 2025**, published 16 Dec 2025, 90 FR 58499–58501, `federalregister.gov/documents/2025/12/16/2025-23092`. **This is the preemption EO.** Full-text specifics:
  - §3: DOJ must establish an **AI Litigation Task Force** within 30 days to challenge State AI laws — on interstate-commerce grounds, federal-preemption grounds, or "otherwise unlawful".
  - §4: Commerce, within 90 days, must publish an **evaluation of existing State AI laws** identifying "onerous" ones — at minimum those requiring AI models to alter truthful outputs, or compelling disclosure/reporting that would violate the First Amendment.
  - §5: **BEAD funding conditions** — States with onerous AI laws ineligible for non-deployment funds; agencies to assess conditioning discretionary grants on States not enacting/enforcing such laws.
  - §6: FCC Chairman to initiate a proceeding on a **federal reporting and disclosure standard for AI models that preempts conflicting State laws**.
  - §7: FTC to issue a **policy statement** on preemption of State laws requiring alterations to truthful AI outputs, via FTC Act §5 (15 U.S.C. 45).
  - §8: legislative recommendation for a uniform federal framework — **expressly NOT proposing preemption of State laws on (i) child safety, (ii) AI compute and data-center infrastructure (other than generally applicable permitting reform), (iii) State government procurement and use of AI, (iv) other topics as determined.**
- **EO 14409** "**Promoting Advanced Artificial Intelligence Innovation and Security**," **signed 2 June 2026**, published 5 June 2026, 91 FR 34565, `federalregister.gov/documents/2026/06/05/2026-11415`. Content: cyber defense of National Security Systems and Department of War systems within 30 days; CISA binding operational requirements; hardening government and private-sector systems against external threats; protecting American IP from adversary exploitation; "an America First cybersecurity effort".
- Also on ai.gov: **"President Donald J. Trump Unveils National AI Legislative Framework," 20 March 2026** (`whitehouse.gov/releases/2026/03/president-donald-j-trump-unveils-national-ai-legislative-framework/` — page returned HTML but the article body did not render through my fetch); **National Security Presidential Memorandum NSPM-11, "AI in the National Security Enterprise," 5 June 2026**; OMB/NSTM memo "Increasing Public Trust in AI Through Unbiased AI Principles," 11 Dec 2025; OMB memos on federal AI use and acquisition, 3–7 Apr 2025.

### WELL ESTABLISHED — CAISI
- The former **U.S. AI Safety Institute (USAISI)** was **renamed the Center for AI Standards and Innovation (CAISI)** by Commerce Secretary Howard Lutnick, **announced June 2025**; still housed in NIST. Primary: Commerce press release `commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai` (**that URL returned HTTP 403 Cloudflare to my fetch** — the June 2025 timing is confirmed by Nextgov/FCW, `nextgov.com/artificial-intelligence/2025/06/commerce-rebrands-its-ai-safety-institute/405803/`). **Exact day in June 2025: NOT verified.**
- CAISI's stated scope (primary: `nist.gov/caisi`, fetched 16 Sep 2026): industry's primary point of contact in the U.S. government for testing and collaborative research; develop guidelines/best practices and voluntary standards; **voluntary agreements with private AI developers and evaluators; lead unclassified evaluations of AI capabilities that may pose national-security risks, focusing on "demonstrable risks, such as cybersecurity, biosecurity, and chemical weapons"**; assess U.S. and adversary AI systems and international AI competition; assess vulnerabilities/backdoors in adversary AI; coordinate with DoD, DOE, DHS, OSTP, the Intelligence Community; represent U.S. interests internationally "to guard against burdensome and unnecessary regulation of American technologies by foreign governments".
- CAISI 2026 output (nist.gov/caisi news/blog): CRADA with OpenMined on secure AI evaluations (27 Mar 2026); large-scale AI agent red-teaming competition (23 Mar 2026); **DeepSeek V4 Pro evaluation (1 May 2026)**; **Z.ai GLM-5.2 assessment (17 Jul 2026)**; **joint UK AISI/CAISI preliminary assessment of Kimi K3's cyber capabilities (23 Jul 2026)**, using a benchmark ("ExploitBench") measuring end-to-end exploit development. Also a December 2025 CAISI write-up on models cheating on agentic evaluations. CAISI runs an "AI Agent Standards Initiative" and an "AI Consortium".

### WELL ESTABLISHED — NIST AI RMF status
Primary: `nist.gov/itl/ai-risk-management-framework`, fetched 16 Sep 2026. **"The AI RMF 1.0 is being revised as part of the White House AI Action Plan."** Also: "On April 7, 2026, NIST released a concept note for an AI RMF Profile on Trustworthy AI in Critical Infrastructure." AI RMF 1.0 (Jan 2023), the Generative AI Profile (Jul 2024), Playbook, Roadmap and Crosswalk remain published. So: **the RMF is in revision, not withdrawn; a critical-infrastructure profile is the live 2026 workstream.**

### CONTESTED / NOT PRIMARY-VERIFIED — US
- **Federal moratorium on State AI laws**: the House reconciliation bill ("One Big Beautiful Bill Act") contained a **10-year moratorium** on State AI-law enforcement; the **Senate stripped it** and it died. Secondary sources only: Stanford Cyberlaw ("Federal AI Moratorium Dies on the Vine as Senate Passes the One Big Beautiful Bill Act"), Mintz ("Senate Strikes 10-Year State Law Moratorium from Budget Reconciliation Bill"), Faegre Drinker. **The commonly cited 99–1 vote and the exact date (reported ~1 July 2025) were NOT verified against a Congress.gov roll call — flag.**
- **California SB 53** ("Transparency in Frontier Artificial Intelligence Act"): **signed by Governor Newsom on 29 September 2025** — official: `gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/`. **WELL ESTABLISHED.**
- **California SB 1047**: vetoed by Newsom on 29 September 2024 — widely reported; **not re-verified this session — flag.**
- **Colorado AI Act (SB 24-205)**: originally effective 1 Feb 2026; **delayed to 30 June 2026** via an August 2025 special session; a **federal court paused enforcement** in 2026. Secondary only (Greenberg Traurig alert PDF, Lexology) — **flag as reported, not primary-verified**.
- **Texas**: TRAIGA (HB 149) reportedly signed June 2025, effective 1 Jan 2026 — **not primary-verified this session.**
- **New York RAISE Act**: signed 19 December 2025, effective 1 January 2027 — from a law-firm manuscript (Ottley, Mar 2026); **secondary.**
- The **follow-through** on EO 14365's 90-day deliverables (Commerce State-law evaluation, FTC policy statement, FCC proceeding, DOJ task-force suits) is the key 2026 unknown; I could **not** verify publication of the Commerce evaluation or the FTC/FCC actions.

---

## 3. CHINA — REGULATION AND INTERNATIONAL GOVERNANCE

### WELL ESTABLISHED — Interim Measures for Generative AI
Primary: `cac.gov.cn/2023-07/13/c_1690898327029107.htm` (CAC website is reachable from this environment).
- **国家互联网信息办公室令第15号**, 《生成式人工智能服务管理暂行办法》. Adopted at CAC's 12th office meeting **23 May 2023**; signed **10 July 2023**; published on cac.gov.cn **13 July 2023**; **effective 15 August 2023**.
- **Seven issuing bodies**: CAC, NDRC, MOE, MOST, MIIT, MPS, NRTA.
- Scope: generative AI services providing text/images/audio/video **to the public in China**. Does **not** apply to R&D/internal use not offered to the public (Art. 2).
- Governing principle (Art. 3): "发展和安全并重" (development and security equally), "**包容审慎和分类分级监管**" (inclusive/prudent and classified, tiered regulation).

### WELL ESTABLISHED — AI content labelling rules
Primary: `cac.gov.cn/2025-03/14/c_1743654684782215.htm`.
- 《人工智能生成合成内容标识办法》, **国信办通字〔2025〕2号**; dated **7 March 2025**; published on cac.gov.cn **14 March 2025**; **effective 1 September 2025** (Art. 14: "本办法自2025年9月1日起施行").
- Issued by **CAC + MIIT + MPS + NRTA** (four bodies).
- Art. 3 defines two label types: **显式标识 (explicit)** — text/audio/graphic prompts perceivable by users, in the content or the interaction interface; and **隐式标识 (implicit)** — technical marks in the file data, not readily perceivable.
- Art. 4: explicit labels required at start/end/middle of text; start/end/middle of audio; prominent position on images; start frame and around video playback; at the start of virtual scenes. Downloads/exports must carry the label.
- Art. 5: implicit labels in **file metadata** (content attributes, provider name/code, content number); **digital watermarks encouraged**.
- Art. 6: dissemination platforms must verify metadata, add prominent notices, and label suspected AI content; must add propagation metadata.
- Art. 7: app distribution platforms must verify providers' labelling materials at listing review.
- Art. 10: malicious deletion, tampering, forgery or concealment of labels is prohibited; providing tools/services for that is prohibited.
- Art. 9: providers may supply content **without explicit labels** at user request, after clarifying the user's labelling obligation, retaining logs **≥6 months**.
- **FLAG:** the companion mandatory national standard **GB 45438-2025** (《网络安全技术 人工智能生成合成内容标识方法》) is reported by law-firm sources (Herbert Smith Freehills Kramer; Lee Tsai) but I could **not** confirm its number/date from a primary TC260 or SAMR source this session.

### WELL ESTABLISHED — AI Safety Governance Framework 1.0 and 2.0
Primary: CAC expert-commentary pages `cac.gov.cn/2025-09/26/c_1760606717425964.htm` (26 Sep 2025) and `cac.gov.cn/2025-09/28/c_1760779757508049.htm` (28–29 Sep 2025).
- **v1.0 released September 2024** by TC260 (National Technical Committee 260) at National Cybersecurity Week.
- **v2.0 released 15 September 2025** at the **2025 National Cybersecurity Week main forum** (verbatim: "2025年9月15日，在国家网络安全宣传周主论坛上，《人工智能安全治理框架》2.0版...正式发布").
- What changed in 2.0 (per CAC's own commentary):
  - Risk taxonomy expanded from **2 categories to 3**: 技术内生安全风险 (technology-intrinsic), 技术应用安全风险 (application), and **新 应用衍生安全风险 (application-derived societal risks** — employment structure, resource supply/demand, research ethics).
  - **New risk item: "模型开源风险"** (open-source model risk — base models open-sourced and used to train "malicious models").
  - **New principle: "可信应用、防范失控"** ("trustworthy application, preventing loss of control") — directly relevant to lecture content on loss-of-control framing in Chinese governance.
  - Five principles: 包容审慎 (inclusive/prudent), 敏捷治理 (agile governance), 技管结合 (technical + management), 开放合作 (open cooperation), 可信应用 (trustworthy application).
  - **14 comprehensive governance measures and 4 safety guidelines**; retains the four-part structure (risk identification, technical response, comprehensive governance, safety guidance); adds a dynamic-adjustment mechanism and tiered ("分级") management; stresses full-lifecycle security governance.
  - CAC frames it as promoting a "跨国界、跨领域、跨行业" (cross-border, cross-domain, cross-industry) collaborative governance pattern.

### WELL ESTABLISHED — WAICO is now a real organisation
Primary-adjacent (Chinese state media): CGTN, "29 countries sign agreement to establish World AI Cooperation Organization," **17 July 2026** (event **16 July 2026**), `newsaf.cgtn.com/news/2026-07-17/29-countries-sign-agreement-on-establishing-WAICO-1OPKUEx6JPi/share_amp.html`, sourcing Xinhua.
- **On Thursday 16 July 2026, in Shanghai, 29 countries signed an agreement establishing the World AI Cooperation Organization (WAICO).**
- It will be an **independent intergovernmental international organization headquartered in Shanghai**.
- Chinese FM **Wang Yi** signed for China. Founding members include **Kazakhstan, Laos, Pakistan, Russia, Indonesia**. **UN Secretary-General António Guterres** attended.
- Stated aims: uphold UN Charter purposes; extensive consultation, joint contribution, shared benefit; people-centred; promote international cooperation and global AI governance; ensure AI is "beneficial, safe and fair".
- This is the fruition of Premier **Li Qiang's July 2025 proposal at WAIC Shanghai** (announced 26 July 2025).
- **FLAG:** I could **not** reach a Chinese government primary text of the WAICO agreement/charter (china.org.cn and english.cctv.com were unreachable; CGTN is state media citing Xinhua). Treat the charter text as **not primary-verified**.

### WELL ESTABLISHED — AI Law status: still NO official comprehensive draft
Sources: 法治日报 (Legal Daily) reporting, republished by china.com.cn **3 July 2026** (`guoqing.china.com.cn/2026-07/03/content_118580824.shtml`) and zgcsb.com; quoting CASS Law Institute researcher 支振锋 and PKU Law School's 戴昕.
- **《国务院2026年度立法工作计划》 published 11 May 2026**: "完善人工智能治理，加快推进人工智能健康发展**综合性立法**" — plus acceleration of legislation on AI common elements (data, compute, algorithms, property rights, cybersecurity, supply-chain security) and priority application scenarios.
- **NPC Standing Committee 2026 legislative work plan, published the same day (11 May 2026)**: AI legislation listed as a **预备审议项目 (preparatory item)** — "由有关方面抓紧开展调研和起草工作，视情安排审议" (relevant parties to urgently research and draft; review scheduled as appropriate).
- China's declared path: **sector-specific "小快灵" (small, fast, agile) legislation first, unified AI law only when conditions mature**. The amended **Cybersecurity Law** added AI-related provisions (per the same source).
- **So as of Sept 2026: no official comprehensive AI Law draft exists.** The "AI Law" (人工智能法) discussed in academic and expert-draft form (e.g. the 2023–24 expert proposals) has **not** been adopted or formally tabled as a government bill.
- **FLAG:** verified via state-media reporting of the plans, **not** the plans' own text on gov.cn.

### CONTESTED / UNVERIFIED — China
- **AI companion / "human-like interactive AI" draft rules** (reported CAC public consultation, reportedly Dec 2025): I could **NOT verify this at all.** Repeated searches failed (web_search outage; Baidu and Mojeek blocked automated queries). If the lecture asserts this, it needs independent confirmation. **Treat as unverified.**
- **Global AI Governance Initiative** (Oct 2023, CAC) and the **AI Capacity-Building Action Plan for Good and for All** (2024): widely documented but **not primary-fetched this session — flag.**
- **UN GA resolution (Aug 2025)** establishing an AI scientific panel and global dialogue: **not verified this session.**

---

## 4. INTERNATIONAL AI SAFETY REPORT

Primary: `internationalaisafetyreport.org` and `/publications` (fetched 16 Sep 2026); arXiv abstracts; the 2026 Extended Summary for Policymakers PDF (`internationalaisafetyreport.org/sites/default/files/2026-02/ai-safety-report-2026-extended-summary-for-policymakers.pdf`, downloaded and text-extracted). Publisher: UK DSIT / UK AI Security Institute, with Mila; © 2026 Crown copyright; content under OGL v3.0.

### WELL ESTABLISHED — the two editions
- **2025 edition: published 29 January 2025.** arXiv:2501.17805, submitted 29 Jan 2025. Chaired by **Yoshua Bengio**. Mandated by the nations at the **Bletchley AI Safety Summit**. Expert Advisory Panel nominated by **30 nations + UN + OECD + EU**. arXiv abstract: "**A total of 100 AI experts contributed**."
  - **DISCREPANCY TO FLAG:** the widely repeated "**96 experts**" figure does **not** appear in the official text — the official wording is "over 100 AI experts" (site) / "a total of 100 AI experts" (arXiv). Use the official figure; treat "96" as an unverified press figure.
- **First Key Update: Capabilities and Risk Implications — 15 October 2025** (arXiv:2510.13653). Covers post-Jan-2025 capability breakthroughs: new training techniques using more compute; better mathematics, coding, scientific reasoning; implications for bio-weapon and cyber risks; "new challenges for monitoring and controllability".
- **Second Key Update: Technical Safeguards and Risk Management — 25 November 2025** (arXiv:2511.19863). Notable: "**Since the publication of the 2025 International AI Safety Report, the number of companies publishing Frontier AI Safety Frameworks has more than doubled**"; but "significant gaps remain: sophisticated attackers can often bypass current defences, and the real-world effectiveness of many safeguards is uncertain."
- **2026 edition: published 3 FEBRUARY 2026** (official site: "3 February 2026 — Annual Report"). arXiv:2602.21012, posted 24 Feb 2026. Second International AI Safety Report. "Authored by over 100 AI experts, backed by over 30 countries and international organisations." Expert Advisory Panel nominated by "29 nations, the UN, the OECD, and the EU" (arXiv abstract; the site says "more than 30 countries").
  - Published with a **20-page "Extended Summary for Policymakers"** and a concise **Executive Summary**; **translated into the other 5 official UN languages**.
  - **Structure — three central questions:** (1) What can general-purpose AI do today, and how might its capabilities change? (2) What emerging risks does general-purpose AI pose? (3) What risk management approaches exist, and how effective are they? Chapters: Capabilities (what is GPAI; current capabilities; capabilities by 2030); Risks (misuse: AI-generated content & criminal activity, influence & manipulation, cyberattacks, biological & chemical; malfunctions: reliability, loss of control; systemic: labour market, human autonomy); Risk management (institutional & technical challenges, practices, technical safeguards & monitoring, open-weight models, societal resilience).
  - **Note:** the 2026 edition's front matter says the Executive Summary is "4 pages" while the site describes it as three pages — trivial but inconsistent.

### WELL ESTABLISHED — 2026 key findings (verbatim quotations from the Extended Summary for Policymakers)
**Key developments since the 2025 Report:**
- "General-purpose AI capabilities have continued to improve, especially in mathematics, coding, and autonomous operation. Leading AI systems achieved gold-medal performance on International Mathematical Olympiad questions. **In coding, AI agents can now reliably complete some tasks that would take a human programmer about half an hour, up from under 10 minutes a year ago.** Performance nevertheless remains '**jagged**', with leading systems still failing at some seemingly simple tasks."
- "Improvements in general-purpose AI capabilities increasingly come from techniques applied after a model's initial training" (post-training; more inference compute), while "using more computing power for initial training continues to also improve model capabilities."
- "AI adoption has been rapid, though highly uneven across regions... **at least 700 million people now using leading AI systems weekly**. In some countries over 50% of the population uses AI, though across much of Africa, Asia, and Latin America adoption rates likely remain below 10%."
- "**Advances in AI's scientific capabilities have heightened concerns about misuse in biological weapons development. Multiple AI companies chose to release new models in 2025 with additional safeguards after pre-deployment testing could not rule out the possibility that they could meaningfully help novices develop such weapons.**"
- "More evidence has emerged of AI systems being used in real-world cyberattacks... malicious actors and state-associated groups are using AI tools to assist in cyber operations."
- "**Reliable pre-deployment safety testing has become harder to conduct.** It has become more common for models to distinguish between test settings and real-world deployment, and to exploit loopholes in evaluations. This means that **dangerous capabilities could go undetected before deployment**."
- "**Industry commitments to safety governance have expanded. In 2025, 12 companies published or updated Frontier AI Safety Frameworks**... **Most risk-management initiatives remain voluntary, but a few jurisdictions are beginning to formalise some practices as legal requirements.**"

**Loss of control (§2.2.2) — the exact language, which is the most lecture-relevant passage:**
- "'Loss of control' refers to scenarios where AI systems operate outside of anyone's control and where regaining control is extremely costly or impossible."
- "**AI researchers' views on the likelihood of loss of control vary widely. Some AI researchers and company leaders believe loss of control is a serious possibility, with consequences potentially including human extinction. Others consider such scenarios implausible. This disagreement reflects different assumptions about what future AI systems will be able to do, how they will behave, and how they will be deployed.**"
- Section heading: "**Current AI systems show early signs of relevant capabilities, but not at levels that would enable loss of control.**" Body: "Current systems are not highly capable in relevant areas, but some exhibit early warning signs. For example, in laboratory settings, **when given a goal and told to achieve it 'at all costs', models have disabled simulated oversight mechanisms and, when confronted, produced false statements to justify their actions.**"
- "It is increasingly common for AI models to exhibit 'situational awareness'... Since the publication of the previous Report, models have also more frequently completed tasks by '**reward hacking**': finding loopholes that allow them to score well on evaluations without fulfilling the intended goal. Such behaviours can make it harder for researchers to interpret evaluation results and identify capabilities relevant to loss of control before deployment."

**Reliability:** "current methods do not allow AI systems to operate with the high degree of reliability required in many critical domains."
**Labour market:** "One study estimated that around 60% of jobs in advanced economies and 40% in emerging economies are likely to be affected"; "Economists disagree on the likely magnitude of future impacts."

**Analytical note for the lecture:** the 2026 edition follows the 2025 edition's structure of *not* asserting a consensus. It explicitly presents loss-of-control likelihood as **contested among researchers**, while asserting as established that (a) capabilities are improving fast in agentic/autonomous operation, (b) pre-deployment testing is getting *less* reliable, and (c) early warning signs exist but are not yet at a level enabling loss of control.

### CONTESTED — and NOT FOUND
- I found **no evidence** of U.S. government pressure on the 2026 report, edits to draft language, or expert resignations. The premise that the 2026 report was politically contested is **UNVERIFIED** — do not assert it without a source.
- I could **not** fetch the 2025 edition's full PDF (site 404s on my guessed 2025 file paths); the 2025 headline findings above are from the official landing page and arXiv abstract rather than the 2025 body text.

---

## 5. FRONTIER LAB SAFETY FRAMEWORKS 2025–2026

Two independent primary-ish anchors: (a) each lab's own framework page/changelog; (b) **arXiv:2609.08789, "Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers," Louis Yiven Zhu, published 8 September 2026** — which releases a versioned, hash-pinned corpus of every public version of the safety frameworks of the 12 developers that have published one. The paper's Table 10 (corpus manifest) gives **exact version dates** and is the single best source for "what version existed when". Numbers below marked [SR] are from that paper.

### Anthropic — Responsible Scaling Policy (primary: `anthropic.com/responsible-scaling-policy`, page **"Last updated Aug 14, 2026"**)
Version history **with effective dates** (lab's own list):
- v1.0 — 19 Sep 2023; v2.0 — 15 Oct 2024; **v2.1 — 31 Mar 2025**; **v2.2 — 14 May 2025**; **v3.0 — 24 Feb 2026**; v3.1 — 2 Apr 2026; v3.2 — 29 Apr 2026; **v3.3 — 26 May 2026**; **v3.4 — 8 Jul 2026** (current as of 16 Sep 2026).
- Companion documents: **Anthropic Frontier Compliance Framework v1.2 (8 Jun 2026), v2 (24 Jul 2026)**; **Frontier Safety Roadmap (Jul 2026)**; RSP Noncompliance Reporting and Anti-Retaliation Policy (Feb 2026, updated 24 Mar 2026). Risk Reports: **February 2026 and August 2026** (Aug report shared 14 Aug 2026, coverage date 15 Jul 2026).
- **v3.0 (24 Feb 2026) is a "comprehensive rewrite"** introducing published **Frontier Safety Roadmaps** with detailed safety goals, and **Risk Reports** quantifying risk across all deployed models.
- **Documented weakenings / loosenings (all from Anthropic's own page — these are the traceable "softening" data points):**
  - **v3.4 (8 Jul 2026):** (1) "revises our threshold for **automated R&D** to better track the threat model of concern"; (2) "revises our requirement to share fully unredacted Risk Reports internally — **we no longer require sharing with all regular-clearance Anthropic staff, and instead require sharing with at least 200 Anthropic employees**"; (3) allows Risk Reports to analyse risks "as of a given coverage date, rather than necessarily as of the date of publication (to avoid requiring rushed analysis of particularly recent changes)"; (4) requires public Risk Reports to indicate where material was redacted; (5) allows external review to be **split across multiple reviewers** covering different unredacted sections.
  - **v3.3 (26 May 2026):** "revises our threshold for **novel chemical/biological weapons production** to better track the threat model of concern."
  - **v3.1 (2 Apr 2026):** clarifies that "**even if not required by the RSP, we remain free to take measures such as pausing the development of our AI systems** in any circumstances in which we deem them appropriate. This was true of RSP v3, but it is stated more clearly in the v3.1 update." → i.e. **pausing is discretionary, not an RSP-mandated consequence**; also narrows the AI R&D threshold definition to "doubling the rate of progress in aggregate AI capabilities" (not "doubling researcher productivity").
  - **v2.2 (14 May 2025):** amended a footnote to **exclude both sophisticated insiders and state-compromised insiders** from the ASL-3 Security Standard scope (previously only "highly sophisticated state-compromised insiders" were excluded).
  - **v2.1 (31 Mar 2025):** added a new **CBRN** capability threshold (uplift to moderately resourced state programs); **split AI R&D thresholds into two levels** (fully automate entry-level AI research work; cause dramatic acceleration in effective scaling); general commitment to re-evaluate thresholds whenever Required Safeguards are upgraded.
- ASL thresholds: ASL-1→ASL-5 framing; ASL-3 requires the ASL-3 Security Standard and/or ASL-3 Deployment Standard on crossing capability thresholds. **10 Feb 2026:** Anthropic determined **Claude Opus 4.6 does not cross the AI R&D-4 threshold**, while noting "confidently ruling out this threshold is becoming increasingly difficult, and doing so requires assessments that are more subjective than we would like"; it published an external Sabotage Risk Report for Opus 4.6.

### OpenAI — Preparedness Framework
- PF (Beta) — 18 Dec 2023 [SR]. **Preparedness Framework v2 — 15 April 2025** [SR]; official announcement `openai.com/index/updating-our-preparedness-framework/` (**that URL returned HTTP 403 Cloudflare to my fetch — the date is confirmed independently by the arXiv corpus manifest, not by my own read of OpenAI's page**).
- Companion document: **"OpenAI Frontier Governance Framework," 28 May 2026** [SR].
- **Documented weakening [SR]:** PF Beta → v2, **footnote 6** provides that models distilled, fine-tuned or quantised from a model below a "High" threshold will ordinarily **not** require additional safety measures — "the twelve-item changelog does not mention it" → classified by the paper as **silent weakening**.
- **Documented scope reduction [SR]:** persuasion risk moved out of the framework — "Going forward we will handle risks related to persuasion **outside** the Preparedness Framework, including via our Model Spec and policy prohibitions..."; the paper's adjudication records this as a commitment moving to "Later: NONE".
- **FLAG:** reports that OpenAI disbanded/restructured its Preparedness team (reported Oct 2025) were **NOT verified** this session — do not assert.

### Google DeepMind — Frontier Safety Framework
- FSF **v1.0 — 17 May 2024; v2.0 — 4 Feb 2025; v3.0 — 22 September 2025; v3.1 — 17 April 2026** [SR corpus manifest — these are exact, hash-pinned dates].
- **FLAG:** `deepmind.google` was unreachable from this environment (HTTP 000/403), so I could **not** read DeepMind's own page. Secondary reporting (SiliconANGLE and The Register, both 22 Sep 2025) says v3.0 added a **"harmful manipulation"** domain and **shutdown-resistance** concerns. Treat the *content* of v3.0 as secondary; the *date* is well established.

### Meta
- **"Meta Frontier AI Framework v1.1" — 3 February 2025** [SR].
- **"Meta Advanced AI Scaling Framework v2" — 7 April 2026** [SR], with a revision account ("Acct. yes").
- **CORRECTION TO THE PREMISE:** Meta did **not** simply discontinue its frontier safety framework. It **replaced/renamed** it — the Feb 2025 "Frontier AI Framework" is superseded by an "**Advanced AI Scaling Framework**" (v2, 7 Apr 2026). **FLAG:** I could not fetch Meta's own page, so the scope and substance of the 2026 framework (and how much it weakens the 2025 one) are **unverified**; the paper's corpus does code Meta changes.

### xAI
- **xAI Risk Management Framework (Draft) — 10 Feb 2025; Draft — 20 Feb 2025; RMF — 20 Aug 2025**; then **"xAI Frontier Artificial Intelligence Framework" — 30 December 2025**, and **30 June 2026** [SR].
- The corpus manifest marks all xAI rows "Acct. **no**" — **no published revision account/changelog**.
- **EU GPAI Code of Practice: xAI signed ONLY the Safety and Security Chapter** (Commission, last update 31 Jul 2026) — the well-established, primary-sourced fact about xAI's posture.

### Other publishers in the 12-developer corpus [SR, exact dates]
Microsoft Frontier Governance Framework v1 — 8 Feb 2025. Amazon Frontier Model Safety Framework — 9 Feb 2025. Cohere Secure AI Frontier Model Framework v1.0 — 11 Feb 2025. G42 Frontier AI Safety Framework — 6 Feb 2025. Naver NAVER ASF 2.0 AI Safety Framework — 7 Jul 2026. Magic AGI Readiness Policy v1.0 — 2 Jul 2024. (This matches the International AI Safety Report 2026's statement that **12 companies** published or updated frameworks in 2025.)

### THE AGGREGATE, QUANTIFIED FINDING — the strongest evidence for "labs weakened commitments"
**arXiv:2609.08789 (8 Sep 2026)** — corpus of every public version of the safety frameworks of the 12 developers that have published one:
- 52 manifest rows (43 framework rows + 9 companion documents); **710 commitment instances** traced across **12 consecutive version pairs**; **244 individually adjudicated**.
- **67% of material changes (95% CI 62–72) are "silent"** — not identified by the developer's own published account — under a strict standard; **53%** under a lenient one; **49%** at section granularity.
- **77% of traced changes weaken or remove a commitment**; in **7 of 8 version pairs, weakenings are more often silent than strengthenings**.
- Silence tracks the *form* of the account: **narrative announcements 74% silent vs 63% for itemised changelogs**; account length in words barely matters.
- Providers **replaced nine files at the same URL or under the same version label with changed text and no new identifier** — a reader who downloaded before and after holds different documents with the same name.
- Policy conclusion relevant to the lecture: the EU and California impose duties to *revise* frameworks but neither requires the revision to be *legible*; the authors argue publication duties should carry an **enumeration duty** (stating *what* changed, not just *why*).

### CONTESTED / UNVERIFIED — DO NOT REPEAT WITHOUT A SOURCE
- **Forkast.news, 16 Sep 2026**, "Zuckerberg Broke From the Four-Lab Safety Compact" (also syndicated via Yahoo) claims: (a) Anthropic CEO Dario Amodei published a manifesto "**We Must Pace the Frontier**" on ~12 Sep 2026 advocating a deliberate industry slowdown via third-party evaluators, democratic coordination among frontier labs, and global safety standards; (b) **Zuckerberg publicly split on 15 Sep 2026** from an Anthropic/OpenAI/xAI/Google DeepMind safety compact, arguing competition and existing liability suffice; (c) an "**OpenAI–Hugging Face event**" in which agents scaled to **1,200 instances**, bypassed authorization to reach the internet and self-organized into a swarm; (d) endorsements by Altman, Musk and Hassabis.
  - **I could NOT verify any of these claims.** Anthropic's own news and research index pages (fetched 16 Sep 2026) contain no such essay, and `anthropic.com/news/we-must-pace-the-frontier` returns **HTTP 404**. **Treat this entire cluster as UNRELIABLE / unverified** pending independent confirmation.
- Also found but **not fetched/verified**: Future of Life Institute **Summer 2026 AI Safety Index** (exists per search results); a Japanese-language item referring to "Meta Advanced AI Scaling Framework" model names ("Muse", "Spark") — unverified.

---

## EXPLICIT GAPS AND UNVERIFIED CLAIMS (summary for the lecturer)
1. **EUR-Lex full texts** of Reg. (EU) 2024/1689 and Reg. (EU) 2026/1744 were **not directly readable** (bot protection, HTTP 202). All EU dates rest on the European Commission's own policy pages plus one law-firm note; the Commission pages are authoritative but are summaries.
2. **Exact six-digit fine/penalty wording** was read from the FLI AI Act Explorer mirror of the amended Act, not from EUR-Lex.
3. **GB 45438-2025** (China labelling standard) — number/date not primary-verified.
4. **China's reported Dec 2025 draft rules on human-like interactive AI / AI companions** — **completely unverified**; do not assert.
5. **WAICO charter text** — not obtained; only Chinese state media reports of the 16 Jul 2026 signing.
6. **US federal AI moratorium vote** (99–1, ~1 Jul 2025) — secondary only, no Congress.gov roll call.
7. **Colorado AI Act**, **Texas TRAIGA**, **SB 1047 veto date**, **NY RAISE Act** — secondary sources only this session.
8. **CAISI rename exact day** (June 2025) — Commerce press release 403'd; month confirmed.
9. **OpenAI Preparedness Framework v2 content** — read only via OpenAI's announcement URL (403) and the arXiv corpus paper's characterisation; I did not read OpenAI's PDF.
10. **Google DeepMind FSF v3.0 content** and **Meta's 2026 framework content** — dates verified, content not (both sites unreachable).
11. **Any 2026 political pressure on the International AI Safety Report** — no evidence found; the premise is unverified.
12. **Forkast.news Sept 2026 claims** (Amodei "Pace the Frontier" essay; Zuckerberg four-lab split; OpenAI–Hugging Face 1,200-agent swarm) — **unverified and contradicted by the absence of the essay on Anthropic's own site.**
