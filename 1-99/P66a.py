# Consider quadratic Diophantine equations of the form:
# x**2 - D * y**2 = 1
# For Example, when D = 13, the minimal solution in x is 649**2 - 13 * 180**2 = 1.
# It can be assumed that there are no solutions in positive integers when D is square.
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
# 3**2 - 2 * 2**2 = 1
# 2**2 - 3 * 1**2 = 1
# 9**2 - 5 * 4**2 = 1
# 5**2 - 6 * 2**2 = 1
# 8**2 - 7 * 3**2 = 1
# Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D = 5.
# Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

def F(D):
	# x**2 = 1 + D*y**2
	squares = [x**2 for x in range(100)]
	for y in range(1, 21):
		if 1+D*(y**2) in squares:
			print((1+D*y**2)**.5,D,y)
		
F(5)