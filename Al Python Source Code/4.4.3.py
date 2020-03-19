import random 
heads=0
tails=0
same=0
for i in range(10000):
    n=random.randint(0,1)
    if n==1:
        heads+=1
    elif n==2:
        tails+=1
        if heads==tails:
            same+=1
print("the amount of tails was",heads,"the amount of heads was",tails, "the amount of times the ocurence of either heads or tail was equla was",same)

