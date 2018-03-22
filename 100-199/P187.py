# A composite is a number containing at least two prime factors. For example, 15 = 3 * 5; 9 = 3 * 3; 12 = 2 * 2 * 3.
# There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
# How many composite integers, n < 10**8, have precisely two, not necessarily distinct, prime factors?

from sean import primesbelow

n = 10 ** 8
primes = primesbelow(n)
i = j = c = 0

while primes[i]**2 < n:
	j = i
	while primes[i] * primes[j] < n:
		c += 1
		j += 1
	i += 1
print(c)
