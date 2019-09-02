def format_duration(seconds):
	if seconds < 1:
		return "0 second"
	else:
		min,hr,sec,day,year,m=0,0,seconds,0,0,[]
		time1=[]
		while sec > 59:
			min += sec//60
			sec = sec % 60
		while min > 59:
			hr += min//60
			min = min%60
		while hr > 23:
			day += hr//24
			hr = hr%24
		while day > 364:
			year += day//365
			day = day%365
		for v,i in enumerate([year,day,hr,min,sec]):
			if i != 0:
				m.append(v)
		var=[year,day,hr,min,sec]
		v1 = ["years","days","hours","minutes","seconds"]
		v2 = ["year","day","hour","minute","second"]
		time1+=[str(j)+' '+o if j > 1 else str(j)+' '+l for j,o,l in zip(var,v1,v2)]
		hu =[]
		hu+=[time1[i] for i in m]
		p=", ".join(hu[:len(hu)-1])
		q = hu[-1]
		k = [p,q]
		if p == "":
			k.remove(p)
		return " and ".join(k)
print(format_duration(365800))