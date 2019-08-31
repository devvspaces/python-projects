def format_duration(seconds):
	if seconds < 1:
		return "0 second"
	else:
		min,hr,sec,day,year,m=0,0,seconds,0,0,[]
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
		if year != 0:
			m.append(0)
		if day != 0:
			m.append(1)
		if hr!=0:
			m.append(2)
		if min!=0:
			m.append(3)
		if sec!=0:
			m.append(4)
		if year > 1:
			year = str(year)+' '+'years'
		else:
			year = str(year)+' '+'year'
		if day > 1:
			day = str(day)+' '+'days'
		else:
			day = str(day)+' '+'day'
		if hr > 1:
			hr = str(hr)+' '+'hours'
		else:
			hr = str(hr)+' '+'hour'
		if min > 1:
			min = str(min)+' '+'minutes'
		else:
			min = str(min)+' '+'minute'
		if sec > 1:
			sec = str(sec)+' '+'seconds'
		else:
			sec = str(sec)+' '+'second'
		time1 =[year,day,hr,min,sec]
		hu =[]
		for i in m:
			hu.append(time1[i])
		p=", ".join(hu[:len(hu)-1])
		q = hu[-1]
		k = [p,q]
		if p == "":
			k.remove(p)
		return " and ".join(k)
print(format_duration(2384940))