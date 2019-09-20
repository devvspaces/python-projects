import os
from FileLooperModule import fileObject
os.chdir("/storage/emulated/0")

objects=[]
dirs=[]
files=[]
parent_cwd=os.getcwd()
changing_cwd=parent_cwd

#Function to load directories
def checkDir(x,p=''):
	global objects
	for i in os.listdir():
		i = fileObject(i)
		objects.append(i)
	for i in objects:
		if i.isDir():
			dirs.append(p+i.name)
		else:
			files.append(i.name)
	objects=[]

checkDir(changing_cwd)
use=''
if len(dirs) == 0:
	pass
else:
	for i in dirs:
		changing_cwd=parent_cwd
		changing_cwd=changing_cwd+'/'+i
		os.chdir(changing_cwd)
		checkDir(changing_cwd,p=i+"/")

#Sorting out each file extension
print(15*"="+"Music")
print([i for i in files if i.endswith(".mp3")])
print(15*"*"+"Images")
print([i for i in files if i.endswith(".jpeg") or i.endswith(".png")])
print(15*"+"+"Texts")
print([i for i in files if i.endswith(".txt") or i.endswith(".mhtml") or i.endswith(".pdf") or i.endswith(".html") or i.endswith(".py")])