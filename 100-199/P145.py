# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd decimal digits.
# For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
# Leading zeroes are not allowed in either n or reverse(n).
# There are 120 reversible numbers below one-thousand.
# How many reversible numbers are there below one-billion (10**9)?

from sys import argv
from time import clock

def sod(n):
	sod = 0
	for i in str(n):
		sod += int(i)
	return sod
	
def all_odd_digits(n):
	for i in str(n):
		if not (int(i) % 2):
			return False
	return True	
	
def rev_sum(n):
	rsum = 0
	l = len(str(n))-1
	for k in range(l+1):
		rsum += int(str(n)[k]) * (10**k + 10**(l-k))
	return rsum
	
def rev_sum2(n):
	rsum = ex = 0
	sn = str(n)
	l = len(sn) - 1
	halfl = int(l/2)
	for k in range(halfl+1):
		rsum += (int(sn[k]) + int(sn[l-k]))*(10**(k) + 10**(l-k))
	if not l%2: ex = 2 * int(sn[halfl]) * 10**(halfl)
	rsum -= ex
	return rsum
	
count = 0
st = clock()
for i in range(10**int(argv[1])):
	si = str(i)
	if si[-1] == '0':	continue
	if all_odd_digits(rev_sum(i)):	count += 1
print(count)
print(clock()-st)