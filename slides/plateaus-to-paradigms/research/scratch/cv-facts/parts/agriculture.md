# ImageNet-pretrained vision backbones transferred to agriculture — verified, sourced facts

Researched 2026-09-19 by a delegated research subagent. Working directory `/home/zecyel/slides/ch1`.
Only this file was written. No git / slidev / build script was run.

## ACCESS CONDITIONS (important for judging "confidence")

The research host egresses from a China-based IP (202.120.234.175, Shanghai Jiao Tong University).
This had two hard consequences:

1. **Many domains are unreachable or Cloudflare-blocked** from here: `arxiv.org`, `nature.com`,
   `frontiersin.org`, `mdpi.com`, `sciencedirect.com`, `academic.oup.com`, `pmc.ncbi.nlm.nih.gov`,
   `europepmc.org`, `web.archive.org`, `researchgate.net`, `core.ac.uk`, `huggingface.co`.
2. **The `web_fetch` tool rejects PDFs outright** (`Error: unsupported content type "application/pdf"`).
   Since most 2016–2019 OA papers exist only as PDFs, "I could not read Table 2" often means
   "the only reachable copy is a PDF", not "the source does not exist".

What *did* work: JSON metadata APIs (`api.crossref.org`, `api.openalex.org`,
`api.semanticscholar.org`, `www.ebi.ac.uk/europepmc/webservices/rest/...`, `api.openaire.eu`,
`data.mendeley.com/public-api`, `api.biorxiv.org`, `api.github.com`), `raw.githubusercontent.com`,
`www.biorxiv.org` HTML full text, `www.alphaxiv.org` (arXiv abstracts + v2 versions),
`agris.fao.org`, `repositori.irta.cat`, and — the key unlock — **Frontiers' NLM full-text XML at
`public-pages-files-2025.frontiersin.org`**, which gave me the actual Mohanty et al. results table.

Confidence vocabulary used below: **HIGH** = I read the claim in the primary/full text or in the
authors' own code; **MEDIUM** = verified from the publisher abstract only; **LOW** = verified only
from an index/secondary record; **NONE** = could not verify, number deliberately not stated.

---

