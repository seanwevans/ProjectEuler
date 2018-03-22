# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from sean import isprime, primesbelow
from itertools import combinations
from math import factorial

def ConcPrimesQ(N):
	sN = str(N)
	for i in range(1, len(sN)):
		l, r = sN[:i], sN[i:]
		if l[0] == '0' or r[0] == '0' or (not isprime(int(l))) or (not isprime(int(r))):
			continue
		if isprime(int(r+l)):
			return(int(r),int(l))
	return((0,0))

L = 5
primes = primesbelow(10**6)
concprimes = []

for p in primes:
	(a, b) = ConcPrimesQ(p)
	if (a,b) != (0,0) and (b,a) not in concprimes:	
		concprimes.append((a,b))

D = {}
a = []

for i in concprimes:
	D[i[0]] = []
	D[i[1]] = []
	
for i in concprimes:
	D[i[0]].append(i[1])
	D[i[1]].append(i[0])
	
for i in D:
	D[i] = list(set(D[i]))
	if len(D[i]) >= L - 1:
		a.append(i)
print(a)
c = 0
