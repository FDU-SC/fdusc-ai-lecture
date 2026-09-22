# Three Things Have to Line Up

<div h-2 />

Every era is a negotiation between **data**, **algorithm**, and **model plus compute**.

<div h-2 />

| Era | Data | Algorithm | Model & compute | Missing |
| --- | --- | --- | --- | --- |
| **1958** Perceptron | ✗ thousands | ✓ a learning rule | ✗ valves | data, compute |
| **1970s** Expert systems | — unused | ✗ hand-written rules | — | nothing was learned |
| **1986** Backprop | ✗ thousands | ✓ backprop | ✗ CPU-weeks | data, compute |
| **1995** Statistical learning | ~ the web arrives | ✓ SVM, kernels | ~ CPUs | features |
| **2012** Deep learning | ✓ 14M images | ✓ ReLU, dropout | ✓ two GPUs | nothing |
| **2017** Transformers | ✓ the internet | ✓ attention | ✓ clusters | nothing |

---
layout: center
---

# Seventy Years, Five Paradigms

<Chart name="paradigm-timeline" width="900px" />

---

# The Bitter Lesson

<div h-3 />

Rich Sutton, 2019. The argument in one paragraph:

<div h-2 />

<div text-center text-2xl color-blue>
General methods that exploit computation beat methods that encode human knowledge — and they win eventually, every time.
</div>

<div h-3 />

| Domain | What people encoded by hand | What actually won |
| --- | --- | --- |
| Chess | Grandmaster heuristics, opening books | Self-play plus search |
| Go | Human joseki, expert patterns | Self-play plus search |
| Speech | Phonemes and pronunciation rules | Learned acoustic models |
| Vision | SIFT, HOG, hand-designed features | Learned convolutional features |
| Language | Grammars, parse trees, ontologies | Predict the next token |

<div h-3 />

A method that encodes knowledge also encodes a ceiling. A method that searches does not.

---

# The Fundamental Tradeoff

| | Rule-based systems | Learned systems |
| --- | --- | --- |
| **What you need** | Expert hours | Data and compute |
| **Cost of 2× coverage** | Roughly 2× the experts | Roughly a constant, once the pipeline exists |
| **Trend over 30 years** | Expert time got **more** expensive | Compute got **exponentially** cheaper |
| **Failure mode** | Brittle, silent, unmaintainable | Wrong confidently, and hard to audit |
| **What it cannot express** | Anything nobody wrote down | Anything absent from the data |

---
layout: center
---

<div h-24 />

<div text-center text-6xl>

<span color-gray>Prologue</span>

</div>

<div h-3 />

<div text-center text-4xl>

1943 – 1969

</div>

<div h-24 />

---

# Prologue: Four Ideas That Started Everything

<div h-3 />

| Year | Who | What |
| --- | --- | --- |
| **1943** | McCulloch & Pitts | A logical calculus of nervous activity — neurons as threshold logic gates |
| **1950** | Alan Turing | *Computing Machinery and Intelligence* — the "imitation game" |
| **1955** | McCarthy, Minsky, Rochester, Shannon | The Dartmouth proposal — the phrase *artificial intelligence* first appears here. The summer workshop follows in 1956. |
| **1958** | Frank Rosenblatt | The Perceptron — the first model that **learns** its parameters from data |

<div h-3 />

The Dartmouth proposal asked for a **two-month, ten-person study**, on the premise that:

<div h-2 />

<div text-center text-2xl color-blue>

"Every aspect of learning ... can in principle be so precisely described that a machine can be made to simulate it."

</div>

---

# Prologue: The Script Writes Itself

<div h-3 />

| Year | Event | What followed |
| --- | --- | --- |
| 1958 | The perceptron learns to classify; the press reports it will soon walk, talk, and reproduce | Hype |
| 1958 | Simon & Newell predict a machine will be world chess champion within ten years | Overpromise |
| 1966 | The ALPAC report ends machine-translation funding | Funding cut |
| 1969 | Minsky & Papert, *Perceptrons*: a **single-layer** perceptron cannot compute XOR | Theoretical limit |
| 1973 | The Lighthill report questions whether AI has delivered anything | Retrenchment |

