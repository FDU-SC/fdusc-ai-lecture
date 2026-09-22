#!/bin/bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
N=${2:-15}
curl -s -m 35 -A "$UA" -H 'Accept-Language: en-US,en;q=0.9' "https://cn.bing.com/search?q=$Q&count=$N&setlang=en" | python3 -c "
import sys,re,html
h=sys.stdin.read()
items=re.findall(r'<li class=\"b_algo\".*?</li>',h,re.S)
out=0
for it in items:
    m=re.search(r'<h2[^>]*>\s*<a[^>]+href=\"([^\"]+)\"[^>]*>(.*?)</a>',it,re.S)
    if not m: continue
    u=html.unescape(m.group(1)); t=re.sub(r'<[^>]+>','',m.group(2)); t=html.unescape(t).strip()
    p=re.search(r'<p[^>]*>(.*?)</p>',it,re.S)
    sn=re.sub(r'<[^>]+>','',p.group(1)) if p else ''
    sn=html.unescape(sn).strip()[:300]
    print(f'* {t}\n  {u}\n  {sn}')
    out+=1
    if out>=int(sys.argv[1]): break
if out==0: print('[NO RESULTS] len=',len(h))
" "$N"
