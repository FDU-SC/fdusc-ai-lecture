# ImageNet-pretrained backbones transferred to industrial inspection / defect detection

Compiled 2026-09-19. Working directory `/home/zecyel/slides/ch1`.
All numbers below are transcribed from text I actually retrieved in this session unless the row is explicitly
marked otherwise. "Read directly" = I retrieved the sentence/table row; "abstract-level" = the number appears in
the paper's abstract only (I could not read its tables); "search-snippet" = the number appeared only as a fragment
in a search-provider snippet of an indexed PDF and I could not open the full text.

Environment note that shapes this file: `arxiv.org`, `export.arxiv.org`, `openaccess.thecvf.com` **PDFs**,
`link.springer.com`, `huggingface.co`, `web.archive.org`, `semanticscholar.org`, `paperswithcode.com`,
`core.ac.uk` and `mdpi.com` were unreachable or refused (see §5). PDF content types are rejected by the fetch
tool (`unsupported content type "application/pdf"`), so every number below comes from an HTML/XML page, and
`ar5iv.labs.arxiv.org` (which did work, intermittently) was the substitute for arXiv full text.

---

## 1. Table

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | confidence |
|---|---|---|---|---|---|---|---|---|
| **Towards Total Recall in Industrial Anomaly Detection** (PatchCore) — Karsten Roth, Latha Pemula, Joaquin Zepeda, Bernhard Schölkopf, Thomas Brox, Peter Gehler; CVPR 2022, pp. 14318–14328 | 2022 (arXiv 2021) | WideResNet-50 pre-trained on **ImageNet**, feature maps from `layer2`+`layer3`, locally aggregated (patchsize 3) | **Neither — frozen fixed feature extractor.** No network optimisation at all: the "training" step is only building a coreset-subsampled memory bank of nominal patch features. Paper: *"PatchCore achieves this while retaining fast inference times without requiring training on the dataset at hand."* | MVTec AD | **image-level AUROC 99.1 %** (PatchCore-25 %), **99.0 %** (PatchCore-10 % and PatchCore-1 %); abstract headline *"up to 99.6 %"*; **pixel-level AUROC 98.1 %** (PatchCore-1 %, Table 1 of the paper / official repo) | Same table: SPADE 85.5, PatchSVDD 92.1, DifferNet 94.9, PaDiM 95.3, Mahalanobis-AD (Rippel et al.) 95.8, PaDiM* 97.9 | https://ar5iv.labs.arxiv.org/html/2106.08265 (Table 1, read directly); https://openaccess.thecvf.com/content/CVPR2022/html/Roth_Towards_Total_Recall_in_Industrial_Anomaly_Detection_CVPR_2022_paper.html (abstract); https://raw.githubusercontent.com/amazon-science/patchcore-inspection/main/README.md | **HIGH** |
| **PaDiM: a Patch Distribution Modeling Framework for Anomaly Detection and Localization** — Thomas Defard, Aleksandr Setkov, Angélique Loesch, Romaric Audigier (Université Paris‑Saclay, CEA List); ICPR 2020 Workshops (proceedings 2021), pp. 475–489; arXiv 2011.08785 | 2020/2021 | ResNet‑18, Wide ResNet‑50‑2 and EfficientNet‑B5, **all pre-trained on ImageNet** (paper: *"all pretrained on ImageNet"*), features from the first three layers | **Frozen fixed feature extractor.** Paper: *"we choose to avoid ponderous neural network optimization by only using a pretrained CNN to generate patch embedding vectors"*; only per-patch Gaussians (μ, Σ) are estimated | MVTec AD | **localisation AUROC 97.1 % and PRO-score 90.8 %** (PaDiM‑R18, all classes, Table I); **detection: 95.3 % image AUROC** (PaDiM) and **97.9 %** (PaDiM*, per-class backbone selection) as tabulated by PatchCore's Table 1 | Table III (localisation AUROC, PRO, texture classes): AE‑SSIM (78, 56.7), AE‑L2 (70, 69.6), VAE (61.2, 49.9), SPADE (92.9, 88.4), PaDiM‑R18‑Rd100 (95.6, 91.3), PaDiM‑WR50‑Rd550 (96.9, 93.2) | https://ar5iv.labs.arxiv.org/html/2011.08785 (Tables I–III, read directly); https://www.alphaxiv.org/abs/2011.08785 (abstract); https://api.openalex.org/works?filter=title.search:PaDiM%20patch%20distribution%20modeling (DOI/venue) | **HIGH** for localisation + ImageNet-pretraining; **MEDIUM** for the 95.3/97.9 detection numbers (they are PatchCore's transcription of PaDiM, not PaDiM's own Table IV, which I could not read) |
| **Uninformed Students: Student–Teacher Anomaly Detection with Discriminative Latent Embeddings** — Paul Bergmann, Michael Fauser, David Sattlegger, Carsten Steger (MVTec Software); CVPR 2020, pp. 4183–4192; arXiv 1911.02357 | 2020 | Teacher network trained by distillation from a pretrained network over **ImageNet** patches (paper: *"A large number of training patches p can be obtained by random crops from any image database. Here, we use ImageNet"*). Teacher is then frozen; the student ensemble is trained on anomaly-free target data | **Mixed:** ImageNet-pretrained teacher is frozen; the students are trained (regression onto teacher descriptors) on the target data | MVTec AD | Per-class AUROC read directly from the paper's MVTec table, "Ours (p=65)" column: Bottle 0.918, Cable 0.865, Capsule 0.916, Hazelnut 0.937, Metal nut 0.895, Pill 0.935, Screw 0.928, Carpet 0.695, Grid 0.819, Leather 0.819, Tile 0.912, Wood 0.725. **The mean row was in the truncated part of the page and is NOT verified.** | Same table contains 1‑NN, OC‑SVM, K‑Means, ℓ2‑AE, VAE, SSIM‑AE, AnoGAN and "CNN-Feature Dictionary" columns with per-class values, e.g. Carpet: 1‑NN 0.512, OC‑SVM 0.355, K‑Means 0.253, ℓ2‑AE 0.456, VAE 0.501, SSIM‑AE 0.647, AnoGAN 0.204, CNN-Feature Dictionary 0.469 | https://ar5iv.labs.arxiv.org/html/1911.02357 ; https://openaccess.thecvf.com/content_CVPR_2020/html/Bergmann_Uninformed_Students_Student-Teacher_Anomaly_Detection_With_Discriminative_Latent_Embeddings_CVPR_2020_paper.html | **HIGH** for "teacher pretrained on ImageNet"; **MEDIUM** for the per-class numbers; **LOW** for what metric they are (see §3) |
| **MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection** — Paul Bergmann, Michael Fauser, David Sattlegger, Carsten Steger; CVPR 2019, pp. 9592–9600; DOI 10.1109/CVPR.2019.00982 | 2019 | Official baseline suite explicitly includes **"feature descriptors using pre-trained convolutional neural networks"** alongside classical CV methods and autoencoders/GANs | Classifier/descriptor on top of frozen pretrained features (the descriptor baselines) | MVTec AD (5354 images, 15 object+texture categories, 70+ defect types) | **Mean AUROC table not verified** — I could not read the paper's tables (CVF serves it as a PDF only). Individual baseline columns are reproduced per-class in Bergmann et al. 2020 (row above) and in PaDiM Table III (row above) | — | https://openaccess.thecvf.com/content_CVPR_2019/html/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.html (abstract, read directly); https://www.mvtec.com/research-teaching/datasets/mvtec-ad | **HIGH** that ImageNet-pretrained CNN feature descriptors were official baselines; **LOW** for their mean AUROC numbers |
| **Rethinking ImageNet Pre-training** — Kaiming He, Ross Girshick, Piotr Dollár (FAIR); ICCV 2019, pp. 4918–4927; arXiv 1811.08883 | 2018/2019 | Not industrial — the controlled COCO study that is the standard citation for "does ImageNet pre-training matter?" | Compares **random init vs ImageNet pre-train + fine-tune** | COCO (detection / instance seg. / keypoints) | Table 1 (bbox AP, Mask R-CNN + GN): R50 random init 41.3 (6×) vs pre-train 41.1; R101 random init 42.7 vs pre-train 42.2. Table 2: R50 41.3 / 61.8 / 45.6 (AP, AP50, AP75) from scratch vs 41.1 / 61.7 / 44.6 pre-trained. Table 3: ResNeXt‑152 from **random init** 50.9 bbox AP / 43.2 mask AP, vs 50.3 / 42.5 with ImageNet pre-training | — | https://ar5iv.labs.arxiv.org/html/1811.08883 (Tables 1–3, read directly) | **HIGH** |
| **Rethinking Transfer Learning for Industrial Inspection: DINOv3 vs. ImageNet Pretraining Across RGB and X-ray Tasks** — Mehdi Gharbage, Céline Teulière, Pierre Bouges, Thierry Chateau (UCA/CNRS Institut Pascal + Michelin); arXiv preprint 2605.23472 | 2026 (**preprint, not peer-reviewed**) | ConvNeXt‑T pretrained with either supervised **ImageNet‑1k** classification or **DINOv3 distillation (LVD‑1689M)**; conventional **ResNet‑50 (ImageNet‑1k)** baseline | Both regimes tested: **frozen** backbone and **fully fine-tuned** | Severstal (RGB steel surface defects, semantic seg.), Rubber Rings (RGB, semantic seg.), RarePlanes (instance seg.), GDXray Castings (**X-ray** defect detection) | Table 2 (mIoU for seg., mask mAP for RarePlanes, box mAP@50 for GDXray): ResNet‑50 ImageNet full‑FT 63.28 / 73.87 / 78.39 / 24.42; ConvNeXt‑T ImageNet **frozen** 62.04 / 73.25 / 72.89 / **21.32**, full‑FT 62.97 / 73.26 / 82.88 / **29.74**; ConvNeXt‑T DINOv3 **frozen** 62.40 / 72.32 / 70.36 / **7.88**, full‑FT 64.01 / 75.60 / 84.50 / 27.84 | DINOv3 is the comparator; under X-ray modality shift ImageNet supervised pre-training wins in **both** regimes (21.32 vs 7.88 frozen; 29.74 vs 27.84 fine-tuned) | https://ar5iv.labs.arxiv.org/html/2605.23472 (Table 2, read directly) | **HIGH** for the numbers; **preprint — not peer-reviewed** |
| **Transfer Learning-Based Ensemble Model for Hot-rolled Steel Surface Defect Classification** — Alaa Aldein M. S. Ibrahim, Jules-Raymond Tapamo (Univ. of KwaZulu-Natal); *Journal of Artificial Intelligence and Technology* 5:242–252, published 2025‑07‑08; DOI 10.37965/jait.2025.0683 | 2025 | Ensemble of **three distinct pre-trained CNN architectures** via transfer learning (each trained on subsets of defect images) | Fine-tuned (transfer learning) | NEU (hot-rolled steel surface defect) and X‑SDD | **100 % classification accuracy on NEU**, **99.27 % on X‑SDD** | Abstract claims the ensemble "outperforms existing methods"; the individual-pretrained-CNN / from-scratch comparison table is **not verified** (the article's HTML "full text" view returned an empty frame) | https://ojs.istp-press.com/jait/article/view/683 (abstract, read directly) | **MEDIUM** — abstract-level only; note 100 % on NEU is implausibly high and is widely considered a sign of protocol leakage in NEU benchmarks |
| **Steel Surface Defect Classification Using an Improved VGG16-Based Model** — Touba Torabipour, Abolfazl Gandomi; *Applied and basic Machine Intelligence research* (Yazd Univ.) 3(2):73–88, 2025; DOI 10.22034/abmir.2025.23563.1162 | 2025 | **VGG16 + transfer learning** plus a 2‑D spatial attention module and an attention-based magnification mechanism | Fine-tuned | NEU‑CLS and NEU‑DET | **99.98 % (NEU‑CLS)** and **99.92 % (NEU‑DET)** classification accuracy; *"an improvement of at least 4 % over the baseline VGG16 model"* | Baseline is a plain VGG16 model in the same paper; **the abstract does not state that the baseline VGG16 is ImageNet-pretrained** and I could not read the body (journal exposes abstract + PDF only) | https://abmir.yazd.ac.ir/article_3954.html?lang=en ; https://abmir.yazd.ac.ir/?_action=xml&article=3954&lang=en | **MEDIUM** — abstract-level; peer-reviewed but a low-profile venue |
| **Convolutional networks for voting-based anomaly classification in metal surface inspection** — Vidhya Natarajan, Tzu-Yi Hung, Sriram Vaikundam, Liang-Tien Chia (Rolls-Royce@NTU / NTU); **2017** IEEE International Conference on Industrial Technology (ICIT), pp. 986–991; DOI 10.1109/ICIT.2017.7915495 | **2017** (not 2020) | Pretrained CNN + voting scheme (per abstract/title; details not verified) | Not verified | Metal surface inspection (dataset not verified) | **Not verified — no numbers obtained** | — | https://api.openalex.org/works?filter=title.search:voting-based%20anomaly%20classification%20metal%20surface%20inspection (citation metadata only) | **LOW** — citation verified, contents not |

---

## 2. Prose, per result, with nuance

### 2.1 PatchCore (CVPR 2022) — the cleanest "ImageNet features, zero target training" result

PatchCore is the strongest single piece of evidence for the lecture's claim, because the transfer is
*maximally* transfer: a WideResNet‑50 with ImageNet weights is used as a pure fixed feature extractor
(`layer2` + `layer3`), and the authors state the method works *"without requiring training on the dataset at hand."*
The only per-dataset step is computing and coreset-subsampling a memory bank of nominal patch features.

Read directly from the paper's Table 1 ("Anomaly Detection Performance (AUROC) on MVTec AD"):

| Method | SPADE | PatchSVDD | DifferNet | PaDiM | Mah. AD | PaDiM* | PatchCore‑25 % | PatchCore‑10 % | PatchCore‑1 % |
|---|---|---|---|---|---|---|---|---|---|
| AUROC ↑ | 85.5 | 92.1 | 94.9 | 95.3 | 95.8 | 97.9 | 99.1 | 99.0 | 99.0 |
| Error ↓ | 14.5 | 7.9 | 5.1 | 4.7 | 4.2 | 2.1 | 0.9 | 1.0 | 1.0 |

Table caption (read directly): *"PaDiM\* denotes a result from [PaDiM] with problem-specific backbone selection."*
So the 97.9 figure is PaDiM with a **per-class** choice of backbone — do not present it as PaDiM's default.

The abstract's "up to 99.6 %" is the ensemble number, not the single-model number. The authors' own
repository README (raw.githubusercontent.com, read directly) resolves this:

| Model | Mean AUROC | Mean Seg. AUROC | Mean PRO |
|---|---|---|---|
| WR50-baseline | 99.2 % | 98.1 % | 94.4 % |
| Ensemble | **99.6 %** | **98.2 %** | **94.9 %** |

and documents the exact invocation: `patch_core -b wideresnet50 -le layer2 -le layer3 ...` with the note
*"which runs PatchCore on MVTec images of sizes 224x224 using a WideResNet50-backbone pretrained on ImageNet."*
The 99.1 % in the paper's Table 1 is the best *single-model* configuration (25 % coreset); the repo reports
99.2 % for the same WR50 baseline. Both are single-model, ImageNet-frozen results — quote 99.1 % (paper table)
or 99.2 % (official implementation), and 99.6 % only for the ensemble.

Nuance worth stating in a lecture: PatchCore's own Related Work says the *reason* mid-level features are used is
that *"very deep and abstract features in ImageNet pretrained networks are biased towards the task of natural image
classification, which has only little overlap with the cold-start industrial anomaly detection task"* — i.e. the
transfer works, but not uniformly across the network depth.

### 2.2 PaDiM (ICPR 2020 Workshops / arXiv 2011.08785) — ImageNet backbone, no optimisation at all

PaDiM is the clearest "frozen ImageNet features" example and it predates PatchCore. Read directly from §IV‑B:
*"We train PaDiM with different backbones, a ResNet18 (R18), a Wide ResNet‑50‑2 (WR50) and an EfficientNet‑B5,
all pretrained on ImageNet."* And from §III‑A: *"we choose to avoid ponderous neural network optimization by only
using a pretrained CNN to generate patch embedding vectors."* The only fitted parameters are a mean vector and a
covariance matrix per patch position.

Numbers read directly:

* Table I (localisation, MVTec AD, tuples `(AUROC %, PRO-score %)`): Layer 1 `(94.8, 86.8)`; Layer 2 `(95.7, 88.5)`;
  Layer 3 `(95.7, 88.3)`; Layers 1+2+3 ensemble `(96.0, 89.0)`; **PaDiM‑R18 `(97.1, 90.8)`** (all classes).
* Table III (localisation comparison, "all texture classes" row): AE‑SSIM `(78, 56.7)`, AE‑L2 `(70, 69.6)`,
  VAE `(61.2, 49.9)`, Patch‑SVDD `(93.7, –)`, SPADE `(92.9, 88.4)`, **PaDiM‑R18‑Rd100 `(95.6, 91.3)`**,
  **PaDiM‑WR50‑Rd550 `(96.9, 93.2)`**.

Framing caveat: PaDiM's headline numbers in its own paper are **localisation** metrics. Its image-level
detection table (Table IV) fell outside the retrievable window, so for detection I quote PatchCore's Table 1
(PaDiM 95.3 % default; 97.9 % with per-class backbone selection). The `anomalib` project's non-peer-reviewed
summary table lists PaDiM at 97.9 classification AUC / 97.5 segmentation AUC, which is consistent with the
97.9 figure being the widely quoted "PaDiM" number — but that attribution mixes the per-class-backbone variant
into the headline, so I flag it.

Venue/DOI correction: OpenAlex records PaDiM as DOI **10.1007/978-3-030-68799-1_35**, pp. 475–489, in
*Pattern Recognition. ICPR International Workshops and Challenges* (2021). The DOI suggested in the task brief,
`10.1007/978-3-030-68763-2_3`, does **not** match this record; I could not verify it (Springer is unreachable here).

### 2.3 Uninformed Students (CVPR 2020) — ImageNet-pretrained teacher, distilled into students

The transfer here is one level of indirection: a descriptive network is distilled into a teacher over
**ImageNet** patches, and student networks then regress the teacher's descriptors on anomaly-free target images.
Read directly from §III‑A: *"A large number of training patches p can be obtained by random crops from any image
database. Here, we use ImageNet."* Also relevant, the same paper's §II‑A surveys the pretrained-feature line of
work (Andrews et al. use pretrained VGG + ν‑SVM; Napoletano et al. use **pretrained ResNet‑18** + K‑Means after
PCA; Sabokrou et al. use **pretrained AlexNet** early maps + unimodal Gaussian) — i.e. by 2020 the
"pretrained backbone + shallow/statistical model" pattern was already the established industrial recipe.

Per-class AUROCs for "Ours (p=65)" are quoted in the table in §1. The **mean** is not verified: the page was
truncated mid-table (the last row I could read is Screw), so the final rows and the mean lie beyond what I
retrieved. The same truncation means I could not read the table caption, so I cannot confirm whether those
column values are image-level (detection) AUROC or pixel-level/localisation AUROC. Treat the numbers as
"per-class AUROC as printed in the paper's MVTec table" and nothing stronger.

### 2.4 MVTec AD (CVPR 2019) — did the official baselines use ImageNet-pretrained networks? Yes.

This is directly answerable from the abstract, which I read on the CVF page:
*"We also conduct a thorough evaluation of current state-of-the-art unsupervised anomaly detection methods based
on deep architectures such as convolutional autoencoders, generative adversarial networks, and feature descriptors
using pre-trained convolutional neural networks, as well as classical computer vision methods."*

So the dataset paper's own benchmark suite is tri-partite: (a) reconstruction/generative models trained from
scratch, (b) **feature descriptors built on pre-trained CNNs**, and (c) classical CV methods — exactly the
"from-scratch vs ImageNet-pretrained vs classical" contrast the lecture wants. The baselines later reproduced as
`1‑NN, OC‑SVM, K‑Means, ℓ2‑AE, VAE, SSIM‑AE, AnoGAN, CNN-Feature Dictionary` (see §2.3 for the per-class values)
are that suite.

What I could **not** verify is the paper's mean AUROC table. The CVF site serves the paper as a PDF
(`unsupported content type "application/pdf"`), the MVTec site serves it as a PDF, the IJCV extended version is
on Springer (unreachable), and OpenAlex confirms there is **no arXiv version** (only
`doi:10.1109/cvpr.2019.00982`). Do not put a specific "MVTec 2019 baseline = X % AUROC" number on a slide from
this file. The one number I can support from a reachable page is via the non-peer-reviewed `anomalib` listing,
which attributes **AE‑SSIM segmentation AUC 87.0** to the MVTec AD paper
(https://anomalib.readthedocs.io/en/0.3.3/research/papers.html) — that is a tooling page, not the paper.

### 2.5 Rethinking ImageNet Pre-training (He et al., ICCV 2019) — the counterweight

Read directly. Headline finding, quoted from the paper: ImageNet pre-training *"speeds up convergence early in
training, but does not necessarily provide regularization or improve final target task accuracy"*, and
*"our results hold even when: (i) using only 10 % of the training data, (ii) for deeper and wider models, and
(iii) for multiple tasks and metrics."* Numbers: Table 1 Mask R‑CNN + GN on COCO, R50 random-init 41.3 bbox AP
at the 6× schedule vs 41.1 with ImageNet pre-training; R101 42.7 vs 42.2. Table 3: ResNeXt‑152 **from random
initialization** 50.9 bbox AP / 43.2 mask AP (vs 50.3 / 42.5 with pre-training).

**Applicability caveat, stated precisely:** this is COCO detection/segmentation with ~118 k training images and
long schedules (540 k iterations). It does *not* show that ImageNet pre-training is unnecessary for small
industrial defect datasets. The mechanism it identifies is convergence speed and effective sample count, and the
paper itself frames pre-training as *"a historical workaround ... for when the community does not have enough
target data or computational resources."* Industrial defect datasets are usually in the 10²–10³ image range, so
the paper's own logic predicts a *large* benefit there. I did **not** find a peer-reviewed industrial paper that
runs the head-to-head "ImageNet fine-tune vs random init, same schedule/longer schedule" experiment; see §3.

### 2.6 The 2026 controlled study: ImageNet pre-training is still the default in industrial inspection

This is the direct evidence for "when did ImageNet transfer become the default assumption in industrial
inspection", and for the "it matters most in low-data regimes" point. Verbatim quotes (read directly from the
HTML full text):

> "For many years, the dominant transfer-learning paradigm in computer vision has relied on supervised ImageNet
> pretraining [20], which has served as the standard initialization strategy for downstream recognition and
> localization tasks. In industrial inspection, this approach remains widely used because it offers a practical
> solution when task-specific annotations are scarce."

> "Prior to the rise of vision foundation models, the standard approach consisted of initializing convolutional
> backbones with supervised ImageNet pre-training [29] and fine-tuning them for downstream tasks such as defect
> classification, object detection, and segmentation. This strategy was particularly attractive in low-data
> industrial settings because pre-trained models improve optimization and reduce overfitting compared with
> training from scratch."

Its own experiments (Table 2, read directly) make the practical point crisply: on the RGB steel-surface
segmentation task (Severstal), ImageNet-pretrained and DINOv3-pretrained ConvNeXt‑T are nearly identical when
the backbone is **frozen** (62.04 vs 62.40 mIoU), and on X‑ray casting defect detection ImageNet pre-training
wins outright in both regimes (frozen 21.32 vs 7.88 box mAP@50; fully fine-tuned 29.74 vs 27.84).

**Status: arXiv preprint (2605.23472), not peer-reviewed.** Cite it as a 2026 preprint. It is nonetheless the
single most on-point citation I found, because its §2.2 exists precisely to state that supervised ImageNet
pre-training + fine-tuning is/was the standard paradigm in industrial inspection. Its bibliography also points to
a peer-reviewed survey that would be the better long-term citation once reachable:
Y. Cheng, Y. Cao, H. Yao, W. Luo, C. Jiang, H. Zhang, W. Shen, "A comprehensive survey for real-world industrial
surface defect detection: Challenges, approaches, and prospects," *Journal of Manufacturing Systems* 84:152–172
(2026), DOI 10.1016/j.jmsy.2025.11.022 — **not fetched, not verified** (Elsevier unreachable here).

### 2.7 Steel-defect transfer learning with concrete numbers

Two dated, published, abstract-level results (both listed in the table):

* Ibrahim & Tapamo 2025, *JAIT* 5:242–252 — an ensemble of **three pre-trained CNNs** with transfer learning,
  **100 %** classification accuracy on NEU and **99.27 %** on X‑SDD. Read from the article's abstract page. The
  per-model comparison table (and any from-scratch control) is not verified — the "HTML" full-text link on that
  OJS install returns an empty frame.
* Torabipour & Gandomi 2025, *Applied and basic Machine Intelligence research* 3(2):73–88 — **VGG16 + transfer
  learning** with attention modules, **99.98 %** on NEU‑CLS and **99.92 %** on NEU‑DET, described as
  *"an improvement of at least 4 % over the baseline VGG16 model."* The journal exposes only the abstract (HTML
  and a JATS XML metadata record, both read) and a PDF.

For a lecture, the honest framing is: *transfer learning from an ImageNet-pretrained CNN is now so standard in
steel-defect classification that papers using it report ≥99 % on NEU and treat "VGG16 with transfer learning" as
the baseline rather than the contribution.* The specific "ImageNet-pretrained vs from-scratch, same protocol"
number for a defect-classification dataset did not turn up in a form I could verify.

---

## 3. COULD NOT VERIFY

Explicit list of things asked for that I could **not** establish. Do not present these as facts.

1. **MVTec AD (CVPR 2019) baseline mean AUROC values.** Not obtained. The paper exists only as PDF at CVF /
   MVTec / IEEE; the IJCV extended version is on Springer; OpenAlex confirms no arXiv/OA HTML copy. I verified
   only *that* ImageNet-pretrained CNN feature descriptors were among the official baselines (abstract quote).
2. **Uninformed Students' mean MVTec AUROC.** The per-class "Ours (p=65)" values were readable; the mean row was
   beyond the truncation point. I did not find the mean in any reachable page. **Also unverified: whether the
   table I read is image-level or pixel-level AUROC** — the caption was not retrievable. Do not label it.
3. **A peer-reviewed industrial paper that runs the explicit "ImageNet fine-tune vs train-from-scratch"
   controlled comparison on a defect dataset** (e.g. NEU‑DET / DAGM 2007 / KolektorSDD / Magnetic Tile / BTAD).
   Not found. The closest verified statements are (a) the He et al. 2019 COCO study (not industrial),
   (b) the Gharbage et al. 2026 preprint's claim that ImageNet pre-training + fine-tuning is the standard
   low-data industrial recipe, and (c) soft "≥4 % over baseline VGG16" in Torabipour & Gandomi 2025 without
   confirmation that the baseline is ImageNet-pretrained.
4. **Natarajan et al. numbers.** Citation verified and *corrected*: the paper is **2017** IEEE ICIT, pp. 986–991,
   DOI 10.1109/ICIT.2017.7915495 (Vidhya Natarajan, Tzu-Yi Hung, Sriram Vaikundam, Liang-Tien Chia,
   Rolls-Royce@NTU Corporate Lab / NTU) — **not 2020**. Contents (what was transferred, frozen vs fine-tuned,
   dataset, metric, score) **not verified**: not open access, and no reachable full text (semanticscholar,
   infona, dr.ntu.edu.sg all blocked/human-verification).
5. **"He et al. 2020, Defect Detection in Thermal Image for FDM 3D Printed Parts."** Not verified at all — I did
   not retrieve a record for it. Treat the citation in the task brief as unconfirmed.
6. **"Ren et al. 2017, State-of-the-art on surface defect detection."** Not verified — no record retrieved.
7. **Datasets named in the brief that produced no verified result here:** DAGM 2007, KolektorSDD, Magnetic Tile
   Defect (MTD), MVTec LOCO, BTAD. PatchCore's abstract says *"we further report competitive results on two
   additional datasets"* (one of which its paper names as Magnetic Tile Defects), but I did not read that table,
   so **no MTD number is quoted**. (An AI-generated summary page claimed 97.9 % AUROC on MTD — I am *not*
   treating that as a source.)
8. **A direct quotation about ImageNet pre-training being "default/standard" from a peer-reviewed review paper.**
   The quotation in §2.6 is from a 2026 **preprint**. The peer-reviewed survey it cites (Cheng et al.,
   *Journal of Manufacturing Systems* 84:152–172, 2026) is a strong candidate but its text was unreachable.
9. **PatchCore's own few-shot/second-dataset numbers and its pixel-level Table 2/3** were beyond the truncation
   window; only the repo README's 98.1 % mean segmentation AUROC (WR50 baseline) and the 98.1/99.6 table in the
   README are verified.
10. **PaDiM's own image-level detection table (Table IV).** Not read; the 95.3 % / 97.9 % detection figures come
    from PatchCore's Table 1 (a third party's transcription).

