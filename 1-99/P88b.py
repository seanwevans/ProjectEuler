# 0,0; 0,1
off = 2
offMaxK = MaxK - off

for a in count(2):
	t = (a,a)
	if F(t) > offMaxK:	break
	
	for b in count(a):
		t = (a,b)
		ft = F(t) + off
		if ft > MaxK:	break
		else:
			#print(t,ft,product(t)) 
			pt = product(t)
			if not KSumProd[ft] or KSumProd[ft] > pt:
				KSumProd[ft] = pt

# 0,0,0; 0,1,1; 0,1,2				
off = 3
offMaxK = MaxK - off

for a in count(2):
	t = (a,a,a)
	if F(t) > offMaxK:	break
	
	for b in count(a):
		t = (a,b,b)
		if F(t) > offMaxK:	break
		
		for c in count(b):
			t = (a,b,c)
			ft = F(t) + off
			if ft > MaxK:	break
			else:
				#print(t,ft,product(t))
				pt = product(t)
				if not KSumProd[ft] or KSumProd[ft] > pt:
					KSumProd[ft] = pt

# 0,0,0,0; 0,1,1,1; 0,1,2,2; 0,1,2,3
off = 4
offMaxK = MaxK - off

for a in count(2):
	t = (a,a,a,a)
	if F(t) > offMaxK: break
	
	for b in count(a):
		t = (a,b,b,b)
		if F(t) > offMaxK:	break
		
		for c in count(b):
			t = (a,b,c,c)
			if F(t) > offMaxK:	break
			
			for d in count(c):
				t = (a,b,c,d)
				ft = F(t) + off
				if ft > MaxK:	break
				else:
					#print(t,ft,product(t))
					pt = product(t)
					if not KSumProd[ft] or KSumProd[ft] > pt:
						KSumProd[ft] = pt
						
MaxK = 12000
KSumProd = {x:0 for x in range(2,MaxK+1)}

def Gen_Code(depth):
	print(depth)

	def AddOne(lis, offset):
		L = []
		for i in range(offset):
			L.append(lis[i])
		for i in range(offset, len(lis)):
			L.append(lis[i]+1)
		return(L)
	
	def Tabs(n):
		a = ''
		for j in range(n):
			a += '\t'
		return(a)
	
	alphabet = [chr(x) for x in range(ord('a'),ord('z'))]
	t = [0] * depth
	
	# Begining
	code = 'off = ' + str(depth) + '\n'
	code += 'offMaxK = MaxK - off\n'
	code += 'for a in count(2):\n'
	code += '\tt = (a' + ',a' * (depth-1) + ')\n'
	code += '\tif F(t) > offMaxK:\tbreak\n'
	 
	# Middle
	for i in range(1, depth):
		t = AddOne(t, i)
		s1 = ','*depth
		s2 = ''.join([alphabet[t[x]] for x in range(depth)])
		code += Tabs(i) + 'for ' + alphabet[i] + ' in count(' + alphabet[i-1] + '):\n'
		code += Tabs(i+1) + 't = (' + ''.join(i for j in zip(s1,s2) for i in j)[1:] + ')\n'
		if i != depth-1:	code += Tabs(i+1) + 'if F(t) > offMaxK:\tbreak\n'
	
	# End
	t = AddOne(t, depth-1)
	code += Tabs(depth) +	'ft = F(t) + off\n'
	code += Tabs(depth) + 'if ft > MaxK:\tbreak\n'
	code += Tabs(depth) + 'else:\n'
	code += Tabs(depth+1) +	'pt = product(t)\n'
	code += Tabs(depth+1) + 'if not KSumProd[ft] or KSumProd[ft] > pt:\tKSumProd[ft] = pt\n'
	
	return(code)

for k in range(2, MaxK):
	exec(Gen_Code(k))

L = [KSumProd[x] for x in KSumProd.keys()]
print(sum(set(L)))