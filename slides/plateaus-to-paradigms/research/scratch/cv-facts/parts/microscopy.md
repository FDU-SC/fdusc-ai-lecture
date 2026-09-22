# ImageNet-pretrained vision backbones transferred to MICROSCOPY / cell & tissue imaging

Compiled 2026-09-19. Scope: microscopy only (histopathology, fluorescence, EM, cell/nucleus
segmentation & classification). Radiology/CT/X-ray transfer studies are explicitly excluded
(one is flagged as out-of-scope at the bottom).

**Method note on evidence quality.** Numbers below are tagged by how I obtained them:

- **READ-TABLE** = I read the number in the paper's own results table / results text, retrieved as
  machine-readable full text (NCBI BioC API for PMC open-access articles, or arXiv/ar5iv HTML).
- **READ-ABSTRACT** = I read it in the paper's own abstract (publisher/PubMed metadata, verbatim).
- **UNVERIFIED** = I could not reach the paper's own text; do not quote.

PDFs are **not retrievable by the fetch tool used here** (`unsupported content type
"application/pdf"`), and several publishers (nature.com, link.springer.com,
sciencedirect, IEEE Xplore) redirect to auth walls. That is the main reason two of the
requested papers (Spanhol 2016/2017, Ciresan 2013 numbers) come back unverified.

---

