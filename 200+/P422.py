# Let H be the hyperbola defined by the equation 12*x**2 + 7*x*y - 12*y**2 = 625.
# Next, define X as the point (7, 1). It can be seen that X is in H.
# Now we define a sequence of points in H, {Pi : i >= 1}, as:
# 	P1 = (13, 61/4)
#	P2 = (-43/6, -4)
# For i > 2, Pi is the unique point in H that is different from Pi-1 and such that line PiPi-1 is parallel to line Pi-2X. 
# It can be shown that Pi is well-defined, and that its coordinates are always rational.
# You are given that P3 = (-19/2, -229/24), P4 = (1267/144, -37/12) and P7 = (17194218091/143327232, 274748766781/1719926784).
# Find Pn for n = 11**14 in the following format:
# If Pn = (a/b, c/d) where the fractions are in lowest terms and the denominators are positive, 
# then the answer is (a + b + c + d) mod 1 000 000 007.
# For n = 7, the answer would have been: 806236837.

# P1 = (13, 1, 61, 4)
# P2 = (-43, 6, -4, 1)
# P3 = (-19, 2, -229, 24)
# P4 = (1267, 144, -37, 12)
# P7 = (17194218091, 143327232, 274748766781, 1719926784)

from fractions import gcd

def F(P1, P2, minusflag = False):
	
	xpn, xpd, ypn, ypd = 7, 1, 1, 1	# X the point (7,1)
	x1n, x1d, y1n, y1d = P2
	x2n, x2d, y2n, y2d = P1
	
	mn, md = x2d*xpd*(y2n*ypd - y2d*ypn), y2d*ypd*(x2n*xpd - x2d*xpn)
	bn, bd = y1n*md*x1d - y1d*mn*x1n, y1d*md*x1d
	
	x0n = md * (24*mn*bn - 7*bn*md + 25 * (bn*bn*md*md - 4*bd*bd * (12*mn*mn - 7*mn*md - 12*md*md)) ** (1/2))
	if gcd(x0n, x1n) == x1n:
		x0n = md * (24*mn*bn - 7*bn*md - 25 * (bn*bn*md*md - 4*bd*bd * (12*mn*mn - 7*mn*md - 12*md*md)) ** (1/2))
	
	x0d = bd * (-24*mn*mn + 14*mn*md + 24*md*md)
	y0n, y0d = bd*mn*x0n + bn*md*x0d, md*x0d*bd
	
	gcdx, gcdy = gcd(x0n, x0d), gcd(y0n, y0d)
	
	P0 = (x0n/gcdx, x0d/gcdx, y0n/gcdy, y0d/gcdy)
	#P0 = (x0n,x0d,y0n,y0d)
	
	return P0
	
if __name__ == '__main__':
	from sys import argv
	from time import clock
	
	st = clock()
	
	numloops = int(argv[1])
	
	P1, P2 = (13, 1, 61, 4), (-43, 6, -4, 1)
	
	for j in range(numloops-2):
		P1, P2 = P2, F(P1, P2)
	
	print('P', numloops, P2, clock() - st)