def format_duration(secs):
	if secs<1:
		return "0 second"
	year=secs//(365*24*3600)
	r=secs%(365*24*3600)
	day=r//(24*3600)
	r=r%(24*3600)
	hr=r//(3600)
	r=r%3600
	min=r//60
	r=r%60
	sec=r
	m,time1=[],[]
	for v,i in enumerate([year,day,hr,min,sec]):
		if i != 0:
			m.append(v)
	var=[year,day,hr,min,sec]
	v1 = ["years","days","hours","minutes","seconds"]
	v2 = ["year","day","hour","minute","second"]
	time1=[str(j)+' '+o if j > 1 else str(j)+' '+l for j,o,l in zip(var,v1,v2)]
	hu=[time1[i] for i in m]
	p=", ".join(hu[:len(hu)-1])
	q = hu[-1]
	k = [p,q]
	if p == "":
		k.remove(p)
	return " and ".join(k)
print(format_duration(9061))