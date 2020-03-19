x=int(input("Please enter a #: "))
y=int(input("Please enter another #: "))

if x>y:
    for z in range(x,y,-1):
     print(z)
if x<y:
    for z in range(y,x,-1):
     print(z)
     #indent after every line in body?