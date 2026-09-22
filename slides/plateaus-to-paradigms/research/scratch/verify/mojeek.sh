#!/bin/bash
# usage: ./mojeek.sh "query" [n]
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
N=${2:-12}
curl -s -m 30 -A "$UA" "https://www.mojeek.com/search?q=$Q" | python3 -c "
import sys,re,html
h=sys.stdin.read()
# results are <a class=\"ob\" href=\"URL\">TITLE</a>
res=re.findall(r'<a[^>]+class=\"ob\"[^>]+href=\"([^\"]+)\"[^>]*>(.*?)</a>',h,re.S)
seen=set()
for u,t in res[:int(sys.argv[1])]:
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t).strip()
    if u in seen: continue
    seen.add(u)
    print(f'{t}\n  {u}')
if not res:
    print('[NO RESULTS PARSED] len=',len(h))
" "$N"