---

## 4. Non-peer-reviewed cross-checks (clearly labelled)

* **anomalib 0.3.3 docs, "Awesome Anomaly Papers: Benchmark"** (README, NOT peer-reviewed):
  PatchCore seg 98.1 / cls 99.1; PaDiM seg 97.5 / cls 97.9; SPADE seg 96.5 / cls 85.5; STFPM 97.0 / 95.5;
  Patch-SVDD 95.7 / 92.1; AE‑SSIM seg 87.0.
  https://anomalib.readthedocs.io/en/0.3.3/research/papers.html
* **anomalib 0.3.3 docs, "Benchmark"** (own reimplementations, NOT peer-reviewed; numbers differ from the
  papers' own — e.g. PaDiM + Wide ResNet-50 image AUC 0.950, pixel AUC 0.979 in their runs, vs 97.9/97.5 as
  reported by the original authors). Useful only as a *cross-check on which backbones are used*
  (ResNet‑18 and Wide ResNet‑50, both ImageNet-initialised).
  https://anomalib.readthedocs.io/en/0.3.3/research/benchmark.html
* **alphaxiv AI-generated overviews** (explicitly an LLM summary, NOT the paper): used only to read the
  *abstracts* of PatchCore and PaDiM, both of which I cross-verified against the CVF and ar5iv pages.

