z = scipy.optimize.root(f, array([5,0])).x
zz = z[0] * cos(z[1]) + 1j*( z[0] * sin(z[1]) )
w = array([ z[0]**(5/8), (5*z[1]+2*pi)/8 ])
ww = w[0] * cos(w[1]) + 1j*( w[0] * sin(w[1]) )

abs(ww-1)/(abs(ww)+1)
abs(zz-1)/(abs(zz)+1)
abs(zz-ww)/(abs(zz)+abs(ww))

ww, zz



z = scipy.optimize.root(ff, array([1,0])).x
zz = z[0] * cos(z[1]) + 1j*( z[0] * sin(z[1]) )
w = array([ z[0]**(5/8), (5*z[1]+2*pi)/8 ])
ww = w[0] * cos(w[1]) + 1j*( w[0] * sin(w[1]) )

abs(ww-1)/(abs(ww)+1)
abs(zz-1)/(abs(zz)+1)
abs(zz-ww)/(abs(zz)+abs(ww))

ww, zz






z1 = scipy.optimize.root(f, array([5,0])).x
zz1 = z1[0] * cos(z1[1]) + 1j*( z1[0] * sin(z1[1]) )
w1 = array([ z1[0]**(5/8), (5*z1[1]+2*pi)/8 ])
ww1 = w1[0] * cos(w1[1]) + 1j*( w1[0] * sin(w1[1]) )

z2 = scipy.optimize.root(ff, array([1,0])).x
zz2 = z2[0] * cos(z2[1]) + 1j*( z2[0] * sin(z2[1]) )
w2 = array([ z2[0]**(5/8), (5*z2[1]+2*pi)/8 ])
ww2 = w2[0] * cos(w2[1]) + 1j*( w2[0] * sin(w2[1]) )