## 1. Results table

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | confidence |
|---|---|---|---|---|---|---|---|---|
| Mohanty, Hughes, Salathé, "Using Deep Learning for Image-Based Plant Disease Detection", *Front. Plant Sci.* 7:1419 | 2016 (pub. 22 Sep 2016) | AlexNet and GoogLeNet, **ImageNet-pretrained**, re-initialising only `fc8` (AlexNet) / loss{1,2,3}/classifier (GoogLeNet) | **FINE-TUNED** — "we do not limit the learning of any of the layers" | PlantVillage (54,306 images, 38 classes = 14 species × 26 diseases + healthy); colour / grayscale / segmented; splits 80-20 … 20-80 with leaf-level grouping | 80-20 colour split: **GoogLeNet transfer-learning mean F1 0.9934, overall accuracy 99.35%**; AlexNet TL F1 0.9927 (acc. 99.28%) | **From-scratch CNN, same architectures**: GoogLeNet 0.9836 (98.37%), AlexNet 0.9782 (97.82%) on the same 80-20 colour split. Random guessing = 2.63% | full text XML: https://public-pages-files-2025.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2016.01419/xml/nlm · DOI https://doi.org/10.3389/fpls.2016.01419 | **HIGH** (read Table 1) |
| Mohanty et al. (same paper) — field-condition test | 2016 | same fine-tuned GoogLeNet/AlexNet | fine-tuned | 121 and 119 verified web images ("taken under conditions different from the images used for training") | **31.40% accuracy on 121 images (dataset 1); 31.69% on 119 images (dataset 2)**; top-5 correct 52.89% / 65.61% | random over 38 classes = 2.63% | same full-text XML; also stated in the arXiv v2 abstract: https://www.alphaxiv.org/abs/1604.03169 | **HIGH** (read the Results + Discussion) |
| Olsen et al., "DeepWeeds: A Multiclass Weed Species Image Dataset for Deep Learning", *Sci. Rep.* 9:2058 | 2019 (14 Feb 2019) | **ResNet-50 and Inception-v3, ImageNet weights** (`weights='imagenet', include_top=False`) + GAP + Dense(9) head | **FINE-TUNED** (whole network re-trained, 5-fold CV) | DeepWeeds: 17,509 images, 8 weed species + "Negative" = 9 classes, 8 sites in northern Australia | **ResNet-50 mean accuracy 95.7%; Inception-v3 95.1%** (average across 5 folds); ResNet-50 inference 53.4 ms/image | the other ImageNet-pretrained architecture (Inception-v3); paper positions both as new baselines vs earlier, smaller weed datasets | https://doi.org/10.1038/s41598-018-38343-3 · authors' code: https://raw.githubusercontent.com/AlexOlsen/DeepWeeds/master/deepweeds.py · README: https://raw.githubusercontent.com/AlexOlsen/DeepWeeds/master/README.md | **HIGH** for numbers (author abstract + author code) |
| Sa et al., "DeepFruits: A Fruit Detection System Using Deep Neural Networks", *Sensors* 16(8):1222 | 2016 | Faster R-CNN, adapted "through transfer learning" (RGB + NIR fusion); backbone is widely reported as **VGG-16 / ImageNet** but I could not read the methods | fine-tuned (transfer learning stated in abstract; layer policy not verified) | own sweet-pepper (and 7 other fruit) image datasets, RGB + NIR | **F1 0.838 for sweet-pepper detection** (multi-modal Faster R-CNN), retraining on a new fruit takes "four hours to annotate and train" | **F1 0.807** = the authors' prior/competing pipeline as reported in the abstract ("improving from 0.807 to 0.838") | https://doi.org/10.3390/s16081222 · abstract via https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/s16081222 | **MEDIUM** (publisher abstract); backbone LOW |
| Bargoti & Underwood, "Deep Fruit Detection in Orchards" (arXiv:1610.03677) | 2016/2017 | Faster R-CNN **"initialising the Deep Convolutional Neural Network directly from ImageNet features"** | fine-tuned from ImageNet init | orchard imagery: mangoes, almonds, apples | **F1 > 0.9 for apples and mangoes** ("best yet detection performance for these orchards") | cross-orchard transfer produced "negligible performance gain" over plain ImageNet init; data augmentation cut required training images >2× | https://www.alphaxiv.org/abs/1610.03677 | **MEDIUM** (v2 abstract read directly) |
| Dyrmann, Karstoft, Midtiby, "Plant species classification using deep convolutional neural network", *Biosystems Engineering* 151:72–80 | 2016 | **Nothing transferred — "The network is built from scratch"** (deliberate from-scratch design) | from scratch | 10,413 images, 22 weed and crop species at early growth stages, 6 source datasets (controlled + hand-held phone, varying light/soil/resolution) | **classification accuracy 86.2%** | no pretrained comparison in the abstract; implicitly the from-scratch model itself is the contribution | https://doi.org/10.1016/j.biosystemseng.2016.08.024 · abstract via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.biosystemseng.2016.08.024 | **MEDIUM** (publisher abstract) |
| Grinblat, Uzal, Larese, Granitto, "Deep learning for plant identification using vein morphological patterns", *Comput. Electron. Agric.* 127:418–424 | 2016 (Sept 2016) | **From-scratch CNN** (no ImageNet transfer; the point of the paper is avoiding handcrafted features) | from scratch | leaf **vein** images of 3 legume species: white bean, red bean, soybean | "significantly improves the accuracy of the referred pipeline" and "the reported accuracy is reached by increasing the model depth" — **exact accuracy NOT VERIFIED** (paywalled; OA copy is PDF-only) | the classical/state-of-the-art handcrafted-feature vein pipeline of Larese et al. | https://doi.org/10.1016/j.compag.2016.07.003 · abstract via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.compag.2016.07.003 | **MEDIUM** for method/baseline, **NONE** for the number |
| Pound et al., "Deep machine learning provides state-of-the-art performance in image-based plant phenotyping", *GigaScience* 6(10):gix083 (preprint bioRxiv 053033) | 2017 (preprint 12 May 2016) | custom small CNN on 32×32 (root) / 64×64 (shoot) patches. **Pretraining status NOT VERIFIED** (methods section truncated) | not verified | wheat root systems (2,500 annotated images from 2,697 seedlings) and wheat shoots (1,664 hand-annotated images; leaf tips/bases, ear tips/bases + background); 80/20 split | **root-tip classification accuracy 98.4%; shoot-feature classification 97.3%; localisation accuracy 99.8% (root tips) and 99.1% (shoot features)** | prior state-of-the-art (SVM / Random-Forest image pipelines), described in the paper as "accuracies of 80–90% have been typical" | preprint full text: https://www.biorxiv.org/content/10.1101/053033v1.full · published DOI https://doi.org/10.1093/gigascience/gix083 | **HIGH** for the preprint numbers, **MEDIUM** that the GigaScience version reports the same |
| Ferreira et al., "Weed detection in soybean crops using ConvNets", *Comput. Electron. Agric.* 143:314–324 | 2017 (Dec 2017) | not verified from primary text | not verified | **verified from the authors' own data deposit**: 15,336 SLIC superpixel segments from 400 UAV images — 3,249 soil, 7,376 soybean, 3,520 grass, 1,191 broadleaf weeds | **accuracy/F1 NOT VERIFIED** — publisher elided the abstract, article is paywalled, no HTML full text reachable | not verified | https://doi.org/10.1016/j.compag.2017.10.027 · dataset record https://data.mendeley.com/public-api/datasets/3fmjm7ncc6?version=2 | **HIGH** for dataset composition, **NONE** for the number |
| Sa et al., "weedNet: Dense Semantic Weed Classification Using Multispectral Images and MAV for Smart Farming", *IEEE RA-L* (arXiv:1709.03329) | 2017/2018 — **not 2016** | SegNet encoder–decoder CNN, fine-tuned ("condition (fine tune) it") — SegNet's encoder is VGG-16/ImageNet, but that is not stated in the abstract | **fine-tuned** (stated) | multispectral MAV imagery of sugar beet vs weed plots; 6 models with different input-channel counts | **~0.8 F1-score and 0.78 AUC** | the 6 input-channel configurations compared against each other; NDVI used for automatic ground truth | https://doi.org/10.1109/LRA.2017.2774979 · abstract via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/lra.2017.2774979 | **MEDIUM** (publisher abstract) |
| Kamilaris & Prenafeta-Boldú, "Deep learning in agriculture: A survey", *Comput. Electron. Agric.* 147:70–90 | 2018 | survey of **40** deep-learning agricultural efforts | n/a | n/a | "deep learning provides high accuracy, outperforming existing commonly used image processing techniques" (abstract). **The specific sentence about ImageNet pretraining being standard practice could NOT be verified** (full text unreachable) | n/a | https://doi.org/10.1016/j.compag.2018.02.016 · arXiv abstract https://www.alphaxiv.org/abs/1807.11809 · OA accepted version (PDF only) https://repositori.irta.cat/handle/20.500.12327/314 | **MEDIUM** (abstract only) |
| Reyes, Caicedo, Camargo, "Fine-tuning Deep Convolutional Networks for Plant Recognition", CLEF 2015 Working Notes (CEUR-WS Vol-1391, paper 121) | 2015 | deep CNNs fine-tuned for plant recognition (LifeCLEF/PlantCLEF 2015 era) | fine-tuned (per title) | PlantCLEF 2015 | **result NOT VERIFIED** (CEUR copy is PDF-only: http://ceur-ws.org/Vol-1391/121-CR.pdf) | not verified | metadata via https://api.openalex.org/works (openalex W2404400986); CLEF hub https://www.imageclef.org/ | **LOW** (metadata only) |

---

## 2. Notes and nuance per result

### 2.1 Mohanty, Hughes & Salathé 2016 — the canonical "99.35%" and the drop to ~31%

This is the one paper where I read the **actual table**, not just the abstract, thanks to the
Frontiers NLM XML endpoint. Exact cell values from Table 1 ("Mean F1 score across various
experimental configurations at the end of 30 epochs"; each cell is
`mean F1{mean precision, mean recall, overall accuracy}`), colour images:

| split | AlexNet transfer | AlexNet from scratch | GoogLeNet transfer | GoogLeNet from scratch |
|---|---|---|---|---|
| 80% train / 20% test | 0.9927{0.9928, 0.9927, 0.9928} | 0.9782{0.9786, 0.9782, 0.9782} | **0.9934{0.9935, 0.9935, 0.9935}** | 0.9836{0.9839, 0.9837, 0.9837} |
| 60 / 40 | 0.9907 | 0.9724 | 0.9924 | 0.9824 |
| 50 / 50 | 0.9896 | 0.9644 | 0.9916 | 0.9772 |
| 40 / 60 | 0.9860 | 0.9555 | 0.9914 | 0.9729 |
| 20 / 80 | 0.9736 | 0.9118 | **0.9820** (acc. 98.21%) | 0.9430 |

(Reproduce with the XML URL above; the section labels in the publisher XML contain typesetting
artefacts — "TRAIN: 200%" etc. — but the dedicated `TRAIN: 80%, TEST: 20%` block is correct.)

* **The headline number is GoogLeNet, not AlexNet.** The abstract's "99.35%" equals the *overall
  accuracy* of `GoogLeNet::TransferLearning::Color::80–20`; the paper's own maximum *mean F1* is
  0.9934 for that same configuration. Widely repeated claims that "AlexNet achieved 99.35%" are
  wrong at table level: AlexNet transfer-learning colour 80-20 gives mean F1 0.9927 / accuracy 0.9928.
* **Small internal inconsistency in the paper**: the Results prose says the accuracy range across all
  configurations was "from 85.53% … to 99.34% (in case of GoogLeNet::TransferLearning::Color::80–20)",
  while Table 1 gives 0.9935 accuracy for that cell and the Discussion says "top accuracy of 99.35%".
  Quote 99.35% (abstract + discussion + table), and be aware of the 99.34% sentence if you quote the
  Results text verbatim.
* **What "transfer" meant**: "we re-initialize the weights of layer fc8 in case of AlexNet, and of the
  loss {1,2,3}/classifier layers in case of GoogLeNet. Then, when training the model, we do not limit
  the learning of any of the layers, as is sometimes done for transfer learning." → ImageNet init +
  **full fine-tuning**, not frozen features.
* **Field-condition nuance (the important part)**: two small verified datasets scraped from
  Bing Image Search + IPM Images (121 and 119 images) gave **31.40%** and **31.69%** accuracy,
  top-5 **52.89% / 65.61%**, vs **2.63%** random over 38 classes. The Discussion: "when tested on a
  set of images taken under conditions different from the images used for training, the model's
  accuracy is reduced substantially, to just above 31%". The published Frontiers abstract does *not*
  contain this sentence; the arXiv **v2** abstract does (hence the alphaXiv URL in the table).
* **Crop-known variant**: if the crop is given, dataset 1 (33 classes / 9 crops) → 0.478 vs 0.225
  random; (25 classes / 5 crops) → 0.411 vs 0.179. Dataset 2 (13 classes / 4 crops) → 0.545 vs 0.314;
  (11 classes / 3 crops) → 0.485 vs 0.288.
* **No classical baseline experiment.** The classical comparison is narrative, in the Discussion
  (SIFT/HoG/SURF hand-engineered features are cited as prior art). The only experimental baselines
  are from-scratch versions of the same two networks and random guessing.
* Splits are leaf-aware: "we have the mappings of such cases for 41,112 images out of the 54,306
  images; and during all these test-train splits, we make sure all the images of the same leaf goes
  either in the training set or the testing set."

### 2.2 DeepWeeds (Olsen et al. 2019)

* Headline: mean accuracy over **5-fold cross-validation** — ResNet-50 **95.7%**, Inception-v3
  **95.1%**; ResNet-50 inference **53.4 ms/image**. Dataset 17,509 images, 8 species + negative = 9
  classes (class names in `deepweeds.py`: Chinee Apple, Lantana, Parkinsonia, Parthenium, Prickly
  Acacia, Rubber Vine, Siam Weed, Snake Weed, Negatives).
* "ImageNet-pretrained + fine-tuned" is not abstract-level information; I verified it in the authors'
  own reference implementation: `ResNet50(weights='imagenet', include_top=False, ...)` /
  `InceptionV3(weights='imagenet', include_top=False, ...)`, then GlobalAveragePooling2D + Dense(9),
  compiled and trained for up to 200 epochs with early stopping — i.e. **the whole network is trained,
  no layers frozen**. Predictions with max probability < 1/9 are forced to the negative class.
* The README repeats: "trains and evaluates Keras' base implementation of ResNet50 and InceptionV3 on
  the DeepWeeds dataset, pre-trained with ImageNet weights", and "the dataset was classified to an
  average accuracy of 95.7% with the ResNet50 deep convolutional neural network". Dataset licence
  CC BY 4.0, added to TensorFlow Datasets in August 2019.
* Per-class precision/recall/F1 are in the paper's classification report but I did not read them.

### 2.3 DeepFruits (Sa et al., Sensors 2016)

* Abstract-level facts: Faster R-CNN "adapt[ed] … through transfer learning"; RGB + NIR early/late
  fusion; "F1 score … improving from **0.807** to **0.838** for the detection of sweet pepper";
  retraining for a new fruit takes "four hours to annotate and train"; bounding-box annotation is
  ~10× faster than pixel-level annotation.
* **Caveat**: the "VGG-16 backbone / ImageNet weights" detail that is normally attached to this paper
  is *not* in the abstract and I could not read the Methods (MDPI blocks this IP; the OA copy is in
  PMC, also blocked). Do not present "VGG-16 + ImageNet" as verified by me.

### 2.4 Pound et al. (2017) — phenotyping

Numbers read directly from the bioRxiv preprint HTML full text (published version = GigaScience
gix083; the published abstract is byte-identical to the preprint abstract, which is why I treat the
numbers as likely, but not certainly, identical):
* root-tip detection accuracy **98.4%**; shoot-feature classification **97.3%** (4 feature classes +
  background); localisation accuracy **99.8%** (root tips) / **99.1%** (shoot features).
* Dataset scale: 2,500 annotated whole-root images drawn from 2,697 imaged seedlings; 1,664
  hand-annotated wheat images; 32×32 px (root) and 64×64 px (shoot) input patches; 80/20 split.
* Baseline framing: "CNNs here have out-performed recent state-of-the-art systems (e.g. accuracies of
  80–90% have been typical)", i.e. SVM/Random-Forest pipelines such as RootNav.
