# The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.

from itertools import count, permutations, combinations

def KDigitCubes(K):
	if K == 1:	st = 0
	else:		st = int((10**(K-1))**(1/3))+1
	for y in count(st):
		y3 = y**3
		if len(str(y3)) == K+1:
			break
		yield y3
		
def IsPerm(first, second):
	f, s = [int(i) for i in str(first)], [int(i) for i in str(second)]
	f.sort()
	s.sort()
	if f == s:	return True
	else:		return False
		
if __name__ == '__main__':
	for numdigits in count(8):
		cubes = [i for i in KDigitCubes(numdigits)]
		Cubedict = {c:0 for c in cubes}
		for p in permutations(cubes, 2):
			if IsPerm(p[0],p[1]):
				Cubedict[p[0]] += 1
		L = []
		for p in Cubedict:
			if Cubedict[p] == 4:
				L.append(p)
		if L:	
			print(min(L))
			break