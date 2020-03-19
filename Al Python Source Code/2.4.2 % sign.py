int1 = (int(input("Please enter an integer: ")))
int2 = (int(input("Please enter an integer: ")))
int3 = (int(input("please enter an integer: ")))
average = ( int1 + int2 + int3 ) /3 
averag2 = 5.0
print("The average is %.2f."  % average)
print ("%f is your avaerage %f" %(average,averag2))
#ten space %10.f 
# %.3f 3 decimsl max
# first in first out, these are like variable names, 
#%-10.2f left align
#
#Field spacing – The field spacing is the total number of spaces used to display your value, including the ones used by your value. e.g
#a = 12.3456				
#	n = 300
#	s = “Ching”
#	%10f		---12.3456	- note the decimal takes up one space
#	%10s		-----Ching	
#	%10i		-------300
#	%10.2f		-----12.35	- note that it will round off
#	%-10.2f	12.35-----	- "-" will left align
#	%2i		300			- making the field smaller than the
#						  number of characters will not chop off
#						  characters