* **Not verified**: whether the networks were ImageNet-pretrained or trained from scratch. The
  Methods section was truncated by the fetch in all three attempts, and the published HTML (OUP) is
  403.

### 2.5 Evidence that ImageNet transfer became the default assumption

Direct quotations I actually read (not paraphrase):

1. **Bargoti & Underwood (arXiv:1610.03677), abstract** — the strongest single statement, because it
   treats plain ImageNet initialisation as the *reference condition*:
   > "In contrast, transferring knowledge between orchards contributed to negligible performance gain
   > over initialising the Deep Convolutional Neural Network directly from ImageNet features."
2. **Mohanty et al. 2016, Methods** (Frontiers NLM XML):
   > "We analyze the performance of both these architectures on the PlantVillage dataset by training
   > the model from scratch in one case, and then by adapting already trained models (trained on the
   > ImageNet dataset) using transfer learning."
   …with Table 1 showing transfer learning winning in **every** configuration for both architectures.
3. **Sa et al. 2016 (DeepFruits), abstract**: "We adapt this model, **through transfer learning**, for
   the task of fruit detection…".
4. **DeepWeeds 2019** official baseline code hard-codes `weights='imagenet'` for both backbones.
5. **Kamilaris & Prenafeta-Boldú 2018** is the paper people usually cite for "pretraining is standard
   practice", but **I could not verify any quotation from it** (see COULD NOT VERIFY).