---

## 5. URLs actually fetched / verified in this session

Fetched successfully (HTTP 200) and used above:

* https://openaccess.thecvf.com/content/CVPR2022/html/Roth_Towards_Total_Recall_in_Industrial_Anomaly_Detection_CVPR_2022_paper.html
* https://openaccess.thecvf.com/content_CVPR_2019/html/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.html
* https://openaccess.thecvf.com/content_CVPR_2020/html/Bergmann_Uninformed_Students_Student-Teacher_Anomaly_Detection_With_Discriminative_Latent_Embeddings_CVPR_2020_paper.html
* https://raw.githubusercontent.com/amazon-science/patchcore-inspection/main/README.md
* https://ar5iv.labs.arxiv.org/html/2106.08265  (PatchCore, arXiv 2106.08265)
* https://ar5iv.labs.arxiv.org/html/2011.08785  (PaDiM, arXiv 2011.08785)
* https://ar5iv.labs.arxiv.org/html/1911.02357  (Uninformed Students, arXiv 1911.02357)
* https://ar5iv.labs.arxiv.org/html/1911.02357v1
* https://ar5iv.labs.arxiv.org/html/1811.08883  (Rethinking ImageNet Pre-training, arXiv 1811.08883)
* https://ar5iv.labs.arxiv.org/html/2605.23472  (DINOv3 vs ImageNet, arXiv 2605.23472)
* https://www.alphaxiv.org/abs/2106.08265
* https://www.alphaxiv.org/abs/2011.08785
* https://api.openalex.org/works?filter=title.search:PaDiM%20patch%20distribution%20modeling
* https://api.openalex.org/works?filter=title.search:MVTec%20AD%20comprehensive%20real-world%20dataset&per_page=5&select=id,doi,title,publication_year,locations
* https://api.openalex.org/works?filter=title.search:voting-based%20anomaly%20classification%20metal%20surface%20inspection&select=id,doi,title,publication_year,type,primary_location,authorships,biblio
* https://www.mvtec.com/research-teaching/datasets/mvtec-ad
* https://anomalib.readthedocs.io/en/0.3.3/research/benchmark.html
* https://anomalib.readthedocs.io/en/0.3.3/research/papers.html
* https://ojs.istp-press.com/jait/article/view/683
* https://ojs.istp-press.com/jait/article/view/683/621  (returned an empty view — no content)
* https://abmir.yazd.ac.ir/article_3954.html?lang=en
* https://abmir.yazd.ac.ir/?_action=xml&article=3954&lang=en
* https://mediatum.ub.tum.de/1662158
* https://mediatum.ub.tum.de/1662158?style=full_text  (Bergmann PhD thesis landing page; the full-text view serves
  the PDF, which this tool cannot parse — so the thesis tables were *not* read)
