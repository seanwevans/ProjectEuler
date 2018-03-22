# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
# Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

from math import floor
from time import clock

st = clock()

def F(s, n, k):
	''' returns the probability of summing to k when throwing an s sided die n times, dictated by this equation:
	the sum from i = 1 to k-n+1 of F(s,1,i)*F(s,n-1,k-i), F(s,1,k) = 1/s for 1 <= k <= s and 0 otherwise. Takes
	about 240s to call this function twice while running k->4-37'''
	
	if n == 1:
		if 1 <= k <= s:
			return 1./s
		else:
			return 0
	
	prob = 0
	
	for i in range(1, k - n + 2):
		prob += F(s, 1, i) * F(s, n - 1, k - i)
		
	return prob
	
Peter_PDF, Colin_PDF = [], []

for k in range(4, 37):
	Peter_PDF.append(F(4, 9, k))
	Colin_PDF.append(F(6, 6, k))
	
result = 0

for j in range(4,37):
	result += Peter_PDF[j-6] * sum(Colin_PDF[:j-6])
print(result)
# P(pete rolls a 6) * P(colin rolls less than a 6) + P(pete rolls a 7) * P(colin rolls less than a 7) + ...