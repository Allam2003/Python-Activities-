
import pygame   
pygame.init()

RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
SIZE = (800, 800)
screen = pygame.display.set_mode(SIZE)
pygame.draw.rect(screen, WHITE, (0,0,200,200))
pygame.draw.rect(screen, WHITE, (0,700,200,200))
pygame.draw.rect(screen, WHITE, (600,700,200,200))
pygame.draw.rect(screen, WHITE, (600,0,200,200))
pygame.draw.rect(screen, RED, (200,200,400,400))
pygame.draw.circle(screen, BLUE, (400,400), 200)
pygame.draw.line(screen, GREEN, (750,750), (100,100), 10)
pygame.draw.line(screen, GREEN, (50,750) , (700,100), 10)




                 
pygame.display.flip()
pygame.time.wait(7000)
pygame.quit()
