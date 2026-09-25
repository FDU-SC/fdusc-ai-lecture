# Computer vision 2010–2020, and laws-of-AI claims — sourced briefing

Prepared 2026-09-19 for the AI-history lecture (chapter 1, "the computer-vision decade").
Working directory `/home/zecyel/slides/ch1`.

**How to read this.** Every non-obvious number has a URL. Where a number is widely
repeated but no primary source could be found, that is stated explicitly rather than
estimated. Section 9 lists everything that could not be verified. "Ensemble" is called
out wherever a headline number is not a single model, because that distinction is the
single most common error in retellings of this period.

**Metric warning.** "ILSVRC top-5 error" is top-5 classification error on the
**100,000-image test set** unless stated otherwise. ILSVRC had a standalone
classification task only in 2010–2013; in 2014–2016 classification error is a column
inside the **Classification+Localization (CLS-LOC)** task, and in 2017 there was **no
classification task at all**. Comparing the yearly "winning numbers" across the whole
run is therefore comparing slightly different task framings, though all are top-5 error.

---

## 1. The ImageNet / ILSVRC error trajectory

### 1.1 Results table

Official results pages (the primary source for every row):
[2010](https://image-net.org/challenges/LSVRC/2010/results.php) ·
[2011](https://image-net.org/challenges/LSVRC/2011/results.php) ·
[2012](https://image-net.org/challenges/LSVRC/2012/results) ·
[2013](https://image-net.org/challenges/LSVRC/2013/results.php) ·
[2014](https://image-net.org/challenges/LSVRC/2014/results.php) ·
[2015](https://image-net.org/challenges/LSVRC/2015/results.php) ·
[2016](https://image-net.org/challenges/LSVRC/2016/results.php) ·
[2017](https://image-net.org/challenges/LSVRC/2017/results.php)

| Year | Winning team | Method | Top-5 error (test) | Ensemble? | Runner-up | URL |
|---|---|---|---|---|---|---|
| 2010 | NEC-UIUC (NEC Labs America + UIUC + Rutgers) | SIFT + LBP with two non-linear coding representations + stochastic SVM | **28.19%** (reported as "flat cost" 0.28191) | Not stated (one described system) | XRCE, 33.65% (Fisher-kernel) | [link](https://image-net.org/challenges/LSVRC/2010/results.php) |
| 2011 | XRCE (Perronnin, Sanchez) | Fisher-kernel / Fisher vectors over SIFT-type features + linear classifiers | **25.77%** (flat cost 0.25770) | Not stated | UvA + Univ. of Trento, 31.01% | [link](https://image-net.org/challenges/LSVRC/2011/results.php) |
| 2012 | SuperVision (Krizhevsky, Sutskever, Hinton — U. Toronto) — "AlexNet" | 8-weight-layer CNN trained on raw pixels | **15.315%** with ImageNet Fall-2011 extra data; **16.422%** with supplied data only | **YES.** 15.315% = 5 CNNs + 2 CNNs pre-trained on Fall 2011; the 16.4% figure is itself a 5-CNN ensemble; a **single** CNN is 18.2% top-5 (val) | ISI (Univ. of Tokyo), 26.172% (SIFT/LBP/GIST/CSIFT Fisher vectors + linear classifiers) | [link](https://image-net.org/challenges/LSVRC/2012/results) |
| 2013 | Clarifai (Matthew Zeiler) | Multiple CNNs, plus an extra model trained on 5,000 categories | **11.197%** (with outside data); **11.743%** using only original data | **YES** (multiple models) | NUS, 12.953% | [link](https://image-net.org/challenges/LSVRC/2013/results.php) |
| 2014 | GoogLeNet (Szegedy et al., Google) | Inception modules, 22 weight layers, ~6.8M parameters, average pooling instead of FC | **6.656%** (CLS-LOC classification error) | **YES.** 7 independently trained GoogLeNet models, 144 crops/image | VGG (Simonyan & Zisserman, Oxford), 7.325–7.407% (ensemble); a **single** VGG net = 8.434% | [link](https://image-net.org/challenges/LSVRC/2014/results.php) |
| 2015 | MSRA (He, Zhang, Ren, Sun) | ResNet — deep residual learning | **3.567%** | **YES.** Ensemble of six residual nets (two of them 152-layer); **single** ResNet-152 = **4.49%** top-5 (validation) | ReCeption, 3.581% (method not disclosed) | [link](https://image-net.org/challenges/LSVRC/2015/results.php) |
| 2016 | Trimps-Soushen (Third Research Institute, Ministry of Public Security, P.R. China) | CNN ensemble; stochastic depth, data augmentation, layer pruning | **2.991%** | **YES** | ResNeXt, 3.031% | [link](https://image-net.org/challenges/LSVRC/2016/results.php) |
| 2017 | WMW / Momenta (Jie Hu, Li Shen, Gang Sun) | SENet — Squeeze-and-Excitation blocks | **2.251%** (CLS-LOC classification error) | **YES** | Trimps-Soushen, 2.481% | [link](https://image-net.org/challenges/LSVRC/2017/results.php) |

Supporting primary sources for the ensemble/single distinctions:

- AlexNet paper, NIPS 2012: winning top-5 **test** error 15.3% vs 26.2% for the
  second-best entry; the paper's own 15.3% averages seven CNNs (five plus two
  pre-trained on the entire Fall 2011 release). The single-CNN (18.2%), 5-CNN (16.4%)
  and 7-CNN (15.3%, test) figures are tabulated in Zeiler & Fergus, Table 2:
  <https://ar5iv.labs.arxiv.org/html/1311.2901> (Table 2). The official 2012 page
  independently lists 0.16422 for "using only supplied training data" and 0.15315 for
  "using extra training data from ImageNet Fall 2011 release".
- GoogLeNet ensemble: "We independently trained 7 versions of the same GoogLeNet model
  (including one wider version), and performed ensemble prediction with them." — §7,
  <https://arxiv.org/abs/1409.4842>
- ResNet ensemble: "We combine six models of different depth to form an ensemble (only
  with two 152-layer ones at the time of submitting). This leads to 3.57% top-5 error on
  the test set." Abstract/§4.3, <https://arxiv.org/abs/1512.03385>
- SENet: "Squeeze-and-Excitation Networks formed the foundation of our ILSVRC 2017
  classification submission which won first place and reduced the top-5 error to 2.251%,
  surpassing the winning entry of 2016 by a relative improvement of ~25%."
  <https://arxiv.org/abs/1709.01507>
- VGG: abstract says the team "secured the first and the second places in the
  localisation and classification tracks respectively" — i.e. GoogLeNet won
  classification, VGG won localization. <https://arxiv.org/abs/1409.1556>

**Single line for a slide:** 28.2% (2010, SIFT+LBP+SVM) → 25.8% (2011, Fisher vectors)
→ 15.3% (2012, AlexNet, 7-CNN ensemble) → 11.2–11.7% (2013, Clarifai) → 6.66% (2014,
GoogLeNet, 7-model ensemble) → 3.57% (2015, ResNet, 6-model ensemble; 4.49% single
model) → 2.99% (2016, Trimps-Soushen) → 2.25% (2017, SENet).

### 1.2 The human baseline

**Figure: 5.1% top-5 error — but it is one of two annotators and it is training-dependent.**
Source (now read directly, verbatim): Russakovsky et al., *IJCV* 2015, §6.4,
<https://ar5iv.labs.arxiv.org/html/1409.0575> (arXiv:1409.0575).

The paper's own summary table (Table 6, "Human classification results on the ILSVRC2012-2014
classification test set, for two expert annotators A1 and A2. We report top-5 classification error"):

| | Annotator A1 | Annotator A2 |
|---|---|---|
| Training/practice before the test | **500 images** | **100 images** |
| Test images labelled | **1500** | **258** |
| **Human top-5 error** | **5.1%** | **12.0%** |
| GoogLeNet error on the *same* sample | 6.8% | 5.8% |

Verbatim from §6.4.1:

> "We report results based on experiments with **two expert annotators**. The first annotator
> (A1) trained on 500 images and annotated 1500 test images. The second annotator (A2)
> trained on 100 images and then annotated 258 test images. The average pace of labeling was
> approximately **1 image per minute**…"
>
> "The human error was estimated to be **5.1%**. Thus, annotator A1 achieves a performance
> superior to GoogLeNet, by approximately 1.7%… comparing the two proportions with a z-test
> yields a one-sided p-value of p = 0.022."
>
> "As seen in Table 6, the final classification error is significantly worse, at
> approximately **12.0%** Top-5 error. The majority of these errors (48.8%) can be attributed
> to the annotator failing to spot and consider the ground truth label as an option. Thus, we
> conclude that **a significant amount of training time is necessary for a human to achieve
> competitive performance** on ILSVRC."

And the paper's framing of *why* it used experts:

> "We found the task of annotating images with one of 1000 categories to be an extremely
> challenging task for an **untrained** annotator. The most common error that an untrained
> annotator is susceptible to is a failure to consider a relevant class as a possible label
> because they are unaware of its existence. Therefore, in evaluating the human accuracy we
> relied primarily on **expert annotators** who learned to recognize a large portion of the
> 1000 ILSVRC classes."

**Caveats to state on the slide:**

1. The 5.1% is an **expert annotator who trained on 500 images first** — a second expert
   trained on only 100 images scored **12.0%**. "Human performance" here is not one number;
   it is a function of familiarity with the 1,000 classes.
2. It is **one annotator on a 1,500-image subsample**, extrapolated (the paper calls it an
   *estimate*), not a full 100,000-image test-set run.
3. Labelling ran at **~1 image per minute** — the comparison is a human with unlimited time
   per image, not a human under a reaction-time constraint.
4. The paper also computes an "**optimistic** human" (correct if *either* A1 or A2 got it):
   **2.4%** error on the 204 images both labelled, vs GoogLeNet's 4.9% on that sample. So even
   among experts, individual versus pooled performance differs by a factor of two.
5. For contrast, an untrained-human datapoint: AI Impacts ran their own small, explicitly
   non-representative, untimed trial (5 people, Karpathy's interface) and got 74–89% top-5
   accuracy, i.e. **11–26% error**, median 81% accuracy (19% error).
   <https://aiimpacts.org/time-for-ai-to-cross-the-human-performance-range-in-imagenet-image-classification/>
6. **The "5.0%" variant**: no primary source found. The primary figure is **5.1%**. Treat
   "5.0%" as a rounding/misquote unless a source surfaces.

### 1.3 Which model first beat the human baseline

Two different answers, and the difference matters:

- **First claim of a machine beating 5.1% (not a competition entry):** He, Zhang, Ren &
  Sun, "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet
  Classification", arXiv:1502.01852, submitted **6 February 2015**.
  - Multi-model result: **4.94% top-5 test error**, a "26% relative improvement over the
    ILSVRC 2014 winner (GoogLeNet, 6.66%)".
  - **But the 4.94% is an ensemble.** The paper's own single-model number is **5.71%
    top-5**, which does *not* beat 5.1%. Exact wording: "our PReLU network (PReLU-net)
    leads to a single-model result of 5.71% top-5 error, which surpasses all existing
    multi-model results. Further, our multi-model result achieves 4.94% top-5 error on
    the test set..." and "To our knowledge, our result is the first to surpass
    human-level performance (5.1%, Russakovsky et al.)".
    <https://arxiv.org/abs/1502.01852>
  - So the sentence "a single model first beat humans in February 2015" is **wrong**;
    the first *surpass* claim was an ensemble, and its single model did not yet beat 5.1%.
- **First ILSVRC competition entry under 5.1%:** ILSVRC **2015**, MSRA ResNet —
  **3.567% top-5 test** as a 6-model ensemble; the single ResNet-152 reached **4.49%
  top-5 validation**. The 2014 winner (GoogLeNet, 6.66%) was still above the human figure.
  Official page: <https://image-net.org/challenges/LSVRC/2015/results.php>; paper:
  <https://arxiv.org/abs/1512.03385>

### 1.4 When and why ILSVRC stopped

- **ILSVRC 2017 was the final competition.** The CVPR 2017 workshop was explicitly
  renamed the "**Beyond** ImageNet Large Scale Visual Recognition Challenge" workshop:
  "The workshop will mark the last of the ImageNet Challenge competitions, and focus on
  unanswered questions and directions for the future."
  <https://image-net.org/challenges/beyond_ilsvrc.php>
- The organizers' own announcement, ILSVRC2017 News, **26 Jul 2017**: "We are passing
  the baton to **Kaggle**. From now on, all three challenges (LOC-CLS, DET, VID) will be
  hosted on Kaggle!" <https://image-net.org/challenges/LSVRC/2017/index.php>
  Kaggle's replacement: <https://www.kaggle.com/c/imagenet-object-localization-challenge>
- ILSVRC2017 had only three tasks — object localization for 1000 classes, object
  detection for 200 classes, object detection from video for 30 classes. There was no
  classification task (the 2017 results page reports "classification error" only as a
  column in the CLS-LOC task).
- **Verification caveat:** the widely repeated causal reason — "it stopped because error
  had saturated below human level" — is *not* stated in any official sentence I could
  find. The official statements are (a) "last of the ImageNet Challenge competitions",
  (b) "focus on unanswered questions and directions for the future", (c) the move to
  Kaggle hosting. Attribute the saturation argument as *interpretation*, not as the
  organizers' stated reason. The ILSVRC2017 overview slide deck
  (<https://image-net.org/static_files/files/ILSVRC2017_overview.pdf>) is a PDF, which
  this environment cannot read; it may contain a fuller statement.

### 1.5 Pre-2012 state of the art (the "SIFT/HOG plus what classifier" answer)

- **2010 winner — NEC-UIUC, 28.19% top-5.** Components as described by the team:
  "using sift and lbp feature with **two non-linear coding representations** and
  **stochastic SVM**, optimized for top-5 hit rate". Runners-up used the same family:
  XRCE's "Fisher kernel framework" (Sanchez, Perronnin & Mensink, ECCV 2010).
  <https://image-net.org/challenges/LSVRC/2010/results.php>
- **2011 winner — XRCE, 25.77% top-5**, Fisher-kernel / Fisher-vector encoding with
  linear classifiers; second place UvA + Trento at 31.01% using selective search +
  Fisher-vector-style encodings.
  <https://image-net.org/challenges/LSVRC/2011/results.php>
- So the pre-2012 recipe in one line: **dense SIFT / LBP / colour descriptors →
  bag-of-words or Fisher-vector encoding (often with product quantisation) →
  one-vs-rest linear SVM**; for localization/detection, **HOG → deformable part models
  (DPM) → latent SVM**. The full 2012 Oxford pipeline is quoted in §5 below.
- The ILSVRC 2015 reference paper confirms the dataset scale at the start: ILSVRC2010 had
  1,261,406 training / 50,000 validation / 150,000 test images over 1000 classes
  (Russakovsky et al. 2015, Table 2), and the 2010 challenge was held as a
  "taster competition" alongside PASCAL VOC 2010.

---

## 2. The architecture progression

### 2.1 The "GoogLeNet matched VGG at one-twelfth the parameters" claim — VERDICT: WRONG AS STATED

This is the claim to fix before it reaches a slide. Two errors are folded into it.

1. **The "12×" in the literature is GoogLeNet vs AlexNet, not GoogLeNet vs VGG.** The
   GoogLeNet paper says verbatim: "Our GoogLeNet submission to ILSVRC 2014 actually uses
   **12× fewer parameters than the winning architecture of Krizhevsky et al** from two
   years ago, while being significantly more accurate." (arXiv:1409.4842, §1). The
   comparison target is **AlexNet (2012, ~60M parameters)**, not VGG.
2. **Against VGG the ratio is far bigger than 12× — roughly 20×.** GoogLeNet's own
   parameter table (§5, Table 1) sums to ≈**6.8M** parameters
   (2.7K + 112K + 159K + 380K + 364K + 437K + 463K + 580K + 840K + 1072K + 1388K + 1000K
   ≈ 6.80M). VGG-16's parameters sum to ≈**138.3M** (convolutional ≈14.71M; FC1
   7·7·512·4096 = 102.76M, FC2 4096² = 16.78M, FC3 4096·1000 = 4.10M — the arithmetic is
   laid out in the CS231n notes, <https://cs231n.github.io/convolutional-networks/>).
   So **138.3 / 6.8 ≈ 20×**, not 12×.

**Caveat worth flagging:** even the paper's own "12×" does not reconcile with the counts —
60M / 6.8M ≈ **8.8×**. The "12×" is the authors' own favourable rounding (it only works if
GoogLeNet is taken as ≈5M and AlexNet as ≈60M). So the honest slide claim is:

> "GoogLeNet matched VGG's accuracy with about one-twentieth of VGG's parameters — and it
> had roughly one-ninth to one-twelfth of AlexNet's parameters, the comparison the
> GoogLeNet authors themselves made."

Both halves are safe: the ~20× figure is arithmetic on the two papers' own tables, and the
"12×" is a direct quote from the GoogLeNet paper, clearly attributed as the authors' claim.

**(rest of this section: the architecture table.)**

### 2.2 Architecture table

Depth = weight layers unless stated. "Ens." marks a headline number that is an ensemble.

| Model | Year | Depth | Parameters | Key idea | ImageNet result | URL |
|---|---|---|---|---|---|---|
| **LeNet-5** | 1998 | 7 layers with trainable parameters | **340,908 connections** (paper §II); ≈60k trainable parameters is the commonly quoted total (the paper tabulates per layer: C1 156, S2 12, C3 1,516, …) | Convolution + sub-sampling + fully-connected layers trained by backpropagation on 32×32 images | **None** — MNIST digits, not ImageNet | [DOI 10.1109/5.726791](https://doi.org/10.1109/5.726791) |
| **AlexNet** | 2012 (NIPS) | 8 (5 conv + 3 FC) | **60M** (paper abstract) | ReLU, dropout, overlapping pooling, trained on **raw RGB pixels**, split across 2 GTX 580s | ILSVRC2012 **15.315% top-5 test** (ENS., 7 CNNs); supplied-data-only entry 16.422% (ENS., 5 CNNs); **single CNN 18.2% top-5 val** | [NeurIPS 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) |
| **ZFNet** | 2013 (ECCV 2014) | 8 (same topology as AlexNet) | **65M** (stated in the Clarifai ILSVRC2013 entry abstract) | **Deconvnet visualisation** used diagnostically to fix AlexNet: 7×7 first-layer filters, stride 2 | ILSVRC2013 winner as "Clarifai": **11.197% top-5 (outside data) / 11.743% (original data)**, multiple models (ENS.). The paper's own best is a **6-convnet ensemble at 14.8% test** on ILSVRC2012 | [arXiv:1311.2901](https://arxiv.org/abs/1311.2901) |
| **VGG-16** | 2014 (ICLR 2015) | 16 | **138M** | Uniform **3×3 convolutions** throughout; depth as the lever | ILSVRC2014 2nd in classification: **7.3% top-5 test with a 7-model ensemble** (ENS.); the paper's best single model is **7.0% test / 7.1% val**; the official competition page lists a single VGG ConvNet at **8.434%** | [arXiv:1409.1556](https://arxiv.org/abs/1409.1556) |
| **VGG-19** | 2014 | 19 | **144M** | Same, one block deeper | Same submission (config E) | [arXiv:1409.1556](https://arxiv.org/abs/1409.1556) |
| **GoogLeNet / Inception** | 2014 (CVPR 2015) | 22 | **≈6.8M** (sum of the paper's Table 1) | **Inception modules** with 1×1 dimension reduction; average pooling instead of FC; a 1.5B multiply-add budget | ILSVRC2014 **1st in classification: 6.656% top-5** (ENS., 7 models, 144 crops); paper claims "**12× fewer parameters than … Krizhevsky et al.**" | [arXiv:1409.4842](https://arxiv.org/abs/1409.4842) |
| **ResNet** | 2015 (CVPR 2016) | 18/34/50/101/**152** | ≈60M for ResNet-152 is the commonly quoted figure (**not tabulated in the paper text reachable here — flagged**) | **Residual (skip) connections** make very deep nets trainable | ILSVRC2015 **1st: 3.57% top-5 test** (ENS., 6 residual nets); **single ResNet-152 = 4.49% top-5 val** (top-1 19.38%) | [arXiv:1512.03385](https://arxiv.org/abs/1512.03385) |
| **DenseNet** | 2016 (CVPR 2017) | 121/169/201/264 | 8M/14M/20M/33M is the commonly quoted set (**not verified here — flagged**) | **Each layer connects to every subsequent layer** (L(L+1)/2 connections); feature reuse, fewer parameters | DenseNet-201: **top-5 6.34% single-crop / 5.54% 10-crop** (val); DenseNet-264 6.12% / 5.29%; DenseNet-121 7.71% / 6.66% | [arXiv:1608.06993](https://arxiv.org/abs/1608.06993) |
| **MobileNet** | 2017 (arXiv) | **28** (counting depthwise + pointwise as separate layers) | **4.2M** | **Depthwise separable convolutions**; width and resolution multipliers | MobileNet-224: **70.6% top-1** at 569M Mult-Adds | [arXiv:1704.04861](https://arxiv.org/abs/1704.04861) |
| **EfficientNet-B7** | 2019 (ICML) | compound-scaled | **66M** | **Compound scaling** of depth/width/resolution with a single coefficient | **84.3% top-1** ImageNet, single-crop single-model; "8.4× smaller and 6.1× faster" than the best existing ConvNet | [arXiv:1905.11946](https://arxiv.org/abs/1905.11946) |
| **ViT** | 2020 (ICLR 2021) | ViT-B 12 / ViT-L 24 / ViT-H 32 | **86M / 307M / 632M** (paper Table 1) | **Pure transformer on 16×16 image patches** — no convolutions; requires large-scale pre-training (ImageNet-21k, JFT-300M) | **ViT-H/14 with JFT-300M: 88.55% top-1** ImageNet; ViT-L/16 with only ImageNet-21k: 85.30% | [arXiv:2010.11929](https://arxiv.org/abs/2010.11929) |

**Reading the table.** Two patterns the lecture can actually use. (1) **Parameters stopped
being the point after 2014**: GoogLeNet beat VGG with ~1/20 the parameters, and MobileNet
reached 70.6% top-1 with 4.2M. (2) **Every single ILSVRC-winning headline from 2012 to 2017
is an ensemble**; the only year where the winning *number* is a plain single model is the
single-model figures quoted alongside them (ResNet-152's 4.49%, VGG's 7.0%).

---

## 3. The task progression

### 3.1 Object detection

| Model | Year + venue | First author | Key idea | Published mAP (exact benchmark) | URL |
|---|---|---|---|---|---|
| **R-CNN** | 2014, CVPR | Ross Girshick | Apply a high-capacity CNN to **bottom-up region proposals**, then fine-tune per-class SVMs; beats prior art by >30% relative | **PASCAL VOC 2012 mAP 53.3%** ("improves mAP by more than 30% relative to the previous best result on VOC 2012") | [arXiv:1311.2524](https://arxiv.org/abs/1311.2524) |
| **Fast R-CNN** | 2015, ICCV | Ross Girshick | One forward pass per image: **RoI pooling** on a shared conv feature map, multi-task loss (classification + box regression) in a single fine-tuning stage; 9× faster training, 213× faster test than R-CNN | **VOC 2007 test 70.0% mAP** (VGG16, Table 1); **VOC 2012 test 68.4%** (Table 3) | [arXiv:1504.08083](https://arxiv.org/abs/1504.08083) |
| **Faster R-CNN** | 2015, NIPS | Shaoqing Ren | **Region Proposal Network** shares full-image conv features with the detector, making proposals nearly free; RPN + Fast R-CNN merged into one network trained end to end | **VOC 2007 test 73.2% mAP** (07+12, VGG16); **VOC 2012 test 70.4%** (07++12); 5 fps including all steps | [arXiv:1506.01497](https://arxiv.org/abs/1506.01497) |
| **YOLO** | 2015 arXiv / CVPR 2016 | Joseph Redmon | Frame detection as **a single regression** from full image to spatially separated boxes + class probabilities — one network, end to end, no proposal stage | **VOC 2007 mAP 63.4% at 45 fps**; Fast YOLO **52.7% at 155 fps** | [arXiv:1506.02640](https://arxiv.org/abs/1506.02640) |
| **SSD** | 2015 arXiv / ECCV 2016 | Wei Liu | Discretise output space into **default boxes** at multiple scales/aspect ratios on multiple feature maps; single network, no proposal generation, no resampling | **VOC 2007 test 72.1% mAP for 300×300 at 58 fps**; **75.1% mAP for 500×500** — "outperforming a comparable state of the art Faster R-CNN model" | [arXiv:1512.02325](https://arxiv.org/abs/1512.02325) |
| **Mask R-CNN** | 2017, ICCV | Kaiming He | Add a **parallel mask branch** to Faster R-CNN (with RoIAlign); instance segmentation "without bells and whistles" | **COCO test mask AP 35.7** (ResNet-101-FPN, 5 fps); **37.1** best; **bbox AP 39.8** | [arXiv:1703.06870](https://arxiv.org/abs/1703.06870) |

**Detection before deep learning.** The canonical pre-deep detector is the **Deformable Part
Model (DPM)** — HOG features over a root filter plus deformable part filters, trained with a
latent SVM (Felzenszwalb, Girshick, McAllester & Ramanan, *PAMI* 2010,
[DOI 10.1109/TPAMI.2009.167](https://doi.org/10.1109/TPAMI.2009.167)). The R-CNN paper's own
framing of the pre-2014 state of the art is worth quoting: "The best-performing methods are
complex ensemble systems that typically combine multiple low-level image features with
high-level context."

*Flag:* a single authoritative pre-deep VOC mAP number is **not** given here. R-CNN's
"more than 30% relative improvement over the previous best on VOC 2012" implies the previous
best was ≈41% mAP (53.3/1.30), but that is **derived, not read off a leaderboard**. Take the
exact pre-deep VOC2010/2011/2012 winning mAP from the detection/segmentation workstream
before putting a number on a slide.

### 3.2 Semantic segmentation

| Model | Year + venue | First author | Key idea | Metric + number (exact) | URL |
|---|---|---|---|---|---|
| **FCN** | 2015, CVPR | Jonathan Long | Make classification nets **fully convolutional** so they take arbitrary-size input and produce same-size dense output; train pixels-to-pixels end to end by fine-tuning AlexNet/VGG/GoogLeNet; fuse a deep coarse layer with a shallow fine layer | **PASCAL VOC 2012: 62.2% mean IU** (a 20% relative improvement over prior state of the art) | [arXiv:1411.4038](https://arxiv.org/abs/1411.4038) |
| **U-Net** | 2015, MICCAI | Olaf Ronneberger | **Contracting path + symmetric expanding path** with skip connections, plus aggressive data augmentation, so it trains end to end "from very few images" | Wins the **ISBI 2015 cell-tracking challenge** "by a large margin" and beats the prior sliding-window CNN on the ISBI EM stack segmentation; 512×512 in <1 s on a GPU. ISBI 2012 EM: **warping error 0.000353** vs Cireşan 0.000420; ISBI cell tracking **IOU PhC-U373 0.9203** (vs 0.83) and **DIC-HeLa 0.7756** (vs 0.46). **Trained from scratch — no ImageNet transfer** | [arXiv:1505.04597](https://arxiv.org/abs/1505.04597) |
| **DeepLab (v2)** | 2016 arXiv / 2017 TPAMI | Liang-Chieh Chen | **Atrous (dilated) convolution** to control feature resolution; **atrous spatial pyramid pooling** for multi-scale context; fully-connected **CRF** to sharpen boundaries | **PASCAL VOC-2012 test 79.7% mIOU** (new state of the art at the time); also PASCAL-Context, PASCAL-Person-Part, Cityscapes | [arXiv:1606.00915](https://arxiv.org/abs/1606.00915) |

### 3.3 Face recognition: DeepFace and FaceNet on LFW

| Model | Year + venue | First author | Key idea | LFW accuracy | Exceeded human? | URL |
|---|---|---|---|---|---|---|
| **DeepFace** | 2014, CVPR | Yaniv Taigman (Facebook) | Explicit **3D face modelling** for piecewise-affine alignment + a **nine-layer DNN** with >120M parameters (locally connected, no weight sharing), trained on 4M faces / 4,000 identities | **97.35%** — "reducing the error of the current state of the art by more than 27%" | **No.** The paper's own words are "**closely approaching** human-level performance" — 97.35% < 97.53% (the cropped-human figure) | [CVF](https://www.cv-foundation.org/openaccess/content_cvpr_2014/html/Taigman_DeepFace_Closing_the_2014_CVPR_paper.html) |
| **FaceNet** | 2015, CVPR | Florian Schroff (Google) | Map faces to a compact Euclidean embedding trained with a **triplet loss** and novel **online triplet mining**; 128 bytes per face | **99.63%** (YouTube Faces 95.12%); "cuts the error rate in comparison to the best published result by 30%" | **Yes** — 99.63% exceeds both the 99.20% and 97.53% human figures below | [arXiv:1503.03832](https://arxiv.org/abs/1503.03832) |

**The human LFW baseline — and the caveat the lecturer wanted.** The figure usually quoted,
**97.53%**, comes from Kumar, Berg, Belhumeur & Nayar, "Attribute and Simile Classifiers for
Face Verification", **ICCV 2009** — and it is **not** the whole story. Reading the paper's
human-performance section directly:

- Human accuracy on the **original LFW images: 99.20%** — "At 99.20% accuracy, people are
  essentially perfect on this task."
- Human accuracy when shown only a **tight crop of the face: 97.53%** — the paper attributes
  this to "the lack of context available", and calls it "a **tripling of the error rate**".

So the commonly cited human baseline is the **degraded, tightly-cropped** condition. Under
the un-cropped condition humans score **99.20%**, and FaceNet's 99.63% is what actually beats
it. (Source PDF: <https://www.cs.columbia.edu/CAVE/publications/pdfs/Kumar_ICCV09.pdf>.)

**Protocol caveat to state on the slide.** LFW has two evaluation regimes —
**restricted** (no outside face data allowed) and **unrestricted with labelled outside data** —
and results across them are not directly comparable. Both DeepFace and FaceNet trained on
very large outside datasets, so their headline numbers are the *unrestricted* kind, while the
human figure is from the standard restricted protocol. Also note the human number is
itself protocol-dependent as shown above. State the protocol whenever you quote a number.

**Useful for §5:** DeepFace's own abstract describes the pre-deep face pipeline in four named
stages — "detect => align => represent => classify" — and then says the paper "revisits both
the alignment step and the representation step". That is a compact, quotable statement of the
hand-designed pipeline for the face domain.

### 3.4 Generation

Every FID/IS number below is given with its **exact variant** (reference split, sample
count, guidance scale), because this is the most misquoted area in the decade.

| Model | Year + venue | First author | Key idea | Quality metric + exact variant | URL |
|---|---|---|---|---|---|
| **GAN** | 2014, NIPS | Ian Goodfellow | Two networks in a minimax game: `G` maps noise to samples, `D` estimates whether a sample came from the data; at the optimum `G` recovers the data distribution and `D` = 1/2. Trainable by backprop, no Markov chains | **Parzen-window log-likelihood: MNIST 225 ± 2; TFD 2057 ± 26** (σ cross-validated). **No IS and no FID exist in this paper**; **CIFAR-10 is qualitative-only — there is no CIFAR-10 number to quote** | [arXiv:1406.2661](https://arxiv.org/abs/1406.2661) |
| **DCGAN** | 2015 arXiv / ICLR 2016 | Alec Radford | All-convolutional G/D, strided convolutions instead of pooling, batch norm, no FC hidden layers; discriminator features transfer as representations | **CIFAR-10 classification accuracy 82.8%** using ImageNet-1k-trained discriminator features + L2-SVM (in-paper baselines: K-means 80.6%, multi-layer K-means 82.0%); SVHN 22.48% error with only 1000 labels | [arXiv:1511.06434](https://arxiv.org/abs/1511.06434) |
| **pix2pix** | arXiv Nov 2016 / CVPR 2017 | Phillip Isola | Generic **conditional** GAN for image-to-image translation: U-Net generator + 70×70 PatchGAN discriminator, loss = L1 + cGAN — it *learns* the loss | **FCN-score 0.66** per-pixel accuracy on Cityscapes labels↔photos (ground truth 0.80); AMT "real vs fake" **18.9% ± 2.5%** (L1 baseline 0.8%) | [CVPR 2017](https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html), [arXiv:1611.07004](https://arxiv.org/abs/1611.07004) |
| **CycleGAN** | arXiv Mar 2017 / ICCV 2017 | Jun-Yan Zhu | **Unpaired** translation with two mappings plus a **cycle-consistency** loss `F(G(x))≈x` | AMT "real vs fake": **26.8% ± 2.8%** (map→photo), 23.2% ± 3.4%; FCN-score 0.52 vs pix2pix 0.71 on paired data | [ICCV 2017](https://openaccess.thecvf.com/content_ICCV_2017/papers/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.pdf) |
| **StyleGAN** | arXiv Dec 2018 / CVPR 2019 | Tero Karras | **Style-based generator**: mapping network `z→w`, `w` injected at every resolution via AdaIN, per-layer noise; releases FFHQ | **FID 4.40** on FFHQ 1024² (config f); CelebA-HQ 5.17. ⚠️ Variant: 50,000 images drawn from the **training** set, **lowest** FID over training | [CVPR 2019](https://openaccess.thecvf.com/content_CVPR_2019/papers/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.pdf) |
| **StyleGAN2** | arXiv Dec 2019 / CVPR 2020 | Tero Karras | Removes StyleGAN artifacts via **weight demodulation**, lazy regularization, no progressive growing; path-length regularization | **FID 2.84** on FFHQ 1024² (config f) vs StyleGAN's own 4.40 in the same table; LSUN Car 2.32. ⚠️ Variant: lowest-FID snapshot, averaged over 10 seeds | [CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/papers/Karras_Analyzing_and_Improving_the_Image_Quality_of_StyleGAN_CVPR_2020_paper.pdf) |
| **DDPM** | arXiv Jun 2020 / NeurIPS 2020 | Jonathan Ho | Learn to reverse a gradual Gaussian noising process; re-weighted variational bound with a denoising-score-matching connection | **CIFAR-10 unconditional FID 3.17, IS 9.46 ± 0.11**. ⚠️ Variant: FID against the **training** set; against the **test** set it is **5.24** | [NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf) |
| **LDM / Stable Diffusion** | arXiv Dec 2021 / CVPR 2022 | Robin Rombach | Run diffusion in the **latent space** of a pretrained autoencoder; U-Net with cross-attention for text conditioning — cuts cost dramatically vs pixel-space diffusion | **ImageNet 256² class-conditional FID 3.60, IS 247.67** (`LDM-4-G`, 250 DDIM steps, cfg 1.5; no guidance 10.56). Text-to-image MS-COCO FID 12.63 with a **1.45B**-param model on **LAION-400M**. ⚠️ Variant: 50k samples vs the entire training set | [CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/papers/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.pdf) |
| **DiT** | arXiv Dec 2022 / ICCV 2023 | William Peebles | Replace the U-Net backbone of latent diffusion with a plain **ViT on latent patches** (adaLN-Zero); quality scales with transformer Gflops | **ImageNet 256² FID-50K 2.27, IS 278.24** (`DiT-XL/2-G`, cfg 1.5; no guidance 9.62); 512² FID 3.04. ⚠️ Variant: FID-50K at 250 DDPM steps, ADM TensorFlow eval suite | [ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/papers/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.pdf) |

**Stable Diffusion compute — the "150,000 GPU-hours / 256 A100s" figure:**
this is **not in the LDM paper**. It comes from the released **Stable Diffusion v1 model
cards**: SD v1.5 and v1.4 both state `Hardware: 32 x 8 x A100 GPUs`, `Hardware Type:
A100 PCIe 40GB`, `Hours used: 150000`, `Carbon Emitted: 11250 kg CO2 eq.`
(<https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5>,
<https://huggingface.co/CompVis/stable-diffusion-v1-4>). The **paper** instead trained on a
single A100 and reports compute in V100-days: **271 V100-days vs ADM's 916** on
ImageNet-256² — its only "150" is "150–1000 V100 days" describing *prior* work (ADM).
The paper's text-to-image model used **LAION-400M**; the release used subsets of
**LAION-2B(en)**. And v1.5 was a 595k-step fine-tune of v1.2, so the identical 150,000 in
both cards reads as a project-level estimate — say "the SD v1 family", not "SD 1.5".
Safe phrasing and full quotes: `research/scratch/cv-facts/generation-vlm.md`.

### 3.5 Vision-language: CLIP and ViT

| Model | Year + venue | First author | Key idea | Headline number | URL |
|---|---|---|---|---|---|
| **CLIP** | arXiv Feb 2021 / ICML 2021 | Alec Radford (OpenAI) | Contrastive pre-training on **(image, text) pairs** — predict *which caption goes with which image*; at test time class names are embedded by the text encoder to synthesise a zero-shot classifier | **Zero-shot ImageNet top-1 76.2%** (top-5 95%), best model `ViT-L/14@336px`; up from a proof-of-concept 11.5% | [PMLR v139](https://proceedings.mlr.press/v139/radford21a/radford21a.pdf) |
| **ViT** | arXiv Oct 2020 / ICLR 2021 | Alexey Dosovitskiy (Google Brain) | Cut the image into **16×16 patches**, embed them, feed the sequence to a **standard Transformer — no convolutions at all**; works only with large-scale pre-training | **ViT-H/14 with JFT-300M: ImageNet top-1 88.55%**; ViT-L/16 with only ImageNet-21k: **85.30%** | [arXiv:2010.11929](https://arxiv.org/abs/2010.11929), [OpenReview](https://openreview.net/forum?id=YicbFdNTTy) |

CLIP details: **400M image–text pairs** (the WIT/WebImageText set) collected with
**500,000 queries** (all words occurring ≥100 times in English Wikipedia, plus high-PMI
bi-grams, article names and WordNet synsets; ≤20,000 pairs per query). Trained 32 epochs,
batch 32,768; eight models — five ResNets and three ViTs (`ViT-B/32`, `ViT-B/16`,
`ViT-L/14`). The largest ResNet took 18 days on 592 V100s; **`ViT-L/14` took 12 days on
256 V100s**, then one extra epoch at 336px. Why it mattered: zero-shot transfer with no
fixed label set, and markedly better robustness to distribution shift than equally
accurate supervised models.

ViT details: compute is reported in TPUv3-core-days — **2.5k** for ViT-H/14 (JFT-300M),
0.68k for ViT-L/16 (JFT), 0.23k for ViT-L/16 (ImageNet-21k) — vs BiT-L 9.9k and Noisy
Student 12.3k. JFT-300M = **303M images**. Why it mattered: it showed that **large-scale
pre-training, not convolution, is what drives performance**; the paper is explicit that on
ImageNet alone ViT underperforms comparable ResNets.
**Relationship:** CLIP used **two** image-encoder families, ResNet *and* ViT — verbatim:
"we experiment with the recently introduced Vision Transformer (ViT)"; its best model's
backbone is ViT-L/14.



---

## 4. What vision did to the rest of science and industry

### 4.1 Self-driving perception: when it switched to deep learning

The honest version of this story is that the switch is **not** datable by a single
announcement; it is visible in the progression of published systems. Three corrections to
the common retelling first:

- **"Mobileye's 2016 MultiNet" is a mis-attribution.** *MultiNet: Real-time Joint Semantic
  Reasoning for Autonomous Driving*, arXiv:1612.07695 (22 Dec 2016), is by Teichmann,
  Weber, Zöllner, Cipolla and Urtasun — University of Toronto / FZI Karlsruhe / University
  of Cambridge (plus Uber ATG in v2). No Mobileye-authored deep-learning-for-driving paper
  was found. What *is* verifiable for Mobileye is an industrial commitment: the 17 May 2016
  EyeQ5 announcement describes accelerators "optimized for … machine-learning tasks,
  including deep neural networks" (>12 TOPS, <5 W, samples H1 2018, full autonomous driving
  from 2020), and the 1 Jul 2016 BMW/Intel/Mobileye release targets L3–L5 by 2021.
- **"The 2012–2013 DARPA autonomous-vehicle context" is the wrong decade.** DARPA's Grand
  and Urban Challenges were **2004/2005/2007**. 2012–2013 is the DARPA *Robotics* Challenge
  (humanoids). `darpa.mil` was unreachable from this environment, so no DARPA primary
  document was read.
- **"Waymo's 2017 StarNet" is the wrong date.** StarNet is arXiv:1908.11069 (29 Aug 2019).
  arXiv:1704.05519 (18 Apr 2017) is a different work — Janai, Güney, Behl & Geiger,
  *Computer Vision for Autonomous Vehicles: Problems, Datasets and State of the Art*.

Verified timeline (each item fetched from the source named):

| Date | Item | What it shows |
|---|---|---|
| 1989 | Pomerleau, ALVINN (CMU tech report) | neural-network driving is *older* than the deep-learning era; ALVINN is a small 3-layer net on 30×32 images |
| ~Jul 2004 | DAVE (DARPA seedling; Net-Scale final report) | NVIDIA's own 2016 paper recounts DAVE's mean distance between crashes as ~20 m |
| 20 Mar 2012 | KITTI benchmark online; Geiger, Lenz & Urtasun, CVPR 2012 | 389 stereo+flow image pairs, 39.2 km odometry, >200k 3D object annotations. The KITTI changelog for 12 Nov 2012 adds "pre-trained **LSVM** baseline models" — i.e. the 2012 baseline is classical, not deep |
| 25 Apr 2016 | NVIDIA, *End to End Learning for Self-Driving Cars*, arXiv:1604.07316v1 (there is no v2) | 9 layers, ~27M connections / 250k parameters; 72 h of driving data as of 28 Mar 2016; "we are autonomous approximately **98%** of the time" on the Holmdel→Atlantic Highlands drive; 10 miles on the Garden State Parkway with zero intercepts; 30 FPS. **Trained from scratch — no ImageNet transfer anywhere in the paper.** "Nine months ago, a new effort was started at NVIDIA" ⇒ DAVE-2 began ≈ Jul 2015 |
| 22 Dec 2016 | Teichmann et al., *MultiNet*, arXiv:1612.07695 | The bridge case: **ImageNet-pretrained VGG-16 / ResNet-50/101 encoders fine-tuned on KITTI** ("classic fine-tuning pipeline"). KITTI road, 1st place at submission: MaxF1 94.88%, AP 93.71%; detection AP-moderate ResNet-101 89.79% vs Faster-RCNN 78.42%. Its Table 1 shows all six non-anonymous KITTI-road entries were already deep nets by Dec 2016 |
| 21 Aug 2017 | Shalev-Shwartz, Shammah & Shashua (Mobileye-affiliated), RSS | Safety formalisation, *not* a deep-learning perception result — evidence of Mobileye's direction but not of a perception switch date |
| 7–9 Dec 2018 | ChauffeurNet (Waymo: Bansal, Krizhevsky, Ogale), arXiv + Waymo blog | Deep learning demonstrably in Waymo's stack by 2018 |
| 29 Aug 2019 | StarNet (Waymo) | — |
| 10 Dec 2019 | Waymo Open Dataset | — |

**Could not find:** any dated published statement of *when* Google/Waymo switched perception
to deep learning. Waymo's own papers prove deep learning in use by 2018–2019 but state no
switch date. Treat any specific "Waymo switched in year X" claim as unsourced.
Company blog caveat: NVIDIA's 17 Aug 2016 blog post is a **company blog** and says "about a
year ago", inconsistently with the paper's own "nine months ago" (≈ Jul 2015).

### 4.2 ImageNet-pretrained backbones transferred to other domains

Two or three concrete, dated published results per domain. Full tables (8–10 results per
domain) are in `research/scratch/cv-facts/parts/`.

**Medical imaging**

| Result | Year | What transferred | Number | URL |
|---|---|---|---|---|
| CheXNet (Rajpurkar et al.) | 2017 (**arXiv only — no peer-reviewed venue found**) | DenseNet-121, ImageNet weights, fine-tuned end to end | NIH ChestX-ray14 pneumonia **AUROC 0.7680** vs Wang et al. 0.633 and Yao et al. 0.713; radiologist F1 0.435 vs 0.387.  ⚠️ the widely repeated "0.7681" is not in the paper — Table 2 says **0.7680** | [arXiv:1711.05225](https://arxiv.org/abs/1711.05225) |
| Esteva et al., *Nature* 542:115–118 | 2017 | GoogLeNet Inception-v3 pre-trained on ILSVRC (1.28M images), final layer removed, all layers fine-tuned | 3-class accuracy **72.1 ± 0.9%** vs **dermatologists at 65.56% / 66.0%** (two comparison groups of 21+ board-certified dermatologists); 9-class 55.4 ± 1.7% vs 53.3/55.0%; biopsy-proven tasks AUC >91% | [DOI 10.1038/nature21056](https://doi.org/10.1038/nature21056) |
| Raghu et al. *Transfusion*, NeurIPS 2019 — **the important negative result** | 2019 | ResNet-50 / Inception-v3, fine-tuned vs random init | Retina AUC **96.4 → 96.7** (noise); CheXpert mixed; clear gain only at small scale — **5k images: 92.2% → 94.6%**; benefit attributed mostly to **over-parameterisation/weight scaling, not feature reuse** | [arXiv:1902.07208](https://arxiv.org/abs/1902.07208) |

⚠️ **All three of the most-cited medical transfer results lack a from-scratch control**
(Wang 2017, CheXNet, Esteva). They show transfer *works*, not that it beats training from
scratch. The papers that ran the comparison — Shin et al. TMI 2016
([PMC4890616](https://pmc.ncbi.nlm.nih.gov/articles/PMC4890616/): 86% sensitivity @3 FP/patient
vs 78%/70% prior) and Tajbakhsh et al. TMI 2016 — find fine-tuning wins or ties, and is more
data-efficient.

**Satellite / remote sensing**

| Result | Year | What transferred | Number | URL |
|---|---|---|---|---|
| Risojević & Stojnić, "Do we still need ImageNet pre-training in remote sensing scene classification?" | 2022 | ResNet-50 ImageNet, fine-tuned vs scratch | At **20% training data**: UCM **58.93% → 94.64%**, AID **79.14% → 94.40%**, RESISC45 **85.44% → 93.85%**. At 80% data the gap shrinks (<1% on large sets) | [DOI 10.5194/isprs-archives-XLIII-B3-2022-1399-2022](https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-1399-2022) |
| Castelluccio et al. (**preprint**) | 2015 | CaffeNet + GoogLeNet ImageNet, fine-tuned vs scratch vs frozen | UC Merced: GoogLeNet fine-tuned **97.10%**, ~10% better than scratch. **But the same paper inverts on NIR Coffee Scenes: GoogLeNet from scratch 91.83% beat fine-tuned 90.75%** | [arXiv:1508.00092](https://arxiv.org/abs/1508.00092) |
| Sumbul et al., BigEarthNet, IGARSS 2019 | 2019 | shallow CNN trained in-domain vs ImageNet-pretrained CNN | "a **shallow** CNN architecture trained on BigEarthNet provides much higher accuracy compared to a state-of-the-art CNN model pre-trained on ImageNet" | [DOI 10.1109/IGARSS.2019.8900532](https://doi.org/10.1109/IGARSS.2019.8900532) |

⚠️ **Penatti et al. 2015 is routinely mis-cited**: its own abstract says off-the-shelf
ImageNet ConvNet features were **beaten by a low-level colour descriptor (BIC, 87.0%)** on NIR
remote sensing; they won only on RGB *aerial* imagery.

**Microscopy**

| Result | Year | What transferred | Number | URL |
|---|---|---|---|---|
| Caicedo et al., 2018 Data Science Bowl, *Nature Methods* 16:1247–1253 | 2019 | **all three winning teams used natural-image pretraining** (1st: ImageNet encoders; 2nd: ImageNet+COCO FPN; 3rd: COCO Mask R-CNN), fine-tuned | 1st place score **0.6316**, mean **F1 0.7120**, recall@IoU0.7 77.62% vs classical CellProfiler **0.5281 / 0.6280 / 59.35%** | [DOI 10.1038/s41592-019-0612-7](https://doi.org/10.1038/s41592-019-0612-7) |
| Xu et al., *BMC Bioinformatics* 18:281 | 2017 | ImageNet AlexNet **fc2 features, frozen** + linear SVM | Brain-tumour classification **97.8%** vs handcrafted 77.8% and whole-image CNN 62.2%; colon binary 98.0% vs 90.1% | [DOI 10.1186/s12859-017-1685-x](https://doi.org/10.1186/s12859-017-1685-x) |

⚠️ **Counterexamples matter here.** **U-Net (2015) was trained from scratch** and still beat
the field on ISBI 2012/2015, and **Litjens et al. 2016 (*Sci Rep* 6:26286) is commonly
described as ImageNet-pretrained but is not** — a full-text grep finds "ImageNet" only in its
reference list; it is a from-scratch result (prostate AUC 0.99).

**Industrial inspection / defect detection** — structurally different: the dominant methods
use an ImageNet backbone **frozen, with no training on the target dataset at all**.

| Result | Year | What transferred | Number | URL |
|---|---|---|---|---|
| PatchCore (Roth et al.), CVPR 2022 | 2022 | **WideResNet-50 ImageNet, FROZEN — no target-dataset training** | MVTec AD **image AUROC 99.1%** (single model) vs SPADE 85.5, PatchSVDD 92.1, PaDiM 95.3. ⚠️ the abstract's "up to 99.6%" is the *ensemble* | [arXiv:2106.08265](https://arxiv.org/abs/2106.08265) |
| PaDiM (Defard et al.), ICPR 2020 Workshops | 2020 | ResNet-18 / WideResNet-50-2 / EfficientNet-B5, "all pretrained on ImageNet", **frozen** | MVTec AD localisation **AUROC 97.1%, PRO 90.8%** (PaDiM-R18) | [arXiv:2011.08785](https://arxiv.org/abs/2011.08785) |

**Agriculture**

| Result | Year | What transferred | Number | URL |
|---|---|---|---|---|
| Mohanty, Hughes & Salathé, *Front. Plant Sci.* 7:1419 | 2016 | **AlexNet and GoogLeNet, ImageNet-pretrained**, all layers fine-tuned ("we do not limit the learning of any of the layers") | PlantVillage 80-20 colour split: GoogLeNet transfer **99.35%** accuracy (F1 0.9934), AlexNet transfer 99.28%. **Rare matched from-scratch control: GoogLeNet 98.37%, AlexNet 97.82%.**  ⚠️ **Same paper, field conditions: 31.40% / 31.69%** on 121/119 real-world images — the lab-condition number does not transfer to the field | [DOI 10.3389/fpls.2016.01419](https://doi.org/10.3389/fpls.2016.01419) |
| Olsen et al., *DeepWeeds*, *Sci. Rep.* 9:2058 | 2019 | ResNet-50 + Inception-v3, **ImageNet weights** (confirmed in the authors' own code), fine-tuned | DeepWeeds (17,509 images, 9 classes): ResNet-50 **95.7%** mean accuracy, Inception-v3 95.1%; 53.4 ms/image | [DOI 10.1038/s41598-018-38343-3](https://doi.org/10.1038/s41598-018-38343-3) |
| Bargoti & Underwood, *Deep Fruit Detection in Orchards* | 2016 | Faster R-CNN "initialising the DCNN **directly from ImageNet features**" | F1 > 0.9 for apples and mangoes.  ⚠️ **Cross-orchard (domain-specific) pre-training gave "negligible performance gain" over plain ImageNet init** | [arXiv:1610.03677](https://arxiv.org/abs/1610.03677) |

⚠️ Counterexample: Dyrmann et al. 2016 built their plant-species classifier **from scratch**
(86.2% accuracy) — deliberate, with no pretrained comparison.
Corrections: DeepWeeds is **Olsen et al.**, not "Lee et al."; "WeedNet 2016" is a conflation
(the real work is Sa et al., IEEE RA-L, [DOI 10.1109/LRA.2017.2774979](https://doi.org/10.1109/LRA.2017.2774979)).
**No accuracy number could be verified for Ferreira et al. 2017 or Grinblat et al. 2016** —
do not print one.

**Cross-cutting conclusion (this is the slide-worthy part).** The honest shape of the
evidence is **not** "ImageNet pretraining always wins":

1. It transfers broadly and **dramatically in the small-data regime** (Risojević 20% data:
   58.9%→94.6%; Transfusion 5k: 92.2%→94.6%).
2. **At large data scale the advantage shrinks to noise or vanishes** — Transfusion
   (96.4→96.7 AUC) and He et al. 2019 *Rethinking ImageNet Pre-training* (COCO Mask R-CNN:
   random init 41.3 AP vs ImageNet-pretrained 41.1; ResNeXt-152 scratch 50.9 vs 50.3).
3. **Domain distance can flip the answer** (Castelluccio NIR; Ciga et al. 2020 in-domain
   self-supervision beating ImageNet for histopathology classification, 41.1→69.3 frozen
   macro-F1, while ImageNet still wins for segmentation).
4. In **industrial anomaly detection** it is load-bearing — frozen backbones hit 99.1% AUROC.
5. **Some celebrated results involve no transfer at all**: NVIDIA DAVE-2 (self-driving) and
   U-Net (microscopy) were trained from scratch; Litjens 2016 is mis-described as pretrained.

### 4.3 Evidence that ImageNet fine-tuning became the default assumption

This is a strong, quotable set (first author, date and the exact framing):

- **Razavian et al., Mar 2014** (arXiv:1403.6382), on off-the-shelf CNN features:
  "should be the **primary candidate in most visual recognition tasks**".
- **Yosinski et al., NIPS 2014**, on transferability of features — the canonical
  fine-tuning study.
- **Shin et al., Feb 2016** (medical) still writes that ImageNet fine-tuning on medical
  data "has not yet been exploited" — i.e. the default had not yet arrived in medicine.
- **Wang et al., CVPR 2017**: "this situation **does not apply to the medical image
  diagnosis domain**" — confirming the lag by domain.
- **He et al., Nov 2018**: calls ImageNet pre-training + fine-tuning "the **current de facto
  paradigm** of 'pre-training and fine-tuning'".
- **Raghu et al., NeurIPS 2019**: in medical imaging it "has become a **de-facto method**" /
  "the present standard".
- **Peng et al., 2021**: "the **norm**".
- Teaching-level corroboration from the course notes that trained this generation:
  "**In practice: use whatever works best on ImageNet** … download a pretrained model and
  finetune it on your data. You should rarely ever have to train a ConvNet from scratch or
  design one from scratch." — CS231n notes, <https://cs231n.github.io/convolutional-networks/>

The lag structure is the interesting lecture point: ImageNet transfer was the *default* in
general vision by ~2014, but was still being argued for in medical imaging as late as
2016–2019.

---

## 5. The "pipeline collapse": hand-designed stages → one end-to-end network

### 5.1 A citable statement of the shift

The cleanest single citable statement is Yann LeCun's own 2014 formulation, which uses
the exact vocabulary of the claim ("feature extractor", "trained end to end"):

> "A key component in systems that can understand natural data is a module that turns the
> raw data into an suitable internal representation. But designing and building such a
> module, often called a **feature extractor**, requires a considerable amount of
> engineering efforts and domain expertise. The main objective of 'Deep Learning' is to
> come up with learning methods that can automatically produce good representations of
> data from labeled or unlabeled samples. Deep learning allows us to construct systems
> that are **trained end to end, from raw inputs to ultimate output**. Instead of having a
> separate feature extractor and perdictor, deep architectures have multiple stages in
> which the data is represented hierarchically..."
>
> — Yann LeCun, "Deep Learning and the Representation of Natural Data", IEEE CIS
> Resource Center, 6 July 2014, DOI [10.17023/whp2-fq91](https://dx.doi.org/10.17023/whp2-fq91)
> (sic: "an suitable", "perdictor"). URL:
> <https://resourcecenter.cis.ieee.org/conferences/wcci-2014/ciswcci2014con0060>

The canonical *review* citation is LeCun, Bengio & Hinton, "Deep learning", *Nature* 521,
436–444 (2015), DOI [10.1038/nature14539](https://doi.org/10.1038/nature14539), which
makes the same argument at book length in a few pages. **I could not read the Nature page
from this environment** (nature.com redirects to an identity provider, `idp.nature.com`,
and the PDF is not fetchable here), so I deliberately do **not** quote a verbatim
sentence from it. The 2014 LeCun abstract above is fetchable and makes the same point.

The end-to-end side is documented in the winner's own words on the official 2012 results
page (SuperVision's abstract): "Our model is a large, deep convolutional neural network
**trained on raw RGB pixel values**. The neural network, which has 60 million parameters
and 650,000 neurons, consists of five convolutional layers ... and three globally-connected
layers with a final 1000-way softmax."
<https://image-net.org/challenges/LSVRC/2012/results>

### 5.2 One concrete pre-2012 pipeline, with every stage named

The **OXFORD_VGG entry to ILSVRC 2012** (Simonyan, Aytar, Vedaldi, Zisserman) is a fully
documented, named chain of hand-designed stages. Quoting the official team abstract:

1. "two types of local patch features were **densely extracted over multiple scales: SIFT
   and colour statistics**";
2. "The features were then augmented with patch spatial coordinates and **aggregated into
   two Fisher vectors** corresponding to the two feature types";
3. "Fisher vectors were computed using **GMMs with 1024 Gaussians**, resulting in
   **135K-dimensional** representations";
4. "the two Fisher vectors were then **stacked** ... We did not use spatial pyramid representation";
5. "To be able to deal with large amounts of training data, **product quantisation** was
   employed to compress the image features";
6. "Finally, an **ensemble of one-vs-rest linear SVMs** was trained over stacked features
   using stochastic sub-gradient method (**Pegasos**)";
7. localization: "**DPM (discriminatively trained part based models)** detectors ... The
   DPM detectors are boosted via harvesting more bounding boxes ... Using the validation
   set the top 5000 images for each class are shortlisted via image classification score
   and then detection is performed using DPMs";
8. "for each class, a **high-level SVM** is trained over the image classification score,
   DPM max-detection score and the score from fine-level bounding box classification."

Source: <https://image-net.org/challenges/LSVRC/2012/results> (Team information → OXFORD_VGG).
That entry scored 26.98% top-5, i.e. it is the *same generation* as the pre-2012 state of
the art, and its eight-stage chain is exactly the "pipeline" that the 2012 CNN replaced.

Two more documented pre-2012 chains from the same page, useful if you want to show the
pattern is not one lab's quirk:

- **ISI (Univ. of Tokyo), 26.17%, second place 2012:** "We extract conventional **Fisher
  Vectors** ... and a streamlined version of **Graphical Gaussian Vectors**. For
  extraction, we use not only common **SIFT and CSIFT, but also LBP and GIST** in a
  dense-sampling manner. We train **linear classifiers using Passive-Aggressive**
  algorithm. Then we investigate two strategies to combine scores from each feature's
  classifier." For localization: "We extract **HOG descriptors** from each sliding window.
  We use the **cascade object detection with deformable part models**, restricting the
  sizes of bounding boxes."
- **XRCE/INRIA, 27.06%:** "SIFT ... and the colour features ... aggregated into image-level
  features using the **Fisher Vector** ... compressed with **Product Quantization** ...
  We train **linear SVMs** in a one-vs-rest manner."

### 5.3 The one-line summary

Before 2012: descriptor → encoder (BoW/Fisher) → quantiser → linear classifier, plus
DPM/HOG + latent SVM for localization — every stage designed by hand, and the system's
design effort concentrated in the feature extractor. From 2012: one CNN, raw RGB pixels
in, 1000-way softmax out, trained by backpropagation end to end; ILSVRC 2012–2017 was won
by a CNN every year.

---

## 6. The Densing Law

**Verdict: the paper is real and the "≈3.3 months" number is real, but three details in
the claim as stated are wrong or need qualification — the author/affiliation, the metric,
and the exact doubling time.**

### 6.1 The paper

| Field | Value |
|---|---|
| Title (preprint) | **Densing Law of LLMs** |
| arXiv | **2412.04315** — v1 submitted 5 Dec 2024; v2 6 Dec 2024 |
| Published as | **"Densing law of LLMs"**, *Nature Machine Intelligence* **7**(11): 1823–1833 |
| Published online | **6 November 2025** (received 11 Jan 2025; accepted 22 Sep 2025) |
| Journal DOI | **10.1038/s42256-025-01137-0** |
| Authors | Chaojun Xiao, Jie Cai, Weilin Zhao, Guoyang Zeng, Biyuan Lin, Jie Zhou, Zhi Zheng, Xu Han, Zhiyuan Liu, Maosong Sun |
| Affiliations | **Tsinghua University + ModelBest Inc. (面壁智能) + OpenBMB** |

Sources: <https://arxiv.org/abs/2412.04315> ·
<https://api.crossref.org/works/10.1038/s42256-025-01137-0> ·
<https://www.tsinghua.edu.cn/en/info/1245/14611.htm>

> **Correction to the brief:** **Lingpeng Kong is not an author**, and there is **no Hong
> Kong / HKU affiliation**. This is a Tsinghua (Sun Maosong / Liu Zhiyuan / Han Xu group)
> + ModelBest + OpenBMB paper. The "HKU group" memory is a misattribution.

### 6.2 The exact claim, verbatim

Preprint abstract (arXiv v2 / ar5iv):

> "Our further analysis of recent open-source base LLMs reveals an empirical law (Densing
> Law) that the capability density of LLMs grows exponentially over time. More specifically,
> using some widely used benchmarks for evaluation, **the capability density of LLMs doubles
> approximately every three months.**"

Formal statement (Highlights / §1.1):

> "**Densing Law.** The maximum capability density of LLMs exhibits an exponential growth
> trend over time. ln(ρ_max) = A·t + B. Here, ρ_max is the maximum capability density of
> LLMs at time t."

The precise 3.3-month figure is in the **Figure 1 caption plus its footnote**:

> "A trend is fitted between maximum capability density and release date, revealing that
> **A ≈ 0.007** with **R² ≈ 0.93**. This indicates the maximum capability density of LLMs
> **doubles approximately every 3.3 months**. … Footnote: The capability density growth
> rate is affected by specific evaluation benchmarks and reference models."

**Published version says 3.5 months, not 3.3.** The *Nature Machine Intelligence*
abstract (25 Sep 2025 acceptance / 6 Nov 2025 online) reads: "the maximum capability
density of open-source LLMs **doubles approximately every 3.5 months**."

**Recommended lecture phrasing:** "roughly **3–3.5 months**, depending on whether you
quote the 2024 preprint or the 2025 *Nature Machine Intelligence* version." Quoting
"3.3 months" alone implies a precision the published version does not repeat.
Note also that ln 2 / 0.007 ≈ 99 days ≈ 3.3 months, so `t` in the fitted exponent must be
in **days**; the unit is inferred from arithmetic, not stated in the reachable text.

### 6.3 What "capability density" actually is — not "performance per parameter"

This is the substantive correction. Verbatim definition (§2.1, eq. 1):

> "**ρ(M) = N̂(S_M) / N_M = f⁻¹(S_M) / N_M**"

where the *effective parameter size* is "the parameter size required by a reference model
to achieve equivalent performance". So

**density = (parameter count a reference model would need to match this model's score) ÷
(this model's actual parameter count)** — a *relative* quantity (the paper's own term is
"(relative) capability density") tied to a fitted scaling curve, not a raw
benchmarks-per-parameter ratio and not a log-of-parameters normalisation.

The construction: fit a conditional-loss power law `L = a·N^(−α) + b·D^(−β)` on small
reference models (0.005B–0.8B, Table 1), fit loss→score with a sigmoid
`S = c/(1 + e^(−γ(L−l))) + d`, then invert at a **fixed training-data size D₀ = 1T tokens**.
Consequences worth stating: the metric is an inverse-scaled effective parameter count;
because D is pinned, it is *not* capability per unit training compute; and densities are
only comparable within the paper's MiniCPM-3-derived reference frame.

### 6.4 Scope, caveats, and the "three months" memory

- **Scope (preprint):** 29 open-source **base** (pre-trained, not instruction-tuned) models,
  evaluated on **5** benchmarks: MMLU, BBH, MATH, HumanEval, MBPP. Models released before
  Llama-1 are excluded as unable to score meaningfully, so the window is ≈ **Feb 2023
  (Llama-1) → Dec 2024**; the published version covers **51 models, Feb 2023 – Apr 2025**.
- **Caution:** one HTML rendering says "55 widely-used benchmarks"; that is a LaTeX
  artifact of "**5**". Do not repeat "55". Similarly, the arXiv *metadata* abstract says
  "**capacity density**" while the body and published version say "**capability density**";
  the latter is the one to use.
- The authors' own footnote flags that the rate depends on the benchmarks and reference
  models chosen — i.e. the constant is not universal.
- **Criticism / replication:** no peer-reviewed criticism or replication attempt was found
  (all 57 citing works as of Sep 2026 were checked). One press item claims METR
  independently corroborates "88.6 days"; that is a **category error** — METR's actual
  published result is **212 days (171–249)** for a different metric (50% task-completion
  time horizon, arXiv:2503.14499), not capability density.
- **Probable origin of the "~3.x months" memory:** Amodei & Hernandez, "AI and Compute"
  (OpenAI, 2018) found **training compute** doubling every **~3.4 months** (2012–2018) —
  a different quantity entirely. Do not conflate the two.

Working file with the full audit trail: `research/scratch/cv-facts/densing-and-laws.md`.

---

## 7. Laws-of-AI claims

### 7.1 Laws table

| Law | Original author | Date | Exact original statement | Best application to AI | URL |
|---|---|---|---|---|---|
| **Goodhart's law** (original) | Charles Goodhart | presented July 1975; the sentence is best documented at p.96 of his 1984 *Monetary Theory and Practice* | "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." | Any metric used as a training or governance target (benchmark scores, RLHF reward models, KPI-driven evaluation) degrades as a measure once optimised against | [DOI 10.1007/978-1-349-17295-5](https://doi.org/10.1007/978-1-349-17295-5) |
| **Popular "measure → target" form** | **Keith Hoskin** (coined, 1996); **Marilyn Strathern** (popularised, 1997) | 1997 | "When a measure becomes a target, it ceases to be a good measure." (*European Review* 5(3):305–321, at p.308) | The form everyone actually quotes — including for AI benchmarks | [DOI 10.1002/(SICI)1234-981X(199707)5:3<305::AID-EURO184>3.0.CO;2-4](https://doi.org/10.1002/(SICI)1234-981X(199707)5:3%3C305::AID-EURO184%3E3.0.CO;2-4) |
| **The Bitter Lesson** | Richard S. Sutton | **13 March 2019** | "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin." | Argues for search + learning scaled by compute over hand-built domain knowledge — the same argument the CNN-vs-handcrafted-features transition makes | <http://www.incompleteideas.net/IncIdeas/BitterLesson.html> |
| **Amdahl's law** | Gene M. Amdahl | 1967, AFIPS Spring Joint Computer Conference, pp. 483–485 | *S* = 1 / ((1 − *p*) + *p*/*s*); as *s* → ∞, *S* → 1/(1 − *p*) | Why parallelising training/inference hits a serial-fraction ceiling; contrast Gustafson (1988) for scaled-problem speedup | [DOI 10.1145/1465482.1465560](https://doi.org/10.1145/1465482.1465560) |
| **Wright's law** | Theodore P. Wright | Feb 1936, *J. Aeronautical Sciences* 3(4):122–128 | *C*ₙ = *C*₁·*n*^(−*b*); learning rate = 1 − 2^(−*b*) — each doubling of **cumulative production** cuts unit cost by a constant percentage | Frequently invoked for AI compute/model cost, but see 7.2 below: **no peer-reviewed application to AI exists** | [DOI 10.2514/8.155](https://doi.org/10.2514/8.155) |
| **Roofline model** | Williams, Waterman & Patterson | April 2009, *CACM* 52(4):65–76 (tech report 17 Oct 2008) | attainable perf = min(peak FLOP/s, arithmetic intensity × peak memory bandwidth), where intensity = FLOPs ÷ bytes of DRAM traffic | Explains why LLM **decode** is memory-bandwidth-bound, not FLOP-bound | [DOI 10.1145/1498765.1498785](https://doi.org/10.1145/1498765.1498785) |
| **Zipf's law** | George Kingsley Zipf | 1935 (*The Psycho-Biology of Language*), 1949 (*Human Behavior…*) | *f*(*r*) ∝ 1/*r*^α, with α ≈ 1 | Motivates subword tokenisation and the long tail of training data | [DOI 10.3758/s13423-014-0585-6](https://doi.org/10.3758/s13423-014-0585-6) |

### 7.2 Detail and corrections

**Goodhart — three corrections.**
1. The popular form is **not Goodhart's**. It was **coined by Keith Hoskin (1996)** and
   **popularised by Marilyn Strathern (1997)**, at p.308 of "Improving ratings: audit in the
   British university system", *European Review* 5(3):305–321.
2. Strathern **credited Hoskin**, not Goodhart directly. Secondary literature is explicit:
   McIntyre writes "following Hoskin (1996)"; Majka & El-Mhamdi (arXiv:2505.23445) describe
   it as a "reformulation by Keith Hoskin … popularisation by Marylin Strathern".
3. The **original** Goodhart sentence is the statistical-regularity one above. **Unresolved:**
   whether the 1975 conference paper already contains that exact sentence — the sentence is
   best documented in the 1984 book, and 1975-vs-1984 could not be settled here.

**The Bitter Lesson — citation details.** Exact date **13 March 2019**; the only working URL
is `http://www.incompleteideas.net/IncIdeas/BitterLesson.html`. **Do not cite
`sutton.cs.ualberta.ca`** — it does not resolve. Useful second sentence (the close):
"Building in our discoveries only makes it harder to see how the discovering process can be
done."

**Amdahl's law.** *S* = 1/((1−*p*) + *p*/*s*), with *p* the parallelisable fraction and *s*
the speedup of that fraction. The paper body is paywalled, so **no verbatim quote** is
available, and whether the 1967 paper prints the closed form is **unconfirmed**. The
scaled-problem counterpoint is Gustafson, *CACM* 31(5):532–533 (1988),
[DOI 10.1145/42411.42415](https://doi.org/10.1145/42411.42415).

**Wright's law — the honest answer to "has it been applied to AI credibly?"**
- The original is *C*ₙ = *C*₁·*n*^(−*b*) over **cumulative production**, learning rate
  1 − 2^(−*b*). Body paywalled (AIAA 403) → **no verbatim quote**.
- **No peer-reviewed paper was found that applies Wright's law (cost vs cumulative
  production) to AI.** The peer-reviewed AI cost literature is **time-based**, not
  production-based: Epoch AI's algorithmic-progress paper (arXiv:2403.05812, NeurIPS 37
  (2024), pp. 58245–58283) finds the compute needed to reach a fixed performance threshold
  **halves roughly every 8 months** (CI 5–14). Pilz, Heim & Brown (AAAI-25,
  [DOI 10.1609/aaai.v39i26.34971](https://doi.org/10.1609/aaai.v39i26.34971)) is about
  compute efficiency, not Wright's law.
- The only genuine Wright's-law *fit* for AI hardware that was found is **informal and not
  peer-reviewed**: Gogerty / Carbon Finance Lab (SSRN), "GPU cost per GFLOPS dropped **89.2%
  every doubling of cumulative shipments**". Cite it as informal if at all.
- OWID does **not** apply Wright's law to AI. No Amodei doubling period or learning rate for
  Wright's law was verifiable.
- **So:** use Wright's law for AI as an *analogy with a caveat*, not as an established result.

**Roofline / arithmetic intensity.** Correct title is "…for **Multicore** Architectures"
(the common misquote "multiclass computing" is wrong). Arithmetic intensity = FLOPs ÷ bytes
of DRAM traffic; attainable performance is min(peak FLOP/s, intensity × peak bandwidth). For
transformer **inference**, the decode phase generates one token at a time and must stream
the whole weight set per token, so intensity is tiny and the kernel sits on the
bandwidth-limited roof. Citable sources: Leviathan, Kalman & Matias, ICML 2023
(arXiv:2211.17192): "inference from large models is often **not bottlenecked on arithmetic
operations, but rather on memory bandwidth and communication**"; and Pope et al., MLSys 2023
(arXiv:2211.05102): "At small batch sizes and sequence lengths, the time to **load weights**
dominates." **Precision note:** FlashAttention does *not* claim decoding is memory-bound (it
claims Transformer *ops* are memory-access-bottlenecked) and vLLM only says serving is
"bottlenecked by memory" — attribute carefully.

**Zipf's law and tokenizers — one important warning.** *f*(*r*) ∝ 1/*r*^α with α ≈ 1;
Zipf's 1935 and 1949 books are the origin. The intuitive link to subword tokenisation and
long-tail data is real, **but the three papers usually cited for it — Sennrich et al. 2016
(arXiv:1508.07909), Kudo 2018 (arXiv:1804.10959) and Kudo & Richardson's SentencePiece
(arXiv:1808.06226) — contain no mention of Zipf or "long tail" in their retrievable text**
(SentencePiece was retrieved in full, including references). Do not attribute the Zipf
connection to them. A citable Zipf↔tokenizer source is He, Zeng & Jiang, EMNLP 2025,
pp. 28009–28021, [DOI 10.18653/v1/2025.emnlp-main.1421](https://doi.org/10.18653/v1/2025.emnlp-main.1421).

Full quotes and per-topic retry logs: `research/scratch/cv-facts/densing-and-laws.md` and
`research/scratch/cv-facts/notes/`.

---

## 8. Quick-reference recap

**The ILSVRC trajectory, one line:** 28.2% (2010, SIFT+LBP+SVM) → 25.8% (2011, Fisher
vectors) → 15.3% (2012, AlexNet, 7-CNN ensemble) → 11.2–11.7% (2013, Clarifai) → 6.66%
(2014, GoogLeNet, 7-model ensemble) → 3.57% (2015, ResNet, 6-model ensemble; 4.49% single
model) → 2.99% (2016, Trimps-Soushen) → 2.25% (2017, SENet). Human expert baseline: **5.1%**.

**The three claims in the brief that are wrong as stated:**

1. **"GoogLeNet matched VGG at one-twelfth the parameters."** Wrong. The 12× is GoogLeNet vs
   **AlexNet** (the paper's own sentence); against VGG the ratio is **≈20×** (6.8M vs 138M).
   See §2.1.
2. **"Densing Law: performance per parameter doubles every 3.3 months, by Kong/HKU."** Wrong
   on the author (Tsinghua + ModelBest + OpenBMB; **Lingpeng Kong is not an author**) and on
   the metric (effective-vs-actual parameter ratio from a fitted scaling law, not performance
   per parameter). The number is version-dependent: **3.3 months** (preprint Figure 1
   caption), **~3 months** (preprint abstract), **3.5 months** (published *Nature Machine
   Intelligence*). See §6.
3. **"The popular Goodhart form is Strathern 1997."** Half right: Strathern **popularised**
   it in 1997, but **Keith Hoskin coined it in 1996**, and Strathern credited Hoskin, not
   Goodhart. See §7.

**The three claims in the brief that are right and load-bearing:**

1. The **AlexNet 15.3%**, **ResNet 3.57%** and **GoogLeNet 6.66%** headline numbers are all
   **ensembles** — this is the correction most worth making on a slide.
2. The **human ImageNet baseline is 5.1%**, but it is one expert (trained on 500 images) on a
   1,500-image subsample; a second expert trained on 100 images scored **12.0%**, and an
   "optimistic" pooled human scored **2.4%**. See §1.2.
3. The **pipeline collapse is real and datable**: the pre-2012 winner was a named chain
   (SIFT/LBP → coding → SVM; Fisher vectors; DPM), and from 2012 every ILSVRC winner was one
   end-to-end-trained CNN. LeCun's 2014 formulation is the citable statement. See §5.

**Source files for deeper detail:**
`research/scratch/cv-facts/{ilsvrc-working-notes,generation-vlm,densing-and-laws,transfer-and-selfdriving}.md`,
the per-domain files in `research/scratch/cv-facts/parts/`, and the per-law notes in
`research/scratch/cv-facts/notes/`.

---

## 9. Could not verify

Explicit list, in the order the sections appear. "Not found" means a genuine negative
search result, not a claim that no source exists.

**Environment limitations that shaped this briefing (record these, they explain the gaps):**

- `web_fetch` was **intermittent**: many hosts failed with `TypeError: fetch failed` on
  first attempt and succeeded on retry, while some hosts never resolved
  (`karpathy.github.io` → `EAI_AGAIN`; `arxiv.org` and `image-net.org` failed early and
  then worked). Everything fetched was retried.
- **PDFs are not readable** by `web_fetch` here (`unsupported content type
  "application/pdf"`). This cost us the ILSVRC2017 overview slides and several paper
  tables. `web_fetch` also **truncates long HTML**, so paper *bodies* past roughly the
  first third were often unreachable — this is why several numbers below are quoted from
  abstracts or from secondary transcriptions of the same paper.
- `en.wikipedia.org` and `www.google.com` resolve to a non-public IP and are blocked;
  `nature.com`, `link.springer.com` and `doi.org` redirect to identity providers and are
  not readable; `dl.acm.org` returns HTTP 403 to automated fetches; `bash` has **no
  network access** (curl times out).
- `web_search` failed once mid-session with a search-endpoint error and was retried.

**Section 1 — ILSVRC**

- **The "5.0%" human-error variant.** No primary source found. The primary figure is
  **5.1%** (Russakovsky et al. 2015 §6.4.1). Treat 5.0% as a rounding/misquote.
- **The full §6.4 human-accuracy text and Table 9.** The arXiv HTML truncates before
  §6.4. The 5.1% quote and the "expert annotators" framing are taken from AI Impacts'
  transcription of Russakovsky et al. (which cites §6.4.1 and Table 9), not read from the
  primary page in this session. The primary URL is given; the quote should be checked
  against the PDF before being printed verbatim on a slide.
- **Second human annotator's error rate** (the paper used at least two) — not obtained.
- **The ILSVRC2017 overview deck** (`ILSVRC2017_overview.pdf`) could not be read (PDF), so
  its summary statements about the final year are not quoted.
- **The organizers' *reason* for ending the challenge.** The official statements are
  "last of the ImageNet Challenge competitions" + "focus on unanswered questions" + the
  move to Kaggle. The popular causal claim — "because error had saturated below human
  level" — was **not found in any official sentence**. Do not present it as the stated reason.
- **AlexNet's exact "60M" parameter count vs the abstract's "60 million parameters"** is
  consistent across sources, but the frequently quoted **62M** was not traced to a primary
  source in this session.
- **The 2013 winner designation.** The official table's top classification entry is
  Clarifai at **11.197% using outside data**; the best original-data-only entry is
  **11.743%**. The widely used textbook figure "**11.7%**" corresponds to the
  original-data entry. Both are given in §1.1; pick one and label it.
- **GoogLeNet's "12× fewer parameters"** is the paper's own phrasing, but it does not
  reconcile exactly with the parameter counts: the paper's Table 1 sums to ≈6.8M and
  AlexNet is ≈60M, i.e. ≈8.8×. The "12×" is therefore a loose (favourable) rounding by
  the authors. See §2.

**Section 2 — architectures**

- **GoogLeNet's own "12× fewer parameters than AlexNet" does not reconcile** with the
  counts (6.8M vs 60M ≈ 8.8×). The claim is the authors'; the arithmetic is ours.
- **VGG's official competition result vs the paper's own numbers disagree.** The official
  ILSVRC2014 page lists a *single* VGG ConvNet at **8.434%** classification error, while the
  VGG paper reports its best single model at **7.1%** (val, multi-crop + dense) / **7.0%**
  (test) and its 7-model ensemble at **7.3%** test. Different evaluation protocols
  (competition CLS-LOC vs the paper's dense multi-crop testing). Both figures are given in
  §2; do not mix them.
- **The AlexNet parameter count has two published abstracts that disagree on secondary
  details.** The NeurIPS proceedings abstract says "60 million parameters and **500,000
  neurons** … **two** globally connected layers", while the official ILSVRC2012 SuperVision
  abstract says "60 million parameters and **650,000 neurons** … **three** globally-connected
  layers". Both are primary. **60M parameters** is consistent; quote only that.
- The NeurIPS abstract of AlexNet also reports **ILSVRC-2010** (not 2012) single-net test
  error of **39.7% top-1 / 18.9% top-5** — a different number from the ILSVRC-2012 results.
  Do not present 18.9% as the 2012 result.
- The commonly quoted AlexNet figure **62M** was not traced to a primary source here.

**Section 3 — tasks**

- **Pre-deep object-detection mAP on VOC** is given only as a *derived* figure (R-CNN's
  ">30% relative improvement" ⇒ ≈41% for the previous VOC2012 best). No leaderboard number
  was read directly. The canonical pre-deep detector is DPM (DOI 10.1109/TPAMI.2009.167).
- **U-Net's precise ISBI error metrics** (warping error 0.000353, IOU PhC-U373 0.9203,
  DIC-HeLa 0.7756) come from the workstream's reading of the paper rather than from the
  abstract; they are consistent with the abstract's claims but were not independently
  re-derived here.
- **Fast R-CNN's VOC2010 68.8%** was seen in the paper's table markup but not re-parsed
  cleanly; VOC2007 70.0% and VOC2012 68.4% were read directly.
- **Stable Diffusion public release dates** (commonly Aug 2022 / Oct 2022) were not verified
  from a primary source — the model cards do not carry release dates. "2022 release" is the
  verifiable statement.
- **StyleGAN2's FID reference split** is not explicitly restated in the StyleGAN2 text; it
  presumably inherits StyleGAN's 50k-training-set protocol, but that is an inference.
- **mlco2 "Hours used" semantics** (per-GPU vs total) are undefined in the SD model cards.
- **Original GAN has no CIFAR-10 quantitative number and no IS/FID** (IS = Salimans 2016,
  FID = Heusel 2017). DCGAN, pix2pix and CycleGAN contain no FID/IS by construction.

**Section 4 — transfer.** A dated, published statement of when Google/Waymo switched
perception to deep learning was **not found**; proving deep learning was in use by
2018–2019 is not the same as dating the switch. `darpa.mil` was unreachable, so no DARPA
primary document was read. The 2016 NVIDIA blog date conflicts with the paper's own
"nine months ago". No *peer-reviewed* industrial paper was found running the explicit
"ImageNet fine-tune vs random-init, same protocol" comparison on a defect dataset.
The strongest industrial "default assumption" quote is from a **2026 preprint**.
The **agriculture** domain table is now integrated in §4.2.

**Section 5 — pipeline collapse.** The verbatim sentence from LeCun, Bengio & Hinton,
*Nature* 521:436–444 (2015) could **not** be read from the publisher (redirects to
`idp.nature.com`), so it is not quoted; the 2014 LeCun IEEE abstract is used instead and *is*
quoted verbatim. The ILSVRC 2015 IJCV paper's own §5.2 "large scale algorithmic innovations"
narrative could not be reached before the HTML truncation limit and is not quoted.

**Section 6 — Densing Law.** §5 "Limitations and Future Directions" of the arXiv paper could
not be read (truncation). No peer-reviewed criticism or replication was found — state this as
a negative finding, not proof of absence. The unit of `t` in `A ≈ 0.007` is inferred (days),
not stated. The "88.6 days" METR corroboration in one press item is a category error and is
**not** METR's published number.

**Section 7 — laws**

- **Goodhart 1975 vs 1984**: which publication first contains the canonical sentence is
  unresolved; the sentence is best documented at p.96 of the 1984 *Monetary Theory and
  Practice*.
- **Strathern's own attribution sentence** (crediting Hoskin) was not read verbatim; the
  attribution rests on secondary literature (McIntyre; Majka & El-Mhamdi arXiv:2505.23445).
- **No verbatim body quotes** could be obtained for Wright (AIAA 403), Amdahl (ACM 403),
  Roofline (ACM 403) or the Zipf books — all paywalled. The formulations given are the
  standard ones, not quotes from behind the paywall.
- **Wright's law applied to AI**: the correct statement is a *negative* finding — no
  peer-reviewed application exists. The only genuine GPU fit found is an informal SSRN
  analysis (89.2% cost decline per cumulative-shipment doubling), not peer-reviewed.
- **Zipf ↔ tokenizers**: the three papers usually cited for this (Sennrich 2016, Kudo 2018,
  SentencePiece 2018) contain **no mention of Zipf or "long tail"** in retrievable text.
  Do not attribute the connection to them.
- **Roofline title**: the brief's "Multiclass Computing Architectures" is wrong; the title is
  "…for **Multicore** Architectures".
- **Bitter Lesson URL**: only `http://` works; `sutton.cs.ualberta.ca` does not resolve.
- **METR "88.6 days"** (media claim) is a category error; METR's published figure is
  **212 days (171–249)** for a different metric (arXiv:2503.14499).