---
layout: center
---

<div h-24 />

<div text-center text-6xl>

<span color-gray>Paradigm 1</span>

</div>

<div h-3 />

<div text-center text-4xl>

Symbolic AI & Expert Systems

</div>

<div h-3 />

<div text-center text-2xl color-gray>

1969 – 1987

</div>

<div h-24 />

---

# Paradigm 1: The Knowledge Is Typed In as Rules

<div h-3 />

<div text-center text-2xl color-blue>

An expert's knowledge is written down as **if-then rules**. The machine fires them, chains the conclusions, and arrives at an answer.

</div>

<div h-3 />

<div h-2 />

- **Knowledge was the bottleneck, not compute.** Medicine and chemistry had expert knowledge that was already written down in textbooks and manuals.
- **Hardware made it affordable.** Dedicated LISP machines (Symbolics, LMI) appeared in the late 1970s, and companies could buy the capability outright.
- **The problems chosen were narrow and high-value.** Diagnosis, configuration, scheduling — small closed worlds where rules really are enough.

---

# Paradigm 1: The Expert Systems

<div h-3 />

| System | What it did |
| --- | --- |
| **DENDRAL** (1965) | read molecular structures off a mass spectrum |
| **MYCIN** (1970s) | diagnosed blood infections from about 600 rules |
| **XCON** (1980, at DEC) | configured VAX computer orders from over 3,000 rules |
| **Cyc** (1980s) | tried to hand-code common sense itself, assertion by assertion |
| **Fifth Generation** (1982–92) | Japan's national bet on parallel inference machines |

---

# What a Rule Looked Like

<div h-2 />

<div class="grid grid-cols-2 gap-6">

<div>

<Chart name="xcon-rules" width="100%" />

</div>

<div>

An expert system was a decision tree written out in English, one rule at a time.

<div h-2 />

<div class="text-base leading-relaxed">

**IF** the ordered memory is larger than 8 MB<br>
**AND** the CPU is a VAX-11/780<br>
**THEN** add a memory cabinet

<div h-2 />

**IF** a memory cabinet was added<br>
**AND** the power budget is already at 90%<br>
**THEN** add a second power supply

</div>

</div>

</div>

---

# Paradigm 1: Where It Stopped Working

<div h-3 />

Rules had to be extracted from human experts, one at a time, by a person whose job title was *knowledge engineer*.

<div h-2 />

- **It did not scale.** Doubling a system's competence meant roughly doubling its rules — and the rules began to conflict.
- **Common sense was not in the books.** Everyday reasoning needs an enormous amount of background knowledge that nobody had ever written down.
- **It did not handle the world.** Rules assumed a closed world; the real world has exceptions, missing data, and ambiguity.
- **It was brittle.** MYCIN outperformed the human prescribers in a blinded test and was **still never used on patients**. Systems that looked impressive in a demo failed in an office.

<div h-2 />

The remaining years went into tooling: certainty factors, rule editors, knowledge-representation languages, and inference engines sold as products.

---

# Paradigm 1: What It Left Behind

<div h-3 />

| Contribution | Where it went |
| --- | --- |
| **Knowledge representation** as a field | Ontologies, description logics, the Semantic Web, and eventually knowledge graphs |
| **Uncertainty in reasoning** | Bayesian networks, probabilistic graphical models — the foundations of Paradigm 3 |
| **The LISP machine industry** | Eroded from 1987 onward; Symbolics filed for bankruptcy in 1993 |
| **A generation of engineers** | Released into the next paradigm |

---
layout: center
---

<div h-24 />

<div text-center text-6xl>

<span color-gray>Paradigm 2</span>

</div>

<div h-3 />

<div text-center text-4xl>

Backpropagation & Connectionism

</div>

<div h-3 />

<div text-center text-2xl color-gray>

1986 – 1995

</div>

<div h-24 />

---

# What Training Actually Is

<div h-2 />

Every model in this deck — the 1958 perceptron and a 2026 frontier model — is doing the same thing:

<div h-2 />

<div text-center text-2xl color-blue>
Adjust the parameters until the average penalty over the training data stops falling.
</div>

<div h-2 />

