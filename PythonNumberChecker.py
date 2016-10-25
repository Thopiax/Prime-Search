from math import sqrt

fnum = int(input("Is it prime? "))

factors = []

fundamental_primes = [2]
prime = True

def count(i):
  x =2
  while str(float(fnum)/float(i**x))[-1] == '0':
      x += 1
  if x>=2: return '%d^%d' % (i,x-1)
  else: return i

for i in range(2,int(sqrt(fnum))):
  for n in fundamental_primes:
    if i%n == 0 and i!=n:
      break
  else:
    fundamental_primes.append(i)
    if fnum%i == 0: 
      prime = False
      factors.append(count(i))

if prime:
  print 'The number %d is prime.' % fnum
else:
  print "The number %d is not prime. It\'s prime factors are %s" % (fnum, "x".join([str(i) for i in factors]))
