#! /usr/bin/python3

import math
import matplotlib.pyplot as plotter

def order(a,N):
  # finds the order of a number a**r = 1 mod N
  # a**r mod N = ((a**(r-1) Mod N) (a Mod N)) Mod N
  x = 1
  for r in range(1,N):
  #  if a**r % N == 1:
    x = (x*a) % N
    if x == 1:
      print('Found r = ',r)
      return r
  return 0

def fastPow(a,b,N):
# returns a^b mod N
  ans = 1
  while (b > 0):
    if b % 2:
      ans = (ans * a) % N
    b = b // 2
    a = (a * a) % N
  return ans

def plot_shor(a,r,N):
  z = list(range(2*r))
  y = list(range(2*r))
  y[0] = 1
  for i in range(1,2*r):
    y[i] = (y[i-1]*a)%N
  y = list(a**z0%N for z0 in z)
  plotter.plot(z,y)
  plotter.xlabel('z')
  plotter.ylabel(f'{a}^z mod {N}')
  plotter.show()

def shor(N, a=0):
  # pick a guess for a
  if a <= 0 or a >= N:
    a = N // 2
  while (a < N):
    a += 1
    if math.gcd(a,N) != 1:  # almost never happens
      q = math.gcd(a,N)
      p = N // q
      r = 0
      return(p,q,a,r)
    r = order(a, N)
    if (r%2 != 0 or r == 0):
      print("r must be an even number.  r =",r)
      continue
    x = fastPow(a, r//2, N)
    if (x - 1) % N == 0 :
      print("N must not divide a**(r/2) - 1")
      continue    
    q = math.gcd((x-1), N)
    p = math.gcd((x+1), N)
    if (p == 1 or q == 1):
      continue
    return (p,q,a,r)
  print('Error: a = ',a,'  r = ',r)
  return(-1,-1,-1,-1)

#N = int(input('Enter a number to factor: '))
#p = 1223
#q = 1217
p = 97117
q = 98453
#p = 11
#q = 23
N = p*q
print('N = ', N)
(p,q,a,r) = shor(N)
print('a = ',a,'  r = ',r,'  p = ',p,' q =',q, '  N = ',N)
#plot_shor(a,r,N)





  
  
