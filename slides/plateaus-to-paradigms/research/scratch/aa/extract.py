import re, json, sys, html

raw = open('/tmp/aa_test.html', encoding='utf-8', errors='replace').read()
print("html len", len(raw), file=sys.stderr)

# Find the RSC flight text embedded via self.__next_f.push([1,"..."])
chunks = []
for m in re.finditer(r'self\.__next_f\.push\((\[.*?\])\)</script>', raw, re.S):
    arg = m.group(1)
    try:
        arr = json.loads(arg)
    except Exception as e:
        continue
    if len(arr) >= 2 and isinstance(arr[1], str):
        chunks.append(arr[1])
flight = "".join(chunks)
print("flight len", len(flight), file=sys.stderr)
open('/home/zecyel/slides/ch1/research/scratch/aa/flight.txt','w').write(flight)

# Count field markers
for k in ['modelCreatorName','intelligenceIndex','"slug"','medianTokensPerTask','priceInput','inputPrice']:
    print(k, flight.count(k), file=sys.stderr)