| Piece | What it is |
| --- | --- |
| **A parameter** | One number inside the model. GPT-3 holds 175 billion of them. |
| **A loss function** | A score for how wrong one prediction was |
| **The training loss** | That score averaged over the dataset. One number. |
| **Training** | Searching for parameters that make that one number small |

---

# Paradigm 2: The Weights Come From the Examples

<div h-3 />

<div text-center text-2xl color-blue>

You supply examples and a way to measure error. The network adjusts its own weights until that error falls — and whatever it learned ends up encoded in those weights.

</div>

<div h-3 />

<div h-2 />

- **1982 — Hopfield networks** connected neural networks to physics: a network settles into low-energy states, and memory is an attractor.
- **1986 — backpropagation**, popularised by Rumelhart, Hinton & Williams, made multi-layer networks trainable.
- **The credit assignment problem was solved.** Training needs only the final label; the intermediate steps are never specified.

---

# Hopfield Networks: Learning Becomes Optimization

<div h-2 />

<div text-center>

$$
E = -\frac{1}{2}\sum_{i \neq j} w_{ij}\, s_i s_j + \sum_i \theta_i s_i
$$

</div>

<div h-2 />

<Chart name="hopfield" width="820px" />

<div h-2 />

Each unit flips if that **lowers** the energy, so the network always settles into a local minimum. Stored patterns become **attractors**: present a corrupted pattern and the dynamics fall into the nearest stored memory.

---

# From Perceptron to Hidden Layers

<div h-2 />

<Chart name="xor" width="750px" />

<div h-2 />

**1969.** Minsky & Papert proved that a single perceptron cannot compute XOR. The field read it as a verdict on the whole approach; it was a verdict on **one layer**.

---

# Paradigm 2: The Networks

<div h-3 />

| System | What it did |
| --- | --- |
| **Neocognitron** (1980) | the first network built on local receptive fields and shared weights |
| **LeNet** (1989–98) | read handwritten digits, and shipped in real cheque-reading machines |
| **TD-Gammon** (1992) | reached world-class backgammon by playing itself |
| **Speech recognisers** (1990s) | neural networks replaced template matching in several systems |

---

# What the Network Was Doing

<div h-2 />

<Chart name="lenet" width="900px" />

<div h-2 />

Nothing in LeNet knows what a digit is. It knows how to slide a small filter across an image and keep what changes. Stack enough of those, and the last layer can tell a 3 from an 8 — using about 60,000 numbers.

---

# Paradigm 2: Where It Stopped Working

<div h-3 />

- **Vanishing gradients.** With saturating activations, gradients shrink multiplicatively with depth. Diagnosed in Hochreiter's 1991 thesis and analysed formally by Bengio and colleagues in 1994: gradients are multiplied at every step, so they shrink or explode by construction. Deep networks could not be trained.
- **There was no data.** ImageNet did not exist. Datasets had thousands of examples, not millions.
- **There was no compute.** Training a useful network meant weeks of CPU time.
- **A better-funded rival appeared.** Support vector machines had a convex objective, a unique solution, and theoretical guarantees. They simply won the benchmarks.

<div h-2 />

**LSTM** (Hochreiter & Schmidhuber, 1997) came out of this period: a gated memory cell that solved the vanishing gradient for sequences. Input and output gates at first, with the forget gate added in 2000.

---

# Paradigm 2: What It Left Behind

<div h-3 />

| Component | Built when | Paid off when |
| --- | --- | --- |
| **Backpropagation** | 1970s–1986 | Never stopped being used |
| **Convolution + weight sharing** | 1980–1989 | AlexNet, 2012 |
| **Gated recurrence (LSTM)** | 1997 | Speech and translation, 2014–2016 |
| **The idea of learned representation** | 1986 | Everything after 2012 |

---
layout: center
---

<div h-24 />

<div text-center text-6xl>

<span color-gray>Paradigm 3</span>

</div>

<div h-3 />

<div text-center text-4xl>

Statistical Learning

</div>

<div h-3 />

<div text-center text-2xl color-gray>

1995 – 2012

</div>

<div h-24 />

---

# Paradigm 3: The Error Is Bounded Before You Train

<div h-3 />

