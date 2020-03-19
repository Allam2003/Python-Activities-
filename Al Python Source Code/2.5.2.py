import math

c1 = (int(input("please enter the first coordinate: ")))
c2 = (int(input("please enter the second coordinate: ")))
x1 = (int(input("please enter another first coordinate: ")))
x2 = (int(input("please enter  another coordinate: ")))

distance = math.sqrt((c2 - c1)*(c2 - c1)+ (x2 - x1)*(x2 - x1))
print("The distance in between the two points is",distance,)
# import math has to in the top
#there is no space after math.sqrt
