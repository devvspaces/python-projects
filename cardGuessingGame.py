import random
comp = ['cat','dog','cow','monkey','lion','tiger','leo','snake','zebra','croc']
c1 = c2 = 0
cp = gp = 0
for i in range(len(comp)):
	random.shuffle(comp)
	c1 = random.choice(comp)
	print("Select the card that the computer has chose to earn points")
	for x in comp:
		print(x, comp.index(x))
	s = int(input("Select the position :- "))
	c2 = comp[s]
	if c2 == c1:
		gp += 5
		print("Correct")
	else:
		cp += 5
		print("Incorrect")
	comp.remove(c1)
print("Computer\t\t\tYou\n"+str(cp)+"\t\t\t"+str(gp))
print("Through with session")