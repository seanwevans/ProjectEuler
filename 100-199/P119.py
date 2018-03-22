# The number 512 is interesting because it is equal to the sum of its digits raised to some power:
# 5 + 1 + 2 = 8, and 8**3 = 512. Another example of a number with this property is 614656 = 284.
# We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
# You are given that a(2) = 512 and a(10) = 614656.
# Find a(30).

from math import log, modf
from itertools import count

def SumOfDigits(n):
	total = 0
	for c in str(n):
		total += int(c)
	return total

c = 1
	
for i in count(10):
	isod = SumOfDigits(i)
	if isod > 1 and modf(log(i,isod))[0] == 0.0:
		print("a(",c,") =",i)
		c += 1