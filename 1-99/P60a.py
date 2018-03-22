from itertools import combinations
from sean import primes, isprime
from time import clock

st = clock()
odd_primes = primes(20000)[1::]
sp = primes(200)[1::]

def f(x):
	slots = len(x)
	for i in odd_primes:
		if i < x[-1]:	continue
		c = 0
		for j in x:
			ij = int(str(i)+str(j))
			ji = int(str(j)+str(i))
			if isprime(ij) and isprime(ji):
				c += 1
		if c == len(x):
			return(i)
	return(None)
	
for ab in combinations(sp,2):
	(a,b) = ab
	print(ab)
	while ab:
		fab = f(ab)
		if fab:
			ab = ab + (fab,)
			print(ab)
			if len(ab) == 5:
				print(ab,"5555555555555555555555555555555555555555555")
				break
		else:
			xx = ab
			ab = None
	if len(xx) == 5:	break
print(clock() - st)