A defensible, sourced formulation for a lecture: *by 2016–2017, ImageNet-initialised backbones were
the default starting point in agricultural vision — papers either fine-tuned from ImageNet or
explicitly justified training from scratch; from-scratch training was the thing that needed an
explanation (Dyrmann et al. 2016), not the transfer (Mohanty et al. 2016, Sa et al. 2016, Bargoti &
Underwood 2016/17).*

---

## 3. COULD NOT VERIFY

1. **Ferreira et al. 2017 "Weed detection in soybean crops using ConvNets" — any accuracy/F1 number.**
   Publisher elided the abstract in both Crossref and Semantic Scholar; ScienceDirect 403; no OA HTML.
   *Do not state a number for this paper.* What I did verify is the dataset (15,336 segments; 3,249
   soil / 7,376 soybean / 3,520 grass / 1,191 broadleaf weeds; 400 UAV images) from the authors'
   Mendeley Data deposit, and the citation metadata (CEA 143:314–324).
2. **Ferreira et al. — whether CaffeNet/AlexNet was ImageNet-pretrained and fine-tuned.** Commonly
   asserted; not verified here.
3. **Grinblat et al. 2016 — the exact accuracy.** Widely repeated numbers exist in the wild, but the
   paper is paywalled and the CONICET OA copy is a PDF (tool refuses PDFs). I deliberately state no
   number. Verified instead: the three legume species (white bean, red bean, soybean), the
   vein-morphology input, the from-scratch CNN, and the comparison against the handcrafted-feature
   pipeline.
