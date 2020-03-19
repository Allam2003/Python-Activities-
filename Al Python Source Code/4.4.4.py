import random
one=0
two=0
three=0
four=0
five=0
six=0
running=True

for die in range(1000):
    x=random.randint(0, 6)
    while running: 
        b=int(input("enter a number in between 1 and 6)"))
        if b>6: print("incorrect input")
        elif b<1:
            print("incorrect input")
        else:
            running=False
    if b==x ==1:
        one+=1
    elif b==x==2:
        two+=2
    elif b==x==3:
        three+=3
    elif b==x==4:
        four+=4
    elif b==x==5:
        five+=5
    else:
        six+=6
        #
total=one+two+three+four+five+six
    
print("your points are",total)