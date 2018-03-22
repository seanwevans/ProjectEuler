# In the following equation x, y, and n are positive integers.
# 1/x + 1/y = 1/n
# For n = 4 there are exactly three distinct solutions:
# 1/5 + 1/20 = 1/4
# 1/6 + 1/12 = 1/4
# 1/8 + 1/8 = 1/4
# What is the least value of n for which the number of distinct solutions exceeds one-thousand?

# 1/x + 1/y = 1/n
# n = 1/(1/x+1/y)
# n = 1/(x+y/xy)
# n = xy / x+y
# if x+y divides xy then n is an integer
# x+y = nxy
# xy % x+y = 0

from itertools import combinations_with_replacement as combo_wr
from sys import argv
from time import clock

st = clock()
lim = int(argv[1])
max_dist_solutions = int(argv[2])
D = {n:0 for n in range(1, lim//2+1)}
for (x,y) in combo_wr(range(1, lim),2):
	s, p = x+y, x*y
	if p % s == 0:
		D[p//s] += 1

L = []
for key in D:
	if D[key] > max_dist_solutions:	
		L.append(key)

print(clock() - st)
if L:	print(min(L))
