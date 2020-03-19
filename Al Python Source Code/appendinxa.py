import pygame
pygame.init()
SIZE = (width,height) = (800,600)
screen = pygame.display.set_mode(SIZE)
 
GREEN = (0,255,0)
BLACK = (0,0,0)
 
# clear the screen, draw off screen and then display
def drawScene(screen):
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, (400,200), 100)
    pygame.display.flip()
 
running = True
myClock = pygame.time.Clock()
 
while running:   # this is our game loop
 
    # Check all the events that happen
    for evnt in pygame.event.get():
       
        # if the user tries to close the window, then raise the "flag"
        if evnt.type == pygame.QUIT:
            running = False
	
rawScene(screen)
	
    # waits long enough to have 60 fps
    myClock.tick(60)
 
pygame.quit()

if 3<4p:
running 
