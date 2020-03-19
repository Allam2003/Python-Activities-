
x = int(input("Please enter the x-coordninate."))
y = int(input("Please enter the y-coordninate."))

if 200<=x<=300 : # to signify a range, you need to put the small number first and then the large and follow the for
            if 100<=y<=300: 
                        print("The coordinates are inside the circle.")
            
else:
            print("The coordinates are outside of circle.")

#center
x1= 200
y1= 200
#point
x2=int(input("Please enter x value."))
x2=int(input("Please enter y value."))

#distance betweeen the center and th epoint determining if it is in the circle
distancex= x2 - x1
distancey= y2 - y1

if distancex ==100:
            if distancey ==100:
                        print("It is on the circle.")