## 1. Results table

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | confidence |
|---|---|---|---|---|---|---|---|---|
| Xu, Jia, Wang, Ai, Zhang, Lai, Chang — "Large scale tissue histopathology image classification, segmentation, and visualization via deep convolutional activation features", *BMC Bioinformatics* 18:281 | 2017 | **AlexNet** (Caffe; the ImageNet LSVRC-2013 "CognitiveVision" model, trained on the full ImageNet); fc2 = 4096-d features; patches resized to 224×224 | **Frozen** (SVM-CNN: fixed CNN features + linear SVM) **and fine-tuned** (SVM-FT) | MICCAI 2014 Brain Tumor Digital Pathology Challenge (GBM vs LGG classification; 45 train / 40 test images) + a colon-cancer dataset from Zhejiang University (717 regions; 355 cancer / 362 normal; 693 for multiclass) | Classification accuracy, **MICCAI brain: SVM-CNN 97.8%** (frozen ImageNet features); **colon binary 98.0%**; **colon multiclass 87.2%**. Segmentation (overlap score): brain SVM-CNN **84.0%**, fine-tuned SVM-FT **84.4%**; colon SVM-CNN **93.2%**, SVM-FT **94.8%** | Hand-crafted features (SIFT+LBP+L\*a\*b histogram, 186-d) + same SVM: **77.8%** brain, 90.1% colon-binary, 75.5% colon-multiclass. Whole-image CNN (no patch pooling): 62.2% / 94.3% / 79.0%. MCIL 91.1% / 95.5%. Segmentation hand-crafted: 64.0% brain, 77.0% colon | https://doi.org/10.1186/s12859-017-1685-x (full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5446756/) | **HIGH** (READ-TABLE, Tables 4 & 6 in the article's own text) |
| Caicedo, Goodman, Karhohs, Cimini, … Carpenter — "Nucleus segmentation across imaging experiments: the 2018 Data Science Bowl", *Nature Methods* 16:1247–1253 | 2019 | Kaggle DSB 2018 winners: 1st place **encoders pretrained on ImageNet** (8 base architectures: ResNet-34/50/101/152, Dual Path Networks, Inception-ResNet, with U-Net or FPN decoders, 32 trained nets); 2nd place FPN backbone **pretrained on ImageNet + COCO**; 3rd place **Mask R-CNN pretrained on COCO** | **Fine-tuned** (all retrained on DSB data) | 2018 Data Science Bowl (BBBC038): 841 images / 37,333 annotated nuclei (train + stage-1); stage-2 holdout 3,200 images, ~100,000 nuclei, 15 unseen experiments; 739 teams in stage 2 | Stage-2 table: 1st [ods.ai] topcoders competition score **0.6316**, average **F1 0.7120**, recall@IoU 0.7 **77.62%**; 2nd Jacobkie 0.6147 / F1 0.6987; 3rd Deep Retina 0.6141 / F1 0.7008 | Classical CellProfiler pipelines (minimally tuned): score **0.5281**, **F1 0.6280**, recall **59.35%**. Also: the authors' own U-Nets trained separately per image group (from scratch, 5 models, ~20 h hand-tuning) "did not reach competitive performance" | https://doi.org/10.1038/s41592-019-0612-7 (full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC6919559/) | **HIGH** (READ-TABLE, Table 1 + results text) |
| Ciga, Xu, Martel — "Self supervised contrastive learning for digital histopathology" (arXiv:2011.13971; journal version in *Machine Learning with Applications*) | 2020 (v1) / 2021 (v2) | **ResNet-18/34/50/101**, compared under three initializations: random, **ImageNet supervised-pretrained**, and SimCLR **self-supervised on 57 unlabeled histopathology datasets** | **Both**: frozen encoder + linear probe / regressor (Table 2) and full fine-tuning (Table 1) | 5 classification sets (BACH 4-class, Lymph 3-class, **BreakHis v1** binary, NCT-CRC-HE-100K 9-class, Gleason2019 5-class); segmentation BACH + DigestPath2019; regression BreastPathQ. Metric = macro-F1 averaged over the 5 classification sets | Fine-tuned, ResNet-18: random 55.7 → **ImageNet 66.7 → in-domain SSL 77.0** (ResNet-50: 55.3 → 65.8 → 76.9). **Frozen features + linear classifier, ResNet-18: ImageNet 41.1 → in-domain SSL 69.3 (+28.2 points)** (ResNet-50: 46.4 → 69.6). Segmentation: ImageNet better for ResNet-50 (69.7 vs 66.7); SSL marginally better for ResNet-18 (74.0 vs 73.5) | Randomly initialized networks (frozen-probe ResNet-18 F1 35.5; fine-tuned 55.7) | https://arxiv.org/abs/2011.13971 (full text: https://arxiv.org/html/2011.13971v2) | **HIGH** (READ-TABLE, Tables 1 & 2; the ">28%" claim in the abstract matches the +28.2-point frozen-feature gap) |
| Ronneberger, Fischer, Brox — "U-Net: Convolutional Networks for Biomedical Image Segmentation", MICCAI 2015 | 2015 | **Nothing transferred — no ImageNet, no pretrained weights.** Trained from scratch in Caffe; weights drawn from a Gaussian with std √(2/N); SGD momentum 0.99 | **Trained from scratch** (counterexample) | ISBI 2012 EM segmentation challenge (Drosophila VNC, 30 train images 512×512); ISBI Cell Tracking Challenge 2015 (PhC-U373, DIC-HeLa) | EM segmentation: **warping error 0.000353 (rank 1)**, Rand error 0.0382, pixel error 0.0611. ISBI CTC 2015 IOU: **PhC-U373 0.9203**, **DIC-HeLa 0.7756** | Ciresan et al. sliding-window CNN (also from scratch): warping error 0.000420, Rand 0.0504 (rank 3). Best pre-U-Net CTC entries: 0.83 and 0.46 IOU. Human: warping error 0.000005 | https://arxiv.org/abs/1505.04597 (full text: https://ar5iv.labs.arxiv.org/html/1505.04597) | **HIGH** (READ-TABLE, Tables 1 & 2; "no pretraining" is an inference from the Methods, which specify Gaussian random init and never mention pretrained weights) |
| Litjens, Sánchez, Timofeeva, Hermsen, Nagtegaal, Kovacs, Hulsbergen-van de Kaa, Bult, van Ginneken, van der Laak — "Deep learning as a tool for increased accuracy and efficiency of histopathological diagnosis", *Scientific Reports* 6:26286 | 2016 | **Nothing transferred.** 4-conv + 3-FC CNN trained from randomly sampled patches with **Theano 0.7 / pylearn2 0.1**; early stopping on validation error; boosting (hard-example resampling) for the lymph-node task. **No ImageNet pretraining anywhere in the paper** — see §3 | **Trained from scratch** (counterexample) | Own cohorts: 225 prostate H&E biopsy slides (100 train / 50 val / 75 test); 271 breast sentinel-lymph-node slides (98/33/42 + 98 consecutive) | Prostate, slide-level **AUC 0.99 (95% CI 0.95–1.0)** for median cancer-likelihood analysis and **0.98 (0.94–0.99)** for 90th-percentile; **32%** of benign slides excluded at 100% sensitivity. Sentinel node slide-level **AUC 0.90 (test, excl. ITC)** and **0.88 (consecutive, excl. ITC)**; 0.88 / 0.74 when ITCs are included; FROC sensitivity **0.90 at 1 FP** and **0.93 at 2 FP** | No learned baseline; comparison is against manual pathologist workflow (efficiency framing). Paper notes the CNN data volume was far below typical deep-learning practice | https://doi.org/10.1038/srep26286 (full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC4876324/) | **HIGH** for the numbers (READ-TABLE, Table 3 + results text). **HIGH–MEDIUM** for "no ImageNet" (argument from absence + explicit from-scratch training description; exact weight initialization is not stated) |
| Cireşan, Giusti, Gambardella, Schmidhuber — "Mitosis Detection in Breast Cancer Histology Images with Deep Neural Networks", MICCAI 2013, LNCS 8150:411–418 | 2013 | **Nothing transferred** — deep max-pooling CNN trained per-pixel on the challenge's own small training set (Xu et al. 2017, whose full text I read, describes this training set as "5 different biopsy H&E stained slides containing about 300 total mitosis events") | Trained from scratch | ICPR 2012 mitosis detection competition (MITOS) | **READ-ABSTRACT:** "Our approach won the ICPR 2012 mitosis detection competition, outperforming other contestants by a significant margin." **No numeric F1 in the abstract.** The widely repeated F1≈0.78 figure is **UNVERIFIED** (see §3) | Other ICPR 2012 contestants | https://doi.org/10.1007/978-3-642-40763-5_51 | **MEDIUM** (READ-ABSTRACT via Europe PMC; numbers UNVERIFIED) |
| Spanhol, Oliveira, Petitjean, Heutte — "Breast cancer histopathological image classification using Convolutional Neural Networks", IJCNN 2016, pp. 2560–2567 | 2016 | **UNVERIFIED** (the paper is known to train ImageNet-family CNNs on BreakHis, but I could not read the text) | UNVERIFIED | BreakHis | **UNVERIFIED — no numbers extracted.** Do not quote any BreakHis number from this file | UNVERIFIED (expected: LBP / GLCM / PFTAS classical features) | https://doi.org/10.1109/IJCNN.2016.7727519 · HAL record: https://hal.science/hal-02113849v1 | citation only |
| Spanhol, Oliveira, Cavalin, Petitjean, Heutte — "Deep features for breast cancer histopathological image classification", IEEE SMC 2017, pp. 1868–1873 | 2017 | **UNVERIFIED** in detail; the paper's premise (per its title and the BreakHis site) is ImageNet-trained CNN *deep features* vs classical LBP/GLCM/PFTAS-style features | UNVERIFIED (likely frozen deep features + classifier) | BreakHis | **UNVERIFIED — no numbers extracted** | UNVERIFIED | https://doi.org/10.1109/SMC.2017.8122889 · HAL record: https://hal.science/hal-02113824v1 | citation only |
| Falk, Mai, Bensch, Çiçek, … Ronneberger — "U-Net: deep learning for cell counting, detection, and morphometry", *Nature Methods* 16:67–70 | 2019 | **UNVERIFIED** whether ImageNet was used. The abstract only says the ImageJ plugin "comes with **pretrained models** for single-cell segmentation" — these are the authors' own microscopy-trained U-Net models, not ImageNet weights, but I could not confirm from the full text | UNVERIFIED | Own microscopy datasets (cell counting / detection / morphometry) | **No numbers extracted** | — | https://doi.org/10.1038/s41592-018-0261-2 | citation + READ-ABSTRACT only; paper is not open access (not in PMC) |
| Srinidhi, Ciga, Martel — "Deep neural network models for computational histopathology: A survey", *Medical Image Analysis* 67:101813 | 2022 (online 2020) | n/a — **survey evidence for "ImageNet pretraining became the default assumption"** | n/a | 130+ surveyed histopathology papers | Direct quotes in §4 | n/a | https://doi.org/10.1016/j.media.2020.101813 (full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7725956/) | **HIGH** (verbatim quotes read in the article's own text) |
| Raghu, Zhang, Kleinberg, Bengio — "Transfusion: Understanding Transfer Learning for Medical Imaging", NeurIPS 2019 (arXiv:1902.07208) | 2019 | **OUT OF SCOPE — radiology, not microscopy** (chest X-ray, retinal fundus, mammography). Included only as the requested contrast | both | radiology tasks | **READ-ABSTRACT:** "transfer offers little benefit to performance, and simple, lightweight models can perform comparably to ImageNet architectures" | from-scratch lightweight models | https://arxiv.org/abs/1902.07208 | **MEDIUM** (abstract only; scope caveat) |

