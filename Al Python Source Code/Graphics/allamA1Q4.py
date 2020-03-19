
# x1,y1 is the center of the first circle and x2,y2 is the center of the second circle if  the distance in between the two coordinates is larger than the value of thier radius then the circles do not collide

x= x2-x1
y= y2-y1
if x>=10 and y>=10:
    print("The circle does not collide.")
else:
    print("The circle does collide.")



import math  
def calculateDistance(x1,y1,x2,y2):  
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist  
print ("(calculateDistance(x1, y1, x2, y2)")  