<div text-center text-2xl color-blue>

Vapnik's theory puts a **bound** on how wrong a model can be on data it has never seen, computed from the model's capacity and the number of samples. The bound is available before training starts.

</div>

<div h-3 />

<div h-2 />

- **The theory arrived.** Vapnik's VC theory gave a bound on generalization error in terms of capacity and sample size. Learning became a branch of statistics with theorems.
- **Kernel methods made it practical.** The kernel trick let a linear method operate in an extremely high-dimensional space without ever computing the embedding.
- **The internet arrived.** For the first time there was more data than any previous method could use.

---

# Overfitting, and Why More Data Wins

<div h-2 />

<Chart name="bias-variance" width="580px" />

<div h-2 />

Total error is **bias** (how wrong the model is on average) plus **variance** (how much it changes when you resample the data). Push one down and the other tends to rise — which is why there is a best level of flexibility rather than a maximum.

<div h-2 />

- **Regularization** is anything that stops the model using its full freedom: weight decay, dropout, early stopping.
- **A held-out set is not optional.** Every claim about a model is a claim about data it never saw.

---

# Paradigm 3: The Methods

<div h-2 />

| Year | Result |
| --- | --- |
| 1988 | **Bayesian networks** (Pearl) — uncertainty with a principled calculus |
| 1995 | **Support-vector networks** (Cortes & Vapnik) — the dominant classifier for fifteen years |
| 1997 | **Deep Blue beats Kasparov** — the symbolic era's most public win |
| 2001 | **Random forests** (Breiman) — ensembles beat single models, reliably |
| 2006 | **Deep belief networks** (Hinton & Salakhutdinov) — deep networks come back |

---

# Paradigm 3: Where It Stopped Working

<div h-3 />

Every statistical method assumed that a human had already turned the raw input into a good vector of features.

<div h-2 />

- **Features were hand-made, per task.** A vision pipeline needed edge detectors, then corner detectors, then descriptors — each designed by a specialist.
- **Progress was measured in descriptors, not in learning.** SIFT, HOG, and their successors were the real state of the art.
- **Kernel methods did not scale.** Training is quadratic in the number of samples; the internet was producing more samples than that allowed.
- **The ceiling was human imagination.** You cannot hand-design a feature for a concept you cannot name.

<div h-2 />

The practice got industrialised: scikit-learn, cross-validation as a reflex, regularization, model selection, and Kaggle as a global benchmark culture.

---

# Paradigm 3: What It Left Behind

<div h-3 />

| Contribution | Where it is now |
| --- | --- |
| **Train / validation / test discipline** | Non-negotiable. The reason benchmark contamination is a scandal. |
| **Regularization** | Weight decay, early stopping, dropout's intellectual ancestors |
| **The kernel view of learning** | Still the cleanest theory of why overparameterized models generalize |
| **Probabilistic graphical models** | Causal inference, and the language of modern generative modelling |
| **Three people who never stopped** | LeCun, Hinton, Bengio — the 2018 Turing Award, for work done while the field looked elsewhere |

---
layout: center
---

<div h-24 />

<div text-center text-6xl>

<span color-gray>Paradigm 4</span>

</div>

<div h-3 />

<div text-center text-4xl>

Deep Learning

</div>

<div h-3 />

<div text-center text-2xl color-gray>

2012 – 2017

</div>

<div h-24 />

---

# Paradigm 4: The Network Builds the Features Too

<div h-3 />

<div text-center text-2xl color-blue>

A deep network constructs its own features, one layer at a time: edges, then strokes, then whole objects. A human designs the architecture, and the features come out of the data.

</div>

<div h-3 />

<div h-2 />

<div class="grid grid-cols-3 gap-4 text-center">

<div>

### Data

**ImageNet**, from 2009

Over **14 million** labelled images across more than 20,000 categories <span color-gray>(the 2014 release; the 2009 paper launched with 3.2 million)</span>

</div>

<div>

### Compute

**GPUs**

A graphics card is a matrix-multiply engine

<span color-gray>3 GB of memory was suddenly enough</span>

</div>

<div>

### Algorithm

**ReLU, dropout, better initialization**

