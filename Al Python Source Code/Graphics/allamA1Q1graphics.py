import pygame   
pygame.init()
RED = (255, 0, 0)
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)

x = int(input("Please enter the x-coordninate."))
y = int(input("Please enter the y-coordninate."))
pygame.draw.circle(screen, RED, ((x), (y)), 100)


pygame.time.wait(3000)
pygame.quit()
