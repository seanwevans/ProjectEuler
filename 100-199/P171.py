# For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.
# f(3) = 3**2 = 9,
# f(25) = 2**2 + 5**2 = 4 + 25 = 29,
# f(442) = 4**2 + 4**2 + 2**2 = 16 + 16 + 4 = 36
# Find the last nine digits of the sum of all n, 0 < n < 10**20, such that f(n) is a perfect square.

from gmpy2 import is_square

def f(n):
	c = 0
	for i in str(n):
		c += int(i) ** 2
	return(c)
	
c = 0	
for i in range(1,10**20):
	print(i,c)
	if is_square(f(i)):
		c += i
		
# a1**2 + a2**2 + a3**2 + ... + at**2 == b**2