from sean import gcd_steps as E

def S(N):
	total = 0
	for x in range(1, N+1):
		for y in range(1, N+1):
			total += E(x, y)
	return total