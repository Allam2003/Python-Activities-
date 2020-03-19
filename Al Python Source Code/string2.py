name =input("please enter your full name with a space in between")
c = name.find(" ")
b = name[0:c] 
d = name[c:]

print("%s, %s"%(d,b))