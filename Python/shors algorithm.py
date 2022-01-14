import math
import matplotlib.pyplot as plotter

def order(a,N):
  # finds the order of a number a**r = 1 mod N
  # a**r mod N = ((a**(r-1) Mod N) (a Mod N)) Mod N
  x = 1
  for r in range(1,N):
  #  if a**r % N == 1:
    x = (x*a)%N
    if x == 1:
      return r
  return 0

def shor(N, a=0):
  # pick a guess for a
  if a <= 0 or a >= N:
    a = N//2
  while (a < N):
    a += 1
    if math.gcd(a,N) != 1:  # almost never happens
      q = math.gcd(a,N)
      p = N//q
      r = 0
      return(p,q,a,r)
    r = order(a,N)
    if (r%2 != 0 or r == 0):
      print("r must be an even number.  r =",r)
      continue 
    x = a**(r//2) # calculate x
    if (x - 1) % N == 0 :
      print("N must not divide a**(r/2) - 1")
      continue    
    q = math.gcd((x-1), N)
    p = math.gcd((x+1), N)
    return (p,q,a,r)
  print('Error: a = ',a,'  r = ',r)
  return(-1,-1,-1,-1)

#N = int(input('Enter a number to factor: '))
#p = 1223
#q = 1217
#p = 97117
#q = 98453
p = 11
q = 23
N = p*q

(p,q,a,r) = shor(N)
print('a = ',a,'  r = ',r,'  p = ',p,' q =',q, '  N = ',N)

z = list(range(N))
y = list(range(N))
y[0] = 1
for i in range(1,N):
    y[i] = (y[i-1]*a)%N
#y = list(a**z0%N for z0 in z)
plotter.plot(z,y)
plotter.xlabel('z')
plotter.ylabel(f'{a}^z(mod{N})')
plotter.show()




  
  
