from math import sqrt

fnum = input("Limit: ")

fundamental_primes = [2]
nonprimes = [0,1]

for i in range(2,int(sqrt(fnum))):
	for n in fundamental_primes:
		if i%n == 0 and i!=n:
			break
	else:
		fundamental_primes.append(i)
		nonprimes += [x*i for x in range(i,int(fnum/i)+1)]

primes = list(set(range(fnum)) - set(nonprimes))
primes_count = len(primes)
primes.sort()

print primes

# num = int(input("Is this a prime number?: "))
# 99877

