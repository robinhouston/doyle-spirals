from __future__ import division

import sys
from math import (cos, sin, pi)

def _d(z,t, p,q):
    """The square of the distance between z*e^(it) and z*e^(it)^(p/q).
    """
    w, s = z**(p/q), (p*t + 2*pi)/q
    return (
          ( z*cos(t) - w*cos(s) )**2
        + ( z*sin(t) - w*sin(s) )**2
    )

def ddz_d(z,t, p,q):
    """The partial derivative of _d with respect to z.
    """
    w, s = z**(p/q), (p*t + 2*pi)/q
    ddz_w = (p/q)*z**((p-q)/q)
    return (
          2*(w*cos(s) - z*cos(t))*(ddz_w*cos(s) - cos(t))
        + 2*(w*sin(s) - z*sin(t))*(ddz_w*sin(s) - sin(t))
    )

def ddt_d(z,t, p,q):
    """The partial derivative of _d with respect to t.
    """
    w, s = z**(p/q), (p*t + 2*pi)/q
    dds_t = (p/q)
    return (
          2*( z*cos(t) - w*cos(s) )*( -z*sin(t) + w*sin(s)*dds_t )
        + 2*( z*sin(t) - w*sin(s) )*( z*cos(t) - w*cos(s)*dds_t )
    )

def _s(z,t, p,q):
    """The square of the sum of the origin-distance of z*e^(it) and
    the origin-distance of z*e^(it)^(p/q).
    """
    return (z + z**(p/q))**2

def ddz_s(z,t, p,q):
    """The partial derivative of _s with respect to z.
    """
    w, ddz_w = z**(p/q), (p/q)*z**((p-q)/q)
    return 2*(w+z)*(ddz_w+1)

def ddt_s(z,t, p,q):
    """The partial derivative of _s with respect to t.
    """
    return 0

def _r(z,t, p,q):
    """The square of the radius-ratio implied by having touching circles
    centred at z*e^(it) and z*e^(it)^(p/q).
    """
    return _d(z,t,p,q) / _s(z,t,p,q)

def ddz_r(z,t, p,q):
    """The partial derivative of _r with respect to z.
    """
    return (
        (
              ddz_d(z,t,p,q) * _s(z,t,p,q)
            - _d(z,t,p,q) * ddz_s(z,t,p,q)
        ) / ( _s(z,t,p,q) )**2
    )

def ddt_r(z,t, p,q):
    """The partial derivative of _r with respect to t.
    """
    return (
        (
              ddt_d(z,t,p,q) * _s(z,t,p,q)
            - _d(z,t,p,q) * ddt_s(z,t,p,q)
        ) / ( _s(z,t,p,q) )**2
    )


"""We want to find (z, t) such that:
    _r(z,t,0,1) = _r(z,t,p,q) = _r(z**(p/q), (p*t + 2*pi)/q, 0,1)
"""
p,q = map(int, sys.argv[1:3])
def _f(z, t):
    return _r(z,t,0,1) - _r(z,t,p,q)

def ddz_f(z, t):
    return ddz_r(z,t,0,1) - ddz_r(z,t,p,q)

def ddt_f(z, t):
    return ddt_r(z,t,0,1) - ddt_r(z,t,p,q)

def _g(z, t):
    return _r(z,t,0,1) - _r(z**(p/q), (p*t + 2*pi)/q, 0,1)

def ddz_g(z, t):
    return ddz_r(z,t,0,1) - ddz_r(z**(p/q), (p*t + 2*pi)/q, 0,1) * (p/q)*z**((p-q)/q)

def ddt_g(z, t):
    return ddt_r(z,t,0,1) - ddt_r(z**(p/q), (p*t + 2*pi)/q, 0,1) * (p/q)


epsilon = 1e-10
def find_root(z, t):
    while True:
        v_f, v_g = _f(z, t), _g(z, t)
        print "z=%s, t=%s, v_f=%s, v_g=%s" % (z, t, v_f, v_g)
        if -epsilon < v_f < epsilon and -epsilon < v_g < epsilon:
            return True, z, t
        
        a,b,c,d = ddz_f(z,t), ddt_f(z,t), ddz_g(z,t), ddt_g(z,t)
        print "df/dz=%s, df/dt=%s, dg/dz=%s, dg/dt=%s" % (a,b,c,d)
        det = a*d-b*c
        print "det=%s" % (det,)
        if -epsilon < det < epsilon:
            return False, z, t
        
        delta_z, delta_t = (d*v_f - b*v_g)/det, (a*v_g - c*v_f)/det
        print "delta_z=%s, delta_t=%s" % (delta_z, delta_t)
        z -= delta_z
        t -= delta_t
    
        if z < epsilon:
            return False, z, t

for i in range(1, 100):
    print "Looking for root from (%d, 0)" % (i,)
    ok, z, t = find_root(i, 0)
    if ok:
        print "z=%s, t=%s" % (z,t)
        break
