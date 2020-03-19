import math, pygame
pygame.init()
RED= (255,0,0)
BLACK = (0, 0, 0)
SIZE = (800, 600) #need to writer size seperately 
screen = pygame.display.set_mode(SIZE)
y=0
for fhgjfhjgf in range(801): #only chagning thie x value not y 
    pygame.draw.rect(screen, BLACK, (0, 0, 800, 600)) #erases the screen 
    pygame.draw.circle(screen, RED, (fhgjfhjgf, y), 50) #draws a new circle
    pygame.display.flip()  #changes (updates)screen
    pygame.time.wait(5)  #wait needed
    fhgjfhjgf+=1  #dony need this becasue rsnge adds 1 any ways
    y+=1#for y 
    # need to have exact same form
    # ask if can use two values
    
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()

