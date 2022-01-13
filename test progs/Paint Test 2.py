import pygame
import tkinter
from random import *
import math
import os


# Colors



BLACK = ( 0, 0, 0)
WHITE = ( 255, 255 ,255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)

cols = [RED,GREEN,BLUE,WHITE]

pygame.font.init()
font = pygame.font.SysFont("Calibri",23)


words = ["w","a","c","k"]

PI = 3.141592653

pygame.init()
width = 1280
height = 720
size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lego Paint")
screen.fill(BLACK)

#Globals
done = False
onCanvas = True
tool = ""
canvas = pygame.Rect(295,5,width-300,600)
pencilBox = pygame.Rect(20,20,20,20)
colourWheel = pygame.image.load('images/colour-wheel.png')
wheelRect = pygame.Rect(30,510,100,100)
print(wheelRect)
pygame.draw.rect(screen,WHITE,canvas)
screen.blit(colourWheel, [30,510])


# Functions





def pencil(omx,omy,x,y):
    pygame.draw.line(screen, BLACK,(omx,omy),(x,y))
    

def brush():
    print("brush")
    

def sprayPaint(x,y):
    print("spraypaint")

   
   
        
def eraser():
    pygame.draw.circle(screen, WHITE,(x,y),10)
    



#Used to manage the framerate
clock = pygame.time.Clock()

#_______Main program loop__________

while not done:
    #_____Main event loop_______

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        

    #_______ logic goes here________
    
    mx,my = pygame.mouse.get_pos()
    mouseDown = pygame.mouse.get_pressed()

    print(tool)
    

    #_______Drawing code goes here______
    
    
    pygame.draw.rect(screen, GREEN, pencilBox)

    if mouseDown[0]:
        if pencilBox.collidepoint(mx,my):
            tool = "pencil"
        word = choice(words)
        ranCol = choice(cols)
        word = font.render(word,True,ranCol)
        w = word.get_width()
        h = word.get_height()
        screen.blit(word,[mx-w//2,my])
        
    if mouseDown[0]:
        if onCanvas:
            #screen.set_clip(canvasRect) # only the canvas rect can be updated
            if tool == "pencil":
                pygame.draw.line(screen, RED,(omx,omy),(mx,my),50)
            if tool == "sprayPaint":
                sprayPaint(mx,my)
    
    if mouseDown[0]:
        if wheelRect.collidepoint(mx,my):
            col = screen.get_at((mx,my))
            print(col)
                
    

    pygame.display.flip() #Updates the screen with what was drawn
    clock.tick(60)
    omx = mx
    omy = my
    
    

pygame.quit()
    
