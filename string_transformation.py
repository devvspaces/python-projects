def string_transformation(s):
	sm =""
	p = s
	s = []
	for i in p:
		if i.isalpha():
			sm += i
		else:
			s.append(sm)
			sm =""
			s.append(" ")
	s.append(sm)
	print(s)
	sm = ""
	for i in s:
		for x in i:
			if x.islower():
				x = x.upper()
				sm += x
			else:
				x = x.lower()
				sm += x
		s[s.index(i)] = sm
		sm =""
	s.reverse()
	return "".join(s)
print(string_transformation("Example Input    foR I Ayo      "))