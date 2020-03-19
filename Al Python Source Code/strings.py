x = input("please enter your first name")
y = input('please enter your last name')
z = x[0] # take the first character from the string
z = z.upper() # upper case it
f = y[0]
e = f.upper()
y= y.replace(f,e) #replece the first character in the string to upper case  
print(z + ". " + y)
