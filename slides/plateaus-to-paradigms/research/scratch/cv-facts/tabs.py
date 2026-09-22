import re,html,sys
def clean(x):
    x=re.sub(r"(?s)<[^>]+>"," ",x); x=html.unescape(x); return re.sub(r"\s+"," ",x).strip()
def tables(fn):
    s=open(fn,encoding="utf-8",errors="replace").read()
    out=[]
    for m in re.finditer(r'(?is)<figure[^>]*class="[^"]*ltx_table[^"]*"[^>]*>(.*?)</figure>',s):
        blk=m.group(1)
        cap=re.search(r'(?is)class="[^"]*ltx_caption[^"]*"[^>]*>(.*?)</figcaption>',blk)
        cap=clean(cap.group(1))[:300] if cap else "(no caption)"
        rows=[]
        for tr in re.findall(r'(?is)<tr[^>]*>(.*?)</tr>',blk):
            cells=[clean(c) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',tr)]
            if any(cells): rows.append(cells)
        out.append((cap,rows))
    return out
fn=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else "."
for i,(cap,rows) in enumerate(tables(fn)):
    body=" ".join(" ".join(r) for r in rows)
    if re.search(pat,cap+" "+body,re.I):
        print(f"\n########## TABLE {i} :: {cap}")
        for r in rows: print("  "+" | ".join(r))