---

## 2. Nuance per result

### 2.1 Xu et al. 2017 — the clearest "frozen ImageNet features beat handcrafted features" result in histopathology

This is the strongest early (2017) domestic demonstration that ImageNet transfer alone — no
histopathology training of the convolutional layers at all — carries a large amount of usable
signal for tissue histology:

- Features are the **fc2 activations (4096-d)** of the AlexNet model "shared by the CognitiveVision
  team at ImageNet LSVRC 2013 … trained on the entire ImageNet dataset". Patches (336×336 or
  672×672 px depending on magnification, resampled to 224×224) are fed through the frozen network,
  aggregated by 3-norm pooling, reduced to the top-100 most discriminative dimensions (binary
  tasks), and classified by a **linear SVM (LIBLINEAR)**.
- The classification gap is large and in favour of transfer: **97.8% vs 77.8%** (brain GBM/LGG),
  **98.0% vs 90.1%** (colon binary), **87.2% vs 75.5%** (colon multiclass) against an
  identically-pooled SIFT+LBP+L\*a\*b pipeline in the same framework. Note that the naive
  whole-image CNN (SVM-IMG) is *worse* than handcrafted features on the brain task (62.2%), so the
  paper's contribution is really "CNN features **+ patch pooling**", not CNN features alone.
