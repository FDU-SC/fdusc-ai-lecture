---
layout: center
---

<div h-20 />

<div text-center text-6xl>
<span color-gray>Act III</span>
</div>

<div h-3 />

<div text-center text-4xl>
Our Turn
</div>

<div h-3 />

<div h-20 />

---

# What Agents Can Actually Do

<div h-3 />

| Benchmark | Best result | The caveat that matters |
| --- | --- | --- |
| **SWE-bench Verified** | ~77% | **Retracted by its own maintainers** — an audit found most sampled tasks had tests that reject correct patches |
| **SWE-bench Pro**, commercial set | **under 18%** | Real enterprise codebases, not curated repositories |
| **FeatureBench** | 74% → **11%** | The same model scores 74% on SWE-bench and 11% on actually *implementing a new feature* |
| **OSWorld** (computer use) | ~61% | Against a human baseline of ~72% |
| **ARC-AGI-3** | 62.7% | Or 99.9% — depending on whose evaluation harness you use |
| **Coding-agent adoption** | ~4% of public GitHub commits | Measured in early 2026 |

<div h-3 />

---

# What Agents Still Cannot Do

<div h-3 />

| Failure mode | The evidence |
| --- | --- |
| **Long-horizon reliability** | The best 50%-success time horizon is around 17 hours — but the error bars are roughly a factor of two each way, and reliability at 99% cannot be measured on any current suite |
| **Compounding error** | A task needing 100 correct steps at 99% per step succeeds about 37% of the time. Agents are not at 99% per step. |
| **Context degradation** | Performance falls as input grows, across all 18 models tested — and the standard "needle in a haystack" test does not reveal it |
| **Confident fabrication** | Purpose-built legal research tools marketed as hallucination-free were measured at **17–33%** hallucination rates under a preregistered evaluation |
| **Reward hacking** | Agents trained with RL learn to game the metric — one disabled a synchronization call to make its kernel *look* faster. And this behaviour generalises to more serious misalignment. |
| **Acting without being asked** | In one documented incident an agent deleted a production database *and its backups* in nine seconds, on its own initiative |

<div h-3 />

---

# The Productivity Question Has a Surprising Answer

<div h-2 />

<div class="grid grid-cols-2 gap-7">

<div>

<Chart name="metr-productivity" width="100%" />

</div>

<div>

In 2025 METR ran a randomised controlled trial: experienced open-source developers, real tasks from their own repositories, AI assistance allowed.

<div h-2 />

**The follow-up, and why to be careful with it.** A 2026 follow-up on the same cohort found an **18% speedup** — but the researchers call their own data unreliable, because 30–50% of participants had quietly withheld tasks they did not want to do without AI.

</div>

</div>

---

# The Honest Ledger

<div h-3 />

| Domain | Where it really stands |
| --- | --- |
| **Protein structure** | Solved for many cases; the remaining failure is *ranking*, not folding |
| **Antibiotics and drug design** | Real wet-lab hits, one drug in Phase III — years from being proven medicine |
| **Materials** | Datasets are a genuine achievement; discovery claims must be audited case by case |
| **Weather** | Operational and cheaper; not yet better on the metrics that matter operationally |
| **Mathematics** | Formal verification works; open-problem success rate is a few percent; credit and priority are unsettled |
| **Chip design and verification** | Benchmarks are weakly instrumented; no verified production deployment of LLM-generated RTL |
| **Autonomous laboratories** | The most public claim failed audit by a factor of fifteen |

<div h-3 />

---

# Announced vs Independently Tested

<div h-2 />

<div class="grid grid-cols-2 gap-8">

<div>

<Chart name="claimed-vs-audited" width="100%" />

</div>

<div>

<div h-2 />

- **A-Lab** counted a material as synthesized without confirming it was new.
- **SWE-bench** graded against tests that rejected correct patches.
- **FeatureBench** measured the task the benchmark was built for, not the task people care about.

</div>

</div>

<div h-2 />

---

# The Cost Side: Energy

<div h-2 />

<Chart name="energy-queue" width="900px" />

<div h-2 />

<div class="grid grid-cols-3 gap-5 text-center">

<div>

**+17%** datacenter demand in 2025; AI-focused datacenters **+50%**

</div>

<div>

US datacenters: 4.7% of electricity in 2024 → **11.8%** in the 2030 reference case

</div>

<div>

**~3%** of everything requested on one grid is actually energized

</div>

</div>

<div h-2 />

---

# The Cost Side: Money

<div h-3 />

| | 2025 spend | 2026 guidance |
| --- | --- | --- |
| Microsoft | \$64.6B | ~\$190B |
| Alphabet | \$91.4B | \$195–205B |
| Amazon | \$131.8B | ~\$220B |
| Meta | \$69.7B | \$130–145B |

<div h-3 />

### What has to be true for this to pay off

One widely cited analysis estimates the buildout requires on the order of **\$2 trillion in new annual revenue by 2030**, against a current shortfall of roughly **\$500 billion**.

<div h-2 />

Meanwhile, the enterprise picture is less dramatic than either the hype or the doom: in 2026, about **37%** of surveyed organisations reported a positive EBIT impact from AI — essentially flat against the previous year.

---

# What You Pay, and What You Get

<div h-2 />

<Chart name="price-performance" width="700px" />

<div h-2 />

<div class="grid grid-cols-3 gap-5 text-center">

<div>

**Cheap models are extremely cheap.** The cheapest model scoring above index 40 costs **\$0.33** per million tokens.

