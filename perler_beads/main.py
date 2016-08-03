#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('-s', dest='src', required= True, help='src image file', type=str)
parser.add_argument('-d', dest='dst', required= True, help='dest image file', type=str)
parser.add_argument('-sw', dest='sw', required= True, help='the width of Sample block', type=int)
parser.add_argument('-dw', dest='dw', required= True, help='the width of PerlerBeads Block', type=int)

def main():
    args = parser.parse_args()

    src_im = Image.open(args.src)
    src_size = src_im.size
    pb_size = (src_size[0] + args.sw - 1) / args.sw, (src_size[1] + args.sw - 1) / args.sw
    dst_size = pb_size[0] * args.dw, pb_size[1] * args.dw
    dst_im = Image.new('RGBA', dst_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(dst_im)

    for x in range(pb_size[0]) :
        for y in range(pb_size[1]) :
            sx = x * args.sw
            sy = y * args.sw
            dx = x * args.dw
            dy = y * args.dw
            draw.rectangle((dx, dy, dx + args.dw, dy + args.dw), src_im.getpixel((sx, sy)), (0, 0, 0, 0))

    dst_im.save(args.dst)

if __name__ == '__main__':
    main()
