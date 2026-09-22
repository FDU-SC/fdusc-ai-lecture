import sys,re,html,subprocess
url=sys.argv[1]
pat=sys.argv[2] if len(sys.argv)>2 else None
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
try:
    r=subprocess.run(["curl","-sS","-L","--max-time","40","-A",UA,url],capture_output=True,text=True)
    t=r.stdout
except Exception as e:
    print("ERR",e); sys.exit(1)
t=re.sub(r'(?is)<(script|style|svg|noscript|header|nav|footer).*?</\1>',' ',t)
t=re.sub(r'(?s)<[^>]+>','\n',t)
t=html.unescape(t)
lines=[re.sub(r'\s+',' ',l).strip() for l in t.split('\n')]
lines=[l for l in lines if l]
# dedupe consecutive
out=[]
for l in lines:
    if not out or out[-1]!=l: out.append(l)
txt='\n'.join(out)
if pat:
    keep=[]
    for i,l in enumerate(out):
        if re.search(pat,l,re.I):
            keep.extend(out[max(0,i-3):i+8])
    seen=set(); res=[]
    for l in keep:
        if l not in seen: seen.add(l); res.append(l)
    print('\n'.join(res)[:9000])
else:
    print(txt[:9000])
