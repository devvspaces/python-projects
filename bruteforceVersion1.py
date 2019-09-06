import random
def fac(n):
	a=1
	for i in range(1,n+1):
		a*=i
	return a
x=list("267")
u=[]
ids=list(set(x))
pattern=[]
while len(pattern)!=fac(len(ids)):
	for i in range(len(x)):
		n=random.choice(x)
		x.remove(n)
		u.append(n)
		pattern.append(u) if u not in pattern else 0
	x.extend(u)
	u=[]
print(pattern)