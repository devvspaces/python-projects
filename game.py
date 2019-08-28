print("Loading Data.......\n")
from cardClass import card
import numpy as np
import random
a = np.zeros((13,4))
b = []
for i in range(13):
	a[i] = i+2
for x in range(4):
	if x == 0:
		sh = "star"
	elif x == 1:
		sh = "square"
	elif x == 2:
		sh = "circle"
	else:
		sh = "triangle"
	for i in a[0:,x]:
		i = int(i)
		if i == 2:
			c = card(sh,i,"pick two")
			b.append(c)
		elif i == 14:
			c = card(sh,i,"pick general")
			b.append(c)
		else:
			c = card(sh,i,None)
			b.append(c)
cmp=[]
you =[]
def start(n):
	random.shuffle(n)
	global cmp
	global you
	cmp = n[0:4]
	for i in range(4):
		n.remove(n[i])
	you = n[0:4]
	for i in range(4):
		n.remove(n[i])
	return n
b = start(b)
pod = []
pod.append(b[0])
b.remove(b[0])
print("Loaded completely\n")
s = 0
player = 0
loc = 0
win = True
while s != 2:
	print("(1.) Play with Computer\n(2.) Exit program")
	s = int(input("Input option no. : "))
	if s == 1:
		print("\n****STARTING PROGRAM****")
		while win:
			if len(b) == 0:
				b = start(b)
				break
			if player % 2 == 0:
				print("Down Card")
				ob = pod[len(pod)-1]
				print(ob.n, ob.fig)
				print("***Computer's turn***")
				for i in cmp:
					if i.n == ob.n:
						pod.append(i)
						cmp.remove(i)
						print("Computer played")
						print(i.n, i.fig)
						if len(cmp) == 0:
							print("\nCOMPUTER WON\n")
							win = False
						break
					elif i.fig == ob.fig:
						pod.append(i)
						cmp.remove(i)
						print("Computer played")
						print(i.n, i.fig)
						if len(cmp) == 0:
							print("\nCOMPUTER WON\n")
							win = False
						break
					else:
						cmp.append(b[0])
						b.remove(b[0])
						print("Computer went to market")
						break
				player += 1
			else:
				print("Down Card")
				ob = pod[len(pod)-1]
				print(ob.n, ob.fig)
				print("***Your turn***")
				print("Your cards")
				for i in you:
					print(i.n, i.fig,end=" ")
				op = input("\nInput A to play and B to go to market: ").upper()
				if op == "A":
					loc = int(input("\nInput the location of your card by either 1,2,3... : "))
					if you[loc-1].n == ob.n or you[loc-1].fig == ob.fig:
						print("You played")
						print(you[loc-1].n,you[loc-1].fig)
						pod.append(you[loc-1])
						you.remove(you[loc-1])
						if len(you) == 0:
							print("\nYOU WIN\n")
							win=False
							break
					else:
						print("Doesn't Match")
						print("You just went to market")
						you.append(b[0])
						b.remove(b[0])
				else:
					print("You just went to market")
					you.append(b[0])
					b.remove(b[0])
				player += 1
		if win == True:
			print("\nCOUNTING CARDS\n")
			b = start(b)
			for i,v in zip(cmp,you):
				print(i.n,v.n)
				print(i.fig,v.fig)
			

	else:
		print("\nExiting Program")
		break