4. **Pound et al. — pretrained vs from scratch**, and whether the published GigaScience tables match
   the preprint numbers. Also, the exact per-class accuracies (Table 1 of the paper) were not read.
5. **Kamilaris & Prenafeta-Boldú 2018 — the exact sentence(s) about ImageNet pretraining.**
   Attempted and failed: arXiv 1807.11809 blocked (arxiv.org, ar5iv.labs.arxiv.org, export.arxiv.org
   all failed); Elsevier paywall; the IRTA accepted-version copy is PDF-only; Europe PMC fullTextXML
   returned HTTP 406 on 4 attempts. **No quotation from this survey can be attributed to me.**
6. **Olsen et al. — per-class precision/recall/F1** (only the headline accuracies + inference time were
   read), and the "95.1%/95.7%" values are 5-fold means, not single-split numbers.
7. **Sa et al. DeepFruits — VGG-16 backbone, ImageNet initialisation, and the fine-tuning schedule.**
8. **PlantCLEF / LifeCLEF results with ImageNet-pretrained models.** I could reach the ImageCLEF hub
   (`imageclef.org`) but the actual challenge overview papers (Goëau/Joly et al.) and the
   Reyes/Caicedo/Camargo 2015 CLEF working note exist only as PDFs (CEUR-WS) or on arXiv (blocked).
   Metadata for Reyes et al. 2015 was verified; **no PlantCLEF accuracy number is reported here.**
