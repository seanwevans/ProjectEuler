# Consider numbers t(n) of the form t(n) = 2*n**2-1 with n > 1.
# The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
# It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
# For n = 10000 there are 2202 numbers t(n) that are prime.
# How many numbers t(n) are prime for n <= 50,000,000 ?

# PrimePi[50000000] == 3001134

# t(n) = 2*n*n - 1
# t(50000000) = 4999999999999999
# (1/2)*(t(n) + 1) = n**2

# print([2*n**2-1 for n in range(2,9)])

# t(2k) = 2*(2k)*(2k) - 1 = 8*k*k - 1
# t(2k+1)= 2*(2k+1)*(2k+1)-1 = 2*(4k**2+4k+1)-1 = 8*k*k+8k+1 = 8k(k+1)+1
# prime[h] = 2*n*n-1
# (1/2)*(prime[h]+1) = n * n

# t(n) = prime(h)
# prime(h) = 2*n*n-1
# (prime(h)+1)(1/2) = n*n

from gmpy2 import mpz, is_square
from sean import genPrimes

L = 167
c = 0

for prime in genPrimes():
	if prime > L:	break
	sq = mpz((1/2) * (prime + 1))
	print(sq)
print(c)