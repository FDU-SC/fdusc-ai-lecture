#!/usr/bin/env python3
"""Bing search via curl, print titles+urls+snippets."""
import sys, subprocess, re, html, urllib.parse

def search(q, n=12):
    url = 'https://www.bing.com/search?q=' + urllib.parse.quote(q) + '&count=30&setlang=en'
    r = subprocess.run(['curl','-sS','--http1.1','-m','40','-L','-A',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36',
        '-H','Accept-Language: en-US,en;q=0.9', url], capture_output=True, text=True)
    s = r.stdout
    out=[]
    for m in re.finditer(r'<li class="b_algo".*?</li>', s, flags=re.S):
        blk = m.group(0)
        a = re.search(r'<h2[^>]*>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', blk, flags=re.S)
        if not a: continue
        link, title = a.group(1), re.sub('<[^>]+>','',a.group(2))
        cap = re.search(r'<p[^>]*>(.*?)</p>', blk, flags=re.S)
        snip = re.sub('<[^>]+>','',cap.group(1)) if cap else ''
        out.append((html.unescape(title), html.unescape(link), html.unescape(snip)))
        if len(out)>=n: break
    return out

if __name__ == '__main__':
    for t,l,sn in search(sys.argv[1], int(sys.argv[2]) if len(sys.argv)>2 else 12):
        print(f'* {t}\n  {l}\n  {sn[:300]}\n')
