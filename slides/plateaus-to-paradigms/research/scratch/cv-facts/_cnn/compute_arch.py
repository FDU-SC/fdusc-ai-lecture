#!/usr/bin/env python3
"""Compute CNN parameter counts directly from the layer specifications published
in the original papers. Independent arithmetic cross-check (no frameworks)."""

def vgg(convs, fc=(4096, 4096, 1000), name=''):
    """convs: list of channel counts, grouped by pooling stage (paper Table 1)."""
    total, in_ch, spatial = 0, 3, 224
    for group in convs:
        for out_ch in group:
            total += 3 * 3 * in_ch * out_ch + out_ch
            in_ch = out_ch
        spatial //= 2
    flat = in_ch * (spatial // 7 if False else 7) * 7  # after 5 pools: 224/32 = 7
    prev = flat
    for out_ch in fc:
        total += prev * out_ch + out_ch
        prev = out_ch
    return total

VGG16 = [[64, 64], [128, 128], [256, 256, 256], [512, 512, 512], [512, 512, 512]]
VGG19 = [[64, 64], [128, 128], [256, 256, 256, 256], [512, 512, 512, 512], [512, 512, 512, 512]]

def resnet_bottleneck(widths, blocks, num_classes=1000):
    """ResNet-50/101/152 per He et al. Table 1 (1x1, 3x3, 1x1 bottlenecks, option B).
    Matches the standard reference implementation: conv layers have no bias,
    BatchNorm contributes 2 channels of parameters (scale + shift)."""
    total = 7 * 7 * 3 * 64                           # conv1 (bias=False)
    total += 2 * 64                                  # bn1
    in_ch = 64
    for stage, (w, n) in enumerate(zip(widths, blocks), start=1):
        for block in range(n):
            stride = 2 if (block == 0 and stage > 1) else 1
            total += 1 * 1 * in_ch * (w // 4)        # conv1 1x1 (bias=False)
            total += 2 * (w // 4)                    # bn
            total += 3 * 3 * (w // 4) * (w // 4)     # conv2 3x3 (bias=False)
            total += 2 * (w // 4)                    # bn
            total += 1 * 1 * (w // 4) * w            # conv3 1x1 (bias=False)
            total += 2 * w                           # bn
            if stride != 1 or in_ch != w:            # downsample projection (option B)
                total += 1 * 1 * in_ch * w           # conv (bias=False)
                total += 2 * w                       # bn
            in_ch = w
    total += in_ch * num_classes + num_classes       # fc (bias=True)
    return total

if __name__ == '__main__':
    print(f'VGG-16 (config D, 13 conv + 3 FC) : {vgg(VGG16):,}  ({vgg(VGG16)/1e6:.2f}M)')
    print(f'VGG-19 (config E, 16 conv + 3 FC) : {vgg(VGG19):,}  ({vgg(VGG19)/1e6:.2f}M)')
    for name, blocks in [('ResNet-50', [3, 4, 6, 3]), ('ResNet-101', [3, 4, 23, 3]), ('ResNet-152', [3, 8, 36, 3])]:
        n = resnet_bottleneck([256, 512, 1024, 2048], blocks)
        print(f'{name:11s} (paper Table 1, bottleneck, option B): {n:,}  ({n/1e6:.2f}M)')
