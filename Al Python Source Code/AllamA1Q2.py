import pygame   
pygame.init()
RED = (255, 0, 0)
BLACK = (0,0,0)
SIZE = (1000, 1000)
screen = pygame.display.set_mode(SIZE)
import math 
pygame.draw.ellipse(screen, (0, 0, 155), (100,100, 200, 500))
pygame.draw.arc(screen,(0, 255, 0), (0, 0, 300, 300), 0, math.pi)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