Fixes for the vanishing gradient that Paradigm 2 never solved

</div>

</div>

---

# A Different Kind of Generation

<div h-2 />

Classification asks *which class?* Detection asks *where?* Generation asks **what would a sample from this data look like?**

<div h-2 />

| Approach | The idea | Year |
| --- | --- | --- |
| **GAN** | a generator and a discriminator train against each other | 2014 |
| **Diffusion** | learn to reverse a noising process, one step at a time | 2020 |
| **Latent diffusion** | the same process in a compressed space, which made it cheap | 2022 |
| **Transformer backbone** | replace the U-Net, and quality scales with compute | 2022 |

<div h-2 />

DDPM reached **FID 3.17** on CIFAR-10 in 2020 — against the *training* set; against the test set it is 5.24.

---

# Before 2012: What a Vision System Was

<div h-2 />

| Stage | Typical choice |
| --- | --- |
| Find interesting points | SIFT, LBP, HOG |
| Describe each patch | SIFT descriptors, Fisher vectors |
| Encode them | sparse coding, vector quantisation |
| **Classify** | a linear SVM — the only learned part |

<div h-2 />

Every stage was a human decision, and each one had to be made again for a new domain. The 2010 and 2011 ImageNet winners were exactly this.

---

# Six Years

<div h-2 />

<Chart name="imagenet-error" width="880px" />

<div h-2 />

<div class="text-base color-gray">

ILSVRC top-5 classification error, official test-set results. From 2012 on, the headline entry is an ensemble; 2016–17 are the classification column of the combined localisation task.

</div>

---

# The Architectures, One After Another

<div h-2 />

<Chart name="arch-params" width="720px" />

<div h-2 />

Three answers to one question: how do you get more accuracy out of the parameters you already have? VGG got bigger. GoogLeNet got smaller and matched it. ResNet got deeper at the same size.

---

# The Tasks Fell in Order

<div h-2 />

| Task | Before deep learning | After |
| --- | --- | --- |
| **Classification** — what is this? | 26% error (2011) | **3.6%** by 2015 |
| **Detection** — where is each object? | ~33 mAP | **73.2** mAP |
| **Segmentation** — which pixels? | hand-built per-class pipelines | **85.7** mIoU |
| **Generation** — make a new one | — | FID **3.17** on CIFAR-10 |
| **Recognition** — is this the same face? | far below human | **99.63%** on LFW |

<div h-2 />

Each row is the previous row's model pointed at a harder question. Detection is classification on candidate boxes; segmentation is classification on every pixel.

---

# Vision Went Everywhere

<div h-2 />

The lasting export of the decade was not a network. It was a **workflow**: pretrain on a huge generic dataset, fine-tune on your small specific one.

<div h-2 />

| Direction | What the recipe did |
| --- | --- |
| **Transfer** | ImageNet features worked on images that look nothing like ImageNet |
| **Medicine** | Models reached specialist agreement on narrow tasks; approval became the bottleneck |
| **Industry** | Inspection and defect detection, where labelled data is scarce |
| **Language** | BERT is this same recipe applied to text |

---

# Paradigm 4: Where It Stopped Working

<div h-3 />

- **Architecture search hit diminishing returns.** After ResNet, the next ImageNet win came from more data and more compute, not from a new idea.
- **The gains came from scale, not structure.** This was noticed, and it changed what people worked on.
- **Sequence modelling was stuck.** RNNs and LSTMs were the state of the art for language, but they process one token at a time and cannot be parallelised across a sequence.
- **The bottleneck moved.** Vision was solved well enough; language was not, and language could not be brute-forced with the tools of 2016.

<div h-2 />

The remaining years went into engineering: batch normalization, better optimizers, initialization schemes, data augmentation, transfer learning, and the whole toolchain of a deep-learning framework.

---

# Paradigm 4: What It Left Behind

<div h-3 />

| Contribution | Consequence |
| --- | --- |
| **End-to-end training** | The default. Nobody builds pipelines of hand-designed stages any more. |
| **The GPU cluster** | Not just hardware — an entire operational discipline of distributed training |
| **ImageNet as a method** | Large, labelled, public benchmarks became how the field measures itself |
| **The belief that scale produces qualitative change** | The premise of Paradigm 5 |
| **Attention** | Invented in 2014 for translation. Three years later it was the whole architecture. |

