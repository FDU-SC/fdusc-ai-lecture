import re,html,sys
fn=sys.argv[1]; key=sys.argv[2] if len(sys.argv)>2 else "FID"
s=open(fn,encoding="utf-8",errors="replace").read()
# generic: find all tr-ish rows anywhere, group by nearest preceding table id
rows=re.findall(r'(?is)<span id="([A-Z0-9]+\.T\d+[^"]*)"[^>]*class="ltx_tr"(.*?)(?=<span id="[A-Z0-9]+\.T\d+|</table>|$)',s)
seen=set()
for tid,body in rows:
    cells=re.findall(r'class="ltx_td[^"]*"[^>]*>(.*?)(?=<span class="ltx_td|</span>\s*</span>\s*$)',body,flags=re.S)
    if not cells:
        cells=re.split(r'(?=<span[^>]*class="ltx_td)',body)
    txt=[]
    for c in cells:
        c=re.sub(r"(?s)<[^>]+>"," ",c); c=html.unescape(c); c=re.sub(r"\s+"," ",c).strip()
        if c: txt.append(c)
    if not txt: continue
    line=" | ".join(txt)
    tag=tid.split('.')[1]
    print(f"[{tag}] {line}")