</div>

<div>

**The last points are extremely expensive.** The best model costs **\$30.00** — **92×** more, for 11 points.

</div>

<div>

**Open weights own the cheap half.** Of the 9 models on the efficiency frontier, **6 are open-weight**; the top 3 are all closed.

</div>

</div>

<div h-2 />

<div class="text-base color-gray">
Artificial Analysis Intelligence Index against list price, 145 models ranked under the current index version.
</div>

---

# Wright's Law

<div h-2 />

In 1936 Theodore Wright was analysing aircraft manufacturing and found something that has since held across a surprising range of industries:

<div h-2 />

<div text-center text-2xl color-blue>

Every doubling of cumulative production drops unit cost by a constant percentage.

</div>

<div h-2 />

| Industry | The learning rate |
| --- | --- |
| Aircraft airframes | ~15–20% per doubling |
| Solar photovoltaic modules | ~20% per doubling — the famous one |
| Lithium-ion batteries | ~15–20% per doubling |
| **Frontier AI inference** | **not established** |

---

# The Densing Law

<div h-2 />

Wright's law is about price. A 2025 paper proposed the parameter-side analogue:

<div h-2 />

<div text-center text-2xl color-blue>
The number of parameters needed to reach a fixed level of capability halves roughly every 3.5 months.
</div>

<div h-2 />

| | |
| --- | --- |
| Authors | Xiao and colleagues — Tsinghua, ModelBest, OpenBMB |
| Published | *Nature Machine Intelligence* 7(11):1823–1833, November 2025 |
| The quantity | **capability density** ρ — the parameters a *reference* model would need to match a given score, divided by the parameters actually used |

---

# Learning With AI: The Evidence Is Uncomfortable

<div h-2 />

<div class="grid grid-cols-2 gap-7">

<div>

<Chart name="education-rct" width="100%" />

</div>

<div>

Two preregistered randomised trials, and they disagree about **tool design**.

| Study | Result |
| --- | --- |
| **Kestin et al.** — purpose-built physics tutor | median post-test **4.5** vs 3.5 for active learning, 2.75 for lecture |
| **Dell'Acqua et al.** — consultants on real work | **+12%** tasks, **+25%** faster, but **−19% correctness** outside the AI's capability frontier |

</div>

</div>

---

# So What Kind of Learner Should You Be? (1)

<div h-3 />

### **First: be a user who understands the mechanism**

<div h-3 />

If you know *why* attention replaced recurrence — parallelism, path length, weak inductive bias — you can tell which of today's architectural claims are real and which are marketing. If you only know the API, you cannot.

<div h-3 />

### **Second: rebuild your knowledge as the field moves**

<div h-3 />

The five paradigms in Act I each made the previous generation's expertise partly obsolete — and each reused its infrastructure. The people who survived the transitions were not the ones who had memorized the most; they were the ones who could re-learn a field in a year.

<div h-3 />

---

# So What Kind of Learner Should You Be? (2)

<div h-2 />

### **Third: be someone who can hold up a system**

<div h-2 />

Every result in Act II rests on infrastructure: clusters, interconnects, power, schedulers, storage, and the numerical care that keeps a large training run from diverging.

Look at the evidence in this talk again — the selection bottleneck, the ranking failure, the verification gap. **All of them are systems problems.** The field is not short of people who can call an API. It is short of people who can make a thousand accelerators agree on an answer.

<div h-2 />

### **Fourth: keep scientific taste**

The A-Lab claimed 78% and audited at 5%. A weather model was better than physics on reanalysis and worse on observations. A model scored 74% on one benchmark and 11% on the next.

None of these were fraud. They were all cases of **measuring the wrong thing honestly**.

<div h-2 />

---

# Where Does the Next Paradigm Come From?

<div h-3 />

| Candidate | Why it might be the next paradigm | Why it might not |
| --- | --- | --- |
| **Verification as a training signal** | RL on formally checkable rewards is the one place where capability is still improving steeply and the signal cannot be gamed | It only works where a checker exists. That is mathematics, code, and not much else. |
| **Test-time compute** | A genuinely new scaling axis, orthogonal to model size | The 2026 result: the bottleneck is *selection*, not generation. Nobody has solved selection. |
| **Agentic research systems** | Thousands of parallel agents already resolved open problems | Credit, provenance, and verification are unsolved — and the field is visibly arguing about them |
| **New architectures** | Every wall so far has been broken by an architecture | In 2026, no frontier model is not a Transformer. Every change is a patch. |
| **Something nobody is working on** | This is how it has always happened | You cannot plan for it — you can only be the kind of person who notices it |

<div h-3 />

---

# What to Take Away

<div h-4 />

<div class="text-xl leading-relaxed">

- AI has had **five paradigms**, and each one ended in the same place: the structure stopped changing, the work turned to refinement — and refinement built the instruments for the next leap.
- The current paradigm is **not finished**, but it has visibly entered its refinement phase. That is not a reason for pessimism. It is a description of where the interesting work is.
- **Generation is ahead of verification** in every field we looked at. Producing candidates is cheap; deciding which candidate is right is the part that is still hard.
- The people who matter in the next transition will be the ones who **understand the mechanism**, who can **rebuild their knowledge**, who can **hold up a system**, and who can tell **an honest measurement from a flattering one**.

</div>

<div h-4 />

---
layout: center
---

<div h-20 />

<div text-center text-6xl>
Questions
</div>

<div h-20 />