---
layout: center
---

<div h-24 />

<div text-center text-6xl>

<span color-gray>Paradigm 5</span>

</div>

<div h-3 />

<div text-center text-4xl>

Transformers & Scale

</div>

<div h-3 />

<div text-center text-2xl color-gray>

2017 –

</div>

<div h-24 />

---

# Paradigm 5: One Matrix Multiplication, Then Scale

<div h-3 />

<div text-center text-2xl color-blue>

A sequence is processed as **one matrix multiplication**: every position is computed at once. That is what let the models grow to their current size.

</div>

<div h-3 />

<div h-2 />

- **Attention is parallel.** Every position attends to every other position at the same time, in one batched matrix product. Nothing waits on anything else.
- **That made the whole internet usable as training data.** Unlabelled text became a supervised signal: predict the next token.
- **Scaling laws made size a plan, not a gamble.** Kaplan et al. (2020) showed loss falls as a predictable power law, and recommended very large models on comparatively little data. Chinchilla (2022) corrected the recipe: parameters and tokens should grow together, at roughly **20 tokens per parameter**.
- **The compute existed**, because the same GPUs that trained AlexNet had been improving for eight years.

---

# Attention: The Decisive Advantage Is Parallelism

<div h-3 />

An RNN must compute step *t* before step *t+1*. That is 1,000 dependent operations for a 1,000-token sequence.

<div h-3 />

<div text-center text-2xl color-blue>
Self-attention computes all positions at once.
</div>

<div h-3 />

$$
\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

<div h-3 />

- Every token builds its query, key and value with one matrix multiply.
- The whole sequence is then **one batched matrix product** — the exact operation GPUs are built for.
- Attention does *more* total arithmetic than an RNN (it is quadratic in sequence length), but the wall-clock time is far lower because the hardware is never idle.

<div h-3 />

---

# Attention: Every Pair Is One Hop

<div h-2 />

<Chart name="attention-paths" width="840px" />

<div h-2 />

| Architecture | Distance between any two positions |
| --- | --- |
| RNN / LSTM | **O(n)** — information passes through every step in between |
| CNN | **O(log n)** with dilation, **O(n)** otherwise |
| Self-attention | **O(1)** — every pair is one hop |
---

# Text Becomes Numbers

<div h-2 />

A model never sees text. It sees a sequence of integers.

<div h-2 />

| Step | Example |
| --- | --- |
| Raw text | `Tokenization is unglamorous.` |
| Split into **tokens** | `Token` · `ization` · ` is` · ` un` · `glam` · `orous` · `.` |
| Mapped to integers | 30642 · 2065 · 374 · 659 · 26547 · 1121 · 13 |
| What the model predicts | one probability per vocabulary entry, at every position |

<div h-2 />

- **Counting and spelling are hard.** `9`, ` 9` and `nine` can be different tokens, and the model never sees individual characters.
- **Some languages cost more.** The same sentence can take several times as many tokens in a language with less training data.
- **The loss is per token, not per word.** A scaling-law exponent measured in tokens is a different curve from one measured in characters.

---

# Paradigm 5: The Milestones

<div h-2 />

| Year | Milestone | The number |
| --- | --- | --- |
| 2017 | **Attention Is All You Need** | June 2017; no recurrence, no convolution |
| 2018 | **BERT / GPT-1** | Pre-train, then fine-tune |
| 2020 | **GPT-3** | 175B parameters; few-shot learning without gradient updates |
| 2022 | **Chinchilla** | Most models were badly under-trained on data |
| 2022 | **ChatGPT** | 30 November 2022 |
| 2023 | **GPT-4** | Multimodal, and almost nothing disclosed about it |
| 2024– | **Reasoning models** | Test-time compute becomes a second scaling axis |

---

# Scaling Laws: Loss Falls as a Power Law

<div h-2 />

### 2020 — Kaplan et al.

Loss falls as a **power law** in model size, dataset size and compute. You could predict the loss of a model you had not trained yet.

<div h-2 />

### 2022 — Chinchilla corrects the recipe