* https://cea.hal.science/cea-03251821  and  /cea-03251821v1/document  (HAL copy of PaDiM; landing page loaded,
  `/document` is a PDF → rejected)
* https://www.ecva.net/papers.php , https://proceedings.mlr.press/ , https://ojs.aaai.org/index.php/AAAI/article/view/28153
  (reachability probes only, not used for content)
* https://example.com (reachability probe)

Attempted and **failed** (recorded so the parent knows what is blocked here):

* `arxiv.org` / `www.arxiv.org` / `export.arxiv.org` / `browse.arxiv.org` (all paths, abs + pdf + html):
  `fetch failed` or DNS failure. `ar5iv.labs.arxiv.org` worked intermittently instead.
* `openaccess.thecvf.com` **PDF** URLs, `www.mvtec.com/.../mvtec_ad.pdf`, `rd.springer.com/...pdf`,
  `cea.hal.science/.../document`, `mediatum.ub.tum.de/.../1662158.pdf`: `unsupported content type
  "application/pdf"` — the fetch tool cannot read PDFs, which is the single biggest limitation on this task.
* `link.springer.com` (fetch failed), `rd.springer.com` (cross-origin redirect to `idp.springer.com`),
  `link-proxy.springer.com` (not followed),
* `huggingface.co/papers/...` and `huggingface.co/buckets/huggingchat/papers-content/...` (the latter is a
  full-text **markdown mirror of arXiv papers** — high value if it can be reached from a different network)
* `web.archive.org` (all URLs, including archived `ar5iv` HTML), `scholar.archive.org`
* `semanticscholar.org`, `api.semanticscholar.org`, `paperswithcode.com`, `github.com`,
  `deepai.org`, `www.themoonlight.io` (HTTP 429 Vercel checkpoint)
* `core.ac.uk` (HTTP 403 Cloudflare, one timeout), `europepmc.org` (403), `www.mdpi.com` (403),
  `www.scilit.com` (403), `www.techrxiv.org` (403)
* `r.jina.ai` (text-extraction proxy — would have solved the PDF problem; not reachable)
* `en.wikipedia.org`, `www.google.com`, `scholar.google.com.tr`: `URL hostname resolves to a non-public IP
  address` (DNS filtered)
* `xxx.itp.ac.cn` (arXiv mirror; `getaddrinfo ENOTFOUND`), `dr.ntu.edu.sg` (HTTP 405, human verification),
  `www.frontiersin.org` (fetch failed), `www.arxiv-vanity.com` / `ar5iv.org` (cross-origin redirect to
  `ar5iv.labs.arxiv.org`, which itself sometimes worked and sometimes did not)
