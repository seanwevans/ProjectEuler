# It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

# 10 	-> {2, 3, 5, 7} 			-> 10/2=5, max 5 terms 		-> combinations_wr(primes,5->2), break once sum > 10
# 100 	-> set(primesbelow(100)) 	-> 100/2=50, max 50 terms	-> combinations_wr(primes,50->2), break once sum > 100
# n		-> set(primesbelow(n))		-> max n/2 terms			-> combinations_wr(primes,n/2->2), break sum > n