For a fixed compute budget, parameters and tokens should grow **together** — at roughly **20 tokens per parameter**. By that standard GPT-3 was badly under-trained: Chinchilla had **70B** parameters and beat models up to **530B**.

<div h-2 />

### After Chinchilla

Models are now deliberately trained **far past** that point — Llama 3's 8B saw about **1,800 tokens per parameter** — because once training ends, inference cost dominates.

---

# The Data Grew Too

<div h-2 />

<Chart name="data-growth" width="780px" />

<div h-2 />

The same model family that saw 40 GB of web text in 2019 saw 15 trillion tokens in 2024. This is the third thread, and it moved as fast as the other two.
---

# The Recipe Change, Measured

<div h-3 />

<div class="grid grid-cols-2 gap-8">

<div>

<Chart name="chinchilla-shift" width="100%" />

</div>

<div>

### The paper said: 20 tokens per parameter

<div h-2 />

### The field, measured across 458 models:

<div h-2 />

<div text-center>

<div class="text-2xl color-gray">Before 2022</div>
<div class="text-5xl color-red">1.1</div>
<div class="text-sm color-gray">tokens per parameter (median)</div>

<div h-3 />

<div class="text-2xl color-blue">After 2022</div>
<div class="text-5xl color-blue">21.5</div>
<div class="text-sm color-gray">tokens per parameter (median)</div>

</div>

</div>

</div>

<div h-3 />

---

# Paradigm 5: What the Numbers Say

<Chart name="params-capability" width="905px" />

---

# The Model Learns From the Prompt

<div h-2 />

Somewhere between GPT-2 and GPT-3, models started doing something nobody had designed them to do.

<div h-2 />

<div text-center text-2xl color-blue>

Give a model a few examples of a task inside the prompt, and it performs the task — with no change to any weight.

</div>

<div h-2 />

| | Fine-tuning | In-context learning |
| --- | --- | --- |
| Where the task lives | in the weights | in the prompt |
| What it costs | a training run | tokens |
| How many examples | thousands | a handful |

<div h-2 />

Nothing in the training objective says "infer the task from the context". The objective is **predict the next token**, and in-context learning is a side effect of getting good at it.

---

# Compute Is Not Following Moore's Law

<div h-2 />

<Chart name="compute-vs-moore" width="790px" />

<div h-2 />

<div class="grid grid-cols-3 gap-6 text-center">

<div>

<div text-base color-orange>Moore's law</div>
<div text-2xl>2× / 24 months</div>

</div>

<div>

<div text-base color-blue>Notable-model compute</div>
<div text-2xl>2× / 5.6 months</div>

</div>

<div>

<div text-base color-red>Gap by 2026</div>
<div text-2xl>~10⁷×</div>

</div>

</div>

<div h-2 />

<div text-center text-base color-gray>
Epoch AI notable-models table: 538 models with disclosed training compute; trend fitted on 2012–2026.
</div>

---

# Why the Hardware Shapes the Algorithm

<div h-3 />

| Era | Hardware | The number that mattered |
| --- | --- | --- |
| 1970s–2005 | CPU, Moore's law | Clock speed, until it stopped in 2005 |
| 2007–2012 | CUDA makes GPUs programmable | Matrix multiply becomes cheap |
| 2012 | **AlexNet on two GTX 580s** | 3 GB of memory per card was enough |
| 2016–2017 | **Tensor cores**; Google's TPU | Mixed precision: FP16 with FP32 accumulation |
| 2020–2022 | A100 → H100 | **FP8** training; HBM bandwidth becomes the limit |
| 2024–2026 | B200 → Rubin; 72-GPU racks | **FP4**; the rack, not the chip, is the unit |

<div h-3 />

### Three walls, in order of arrival

<div h-3 />

- **The memory wall.** Arithmetic is fast; moving data is slow. This is why attention variants are judged on memory traffic, not FLOPs.
- **The communication wall.** Beyond one node, the interconnect dominates. Hence rack-scale designs that keep 72 accelerators in one domain.
- **The power wall.** A rack now draws what a small factory drew. Power procurement, not silicon, is the binding constraint on scaling.

<div h-3 />

