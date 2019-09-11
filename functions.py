total = 4
#Required arguments
def req(n):
	total = n ** 2
	print(total)
#Keyword arguments
def key(str,num):
	total = str * num
	print(total)
#Default arguments
def dlt(name,age="i"):
	print(name, age)
#Variable-length arguments
def var(arg, *var_tuple):
	print(arg)
	for i in var_tuple:
		print(i)
#Anonymous arguments
sum = lambda n:n**2
req(4)
key(num = 3,str = "Ayo")
dlt("me",45)
var(3,4,5,6,7,8)
print(sum(6))