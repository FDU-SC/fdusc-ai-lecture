#!/usr/bin/env python3
"""Count parameters of a Caffe deploy.prototxt by tracking feature-map shapes.
Primary-source check of published parameter counts (BVLC Caffe model zoo)."""
import re, sys

def blocks(txt):
    out, depth, start = [], 0, None
    for m in re.finditer(r'[{}]', txt):
        if m.group() == '{':
            if depth == 0:
                start = m.start()
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                out.append(txt[start:m.end()])
    return out

def field(b, name, default=None):
    m = re.search(r'\b%s\s*:\s*"?([^"\s]+)"?' % name, b)
    return m.group(1) if m else default

def count(path):
    txt = open(path).read()
    top_shape = {}
    params = 0
    rows = []
    for b in blocks(txt):
        tm = re.search(r'type\s*:\s*"([^"]+)"', b)
        if not tm:
            continue
        typ = tm.group(1)
        bottom = re.findall(r'bottom\s*:\s*"([^"]+)"', b)
        top = re.findall(r'top\s*:\s*"([^"]+)"', b)
        if not top:
            continue
        t = top[-1]
        # shape of first bottom (assume single-bottom for conv/ip)
        c, h, w = top_shape.get(bottom[0], (3, 224, 224)) if bottom else (3, 224, 224)
        if typ == 'Input':
            dims = re.findall(r'dim\s*:\s*(\d+)', b)
            if len(dims) >= 4:
                c, h, w = int(dims[1]), int(dims[2]), int(dims[3])
            top_shape[t] = (c, h, w)
            continue
        if typ == 'Convolution':
            no = int(field(b, 'num_output'))
            k = int(field(b, 'kernel_size', 1))
            s = int(field(b, 'stride', 1))
            p = int(field(b, 'pad', 0))
            g = int(field(b, 'group', 1))
            n = no * (c // g) * k * k + (no if 'bias_term: false' not in b else 0)
            params += n
            oh, ow = (h + 2 * p - k) // s + 1, (w + 2 * p - k) // s + 1
            top_shape[t] = (no, oh, ow)
            rows.append((re.search(r'name\s*:\s*"([^"]+)"', b).group(1), 'conv', n))
        elif typ == 'InnerProduct':
            no = int(field(b, 'num_output'))
            n = no * c * h * w + no
            params += n
            top_shape[t] = (no, 1, 1)
            rows.append((re.search(r'name\s*:\s*"([^"]+)"', b).group(1), 'ip', n))
        elif typ == 'Pooling':
            k = int(field(b, 'kernel_size', 1))
            s = int(field(b, 'stride', 1))
            p = int(field(b, 'pad', 0))
            if field(b, 'global_pooling') == 'true':
                oh, ow = 1, 1
            else:
                # Caffe pooling uses ceil mode: ceil((H + 2p - k)/s) + 1
                oh = -(-(h + 2 * p - k) // s) + 1
                ow = -(-(w + 2 * p - k) // s) + 1
            top_shape[t] = (c, oh, ow)
        elif typ == 'Concat':
            ch = sum(top_shape.get(bt, (0, 1, 1))[0] for bt in bottom)
            hh, ww = top_shape.get(bottom[0], (0, 1, 1))[1:]
            top_shape[t] = (ch, hh, ww)
        else:  # ReLU, LRN, Dropout, Softmax, ...
            top_shape[t] = (c, h, w)
    return params, rows

if __name__ == '__main__':
    total, rows = count(sys.argv[1])
    for name, kind, n in rows:
        print(f'  {name:35s} {kind:5s} {n:>12,}')
    print(f'TOTAL trainable parameters: {total:,}  ({total/1e6:.3f}M)')
