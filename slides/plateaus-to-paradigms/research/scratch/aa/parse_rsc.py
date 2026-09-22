import json, re, sys

def extract_array(s, start):
    depth=0; instr=False; esc=False
    for i in range(start, len(s)):
        c=s[i]
        if instr:
            if esc: esc=False
            elif c=='\\': esc=True
            elif c=='"': instr=False
            continue
        if c=='"': instr=True
        elif c=='[': depth+=1
        elif c==']':
            depth-=1
            if depth==0: return s[start:i+1]
    return None

def find_arrays(flight, key):
    out=[]; idx=0; pat=f'"{key}":['
    while True:
        j=flight.find(pat, idx)
        if j<0: break
        p=j+len(pat)-1
        txt=extract_array(flight,p); idx=j+1
        if not txt: continue
        try: out.append((j, json.loads(txt)))
        except Exception as e: out.append((j, None))
    return out

if __name__=="__main__":
    fl=open(sys.argv[1],encoding='utf-8',errors='replace').read()
    for key in sys.argv[2:]:
        for pos,arr in find_arrays(fl,key):
            if arr is None: print(f"  {key}@{pos}: parse err"); continue
            ks=list(arr[0].keys()) if arr and isinstance(arr[0],dict) else None
            print(f"  {key}@{pos}: len={len(arr)} nkeys={len(ks) if ks else '?'} first={ks[:6] if ks else arr[:2]}")
