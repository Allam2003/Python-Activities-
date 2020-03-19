RED=(255,0,0)
for level in range(5):
    obsx=[]
    obsy=[]
    for x in range(level*100):
        x1=random.randint(0, 1000)
        y=random.randint(0, 700)
        obx.append(x1)
        oby.append(y)
        pygame.draw.rect(screen, RED, (x1,y,10,10))
        
    