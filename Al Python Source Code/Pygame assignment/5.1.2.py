myList=[]
myList2=[]

for i in range(5):
    x=input("please input a name:")
    y=input("please input a last name:")
    myList.append(x)
    myList2.append(y)
newList= myList + myList2    
newList.sort()
print("here are thier names in alphabietical order %s" %newList)
#can not merge in between int and str