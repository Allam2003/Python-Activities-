#if the circles are colliding, touching or doing neither
 
import math #for square root 
 
cord1       = input ("Enter the coordinates. ")
cord_circle = input ("Please the coordinates and the radius of your circle (x,y) ")
#in the form of string
 
# changing strings into variables, characters are individual numbers
cut    = (cord1.find(','))
cut2   = (cord_circle.find(','))
end1   = (cord1.find(')'))
end2   = (cord_circle.find(')'))
start1 = (cord1.find('('))
start2 = (cord_circle.find('('))
 
cord1x  = float(cord1[start1+1:cut1])
cord1y  = float(cord1[cut+1:end1])
radius1 = float(cord1[end1+1:])
cord2x  = float(cord_circle [start2+1:cut2])
cord2y  = float(cord_circle[cut2+1:end2])
radius2 = float(cord_circle[end2+1:])
 
#distance in between the centers of the two circles
distx = cord2x-cord1x  
disty = cord2y-cord1y
totalDistance = round(math.sqrt(abs(distx**2 + disty**2)))
 
#finding the sum of radii to compare with the distances
totalRadius   = radius1 + radius2
 
if totalDistance < totalRadius:
    print ("Circles colliding.")
elif totalDistance == totalRadius:
    print ("Circles touching.")
else:
    print ("Circles not colliding.") 
