import pygame
import random
pygame.init()
x=random.randint(0,100)
SIZE = (100,100)
screen = pygame.display.set_mode(SIZE)   
counter=0
y=0
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)    
for x in range(81):
    c=random.choice([RED,GREEN,BLUE])
    pygame.draw.rect(x, c, (x,y), 20)
    if counter%5==0:
        y+=20
    
    

pygame.display.flip()   
pygame.time.wait(10000)
pygame.quit()    






#math can cn beused instead of if staatemnet # for h) use rand.int(0,1)#try a nested loop
#REnFERIGN TO VARIABLE NEED BRACKERS SINCE FUNC,can not hav e this before the defineing , under for loop to change everythimer, if statemet optimal optimal if commdand completely differnet
#for y in five times and then 20 more
#non=inlcusive