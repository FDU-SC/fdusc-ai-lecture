#!/usr/bin/env python3
"""Fetch arXiv HTML full text and grep around keywords."""
import sys, subprocess, re, html, os

def get(aid):
    fn = f'fx/{aid}.html'
    if os.path.exists(fn) and os.path.getsize(fn) > 5000:
        return open(fn, encoding='utf-8', errors='ignore').read()
    os.makedirs('fx', exist_ok=True)
    for base in [f'https://arxiv.org/html/{aid}', f'https://arxiv.org/abs/{aid}']:
        r = subprocess.run(['curl','-sS','--http1.1','-m','90','-L','-A','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36', base], capture_output=True, text=True)
        if r.stdout and len(r.stdout) > 20000:
            open(fn,'w',encoding='utf-8').write(r.stdout)
            return r.stdout
    return ''

def text(s):
    s = re.sub(r'<(script|style|math)[^>]*>.*?</\1>','',s,flags=re.S)
    b = re.sub(r'<[^>]+>',' ',s); b = html.unescape(b); return re.sub(r'\s+',' ',b)

if __name__ == '__main__':
    aid = sys.argv[1]
    kws = sys.argv[2:] or ['per site','energy error','DMRG','relative error']
    s = get(aid)
    if not s: print('FETCH FAIL', aid); sys.exit(1)
    b = text(s)
    print(f'### {aid} chars={len(b)}')
    seen=set()
    for kw in kws:
        c=0
        for m in re.finditer(re.escape(kw), b):
            seg = b[max(0,m.start()-450):m.start()+450]
            k = seg[:80]
            if k in seen: continue
            seen.add(k)
            print(f'--- [{kw}] ---'); print(seg); print()
            c+=1
            if c>=3: break
