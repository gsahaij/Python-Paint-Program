import pygame
from tkinter import *

root = Tk()
root.withdraw() # hides the extra window


# Colors

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255 ,255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)

PI = 3.141592653

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Re_run")

canvasRect = pygame.Rect(150,125,500,500)
loadRect = pygame.Rect(40,50,50,50)
saveRect = pygame.Rect(100,50,50,50)

pygame.draw.rect(screen,WHITE,canvasRect)
pygame.draw.rect(screen,GREEN,loadRect)
pygame.draw.rect(screen,BLUE,saveRect)

pygame.draw.line(screen,RED,(200,200),(300,300))
pygame.draw.rect(screen,BLACK,(200,200,100,100),1)



#Loop until the close button is clicked
done = False

#Used to manage the framerate
clock = pygame.time.Clock()

#_______Main program loop__________

while not done:
    #_____Main event loop_______

    for event in pygame.event.get(): #The user did something
        if event.type == pygame.QUIT:#If the user attempts to close the window
            done = True #Telling us to exit the loop and therefore the window
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key. ")
        elif event.type == pygame.KEYUP:
            print("User let go fo a key ")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button ")

    #_______Game logic goes here________
            
    mb = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()


    if saveRect.collidepoint(mx,my):
        try:
            fname = filedialog.asksaveasfilename(defaultextension=".png")
            pygame.image.save(screen,fname)
        except:
            print("saving error")
        # make sure the program does not save something w/o a file name
    if loadRect.collidepoint(mx,my):
        try:
            fname = filedialog.askopenfilename()
            print(fname)
            # need to open the image itself
        except:
            print("lmao")

    
    
    #screen.fill(WHITE) #Clears the screen to white. DO NOT put drawing code above this
    

    #_______Drawing code goes here______

    pygame.display.flip() #Updates the screen with what was drawn


    clock.tick(60)# This sets framerate to 60
    

pygame.quit()
    
