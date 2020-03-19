#so the point is the first dice roll
#use while loop and counter to see how long it takes to get the same dice

import random

point = random.randint(1,6)
count = 0
running  = True
while running:
    currentRoll = random.randint(1,6)
    count += 1
    if point==currentRoll:    
        running = False


print(count)
