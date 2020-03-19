#Allam Atif
#Data Assignment
#Mr.Cutler
#2019/12/16


# Reading from a file
numFile = open("icedTeadata.dat", "r")
 
#defining the emtpy lists
nameList=[]
caList=[]
fatList=[]
carbList=[]
fiberList=[]
proteinList=[]
sodiumList=[]
title1 = "Name"
title2 = "Calories"
title3 = "Fat"
title4 = "Carbs"
title5 = "Fiber"
title6 = "Protien"
title7 = "Sodium"

#adding meaning to the lists


while True :
     text = numFile.readline()
     
     if text=="": 
          break    
     #rstrip removes the newline character read at the end of the line
     text = text.rstrip("\n")
     
     #spliting up the list 
     currentList= text.split(",")
     

 #look at the values when using for loop
     nameList.append(currentList[0])
     caList.append(currentList[1])
     fatList.append(currentList[2])
     carbList.append(currentList[3])
     fiberList.append(currentList[4])
     proteinList.append(currentList[5])
     sodiumList.append(currentList[6])

def printAll():#useful when you want to print everything formatted
     print("%20s\t%5s\t%5s\t%5s\t%5s\t%5s\t%5s" % (title1,title2,title3,title4,title5,title6,title7)) 
     for x in range(len(nameList)):
               print("%20s\t%5s\t%5s\t%5s\t%5s\t%5s\t%5s" % (nameList[x],caList[x],fatList[x],carbList[x],fiberList[x], proteinList[x],sodiumList[x]) )       
def printLine(lineNum):#useful when changing records
     print("Name\t\t\tCalories  Fat  Carbs  Fiber  Protein")
     print(nameList[lineNum],caList[lineNum],fatList[lineNum],carbList[lineNum],fiberList[lineNum], proteinList[lineNum],sodiumList[lineNum])   
def printLine1(lineNum1):#useful when changing records
     print("Name\t\t\tCalories  Fat  Carbs  Fiber  Protein\n")
     print(nameList[lineNum1],caList[lineNum1],fatList[lineNum1],carbList[lineNum1],fiberList[lineNum1], proteinList[lineNum1],sodiumList[lineNum1])
printAll()
#changing fields
def changeField():
     lineNum=int(input("Which line would you like to change? (press -1 for no, the first line is line 0):"))
     
     if lineNum==-1 :
          running=False
     else:
          printLine(lineNum)
          element=input("What would you like to change, calories,fat,carbs,fiber,protein,sodium?(n for no):")
          if element =="n":
               running=False   
          elif element == "calories":
               i=input("What is the new value?:")
               caList[lineNum]=i
               printLine(lineNum)
               print("The new menu is:")
               printAll()   
          elif element== "fat":
               i=input("What is the new value?:")
               fatList[lineNum]=i
               printLine(lineNum)
               print("The new menu is:")
               printAll()         
          elif element== "carbs":
               i=input("What is the new value?:")
               carbList[lineNum]=i
               printLine(lineNum)
               print("The new menu is:")
               printAll()       
          elif element== "fiber":
               i=input("What is the new value?:")
               fiberList[lineNum]=i
               printLine(lineNum)
               print("The new menu is:")
               printAll()         
          elif element== "protein":
               i=input("What is the new value?:")
               proteinList[lineNum]=i 
               printLine(lineNum)
               print("The new menu is:")
               printAll()        
          elif element== "sodium":
               i=input("What is the new value?:")
               sodiumList[lineNum]=i
               printLine(lineNum)
               print("The new menu is:")
               printAll()
#making a new record
def addRecord():
     ans=input("Would you like to add a new record? (y/n)")
     if ans=="n":
          running1=False
     else:
          nName = input("What is the name of the record")
          nameList.append(nName)
          nCal = int(input("enter calorie value"))
          caList.append(nCal)
          nFat = int(input("enter fat value"))
          fatList.append(nFat)
          nCarbs = int(input("enter carbs value"))
          carbList.append(nCarbs)
          nFiber = int(input("enter fiber  value"))
          fiberList.append(nFiber)
          nProtein = int(input("enter protein value"))
          proteinList.append(nProtein)
          nSodium= input("What is the sodim value?")
          sodiumList.append(nSodium)
          print("the new menu is")
     
               
               
#removing records
def removeRecord():
     remove = input("Would like you like to remove any records from the list? (n for no)")
     if remove[0] == "n":
          running2=False #double == vs =
     else:
          lineNum1=int(input("What line would you like to remove?(line starts at 0)"))
          printLine1(lineNum1)
          print("The record will be deleted...")
          del(nameList[lineNum1],caList[lineNum1],fatList[lineNum1],carbList[lineNum1],fiberList[lineNum1], proteinList[lineNum1],sodiumList[lineNum1])
          
def quitPygame():#quits pygame
     pygame.display.flip() 
     pygame.time.wait(300)  
     pygame.font.quit()
     pygame.quit() 

#initializations and imports
import pygame,sys,time
pygame.init()
pygame.font.init()
     
SIZE = (1000,700)
screen = pygame.display.set_mode(SIZE)

#colours
GREEN = (0,255,0)
BLACK = (0,0,0)

font = pygame.font.SysFont("Times New Roman",30)

string1= "Remove record."
string2= "New record."
string3= "Change field."
string4= 'Display file.'
text1 = font.render(string1, 100, BLACK)
text2= font.render(string2,  100, BLACK)
text3 = font.render(string3, 100, BLACK)
text4 = font.render(string4, 100, BLACK)

#Graphical Navigation Menu, Press a button to fullfil any need!
running=True

while running:
     #making the boxes
     for i in range(0,1000,255):
          pygame.draw.rect(screen, GREEN, (i,235,245,235))
     
     #text generation
     screen.blit(text1, pygame.Rect(0, 235, 145, 105))
     screen.blit(text2, pygame.Rect(255, 235, 145, 105))
     screen.blit(text3, pygame.Rect(510, 235, 245, 105))
     screen.blit(text4, pygame.Rect(766, 235, 245, 105))      
     
     pygame.display.flip()
     
     x1, y1 = pygame.mouse.get_pos()#gets the position
     for evnt in pygame.event.get():#gets the events
          
          if 470>=y1>=235 and evnt.type ==pygame.MOUSEBUTTONDOWN:
               if 0<=x1<=255:
                    removeRecord() 
                 
               elif 510>=x1>=255:
                    addRecord() 
                   
               elif 765>=x1>=510:
                    changeField()
                    
               elif 1000>=x1>=765:        
                    printAll()
                         
          elif evnt.type == pygame.QUIT:
               quitPygame()
               running = False
          
#writing to the file
numFile = open ("icedTeadata.dat", "w")
for x in range(len(nameList)) :
     numFile.write(str(nameList[x])+","+str(caList[x])+","+str(fatList[x])+","+str(carbList[x])+","+str(fiberList[x])+","+str(proteinList[x])+","+str(sodiumList[x])+"\n")
      
  
numFile.close()