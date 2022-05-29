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
rb = cl.wedge(r,b)
print('rnb =',rb)
ab = cl.wedge(a,b)
print('anb =',ab)
ar = cl.wedge(a,r)
print('anr =',ar)
alpha = rb*ab.inverse()
beta = ar*ab.inverse()
print('alpha =',alpha)
print('beta =',beta)
