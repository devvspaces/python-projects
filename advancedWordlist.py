from itertools import product
from time import process_time
from random import choice,randint
def decor(word):
	def wrap():
		hello(word)
		print("="*50)
	wrap()
def hello(word):
	print(word)

decor(50*"*"+"\nWelcome to my fast and efficient wordlist.py")
decor("What type of word list do you want to create\na. Numerical data\nb. Alphabetical data\nc. Alphanumerical data\nd. Exit")
option =""
alpha=list("abcdefghijklmnopqrstuvwxyz")
num=[0,1,2,3,4,5,6,7,8,9]

def collectInput(word,use="abcd"):
	global option
	option=input(word).strip()
	if use[0].isnumeric():
		use=[]
		use=[str(i) for i in range(1,16)]
	try:
		option=option.lower()
		assert option in list(use)
	except:
		decor("Invalid input")
		collectInput(word,use)
	return option

collectInput("Enter either (a,b,c or d) : ")

def creator(type_):
	n=randint(4,15)
	global option
	x="".join([str(choice(type_)) for i in range(n)])
	y="".join([str(choice(type_)) for i in range(n)])
	decor("Information:\nIf you input the limit, that will be the amout of number each you will get e.g if you inputed {} \n{}\n{}\netc for all possible combinations".format(n,x,y))
	collectInput("Enter limit : ",use="1")
	option=int(option)
	temp_storage=""
	start=process_time()
	for i in product(type_,repeat=option):
		i=[str(x) for x in i]
		i="".join(i)+"\n"
		temp_storage+=i
	end=process_time()
	decor("Wordlist created within {} s".format(round(end-start,3)))
	decor("Text file created, decide name of file")
	name=input("Enter file name only : ")
	with open(name+".txt", "w") as f:
		f.write(temp_storage)
		del temp_storage
	decor("File stored at program directory as "+name+".txt")


if option=="a":
	creator(num)
elif option=="b":
	creator(alpha)
elif option=="c":
	creator(alpha+num)
else:
	pass