9. **"Lee et al. 2017/2018 DeepWeeds".** The task brief conflates two things: DeepWeeds is
   **Olsen et al.** (2019). There *is* a distinct earlier paper — Lee, Chan, Wilkin & Remagnino,
   "Deep-Plant: Plant Identification with Convolutional Neural Networks" (IEEE ICIP 2015) — which I
   could not retrieve (Semantic Scholar rate-limited; IEEE Xplore returned an empty HTTP 202).
   **No Deep-Plant number is reported here.**
10. **"Sa et al. 2016 WeedNet".** WeedNet is **not 2016**: it is Sa et al., *IEEE Robotics and
    Automation Letters*, DOI 10.1109/LRA.2017.2774979, arXiv:1709.03329 (Sept 2017) — verified via
    OpenAlex and the Semantic Scholar record. Its abstract reports "~0.8 F1-score and 0.78 area under
    the curve", 6 input-channel configurations, SegNet, sugar beet/weed plots.
11. **Any per-species breakdown, confusion matrices, or additional splits** for Mohanty et al. beyond
    what is quoted above (I read the Results and Discussion text and Table 1; the paper has only 1
    table and 4 figures, so this is close to complete).
12. **Any classical SVM/HOG/colour-histogram baseline *numbers*** for Mohanty, DeepWeeds, DeepFruits,
    Pound or Ferreira. None of the abstracts I read reports such a baseline numerically. Only Pound
    gives a qualitative baseline range ("80–90% have been typical"); Mohanty's only experimental
    baseline is from-scratch CNN + random (2.63%).

---

## 4. URLs actually fetched / verified

### 4.1 Successfully fetched (HTTP 200) and used

Primary / full text and authors' own artefacts:

1. https://public-pages-files-2025.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2016.01419/xml/nlm — **Mohanty et al. full text + Table 1 (the key source)**
2. https://www.biorxiv.org/content/10.1101/053033v1.full — **Pound et al. preprint full text (numbers)**
3. https://raw.githubusercontent.com/AlexOlsen/DeepWeeds/master/deepweeds.py — **`weights='imagenet'`, fine-tuning, 9 classes**
4. https://raw.githubusercontent.com/AlexOlsen/DeepWeeds/master/README.md — **95.7% ResNet-50, ImageNet weights**
5. https://raw.githubusercontent.com/spMohanty/PlantVillage-Dataset/master/README.md — **54,306 images, 14 species, 26 diseases**
6. https://data.mendeley.com/public-api/datasets/3fmjm7ncc6?version=2 — **Ferreira dataset composition**
7. https://api.biorxiv.org/details/biorxiv/10.1101/053033 — preprint metadata → published DOI
8. https://repositori.irta.cat/handle/20.500.12327/314 — Kamilaris accepted version (PDF only)
9. https://www.alphaxiv.org/abs/1604.03169 — **Mohanty arXiv v2 abstract incl. 31.4%**
10. https://www.alphaxiv.org/abs/1810.05726 — DeepWeeds arXiv abstract
11. https://www.alphaxiv.org/abs/1610.03677 — **Bargoti & Underwood abstract (ImageNet-init quote)**
12. https://www.alphaxiv.org/abs/1807.11809 — Kamilaris arXiv abstract
13. https://agris.fao.org/search/en/records/675ac85d0ce2cede71d16ec1 — Mohanty abstract (FAO AGRIS)
14. https://www.imageclef.org/ — LifeCLEF/PlantCLEF hub

