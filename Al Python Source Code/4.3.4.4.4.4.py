num1=input("please input a number:")
sum1=1
for char in num1:
    if int(char)%2==1: #unnessary brackets
        sum1*=int(num1) #make consise
    print(int(char))
print(sum1)
#what is the value of char in a string it is "6"