- Fine-tuning adds little on segmentation: **84.0% → 84.4%** (brain) and **93.2% → 94.8%**
  (colon). The paper's own claim that "fine-tuned CNN models can reach better accuracy on both
  classification and segmentation tasks" is stronger than its segmentation tables support.
- **Internal inconsistency, flag for slides:** the Conclusions text says "state-of-the-art results of
  **97.5%** for classification and 84% for segmentation in the MICCAI brain tumor challenge", while
  **Table 4 says 97.8%**. Use 97.8% if citing the table, and note the 97.5% in the conclusion.
- The paper also reports the freeze/thaw comparison honestly: ImageNet transfer works "with little
  training data" (22 LGG + 23 GBM training images).

### 2.2 Caicedo et al. 2019 (DSB 2018) — the point where natural-image pretraining became the winning recipe in a microscopy challenge

The 2018 Data Science Bowl is the cleanest event-level evidence for the shift: by late 2018 /
published 2019, **all three winning nucleus-segmentation solutions used natural-image pretraining**
(ImageNet, ImageNet+COCO, or COCO), while the classical CellProfiler reference scored 0.5281
competition score / 0.6280 mean F1 / 59.35% recall at IoU 0.7 versus 0.6316 / 0.7120 / 77.62% for
the ImageNet-pretrained 32-network ensemble.

Two important caveats that make this a *nuanced* data point rather than a clean transfer win:

1. The winners' advantage was **not only pretraining**: the paper attributes the win to
   "a combination of pre-processing and post-processing techniques, as well as the application of
   best practices during training (mostly data balancing and data augmentation)", plus a
   mask-ranking strategy used by all top three.
2. The authors' own control experiment — plain U-Nets trained from scratch, split across five image
   groups, with ~20 h of hand tuning — "did not reach competitive performance". But the paper
   attributes this to "limited learning capacity of the evaluated U-Net relative to the top models,
   reduced number of training examples in the five groups after splitting and experimental
   variability of the test sets" — i.e. it is **not** presented as a pretraining ablation.
   **There is no from-scratch-vs-ImageNet ablation at matched architecture in this paper.**
3. Scale context: 3,891 teams / 17,929 competitors registered; 739 teams made valid stage-2
   submissions; 85 candidate algorithms beat the (manually configured) classical reference.

### 2.3 Ciga et al. 2020/2021 — the explicit ImageNet-vs-in-domain pretraining comparison in histopathology

This is the paper that most directly answers "does ImageNet pretraining help histopathology?" and
it gives a *mixed* but quantified answer:

- **Fine-tuned** models: in-domain self-supervised pretraining wins on classification
  (77.0 vs 66.7 macro-F1, ResNet-18, averaged over BACH + Lymph + BreakHis + NCT-CRC-HE-100K +
  Gleason2019) and on the BreastPathQ regression L1 error (6.6 vs 9.3).
