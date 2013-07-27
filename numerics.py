from __future__ import division

from numpy import (cos, sin, pi, array)
import scipy.optimize

p, q = 5, 8

def _d(z1, t1, z2, t2):
    return (z1*cos(t1) - z2*cos(t2))**2 + (z1*sin(t1) - z2*sin(t2))**2

def _s(z1, t1, z2, t2):
    return (z1 + z2)**2

def _r(z1, t1, z2, t2):
    return _d(z1, t1, z2, t2) / _s(z1, t1, z2, t2)

def f(a):
    z, t = a
    w, s = z**(p/q), (p*t + 2*pi)/q
    return array([
        _r(z, t, 1, 0) - _r(w, s, 1, 0),
        _r(z, t, 1, 0) - _r(w, s, z, t),
    ])

def ff(a):
    z, t = a
    w, s = z**(p/q), (p*t + 2*pi)/q
    return array([
        _d(z,t, 1,0)*_s(w,s, 1,0) - _s(z,t, 1,0)*_d(w,s, 1,0),
        _d(z,t, 1,0)*_s(w,s, z,t) - _s(z,t, 1,0)*_d(w,s, z,t),
    ])

result = scipy.optimize.root(f, array([1,0]))
if not result.success:
    raise Exception("Numerical optimization failed to converge: " + result.message)

z = result.x
zz = z[0] * cos(z[1]) + 1j*( z[0] * sin(z[1]) )
w = array([ z[0]**(5/8), (5*z[1]-2*pi)/8 ])
ww = w[0] * cos(w[1]) + 1j*( w[0] * sin(w[1]) )

abs(ww-1)/(abs(ww)+1)
abs(zz-1)/(abs(zz)+1)
abs(zz-ww)/(abs(zz)+abs(ww))

1/zz
1/ww
