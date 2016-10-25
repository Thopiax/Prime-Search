from math import sqrt

fnum = int(input("Is it prime? "))
fundamental_primes = [2]

prime = True


factors = []

for i in range(2,int(sqrt(fnum))):
  if i > 1:
    for n in fundamental_primes:
      if i%n == 0 and i!=n and i!=1:
        break
    else:
      fundamental_primes.append(i)
      if fnum%i == 0: prime = False

def calcFactors(ni,p=False):
  n = ni
  for x in list(set(fundamental_primes)):
    while True:
      if n%x == 0:
        factors.append(x)
        n = n/x
      else: break

  if n!=1: factors.append(n)
  factors.sort()
  p = True

if prime:
  print 'The number %d is prime.' % fnum
else:
  calcFactors(fnum)
  print "The number %d is not prime. It\'s prime factors are %s" % (fnum, "x".join([str(i) for i in factors]))
