#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division

from cmath import phase
from math import pi

import cairo

import doyle


W, H = 500, 500
P, Q = 9, 24
FRAMES = 22

COLORS = [
    cairo.SolidPattern(0x44 / 0xFF, 0x99 / 0xFF, 0xBB / 0xFF, 1),
    cairo.SolidPattern(0x48 / 0xFF, 0x33 / 0xFF, 0x53 / 0xFF, 1),
    cairo.SolidPattern(0x48 / 0xFF, 0x60 / 0xFF, 0x78 / 0xFF, 1)
]


spiral = doyle.spiral(P, Q)
def render_frame(frame_index, t):
    im = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cx = cairo.Context(im)
    cx.rectangle(0,0,W,H)
    cx.set_source(cairo.SolidPattern(1,1,1, 1))
    cx.fill()
    cx.translate(W//2, H//2)
    scale = abs(spiral.a)**t
    cx.scale(scale, scale);
    cx.rotate(phase(spiral.a) * t);

    def spiral_from(p, i):
        while abs(p) > 0.1:
            p /= spiral.b
            i -= 1
        while abs(p) < W*3:
            cx.arc(p.real, p.imag, spiral.r*abs(p), 0, 2 * pi)
            cx.set_source(COLORS[i%len(COLORS)])
            cx.fill()
            p *= spiral.b
            i += 1

    q = 1
    for i in range(P):
        spiral_from(q, 2*i)
        q *= spiral.a

    output_filename = "frame-%02d.png" % (frame_index,)
    with open(output_filename, 'w') as out:
        im.write_to_png(out)

for frame_index in range(FRAMES):
    render_frame(frame_index, 3*frame_index/FRAMES)
