import random 
suits=["hearts","clubs","spades","diamonds"]
number=['1','2','3','4','5','6','7','8','9','10']
other=['king','queen','jack','joker']
x=random.choice(['0','1'])
def b():
    for i in range(0,5):
        s=random.choice(suits)
        y=random.choice(number)
        print(s,y)
if x=='0':
    for i in range(0,10):
        s=random.choice(suits)
        y=random.choice(number)
        print(s,y)
elif x=='1':
    for i in range(0,5):
        print(random.choice(other))
        b()
