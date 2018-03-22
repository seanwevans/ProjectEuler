# Let N be a positive integer and let N be split into k equal parts, r = N/k, so that N = r + r + ... + r.
# Let P be the product of these parts, P = r * r * ... * r = r**k.
# For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.2**5 = 51.53632.
# Let M(N) = P_max for a given value of N.
# It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts which 
# leads to P_max = (11/4)**4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.
# However, for N = 8 the maximum is achieved by splitting it into three equal parts, 
# so M(8) = 512/27, which is a non-terminating decimal.
# Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.
# For example, Sum of D(N) from N=5 to 100 = 2438.
# Find Sum of D(N) from N=5 to 10000.

from sean import primefactors

def M(N):
	maxs = 0
	for k in range(1,N):
		s = N**k/k**k
		if s > maxs:
			maxk = k
	return maxk
	
def Terminates(n):
	if not n%2 or not n%5:
		return True
	else:
		return False
	
def D(N):
	if Terminates(M(N)):
		return -N
	else:
		return N

count = 0
		
for N in range(5, 101):
	print(N)
	count += D(N)
	
print(count)