Index / metadata APIs:

15. https://api.openalex.org/works/doi:10.3389/fpls.2016.01419
16. https://api.crossref.org/works/10.3389/fpls.2016.01419
17. https://api.crossref.org/works/10.1016/j.compag.2016.07.003 — **Grinblat vol 127, pp. 418–424**
18. https://api.crossref.org/works/10.1016/j.compag.2017.10.027 — Ferreira vol 143, pp. 314–324
19. https://api.openalex.org/works?search=Deep%20learning%20for%20plant%20identification%20using%20vein%20morphological%20patterns… — **DOI correction to 10.1016/j.compag.2016.07.003**
20. https://api.openalex.org/works?search=Weed%20detection%20in%20soybean%20crops%20using%20ConvNets… — Ferreira DOI + dataset DOI
21. https://api.openalex.org/works?search=WeedNet%20dense%20semantic%20weed%20classification%20multispectral… — WeedNet DOI/year
22. https://api.openalex.org/works?search=Fine-tuning%20deep%20convolutional%20networks%20for%20plant%20recognition… — Reyes et al. 2015 metadata
23. https://api.openalex.org/works?search=PlantCLEF%20plant%20identification%20challenge%20overview… and …Plant%20identification%20based%20on%20noisy%20web%20data… — PlantCLEF overview records
24. https://api.openalex.org/works/doi:10.1016/j.compag.2017.10.027?select=…abstract_inverted_index — (no abstract available)
25. https://api.openalex.org/works/doi:10.1038/s41598-018-38343-3?select=id,title,content_urls,has_content
26. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/s41598-018-38343-3 — DeepWeeds abstract
27. https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/s16081222 — DeepFruits abstract
28. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.biosystemseng.2016.08.024 — Dyrmann abstract
29. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.compag.2016.07.003 — Grinblat abstract
30. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.compag.2017.10.027 — abstract elided by publisher
31. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1093/gigascience/gix083 — Pound metadata (PMC5632296)
32. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/lra.2017.2774979 — **WeedNet abstract**
33. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41598-018-38343-3%22&resultType=core&format=json — DeepWeeds abstract (Europe PMC)
34. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22FIELD%20CONDITIONS%22%20AND%20DOI:%2210.3389/fpls.2016.01419%22… and …%22confusion%20matrix%22… — 0 hits both times (phrase search did **not** reach full text; recorded as a negative result)
35. https://api.openaire.eu/search/publications?title=Deep%20learning%20in%20agriculture&format=json — Kamilaris metadata + IRTA/Recolecta OA links
36. https://api.unpaywall.org/v2/10.3389/fpls.2016.01419?email=research@example.org — OA locations
37. https://api.github.com/users/spMohanty/repos?per_page=100
38. https://api.github.com/users/inkyusa/repos?per_page=100
39. https://api.github.com/search/repositories?q=deepfruits
40. https://hf-mirror.com/buckets/huggingchat/papers-content/tree/1604 — HF mirror reachable, files exist
41. https://example.com/ — connectivity probe
42. https://cn.bing.com/search?q=Mohanty+plant+disease+99.35+accuracy — **returned irrelevant localised results; useless**
43. https://www.researchgate.net/publication/301940414 — 403 (used only to identify the egress IP)
44. https://ouci.dntb.gov.ua/en/works/42knQDel/ — HTTP 502

### 4.2 Attempted and FAILED (so the parent knows what was tried)

