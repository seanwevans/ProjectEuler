# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, 
# and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?

from sean import gcd

L = 1500000
NumIntTri = {x:[] for x in range(12, L+1)}
UpperM = int((1/2) * (1 + (1 + 4*L)**.5))

for m in range(2, UpperM):
	for n in range(m-1, 0, -2):
		if gcd(m, n) == 1:
			k = 1
			Sumabc = 0
			while Sumabc <= L:
				a = k * (m**2 + n**2)
				b = k * 2 * m * n
				c = k * (m**2 - n**2)
				abc = (a,b,c)
				Sumabc = a + b + c
				if Sumabc <= L and abc not in NumIntTri[Sumabc]:
					NumIntTri[Sumabc].append(abc)
				k += 1

cnt = 0
for Triangles in NumIntTri.values():
	if len(Triangles) == 1:
		cnt += 1

print(cnt)