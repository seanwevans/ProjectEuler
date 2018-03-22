from itertools import combinations

def product(numlist):
	c = 1
	for i in numlist:
		c *= i
	return(c)
	
def F(x):
	return(product(x)-sum(x))
	
d = {i:[] for i in range(2,)}

for x in range(2,15):
	for a in combinations(range(2,21),x):
		d[F(a)+x].append(sum(a)+F(a))
	
print(d)