* **arXiv and mirrors** (all failed, ≥3 attempts each): https://arxiv.org/abs/1604.03169 ;
  https://arxiv.org/abs/1604.03169v2 ; https://export.arxiv.org/abs/1604.03169 ;
  http://arxiv.org/abs/1604.03169 ; https://cn.arxiv.org/abs/1810.05726 (cross-origin redirect to
  arxiv.org) ; https://ar5iv.org/abs/1604.03169 ; https://ar5iv.labs.arxiv.org/html/1604.03169 ;
  https://ar5iv.labs.arxiv.org/html/1807.11809 ; http://xxx.itp.ac.cn/abs/1604.03169 (DNS ENOTFOUND)
* **Publisher sites**: https://www.frontiersin.org/articles/10.3389/fpls.2016.01419/full (and
  /journals/... form) ; https://doi.org/10.3389/fpls.2016.01419 (cross-origin redirect to
  journal.frontiersin.org) ; https://www.nature.com/articles/s41598-018-38343-3 ;
  https://www.mdpi.com/1424-8220/16/8/1222 (and /htm) — HTTP 403 Akamai ;
  https://www.sciencedirect.com/science/article/pii/S0168169916300889 — HTTP 403 ;
  https://academic.oup.com/gigascience/article/6/10/gix083/4110124 — HTTP 403 Cloudflare ;
  https://ieeexplore.ieee.org/document/7953259 — HTTP 202, empty ;
  https://link.springer.com/article/10.1007/s11119-017-9534-5 — cross-origin redirect to idp.springer.com
* **PMC / Europe PMC**: https://pmc.ncbi.nlm.nih.gov/articles/PMC5032846/ (and PMC5632296, PMC5017387) ;
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5032846/ ; https://pubmed.ncbi.nlm.nih.gov/27713752/ ;
  https://europepmc.org/articles/PMC6375952 — HTTP 403 Cloudflare ;
  https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5032846/fullTextXML (and PMC6375952, PMC5632296,
  also with `?format=xml` and over http) — **HTTP 406 four-plus times** ;
  https://www.ncbi.xyz/pmc/articles/PMC5032846/ and https://ncbi.xyz/... — DNS ENOTFOUND ;
  https://www.chinapubmed.net/PMC5032846 — DNS ENOTFOUND
* **Archives**: https://web.archive.org/web/2020/…frontiersin.org/… ; https://web.archive.org/web/2019id_/… ;
  http://archive.org/wayback/available?url=… ; https://archive.ph/newest/…academic.oup.com… —
  all failed (DNS / fetch), ≥3 attempts
* **Aggregators**: https://scholar.archive.org/search?q=… (failed) ; https://paperity.org/search/?q=…
  (403) ; https://www.scilit.com/ (403) ; https://www.scienceopen.com/search#… (403) ;
  https://core.ac.uk/search?q=… (403) ; https://www.semanticscholar.org/paper/… (failed) ;
  https://www.paperswithcode.com/… (failed) ; https://content.openalex.org/works/W2473156356.grobid-xml
  — HTTP 401 "API key required"
* **bioRxiv rate limiting**: https://www.biorxiv.org/content/10.1101/053033v1.full-text and
  …/053033.source.xml returned HTTP 429 Cloudflare "Attention Required" on 4 attempts;
  the `.full` URL succeeded later (the successful read is what the numbers come from)
* **Misc**: https://r.jina.ai/https://arxiv.org/abs/1604.03169 (failed) ;
  https://huggingface.co/buckets/huggingchat/papers-content/resolve/1604/1604.03169.md (failed) ;
  https://hf-mirror.com/buckets/huggingchat/papers-content/resolve/1604/1604.03169.md?download=true
  (cross-origin redirect to cas-bridge.xethub.hf.co, not followed) ;
  https://repositori.irta.cat/bitstream/20.500.12327/314/1/kamilaris_deep_2018.pdf — DNS EAI_AGAIN (2×),
  and the eventual handle page confirms it is only a PDF ;
  https://agris.fao.org/search/en/records/65deb13f4c5aef494fdd60d1 — DNS EAI_AGAIN (2×) ;
  https://www.x-mol.com/paper/1234567 — timeout
* **Rate-limited (recovered later)**: https://api.semanticscholar.org/graph/v1/paper/search… (HTTP 429
  on 4 consecutive queries — the `Deep-Plant` search was never completed)
