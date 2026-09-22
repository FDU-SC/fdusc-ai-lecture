#!/bin/bash
cd "$(dirname "$0")"
mkdir -p src txt
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
fetch(){ # name url
  local n="$1" u="$2"
  local code
  code=$(curl -sL --max-time 120 -A "$UA" -o "src/$n.raw" -w "%{http_code}" "$u")
  echo "$n HTTP=$code bytes=$(stat -c%s src/$n.raw 2>/dev/null) <- $u"
  case "$n.raw" in
    *.pdf) : ;;
    *) : ;;
  esac
  if [ "${n##*.}" = "pdf" ]; then
    pdftotext -layout "src/$n.raw" "txt/$n.txt" 2>/dev/null && echo "   lines=$(wc -l < txt/$n.txt)"
  else
    python3 - "$n" <<'PY'
import sys,re,html
n=sys.argv[1]
s=open(f"src/{n}.raw",encoding="utf-8",errors="replace").read()
s=re.sub(r"(?is)<(script|style|svg|head)[^>]*>.*?</\1>"," ",s)
s=re.sub(r"(?is)<br\s*/?>","\n",s)
s=re.sub(r"(?is)</(p|div|tr|li|h[1-6]|table|section)>","\n",s)
s=re.sub(r"(?is)</t[dh]>"," | ",s)
s=re.sub(r"(?s)<[^>]+>"," ",s)
s=html.unescape(s)
s=re.sub(r"[ \t\xa0]+"," ",s)
s=re.sub(r"\n\s*\n+","\n",s)
open(f"txt/{n}.txt","w",encoding="utf-8").write(s)
print("   lines=",s.count("\n"))
PY
  fi
}
for spec in \
 "gan:https://ar5iv.labs.arxiv.org/html/1406.2661" \
 "dcgan:https://ar5iv.labs.arxiv.org/html/1511.06434" \
 "pix2pix:https://ar5iv.labs.arxiv.org/html/1611.07004" \
 "stylegan:https://ar5iv.labs.arxiv.org/html/1812.04948" \
 "stylegan2:https://ar5iv.labs.arxiv.org/html/1912.04958" \
 "ddpm:https://ar5iv.labs.arxiv.org/html/2006.11239" \
 "ldm:https://ar5iv.labs.arxiv.org/html/2112.10752" \
 "dit:https://ar5iv.labs.arxiv.org/html/2212.09748" \
 "clip:https://ar5iv.labs.arxiv.org/html/2103.00020" \
 "vit:https://ar5iv.labs.arxiv.org/html/2010.11929" \
 "cyclegan.pdf:https://openaccess.thecvf.com/content_ICCV_2017/papers/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.pdf" \
 "stylegan_cvf.pdf:https://openaccess.thecvf.com/content_CVPR_2019/papers/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.pdf" \
 "stylegan2_cvf.pdf:https://openaccess.thecvf.com/content_CVPR_2020/papers/Karras_Analyzing_and_Improving_the_Image_Quality_of_StyleGAN_CVPR_2020_paper.pdf" \
 "dit_cvf.pdf:https://openaccess.thecvf.com/content/ICCV2023/papers/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.pdf" \
 "ddpm_neurips.pdf:https://proceedings.neurips.cc/paper_files/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf" \
 ; do
  fetch "${spec%%:*}" "${spec#*:}"
done
echo "DONE"