---

# Why Parallelism Has a Ceiling

<div h-2 />

<div class="grid grid-cols-2 gap-6">

<div>

<Chart name="roofline" width="100%" />

</div>

<div>

### Amdahl's law (1967)

$$
S(N) = \frac{1}{s + \dfrac{p}{N}}
$$

If a fraction *p* of the work parallelises and *s* does not, no number of processors gets past *1/s*.

| Serial fraction | Best speedup | Processors to get within 10% |
| --- | --- | --- |
| 5% | 20× | ~200 |
| 1% | 100× | ~1,000 |
| 0.1% | 1,000× | ~10,000 |

</div>

</div>

---

# Post-Training: From Fluent to Useful

<div h-3 />

Pre-training produces a model that continues text. It does not produce one that answers.

<div h-3 />

| Stage | Signal | What it teaches |
| --- | --- | --- |
| **Pre-training** | Next token, from raw text | Language, facts, and a great deal of structure |
| **SFT** | Human-written demonstrations | The *format* of an answer |
| **RLHF** | A reward model learned from human preferences | Which answers people actually prefer |
| **RLVR** | A program that checks the answer | How to *reason* toward a verifiable result |

<div h-3 />

<div h-3 />

Reinforcement learning from **verifiable** rewards needs no reward model and no human in the loop. A maths answer is right or wrong. A program passes or fails its tests. That means you can generate millions of training problems and let the model try, fail, and improve — automatically.

<div h-3 />

---

# From Answering to Thinking

<div h-2 />

Pre-training taught a model to continue text. Post-training taught it to answer. The next shift taught it to **work through a problem**.

<div h-2 />

| Step | What changed | When |
| --- | --- | --- |
| **Chain of thought** | write the reasoning before answering, and accuracy jumps — with no training at all | 2022 |
| **Reasoning models** | train it to produce those traces, with RL on problems whose answer can be checked | 2024 |
| **Test-time compute** | let it think longer at inference; accuracy scales with thinking time, not only model size | 2024– |

<div h-2 />

A transformer does a **fixed amount of computation per token**, so writing intermediate steps gives it more computation to reach an answer. It only works where a **checker exists** — maths and code took off fastest because a program can verify the result.

---

# Evaluation: Benchmarks Saturate, and Then Break

<div h-2 />

<Chart name="benchmark-saturation" width="840px" />

<div h-2 />

<div class="grid grid-cols-3 gap-4 text-center">

<div>

**Contamination**

The test set leaked into training data. Models that scored 100% on AIME 2025 scored lower on the unseen 2026 paper.

</div>

<div>

**Saturation**

Everyone reaches the ceiling, so the benchmark stops discriminating. GPQA is nearly there; HLE is not.

</div>

<div>

**Broken grading**

The tests themselves are wrong. An audit of SWE-bench Verified found a majority of sampled tasks rejected correct patches.

</div>

</div>

<div h-3 />

---

# Goodhart's Law

<div h-2 />

| Source | Statement |
| --- | --- |
| **Goodhart** (1975) | "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." |
| **Strathern** (1997), the popular form | "When a measure becomes a target, it ceases to be a good measure." |
| **Hoskin** (1996) | The form above is usually attributed to Goodhart, but Hoskin published that wording first |

---

# The Shape of the Cycle

<div h-2 />

<Chart name="paradigm-cycle" width="880px" />

<div h-2 />

<div class="text-base color-gray">

The vertical axis is illustrative, not measured. The claim is about the shape; the dates are the historical record.

</div>

---

# Paradigm 5: Are We Still in the Rush?

<div h-2 />

<div class="grid grid-cols-2 gap-8">

<div>

### Still in the rush

- Reasoning models opened a new scaling axis, and RL on verifiable rewards is still improving fast
- Agents went from unusable to economically useful in about two years
- New frontier models still appear every few weeks

</div>

<div>

### Entered refinement

- **No new architecture since 2017.** Mixture-of-experts, sparse attention, hybrid layers — all modifications, not replacements.
- Training compute is no longer disclosed. Nobody publishes the recipe.
- Benchmark scores saturate in months, then the benchmark is retired.

</div>

</div>
