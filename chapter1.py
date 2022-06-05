#!/usr/bin/python3

import clifford as cl

print('Capítulo 1')

print('\nEjercicio 1')
# Define vectors
a = cl.Clifford2(0,0,1,-1)
b = cl.Clifford2(0,1,1,0)
c = cl.Clifford2(1,0,1,0)
print('a =',a)
print('b =',b)
print('c =',c)
# Compute ab, ac.
print('ab =',a*b)
print('ac =',a*c)

print('\nEjericio 2')
# Define vectors
a = cl.Clifford2(0,0,1,1)
b = cl.Clifford2(0.5,0.5,0,0)
print('a =',a)
print('b =',b)
# Compute ab, ba.
print('ab =',a*b)
print('ba =',b*a)

print('\nEjericio 3')
# Define vectors
a = cl.Clifford2(1,1,0,0)
b = cl.Clifford2(-1,1,0,0)
c = cl.Clifford2(0,1,1,0)
print('a =',a)
print('b =',b)
print('c =',c)
# Compute ab, ba, ac, ca, bc.
print('ab =',a*b)
print('ba =',b*a)
print('ac =',a*c)
print('ca =',c*a)
print('bc =',b*c)

print('\nEjericio 4')
# Define vectors
a = cl.Clifford2(0.5,0.5,0,0)
b = cl.Clifford2(0,1,0,1)
print('a =',a)
print('b =',b)
# Compute a^2, b^2, ac, ca, bc.
print('a^2 =',a*a)
print('b^2 =',b*b)

print('\nEjericio 5')
# Define vectors
a = cl.Clifford2(0,1,-2,0)
b = cl.Clifford2(0,1,1,0)
r = cl.Clifford2(0,5,-1,0)
print('a =',a)
print('b =',b)
print('r =',r)
# Compute alpha, beta in r = alpha*a + beta*b.
rb = r.wedge(b)
print('rnb =',rb)
ab = a.wedge(b)
print('anb =',ab)
ar = a.wedge(r)
print('anr =',ar)
alpha = rb*ab.inverse()
beta = ar*ab.inverse()
print('alpha =',alpha)
print('beta =',beta)

print('\nEjericio 6')
# Define vectors
a = cl.Clifford2(0,8,-1,0)
b = cl.Clifford2(0,2,1,0)
print('a =',a)
print('b =',b)
# Compute a||, a_|
ap = a.dot(b)*b.inverse()
print('a|| = ',ap)
ap = a.wedge(b)*b.inverse()
print('a_| = ',ap)

print('\nEjericio 7')
# Define vectors
r = cl.Clifford2(0,4,-3,0)
a = cl.Clifford2(0,3,-1,0)
b = cl.Clifford2(0,2,1,0)
print('r =',r)
print('a =',a)
print('b =',b)
# Reflect r across a and then across b
r1 = a*r*a.inverse()
print('ara^-1 = ',r1)
r2 = (b*a)*r*(b*a).inverse()
print('(ba)r(ba)^-1 = ',r2)

print('\nEjericio 8')
# Define vectors
print('Symbolic operations not available')

print('\nEjericio 9')
# Define vectors
u = cl.Clifford2(1,1,0,1)
print('u =',u)
# Compute u^-1
ui = u.inverse()
print('u^-1 = ',ui)
print('u.ginv*(u*u.ginv)^-1 = ', u.ginv()*(u*u.ginv()).inverse())
print('(u*u.ginv)^-1*g.ginv = ', (u*u.ginv()).inverse()*u.ginv())
print('u.ginv*(u.ginv*u)^-1 = ', u.ginv()*(u.ginv()*u).inverse())
print('u.reverse*(u*u.reverse)^-1 = ', u.reverse()*(u*u.reverse()).inverse())
print('(u*u.reverse)^-1*g.reverse = ', (u*u.reverse()).inverse()*u.reverse())
print('u.reverse*(u.reverse*u)^-1 = ', u.reverse()*(u.reverse()*u).inverse())

print('\nEjericio 10')
# Define vectors
print('Symbolic operations not available')
