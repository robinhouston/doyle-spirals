#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division

from cmath import exp, phase, pi

import cairo

import doyle


W, H = 500, 500
P, Q = 9, 24
FRAMES = 16

COLORS = [
    cairo.SolidPattern(0x66 / 0xFF, 0x87 / 0xFF, 0x50 / 0xFF, 1),
    cairo.SolidPattern(0xC0 / 0xFF, 0xCA / 0xFF, 0x35 / 0xFF, 1),
    cairo.SolidPattern(0xEA / 0xFF, 0xEA / 0xFF, 0x30 / 0xFF, 1)
]

def transform_point(p):
    return (p-1)/(p+1)

def transform_circle(p, r):
    a = transform_point(p-r)
    b = transform_point(p+r)
    c = transform_point(p+r*1j)
    return circle_through_points(a, b, c)

def circle_through_points(a, b, c):
    na, nb, nc = abs(a)**2, abs(b)**2, abs(c)**2
    y = (
        (a-b).real*(nb-nc) - (b-c).real*(na-nb)
    ) / (
        2*(b-a).imag*(b-c).real - 2*(a-b).real*(c-b).imag
    )
    x = (na-nb + 2*(b-a).imag*y) / (2*(a-b).real)
    p = x + y*1j
    return p, abs(p-a)

def circle(cx, p, r):
    p, r = transform_circle(p, r)
    if r > 10: return
    cx.arc(p.real, p.imag, r, 0, 2 * pi)


spiral = doyle.spiral(P, Q)
def render_frame(frame_index, t):
    im = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cx = cairo.Context(im)
    cx.rectangle(0,0,W,H)
    cx.set_source(cairo.SolidPattern(1,1,1, 1))
    cx.fill()
    cx.translate(W//2, H//2)
    cx.scale(200, 200)
    cx.rotate(pi/4)

    def spiral_from(p, i):
        while abs(p) > 1e-3:
            p /= spiral.b
            i -= 1
        while abs(p) < 1e3:
            circle(cx, p, spiral.r*abs(p))
            cx.set_source(COLORS[i%len(COLORS)])
            cx.fill()
            p *= spiral.b
            i += 1

    q = spiral.a**t
    for i in range(P):
        spiral_from(q, 2*i)
        q *= spiral.a

    output_filename = "double-%02d.png" % (frame_index,)
    with open(output_filename, 'w') as out:
        im.write_to_png(out)

for frame_index in range(FRAMES):
    render_frame(frame_index, 3*frame_index/FRAMES)
