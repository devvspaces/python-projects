s=["file","sample","sample","file","file","file(1)","file(1)"]
print(s)
j=["({})".format(i) for i in range(1,len(s))]
j.insert(0,'')
print(j)
m=""
n=0
l2=[]
for i in set(s):
	for x in s:
		if i == x:
			m=x
			if x in l2:
				n+=1
			m+=j[n]
			print(m)
			l2.append(m)
			print(l2)
		m=""
	n=0