- **Frozen features + linear classifier**: the gap explodes in favour of in-domain pretraining
  (69.3 vs 41.1 macro-F1, +28.2 points, ResNet-18; 69.6 vs 46.4, ResNet-50). This is the number
  behind the abstract's "boosting task performances by more than 28% in F1 scores on average" —
  and it applies to the **frozen/linear-probe** setting, not to the headline fine-tuning numbers.
  Any slide that says "SSL beats ImageNet by 28% F1" should specify frozen features.
- **Segmentation** (U-Net encoder + randomly initialised decoder) is where ImageNet holds up:
  ResNet-50 ImageNet 69.7 vs SSL 66.7; ResNet-101 ImageNet 69.0 vs SSL 65.9. ResNet-18 is roughly a
  tie (73.5 vs 74.0).
- The difference is largest with little labelled data: "self supervision outperforms training from
  scratch (random setting) by over 40% for the NCT dataset when only 5% of the labeled images are
  used for training."
- Caveat for a lecture: SSL pretraining used **57 unlabeled histopathology datasets** — a resource
  most groups do not have, so this is not a like-for-like "cheaper than ImageNet" argument.

### 2.4 U-Net 2015 and Litjens 2016 — the "before ImageNet transfer was default" data points

Both are from-scratch and both were state of the art in their task at the time:

