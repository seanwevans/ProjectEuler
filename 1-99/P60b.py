# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from itertools import *

def smallprimes(k):
	sieve = [True] * k
	for i in range(3, int(k ** .5) + 1, 2):
		if sieve[i]:
			sieve[i*i::2*i] = [False] * int(((k-i * i-1)/(2*i) + 1))
	return [2] + [i for i in range(3,k,2) if sieve[i]]

def isprime(k):
	for i in range(2, int(k ** 0.5)+1):
		if not k % i:	return False
	return True
	
primes = smallprimes(1000)

conc_primes = []

for (p1, p2) in combinations(primes, 2):
	q1 = int(str(p1)+str(p2))
	q2 = int(str(p2)+str(p1))
	if isprime(q1) and isprime(q2):
		conc_primes.append((p1,p2))

conc_primes = list(set(conc_primes))
pr_dict = {x:[] for (x,y) in conc_primes}
for (a,b) in conc_primes:
	pr_dict[a].append(b)
	
print(pr_dict)