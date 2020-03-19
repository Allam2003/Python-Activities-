#Allam Python Graphics Assignment


import pygame   
pygame.init()
#colours
RED = (135, 50, 0)
REDO = (135, 100, 0)
ROOF= (135,100,0)
BROWN = (165,42,45)
DOOR = (100,70,45)
BLUE=  (100,50,205)
STREAK=  (100,120,205)
KNOB = (135,100,255)
MOON = (200, 70, 105)
STAR = (255,255,153)
#size
SIZE = (1000, 700)  

screen = pygame.display.set_mode(SIZE)

#GROUND
pygame.draw.rect(screen, RED,(0, 400, 1200, 300))

#HOUSE
pygame.draw.rect(screen, BROWN,(233, 233, 233, 200))

#SECOND FLOOR WINDOW
pygame.draw.rect(screen, BLUE,(243, 243, 46, 46))


#GARAGE
pygame.draw.rect(screen, REDO,(313, 300, 146, 133))
pygame.draw.rect(screen, BLUE,(323, 310, 46, 46))

pygame.draw.rect(screen, BLUE,(313, 243, 146, 46))
pygame.draw.line(screen, STREAK, (323,310), (343,330)) 
pygame.draw.line(screen, STREAK, (323,315), (343,335)) 

#BEDROOM WINDOW
pygame.draw.rect(screen, BLUE,(300, 243, 146, 46))
pygame.draw.line(screen, STREAK, (323,310), (343,330)) 
pygame.draw.line(screen, STREAK, (323,315), (343,335)) 




pygame.display.flip() 
#MOON
pygame.draw.circle(screen, MOON, (600,150), 100) 
#STARS
pygame.draw.circle(screen, STAR, (200,100), 10) 
pygame.draw.circle(screen, STAR, (400,119), 10) 
pygame.draw.circle(screen, STAR, (600,149), 10) 
pygame.draw.circle(screen, STAR, (700,139), 10) 
pygame.draw.circle(screen, STAR, (900,159), 10) 
pygame.draw.circle(screen, STAR, (100,189), 10) 
pygame.draw.circle(screen, STAR, (200,199), 10) 
pygame.draw.circle(screen, STAR, (300,209), 10) 
pygame.draw.circle(screen, STAR, (400,309), 10) 
pygame.draw.circle(screen, STAR, (500,259), 10) 
pygame.draw.circle(screen, STAR, (600,309), 10) 
pygame.draw.circle(screen, STAR, (700,189), 10) 
pygame.draw.circle(screen, STAR, (800,199), 10) 
pygame.draw.circle(screen, STAR, (900,209), 10) 
pygame.draw.circle(screen, STAR, (1000,219), 10) 
pygame.draw.circle(screen, STAR, (110,229), 10) 
pygame.draw.circle(screen, STAR, (120,239), 10) 

pygame.draw.circle(screen, STAR, (110,200), 10) 
pygame.draw.circle(screen, STAR, (400,110), 10) 
pygame.draw.circle(screen, STAR, (600,140), 10) 
pygame.draw.circle(screen, STAR, (700,130), 10) 
pygame.draw.circle(screen, STAR, (900,150), 10) 
pygame.draw.circle(screen, STAR, (100,180), 10) 
pygame.draw.circle(screen, STAR, (200,190), 10) 
pygame.draw.circle(screen, STAR, (300,200), 10) 
pygame.draw.circle(screen, STAR, (400,300), 10) 
pygame.draw.circle(screen, STAR, (500,320), 10) 
pygame.draw.circle(screen, STAR, (600,360), 10) 
pygame.draw.circle(screen, STAR, (700,180), 10) 
pygame.draw.circle(screen, STAR, (800,190), 10) 
pygame.draw.circle(screen, STAR, (900,200), 10) 
pygame.draw.circle(screen, STAR, (1000,210), 10) 
pygame.draw.circle(screen, STAR, (110,220), 10) 
pygame.draw.circle(screen, STAR, (120,230), 10) 

pygame.draw.circle(screen, STAR, (200,110), 10) 
pygame.draw.circle(screen, STAR, (110,340), 10) 
pygame.draw.circle(screen, STAR, (140,240), 10) 
pygame.draw.circle(screen, STAR, (130,340), 10) 
pygame.draw.circle(screen, STAR, (150,130), 10) 
pygame.draw.circle(screen, STAR, (180,100), 10) 
pygame.draw.circle(screen, STAR, (190,200), 10) 
pygame.draw.circle(screen, STAR, (200,300), 10) 
pygame.draw.circle(screen, STAR, (300,20), 10) 
pygame.draw.circle(screen, STAR, (400,50), 10) 
pygame.draw.circle(screen, STAR, (600,50), 10) 
pygame.draw.circle(screen, STAR, (180,70), 10) 
pygame.draw.circle(screen, STAR, (190,80), 10) 
pygame.draw.circle(screen, STAR, (200,90), 10) 
pygame.draw.circle(screen, STAR, (210,100), 10) 
pygame.draw.circle(screen, STAR, (220,110), 10) 
pygame.draw.circle(screen, STAR, (320,130), 10) 



pygame.display.flip() 


pointlist_3 = [(233, 233), (466, 233), (346, 156)]
pygame.draw.polygon(screen, RED, pointlist_3, 0)

pygame.draw.rect(screen, DOOR,(243, 313, 60, 120))
pygame.draw.rect(screen, RED,(250, 350, 10, 20))

pygame.draw.line(screen, STREAK, (243,243), (263,263)) 

pygame.draw.line(screen, STREAK, (243,248), (263,268)) 


pygame.draw.line(screen, STREAK, (313,243), (333,262)) 
pygame.draw.line(screen, STREAK, (313,248), (333,267)) 




pygame.display.flip() 
pygame.time.wait(1000)  
pygame.quit() 