- **U-Net (MICCAI 2015)** explicitly frames the problem as "thousands of training images are usually
  beyond reach in biomedical tasks" and answers it with **elastic data augmentation**, not transfer.
  It beat the previous best (Cireşan's sliding-window CNN) on the ISBI 2012 EM challenge
  (warping error 0.000353 vs 0.000420) and won the ISBI Cell Tracking Challenge 2015 2D transmitted-light
  categories by a wide margin (IOU 0.9203 vs 0.83; 0.7756 vs 0.46). **ImageNet appears in the paper
  only as a citation to Krizhevsky et al.** — never as a source of weights.
- **Litjens 2016 (Sci Rep)** reached slide-level AUC 0.99 on prostate biopsies with 100 training
  slides and a ~7-layer CNN trained from random patches with Theano/pylearn2, plus Cireşan-style
  boosting for the lymph-node task. **I searched the entire article text for "ImageNet",
  "pretrain", "pretrained", "initialize", "weights": the only ImageNet occurrence is in the
  reference list.** The Methods describe validation-monitored training from randomly extracted
  patches and structure/parameter tuning, with no mention of pretrained initialization.
  → **The task brief's premise that this is "an ImageNet-pretrained CNN for prostate cancer" is not
  supported by the paper.** Treat it as a from-scratch CNN and say so.

### 2.5 Cireşan 2013 — the pre-ImageNet "before" point

Verified only at abstract level: deep max-pooling CNNs, per-pixel classification with a patch
context, simple post-processing, **won the ICPR 2012 mitosis detection competition, "outperforming
other contestants by a significant margin"**. The abstract contains **no F1 number**, and the paper
predates the widespread use of ImageNet transfer in microscopy (the training set was ~5 slides /
~300 mitoses). If a slide needs the exact score, it must be read from the MICCAI PDF — I could not
reach it (see §3). Related primary context: Veta et al., *Medical Image Analysis* 20(1):237–248
(2015), the AMIDA13 challenge paper, reports 11 methods and states only that "the top performing
method has an error rate that is comparable to the inter-observer agreement among pathologists" —
its abstract also carries no F1 values.

### 2.6 Spanhol / BreakHis — citations verified, numbers not

Citations are verified from two independent scholarly registries:

- IJCNN 2016: F. A. Spanhol, L. F. L. Oliveira, C. Petitjean, L. Heutte, pp. 2560–2567,
  DOI 10.1109/IJCNN.2016.7727519 (HAL hal-02113849; Semantic Scholar).
- IEEE SMC 2017: F. Spanhol, L. S. Oliveira, P. Cavalin, C. Petitjean, L. Heutte, pp. 1868–1873,
  DOI 10.1109/SMC.2017.8122889 (HAL hal-02113824; Crossref).
- Detector note: the DOI I first guessed for the SMC paper (10.1109/SMC.2017.8122712) is a *different*
  paper ("Predicting purchase intention according to fan page users' sentiment"). The correct DOI is
  8122889. If a deck cites 8122712, that is wrong.
- Dataset facts (author-maintained page): BreakHis v1 = 9,109 microscopic images from 82 patients at
  40×/100×/200×/400×, 2,480 benign + 5,429 malignant, 700×460 px RGB PNG (the page's own per-magnification
  table sums to 7,909 images, while the prose says 9,109 — an internal inconsistency in the source).
- I could **not** read any accuracy/F1 from either paper. The author-hosted PDFs
  (`www.inf.ufpr.br/lesoliveira/download/IJCNN2016-BC.pdf`, `SpanholSMC2017.pdf`) were unreachable
  (3 attempts each, `fetch failed`; the bare directory too), and PDFs are unsupported by the fetch
  tool regardless. **Do not put a BreakHis number on a slide from this research file.**

### 2.7 Falk et al. 2019 — open question

The paper is **not open access and not in PMC**, so no full text. Its abstract (read verbatim) says
the ImageJ plugin "comes with **pretrained models** for single-cell segmentation and allows for
U-Net to be adapted to new tasks on the basis of a few annotated samples". Those pretrained models
are the authors' own microscopy-trained U-Nets (the plugin workflow trains/adapts per dataset), so
the paper is best described as a from-scratch / task-specific-training line of work — but **I did
not verify that the paper never uses ImageNet initialization**, so do not assert it.

---

## 3. COULD NOT VERIFY

1. **Spanhol IJCNN 2016 and SMC 2017 numbers (any of them).** IEEE Xplore is paywalled; the
   author-hosted PDFs at `www.inf.ufpr.br` are unreachable from this environment (3 attempts, both
   files and the directory); PDFs are unsupported by the fetch tool. The specific claims in the task
   brief (CNN features vs LBP/GLCM/PFTAS with exact accuracies; "compare CNN features vs classical
   with exact accuracy numbers") are **not confirmed by me**. Widely repeated BreakHis numbers were
   deliberately not transcribed here because I could not trace them to the primary tables.
2. **Cireşan et al. 2013 numeric F1** (commonly quoted around 0.78 for the ICPR 2012 set).
   The MICCAI chapter is paywalled (Springer redirects to idp.springer.com); the abstract has no
   number. VERIFIED at abstract level only: they won ICPR 2012 by a significant margin.
3. **Veta et al. 2015 (AMIDA13)** numeric per-team F1 scores — abstract read, contains no numbers.
4. **Whether Litjens et al. 2016 used ImageNet pretraining.** No evidence of it; strong
   counter-evidence (from-scratch Theano/pylearn2 training described in Methods; ImageNet appears
   only in the reference list). Strictly, the paper does not print the sentence "we did not use
   pretraining", and "The full network specifications can be found in the supplementary files" was
   not read (supplementary not retrieved). Treat "from scratch" as **high-probability, not proven**;
   treat the task brief's "ImageNet-pretrained CNN" claim as **unsupported**.
5. **Whether Falk et al. 2019 used ImageNet initialization.** Paper not open access, not in PMC.
6. **Exact U-Net 2015 weight-initialization wording as an explicit denial of transfer.** I read the
   Training section (Caffe, SGD, momentum 0.99, Gaussian init std √(2/N)); the paper never mentions
   pretrained weights, but there is no explicit "we did not use ImageNet pretraining" sentence.
7. **"Transfusion"-style question for microscopy.** I found no microscopy-specific paper titled or
   framed as "do ImageNet weights help in microscopy?" with numbers I could verify. The Raghu et al.
   "Transfusion" result is radiology, not microscopy, and is flagged as out of scope.
8. **Tellez et al. 2019** ("Quantifying the effects of data augmentation and stain color
   normalization…", *Medical Image Analysis* 58:101544; arXiv:1902.06543) — I retrieved the paper's
   abstract and its AUC table (stain augmentation/normalization comparison; e.g. Identity+HED-light
   ranking 1.2, best external AUCs 0.98 on crc-labpon), but the fetch truncated before the
   architecture/training section, so its **ImageNet-pretraining setting is unverified**.
9. **Fetches that failed outright** (retried where noted): nature.com article + PDF (302 → idp.nature.com
   auth), rd.springer.com / link.springer.com (redirect to idp.springer.com), europepmc.org article
   pages (HTTP 403 Cloudflare), Europe PMC `fullTextXML` (HTTP 406), PMC PDF and PMC per-table pages
   (reCAPTCHA), `www.inf.ufpr.br` (connection failure ×3), `web.archive.org` (connection failure ×2),
   `r.jina.ai` (connection failure ×2), `api.allorigins.win` (HTTP 520), `api.codetabs.com` (HTTP 522),
   Semantic Scholar *search* endpoint (HTTP 429, repeatedly), `pmc.utils.idconv` (redirect then 404),
   NCBI BioC for `PMC6976525` ("no result" — that PMCID is not Falk 2019; the paper is not in the PMC
   OA subset), BioC rate limit 429 (max 3 req/s; succeeded on retry).

---

## 4. When did ImageNet transfer become the default assumption in microscopy/histopathology?

Verbatim quotations (all read in the article's own full text):

**Srinidhi, Ciga & Martel, "Deep neural network models for computational histopathology: A survey",
*Medical Image Analysis* 67:101813 (2022; online 2020)** — https://doi.org/10.1016/j.media.2020.101813
(full text https://pmc.ncbi.nlm.nih.gov/articles/PMC7725956/):

> "Training a deep CNN from scratch requires large amounts of annotated data, which is very expensive
> and cumbersome to obtain in practice. A promising alternative is to use a pre-trained network
> (trained on a vast set of natural images, such as ImageNet) to fine-tune on a problem in different
> domain with limited number of annotations."

> "Pre-trained networks are widely employed but although pre-training is known to improve convergence
> speed significantly, it might not always lead to a better performance compared to a network trained
> from scratch, given enough time for convergence. In pre-trained networks, natural scene image
> databases (e.g., ImageNet) are commonly used, and it is possible that the learned feature
> representations may not be accurate for histopathology images."

This is the closest thing I found to an explicit statement that natural-image pretraining is
standard practice in computational histopathology — and it is paired with the standard caveat.

**Ciga, Xu & Martel 2020/2021** (arXiv:2011.13971v2, §5.2) — https://arxiv.org/html/2011.13971v2:

> "It is generally accepted that pretrained networks boost the performance in medical image analysis
> [57] and digital histopathology tasks [40]."

**Caicedo et al. 2019** is the *event-level* marker of the shift: in a challenge whose explicit goal
was a single configuration-free model across 15 unseen microscopy experiments, **all three winning
solutions used natural-image pretraining** (ImageNet encoders; ImageNet+COCO; COCO), reported in
*Nature Methods* in 2019 — https://doi.org/10.1038/s41592-019-0612-7.

**Litjens et al. 2016** and **Ronneberger et al. 2015** are the counter-marker for the period before
that: two of the most-cited microscopy deep-learning papers of 2015–2016 both trained from scratch
and both won their respective challenges/tasks that way.

---

## 5. All URLs actually fetched / verified in this session

**Fetched successfully (HTTP 200) — used as evidence**

- https://arxiv.org/abs/2011.13971 — Ciga et al. abstract (READ-ABSTRACT)
- https://arxiv.org/html/2011.13971v2 — Ciga et al. full text, Tables 1 & 2 (READ-TABLE)
- https://arxiv.org/abs/1902.07208 — Raghu et al. "Transfusion" abstract (READ-ABSTRACT, out of scope)
- https://ar5iv.labs.arxiv.org/html/1505.04597 — U-Net 2015 full text, Tables 1 & 2, Training section (READ-TABLE)
- https://ar5iv.labs.arxiv.org/html/1902.06543 — Tellez et al. 2019 full text (truncated before methods; Table 1 AUCs only)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4876324/ — Litjens 2016 HTML (truncated at Methods)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4876324/?report=classic — same, no extra content
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5446756/ — Xu 2017 HTML (truncated at Evaluation)
- https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC4876324/unicode — Litjens 2016 **full text** (READ-TABLE; grepped for ImageNet/pretrain/weights)
- https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC5446756/unicode — Xu 2017 **full text**, Tables 4 & 6 (READ-TABLE)
- https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC6919559/unicode — Caicedo 2019 **full text**, Table 1 + winner descriptions (READ-TABLE)
- https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC7725956/unicode — Srinidhi et al. survey **full text** (verbatim quotes)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41592-019-0612-7%22&resultType=core&format=json — Caicedo metadata + PMCID
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41592-018-0261-2%22&resultType=core&format=json — Falk 2019 metadata + abstract
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24579167&resultType=core&format=json — Cireşan 2013 abstract + venue/DOI/PubMed ID
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1016/j.media.2014.11.010%22&resultType=core&format=json — Veta 2015 (AMIDA13) abstract
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/srep26286?fields=title,abstract,year,venue,openAccessPdf,externalIds — Litjens bibliographic record
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/IJCNN.2016.7727519?fields=title,abstract,year,venue,externalIds,authors — Spanhol IJCNN citation
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-642-40763-5_51?fields=title,abstract,year,venue,externalIds,authors — Cireşan citation
- https://hal.science/hal-02113849v1 — Spanhol IJCNN 2016 record (pp. 2560–2567)
- https://hal.science/hal-02113824v1 — Spanhol SMC 2017 record (pp. 1868–1873)
- https://api.archives-ouvertes.fr/search/?q=Spanhol+breast+cancer+histopathological&fl=title_s,doiId_s,uri_s,producedDate_s,fileMain_s&rows=10&wt=json — HAL search
- https://api.crossref.org/works?query.title=Deep+features+for+breast+cancer+histopathological+image+classification&rows=5&select=DOI,title,issued,container-title,page — correct SMC DOI 10.1109/smc.2017.8122889
- https://web.inf.ufpr.br/vri/databases/breast-cancer-histopathological-database-breakhis/ — BreakHis dataset statistics + author-hosted PDF links
- https://www.diagnijmegen.nl/publications/geert-litjens/2016/ — Litjens 2016 bibliographic confirmation
- https://export.arxiv.org/api/query?search_query=all:Spanhol&start=0&max_results=20 — 0 results (Spanhol papers are not on arXiv)

**Fetched but yielded no usable evidence (recorded failures)**

- https://www.nature.com/articles/srep26286 — 302 to idp.nature.com (auth wall)
- https://www.nature.com/articles/srep26286.pdf — same redirect
- https://rd.springer.com/article/10.1038/srep26286 — fetch failed
- https://link.springer.com/chapter/10.1007/978-3-642-40763-5_51 — redirect to idp.springer.com
- https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-017-1685-x — redirect to link.springer.com
- https://europepmc.org/article/PMC/PMC4876324 and https://europepmc.org/article/PMC/4876324 — HTTP 403 (Cloudflare)
- https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4876324/fullTextXML (and ?format=xml) — HTTP 406
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4876324/pdf/srep26286.pdf — reCAPTCHA interstitial
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5446756/table/Tab2/, Tab3, Tab4, Tab5 — reCAPTCHA interstitial
- https://pmc.ncbi.nlm.nih.gov/utils/idconv/v1.0/?ids=… — HTTP 404
- https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=… — cross-origin redirect (not followed)
- https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC6976525/unicode — "No result can be found" (wrong PMCID for Falk 2019)
- https://www.ncbi.nlm.nih.gov/research/bionlp/…/PMC7725956/unicode — first attempt HTTP 429, retry OK
- https://arxiv.org/pdf/2011.13971v2 — `unsupported content type "application/pdf"`
- http://www.inf.ufpr.br/lesoliveira/download/IJCNN2016-BC.pdf — fetch failed ×3
- http://www.inf.ufpr.br/lesoliveira/download/SpanholSMC2017.pdf — fetch failed ×2
- https://www.inf.ufpr.br/lesoliveira/download/SpanholSMC2017.pdf — fetch failed
- http://www.inf.ufpr.br/lesoliveira/ — fetch failed (host unreachable)
- https://web.archive.org/web/2021id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC4876324/ — fetch failed
- https://web.archive.org/web/2023/https://www.nature.com/articles/srep26286 — fetch failed
- https://r.jina.ai/https://pmc.ncbi.nlm.nih.gov/articles/PMC4876324/ and …/nature.com/articles/srep26286 — fetch failed ×2
- https://api.allorigins.win/raw?url=… — HTTP 520
- https://api.codetabs.com/v1/proxy?quest=… — HTTP 522
- https://api.semanticscholar.org/graph/v1/paper/search?query=… — HTTP 429 (rate limit), twice
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/SMC.2017.8122712?… — resolved to an unrelated paper (wrong DOI guess)
- https://scholar.archive.org/fatcat/release/chltji6bmfcxdncwxkaketrrue — fetch failed
