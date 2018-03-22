#a^2+b^2=c^2+1
from itertools import combinations
limit = int((25000000) ** .5) + 1
almost_squares = set([i**2+1 for i in range(1,limit)])
sumsq = set([i+j for (i,j) in combinations([k**2 for k in range(1,limit**2)],2)])
print(sum(list(almost_squares.intersection(sumsq))))