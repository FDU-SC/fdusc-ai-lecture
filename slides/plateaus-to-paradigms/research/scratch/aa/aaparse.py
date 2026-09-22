import re, json, sys

def flight_from_html(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    chunks=[]
    for m in re.finditer(r'self\.__next_f\.push\((\[.*?\])\)</script>', raw, re.S):
        try: arr=json.loads(m.group(1))
        except Exception: continue
        if len(arr)>=2 and isinstance(arr[1], str): chunks.append(arr[1])
    return "".join(chunks)

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
        p=j+len(pat)-1  # point AT '['
        txt=extract_array(flight,p)
        idx=j+1
        if not txt: continue
        try: arr=json.loads(txt)
        except Exception as e: 
            out.append((p,None,str(e))); continue
        out.append((p,arr,None))
    return out

if __name__=="__main__":
    path=sys.argv[1]
    fl=flight_from_html(path)
    print("flight len", len(fl))
    for key in sys.argv[2:]:
        for p,arr,err in find_arrays(fl,key):
            if err: print(f"  {key}@{p}: PARSE ERR {err}"); continue
            ks = list(arr[0].keys()) if arr and isinstance(arr[0],dict) else type(arr[0]).__name__ if arr else "empty"
            print(f"  {key}@{p}: len={len(arr)} firstkeys={ks}")
