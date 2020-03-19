
import pygame   
pygame.init()

RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
Y=X
SIZE = (X,Y)
screen = pygame.display.set_mode(SIZE)


pygame.draw.rect(screen, WHITE, (0,0,X/4,X/4))
pygame.draw.rect(screen, WHITE, (0,700,X/4,X/4))
pygame.draw.rect(screen, WHITE, (600,700,X/4,X/4))
pygame.draw.rect(screen, WHITE, (600,0,X/4,X/4))
pygame.draw.rect(screen, RED, (200,200,X/2,X/2))
pygame.draw.circle(screen, BLUE, (X/2,X/2), X/3)
pygame.draw.line(screen, GREEN, (X-50,X-50), (X-700,X-700), 10)
pygame.draw.line(screen, GREEN, (X-750,X-50) , (X-100,X-700), 10)




                 
pygame.display.flip()
pygame.time.wait(7000)
pygame.quit()
