x=int(input("please enter a number "))
original = x
y= 2
counter = 0
divisible = True
while divisible:
    if x%y==0:
        x=x/y
        counter+=1 
    else: 
        print("",original, "is divisible",counter,"times.")
        divisible = False
#make output exactly as shown
    

    
     