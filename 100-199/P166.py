# d1 + d2 + d3 + d4 = a
# d5 + d6 + d7 + d8 = a
# d9 + d10 + d11 + d12 = a
# d13 + d14 + d15 + d16 = a
# d1 + d5 + d9 + d13 = a
# d2 + d6 + d10 + d14 = a
# d3 + d7 + d11 + d15 = a
# d4 + d8 + d12 + d16 = a
# d1 + d6 + d11 + d16 = a
# d4 + d7 + d10 + d13 = a

# [1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0][a]
# [0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0][a]
# [0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0][a]
# [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1][a]
# [1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0][a]
# [0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0][a]
# [0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0][a]
# [0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1][a]
# [1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1][a]
# [0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0][a]

from itertools import product
c = 0
for d in product(range(10), repeat = 16):
	print(d,c)
	e5 = d[4] + d[7] - d[9] - d[10]
	if e5 == 0:
		e8 = d[8] + d[9] + d[10] + d[11]
		e9 = d[12] + d[13] + d[14] + d[15]
		if e8 == e9:
			e1 = d[0] - d[7] - d[11] - d[13] - d[14] - d[15]
			e2 = d[1] - d[7] + d[9] - d[10] - d[11] - d[14] - d[15] - d[15]
			if  e1 == e2:
				e3 = d[2] + d[7] - d[9] + d[10] + d[11] + d[13] + d[14] + d[14] + d[15] + d[15]
				e6 = d[5] + d[7] + d[10] + d[11] + d[13] + d[14] + d[15] + d[15]
				if e3 == e6:
					e4 = d[3] + d[7] + d[11] + d[15]
					e7 = d[6] - d[7] + d[9] - d[11] - d[13] - d[14] - d[15] - d[15]
					if e4 == -e7:
						c += 1
print(c)