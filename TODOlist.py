import time
boo=True
while boo:
    print("1. View Todo List\n2.Add Todo list\n3. Format TODO List\nENTER NEITHER TO EXIT")
    y = eval(input("Enter option: "))
    if y==1:
        with open("todoLists.csv","r+") as f:
            print("{0}Your Todo list{0}".format(" "*30))
            b, x= f.read(), ''
            print(b) if len(b)!= 0 else print("{0}Empty List{0}".format(" "*30))
    elif y == 2:
        with open("todoLists.csv","r+") as g:
            print("Starting new input")
            while len(x)==0:
                x = input("Your next list: ")
                g.seek(0,2)
                g.write("{3}{2}{0}{1}{2}".format("->> ",x,"\n",time.asctime(time.localtime())))
    elif y==3:
        with open("todoLists.csv","w") as j:
            j.write("")
    else:
        boo=False
