import pygame
import tkinter
import random
import math
import os



# Colors

root = tkinter.Tk()
root.withdraw()

pygame.font.init()


BLACK = ( 0, 0, 0)
WHITE = ( 255, 255 ,255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255,255,0)

PI = 3.141592653



pygame.init()
width = 1280
height = 720
size = (width,height)
pygame.display.set_icon(pygame.image.load("images/Spongebob_Icon.jpg"))
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SpongeBob Paint")



#_____Globals______
#Global Variables
done = False
clock = pygame.time.Clock()
tool = ""
onCanvas = False
thickness = 10
col = BLACK
eraserCol = WHITE
start = True
helpScreen = False
normalScreen = False
fullScreen = False
oneTime = True
startX = 0
startY = 0
omx = 0
omy = 0
undoList = []
redoList = []
undo = False
redo = False
selectList = []
startPoints = []
rightClick = False
leftClick = False
polygonFinished = False
screenShot = None
loadImage = None
fill = False
toolSelected = False
userText = ""
canType = False
keyList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space','caps lock','return','backspace','.','/',',','tab',1,2,3,4,5,6,7,8,9]
textboxPos = 0
stampList = []
normalStampList = []
fullStampList = []
stampRects = []


mediumFont = pygame.font.SysFont('Arial',21,True,False)
smallFont = pygame.font.SysFont('Arial',14,True,False)
bigFont = pygame.font.SysFont('Calibri',36,True,False)
toolText = mediumFont.render("",True,BLACK)


# Initial text info
colourText = mediumFont.render("Current Colour", True, col)
screen.blit(colourText, [30,510])



#Global Images
background = pygame.image.load("images/background_.jpg")
background2 = pygame.transform.rotate(background,180)
screen.blit(background,[0,0])
screen.blit(background2,[0,467])
screen.blit(background2,[550,467])
screen.blit(background2,[800,467])
colourSelect = pygame.image.load("images/colours.png")
fullButton = pygame.image.load("images/fullScreen.png")
pencilButton = pygame.image.load("images/pencil.png")
undoButton = pygame.image.load("images/Undo.png")
redoButton = pygame.image.load("images/Redo.png")
miniUndoButton = pygame.transform.scale(undoButton, (25,25))
miniPencilButton = pygame.transform.scale(pencilButton,(25,25))
paintBrushButton = pygame.image.load("images\paintBrush.png")
miniBrushButton = pygame.transform.scale(paintBrushButton,(25,25))
sprayPaintButton = pygame.image.load("images\sprayPaint.png")
miniSprayPaintButton = pygame.transform.scale(sprayPaintButton,(25,25))
eraserButton = pygame.image.load("images\eraser.png")
miniEraserButton = pygame.transform.scale(eraserButton, (25,25))
saveButton = pygame.image.load("images/Save.png")
loadButton = pygame.image.load("images/load.png")
textButton = pygame.image.load("images/text.png")
miniTextButton = pygame.transform.scale(textButton,(25,25))
bucketButton = pygame.image.load("images/bucket.png")
miniBucketButton = pygame.transform.scale(bucketButton,(25,25))
polygonButton = pygame.image.load("images/polygon.png")
miniPolygonButton = pygame.transform.scale(polygonButton,(25,25))
startBackground = pygame.image.load("images/startBackground.jpg")
title = pygame.image.load("images/SpongebobTitle.png")
paintTitle = pygame.image.load("images/paintTitle.png")
button = pygame.image.load("images/button.png")
back = pygame.image.load("images/back.png")
infoPic = pygame.image.load("images/info.png")

# Stamps
krabs = pygame.image.load("images/stamps/krabs.png")
patrick = pygame.image.load("images/stamps/patrick.png")
spongebob = pygame.image.load("images/stamps/spongebob.png")
spongebob2 = pygame.image.load("images/stamps/spongebob2.png")
squidward = pygame.image.load("images/stamps/squidward.png")
fish = pygame.image.load("images/stamps/fish.png")

stampList = [krabs,patrick,spongebob,spongebob2,squidward,fish]

for i in stampList:
    i = pygame.transform.scale(i,(75,75))
    normalStampList.append(i)
    i = pygame.transform.scale(i,(45,45))
    fullStampList.append(i)

stamp1 = pygame.Rect(280,620,80,80)
stamp2 = pygame.Rect(380,620,80,80)
stamp3 = pygame.Rect(480,620,80,80)
stamp4 = pygame.Rect(580,620,80,80)
stamp5 = pygame.Rect(680,620,80,80)
stamp6 = pygame.Rect(780,620,80,80)



    

#Global Objects
canvas = pygame.Rect(300,0,width-300,600)
subCanvas = screen.subsurface(canvas)

normalRect = pygame.Rect(1050,220,200,99)
normalTextA = mediumFont.render("Normal Screen",True,BLUE)
normalTextB = mediumFont.render("(Better for beginners)",True,BLUE)

fullRect = pygame.Rect(800,220,200,99)
fullTextA = mediumFont.render("Full Screen",True,BLUE)
fullTextB = mediumFont.render("(Better for pros)",True,BLUE)

helpRect = pygame.Rect(925,400,200,99)
helpTextA = mediumFont.render("Help",True,BLUE)
helpTextB = mediumFont.render(" &",True,BLUE)
helpTextC = mediumFont.render("Info",True,BLUE)

backRect = pygame.Rect(25,30,50,50)




pencilRect = pygame.Rect(30,30,50,50)


paintBrushRect = pygame.Rect(90,30,50,50)


eraserRect = pygame.Rect(30,90,50,50)


sprayPaintRect = pygame.Rect(90,90,50,50)


thicknessUpRect = pygame.Rect (90,410,50,50)

thicknessDownRect = pygame.Rect(30,410,50,50)

colourRect = pygame.Rect(30,540,200,150)

undoButtonRect = pygame.Rect(200,60,30,30)

redoButtonRect = pygame.Rect(230,60,30,30)

saveButtonRect = pygame.Rect(200,20,32,32)

loadButtonRect = pygame.Rect(240,20,32,32)

clearRect = pygame.Rect(150,350,50,50)

lineRect = pygame.Rect(30,150,50,50)

polygonRect = pygame.Rect(30,270,50,50)

rectangleRect = pygame.Rect(90,150,50,50)

textBoxRect = pygame.Rect(90,210,50,50)


fillRect = pygame.Rect(90,350,50,50)


noFillRect = pygame.Rect(30,350,50,50)


circleRect = pygame.Rect(30,210,50,50)




#_____Functions_______

#Tool Functions

def pencil(ox,oy,x,y,r,col):
    pygame.draw.line(screen, col, (ox,oy),(x,y),r)
    
def sprayPaint(mx,my,r,col):
    for i in range(50):
        posX = random.randint(mx-r,mx+r)
        posY = random.randint(my-r,my+r)
        posX = posX - mx
        posY = posY - my
        dist = int(math.sqrt(posX**2 + posY**2))
        if dist <= r:
            pygame.draw.circle(screen, col, [mx+posX,my+posY],0)
        
    
def paintBrush(ox,oy,x,y,r,col):
    dx = x-ox # horizontal distance
    dy = y-oy # vertical distance
    dist  = int(math.sqrt(dx**2+dy**2))
    for i in range(1,dist+1):
        dotX = int(ox+i*dx/dist)
        dotY = int(oy+i*dy/dist)
        pygame.draw.circle(screen,col,(dotX,dotY),r)
        
        
    
    
def eraser(ox,oy,x,y,r,eraserCol):
    dx = x-ox # horizontal distance
    dy = y-oy # vertical distance
    dist  = int(math.sqrt(dx**2+dy**2))
    for i in range(1,dist+1):
        dotX = int(ox+i*dx/dist)
        dotY = int(oy+i*dy/dist)
        pygame.draw.circle(screen,eraserCol,(dotX,dotY),r)
    
    
    
def drawLine(sx,sy,x,y,col,screenShot,r):
    screen.blit(screenShot,[0,0])
    pygame.draw.line(screen, col, (sx,sy),(x,y),r)
    
def drawRect(sx,sy,thickness,col,mx,my,screenShot,fill):
    screen.blit(screenShot, (0, 0))
    distX = math.sqrt((mx - sx) ** 2)
    distY = math.sqrt((my - sy) ** 2)
    if sx > mx:
        distX = -distX
        thicknessA = -thickness
        thicknessB = thickness
    else:
        thicknessA = thickness
        thicknessB = -thickness
    if sy > my:
        distY = -distY
            
    pygame.draw.line(screen, col, (sx + thicknessB//2, sy), (sx + distX + thicknessA//2, sy), thickness)
    pygame.draw.line(screen, col, (sx + thicknessB//2, sy + distY), (sx + distX + thicknessA//2, sy + distY), thickness)
    pygame.draw.line(screen, col, (sx + thicknessB//(thickness * 20), sy), (sx + thicknessB//(thickness * 20), sy + distY), thickness)
    pygame.draw.line(screen, col, (sx + thicknessA//(thickness * 20) + distX, sy), (sx + thicknessA//(thickness * 20) + distX, sy + distY), thickness)
    if fill:
        pygame.draw.rect(screen, col, [sx,sy,(mx-sx),(my-sy)],0)

def drawCircle(sx,sy,thickness,mx,my,screenShot,col,fill):
    screen.blit(screenShot,(0,0))
    distX = (mx - sx)
    distY = (my - sy)
    ellRect = pygame.Rect(sx,sy,distX, distY)
    ellRect.normalize()
    ellRect1 = pygame.Rect(sx+1,sy,distX, distY)
    ellRect1.normalize()
    ellRect2 = pygame.Rect(sx-1,sy,distX, distY)
    ellRect2.normalize()
    ellRect3 = pygame.Rect(sx,sy+1,distX, distY)
    ellRect3.normalize()
    ellRect4 = pygame.Rect(sx,sy-1,distX, distY)
    ellRect4.normalize()
    try:
        if fill:
            pygame.draw.ellipse(screen, col, ellRect,0)
        else:
            pygame.draw.ellipse(screen, col, ellRect,thickness)
            pygame.draw.ellipse(screen, col, ellRect1,thickness)
            pygame.draw.ellipse(screen, col, ellRect2,thickness)
            pygame.draw.ellipse(screen, col, ellRect3,thickness)
            pygame.draw.ellipse(screen, col, ellRect4,thickness)
    except:
        pass

def drawPolygon(sx,sy,mx,my,screenShot,startPoints,rightClick,col,thickness):
    if leftClick:
        screen.blit(screenShot,[0,0])
        pygame.draw.line(screen,col,(sx,sy),(mx,my),thickness)
        startPoints.append((sx,sy))

def finishPolygon(startPoints,col,thickness):
        pygame.draw.line(screen,col,(startPoints[0]),(mx,my),thickness)
    

def textBox(sx,sy,userText,font,canType,tool,col,onCanvas,textboxPos,thickness):
    if tool == "text box" and onCanvas:
        if canType:
            for i in range(len(userText)):
                textboxPos += 12
            mediumFont = pygame.font.SysFont('Arial',thickness,True,False)
            textRect = pygame.Rect(sx,sy,textboxPos,20)
            screenText = font.render(userText,True,col)
            screen.blit(screenText,[sx,sy])
        else:
            textboxPos = 0
            pass

def fillScreen(canvas,col):
    pygame.draw.rect(screen,col,canvas)

def drawStamps(tool,mx,my,screenShot,stampList):
    
    if tool == "stamp 0":
        screen.blit(screenShot,[0,0])
        screen.blit(stampList[0],(mx - 100,my - 100))
    if tool == "stamp 1":
        screen.blit(screenShot,[0,0])
        screen.blit(stampList[1],(mx - 100,my - 100))
    if tool == "stamp 2":
        screen.blit(screenShot,[0,0])
        screen.blit(stampList[2],(mx - 100,my - 100))
    if tool == "stamp 3":
        screen.blit(screenShot,[0,0])
        screen.blit(stampList[3],(mx - 100,my - 100))
    if tool == "stamp 4":
        screen.blit(screenShot,[0,0])
        screen.blit(stampList[4],[mx - 100,my - 100])
    if tool == "stamp 5":
        screen.blit(screenShot,[0,0])
        screen.blit(stampList[5],[mx - 100,my - 100])

    
def drawing(mb,omx,omy,mx,my,tool,onCanvas,screenShot,thickness,col,sx,sy,fill,selectRect):
    if mb[0] and onCanvas:
        if tool == "pencil":
            pencil(omx,omy,mx,my,thickness,col)
        if tool == "paint brush" and onCanvas:
            paintBrush(omx,omy,mx,my,thickness,col)
        if tool == "eraser":
            eraser(omx,omy,mx,my,thickness,eraserCol)
        if tool == "spray paint":
            sprayPaint(mx,my,thickness,col)
        if tool == "line":
            drawLine(sx,sy,mx,my,col,screenShot,thickness)
        if tool == "rectangle":
            drawRect(sx,sy,thickness,col,mx,my,screenShot,fill)
        if tool == "circle":
            drawCircle(sx,sy,thickness,mx,my,screenShot,col,fill)
        drawStamps(tool,mx,my,screenShot,stampList)
    
    
            

# Mechanical Functions
        
def selectTool(tool):
    if tool == "pencil":
        pygame.draw.rect(screen, (BLUE), pencilRect, 2)
    else:
        pygame.draw.rect(screen, BLACK, pencilRect, 2)
                    
    if tool == "paint brush":
        pygame.draw.rect(screen, (BLUE),paintBrushRect, 2)
    else:
        pygame.draw.rect(screen, BLACK, paintBrushRect, 2)

    if tool == "eraser":
        pygame.draw.rect(screen, BLUE, eraserRect,2)
    else:
        pygame.draw.rect(screen, BLACK, eraserRect,2)
        
    if tool == "spray paint":
        pygame.draw.rect(screen, BLUE, sprayPaintRect,2)
    else:
        pygame.draw.rect(screen, BLACK,sprayPaintRect,2)
        
    if tool == "line":
        pygame.draw.rect(screen, BLUE, lineRect, 2)
    else:
        pygame.draw.rect(screen, BLACK, lineRect,2)

    if tool == "rectangle":
        pygame.draw.rect(screen, BLUE, rectangleRect,2)
    else:
        pygame.draw.rect(screen, BLACK, rectangleRect,2)

    if tool == "circle":
        pygame.draw.rect(screen, BLUE, circleRect,2)
    else:
        pygame.draw.rect(screen, BLACK, circleRect,2)
    if tool == "text box":
        pygame.draw.rect(screen,BLUE,textBoxRect,2)
    else:
        pygame.draw.rect(screen,BLACK,textBoxRect,2)
        
    if tool == "polygon":
        pygame.draw.rect(screen,BLUE,polygonRect,2)
    else:
        pygame.draw.rect(screen,BLACK,polygonRect,2)

    if tool == "stamp 0":
        pygame.draw.rect(screen,BLUE,stampRects[0],2)
    else:
        pygame.draw.rect(screen,BLACK,stampRects[0],2)
        
    if tool == "stamp 1":
        pygame.draw.rect(screen,BLUE,stampRects[1],2)
    else:
        pygame.draw.rect(screen,BLACK,stampRects[1],2)
        
    if tool == "stamp 2":
        pygame.draw.rect(screen,BLUE,stampRects[2],2)
    else:
        pygame.draw.rect(screen,BLACK,stampRects[2],2)
        
    if tool == "stamp 3":
        pygame.draw.rect(screen,BLUE,stampRects[3],2)
    else:
        pygame.draw.rect(screen,BLACK,stampRects[3],2)
        
    if tool == "stamp 4":
        pygame.draw.rect(screen,BLUE,stampRects[4],2)
    else:
        pygame.draw.rect(screen,BLACK,stampRects[4],2)
        
    if tool == "stamp 5":
        pygame.draw.rect(screen,BLUE,stampRects[5],2)
    else:
        pygame.draw.rect(screen,BLACK,stampRects[5],2)

   


def highlightTool():
    if pencilRect.collidepoint(mx,my) and tool is not "pencil":
        pygame.draw.rect(screen,YELLOW,pencilRect,2)

    if paintBrushRect.collidepoint(mx,my) and tool is not "paint brush":
        pygame.draw.rect(screen,YELLOW,paintBrushRect,2)
        
    if eraserRect.collidepoint(mx,my) and tool is not "eraser":
        pygame.draw.rect(screen,YELLOW,eraserRect,2)

    if sprayPaintRect.collidepoint(mx,my) and tool is not "spray paint":
        pygame.draw.rect(screen,YELLOW,sprayPaintRect,2)
        
    if thicknessUpRect.collidepoint(mx,my):
        pygame.draw.rect(screen,YELLOW,thicknessUpRect,2)
        
    if thicknessDownRect.collidepoint(mx,my):
        pygame.draw.rect(screen,YELLOW,thicknessDownRect,2)
 
    if clearRect.collidepoint(mx,my):
        pygame.draw.rect(screen,YELLOW,clearRect,2)
        
    if lineRect.collidepoint(mx,my) and tool is not "line":
        pygame.draw.rect(screen,YELLOW,lineRect,2)

    if polygonRect.collidepoint(mx,my) and tool is not "polygon":
        pygame.draw.rect(screen,YELLOW,polygonRect,2)
        
    if rectangleRect.collidepoint(mx,my) and tool is not "rectangle":
        pygame.draw.rect(screen,YELLOW,rectangleRect,2)
        
    if textBoxRect.collidepoint(mx,my) and tool is not "text box":
        pygame.draw.rect(screen,YELLOW,textBoxRect,2)
        
    if fillRect.collidepoint(mx,my) and tool is not "fill":
        pygame.draw.rect(screen,YELLOW,fillRect,2)
        
    if noFillRect.collidepoint(mx,my) and tool is not "no fill":
        pygame.draw.rect(screen,YELLOW,noFillRect,2)
        
    if circleRect.collidepoint(mx,my) and tool is not "circle":
        pygame.draw.rect(screen,YELLOW,circleRect,2)

    for i in stampRects:
        if i.collidepoint(mx,my):
            pygame.draw.rect(screen,YELLOW,i,2)
 
        
def limitArea(onCanvas):
    if onCanvas:
        screen.set_clip(canvas)

    else:
        screen.set_clip()

def resetBoxCol():
    pygame.draw.rect(screen, BLACK, thicknessDownRect,2)
    pygame.draw.rect(screen, BLACK, thicknessUpRect,2)
    pygame.draw.rect(screen, BLACK, fillRect,2)
    pygame.draw.rect(screen, BLACK, noFillRect,2)
    pygame.draw.rect(screen, BLACK, clearRect,2)
    

def toolDialogBox(mx,my,fillRect,noFillRect,fullScreen,normalScreen,toolText):
    if normalScreen:
        if tool == "pencil":
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
            toolText = mediumFont.render("Pencil",True,BLACK)
        if tool == "paint brush":
            toolText = mediumFont.render("Paint Brush",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "spray paint":
            toolText = mediumFont.render("Spray Paint",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "eraser" :
            toolText = mediumFont.render("Eraser",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "line":
            toolText = mediumFont.render("Line",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "rectangle" :
            toolText = mediumFont.render("Rectangle",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "circle":
            toolText = mediumFont.render("Circle",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "text box":
            toolText = mediumFont.render("Text box",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "polygon":
            toolText = mediumFont.render("Polygon",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if tool == "stamp 0" or tool == "stamp 1" or tool == "stamp 2" or tool == "stamp 3" or tool == "stamp 4" or tool == "stamp 5":
            toolText = mediumFont.render("Stamp",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
            
            
        if fillRect.collidepoint(mx,my):
            toolText = mediumFont.render("Filled shape",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if noFillRect.collidepoint(mx,my):
            toolText = mediumFont.render("Non filled shape",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if undoButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Undo",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if redoButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Redo",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if thicknessUpRect.collidepoint(mx,my):
            toolText = mediumFont.render("Increase size",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if thicknessDownRect.collidepoint(mx,my):
            toolText = mediumFont.render("Decrease size",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if saveButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Save",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if loadButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Load File",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        if clearRect.collidepoint(mx,my):
            toolText = mediumFont.render("Fill the canvas",True,BLACK)
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        screen.blit(toolText,[970,630])

            
    if fullScreen:
        if tool == "pencil":
            toolText = mediumFont.render("Pencil",True,BLACK)
        if tool == "paint brush":
            toolText = mediumFont.render("Paint Brush",True,BLACK)
        if tool == "spray paint":
            toolText = mediumFont.render("Spray Paint",True,BLACK)
        if tool == "eraser" :
            toolText = mediumFont.render("Eraser",True,BLACK)
        if tool == "line":
            toolText = mediumFont.render("Line",True,BLACK)
        if tool == "rectangle" :
            toolText = mediumFont.render("Rectangle",True,BLACK)
        if tool == "circle":
            toolText = mediumFont.render("Circle",True,BLACK)
        if tool == "text box":
            toolText = mediumFont.render("Text box",True,BLACK)
        if tool == "polygon":
            toolText = mediumFont.render("Polygon Tool",True,BLACK)
        if fillRect.collidepoint(mx,my):
            toolText = mediumFont.render("Filled shape",True,BLACK)
        if noFillRect.collidepoint(mx,my):
            toolText = mediumFont.render("Non filled shape",True,BLACK)
        if undoButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Undo",True,BLACK)
        if redoButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Redo",True,BLACK)
        if thicknessUpRect.collidepoint(mx,my):
            toolText = mediumFont.render("Increase size",True,BLACK)
        if thicknessDownRect.collidepoint(mx,my):
            toolText = mediumFont.render("Decrease size",True,BLACK)
        if saveButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Save",True,BLACK)
        if loadButtonRect.collidepoint(mx,my):
            toolText = mediumFont.render("Load File",True,BLACK)
        if clearRect.collidepoint(mx,my):
            toolText = mediumFont.render("Fill the canvas",True,BLACK)
        screen.blit(toolText, (1050,50))

def save(mb,mx,my,canvas):
    # Saves the file as an image
    if mb[0] and saveButtonRect.collidepoint(mx,my):
        try:
            fname = tkinter.filedialog.asksaveasfilename(defaultextension=".png")
            if len(fname) >= 1:
                pygame.image.save(canvas,fname)
        except:
            print("saving error")

def load(mb,mx,my,loadImage):
    if mb[0] and loadButtonRect.collidepoint(mx,my):
        fname = tkinter.filedialog.askopenfilename()
        loadImage = pygame.image.load(fname)
        try:
            if fullScreen:
                loadImage = pygame.transform.scale(loadImage,(1280,620))
                screen.blit(loadImage,(0,100))
            if normalScreen:
                loadImage = pygame.transform.scale(loadImage,(width - 300,600))
                screen.blit(loadImage,(300,0))
        except:
            pass
        
        
        
while not done:
    #_____Main event loop_______

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            #Typing
            if tool == "text box":
                for i in keyList:
                    if i == pygame.key.name(event.key):
                        currentKey = pygame.key.name(event.key)
                        if currentKey == "space":
                            currentKey = " "
                            userText += str(currentKey)
                        elif currentKey == "caps lock":
                            userText += ""
                        elif currentKey == "return":
                            currentKey = ""
                            canType = False
                        elif currentKey == "tab":
                            currentKey = "          "
                            userText += str(currentKey)
                        elif currentKey == "backspace":
                            currentKey = None
                            if len(userText) > 0:
                                userTextList = list(userText)
                                del(userTextList[-1])
                                userText = ""
                                for i in userTextList:
                                    userText += i
                            screen.blit(screenShot,[0,0])
                        else:
                            userText += str(currentKey)
                        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button != 4 and event.button != 5:
                if event.button == 3 and tool == "polygon" and onCanvas:
                    rightClick = True
                else:
                    rightClick = False
                if event.button == 1 and tool == "polygon" and onCanvas:
                    leftClick = True
                else:
                    leftClick = False
                screenShot = screen.copy()
                startX,startY = pygame.mouse.get_pos()
                
                #Typing
                if not canType:
                    canType = True
                    userText = ""
                
                #Undo/Red0
                if undoButtonRect.collidepoint(mx,my) and toolSelected:
                    if tool == "text box":
                        tool = "no tool"
                        userText = ""
                        cantype = False
                        
                    try:
                        redoList.append(undoList[-1])
                        screen.blit(undoList[-2],[0,0])
                        del(undoList[-1])
                    except:
                        pass
                    if len(undoList) == 1:
                        pygame.draw.rect(screen, WHITE, canvas)
                        
                if redoButtonRect.collidepoint(mx,my) and toolSelected:
                    if tool == "text box":
                        tool = "no tool"
                        userText = ""
                        cantype = False
                        
                    try:
                        undoList.append(redoList[-1])
                        screen.blit(redoList[-1],[0,0])
                            
                        del(redoList[-1])
                    except:
                        pass
                    
                     
        if event.type == pygame.MOUSEBUTTONUP and onCanvas:
            undoShot = screen.copy()
            undoList.append(undoShot)
            
    
    # Get the mouse information and change the mouse cursor
    mouseDown = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    
    if start:
        screen.blit(startBackground,[0,0])
        screen.blit(title,[800,20])
        screen.blit(paintTitle,[1100,110])
        screen.blit(button,[1050,220])
        screen.blit(normalTextA,[1055,230])
        screen.blit(normalTextB,[1055,270])
        screen.blit(button,[800,220])
        screen.blit(fullTextA,[805,230])
        screen.blit(fullTextB,[805,270])
        screen.blit(button,[920,400])
        screen.blit(helpTextA,[1000,400])
        screen.blit(helpTextB,[1000,425])
        screen.blit(helpTextC,[1000,450])
        
        
        
        if mouseDown[0]:
            if normalRect.collidepoint(mx,my):
                normalScreen = True
                start = False
            if fullRect.collidepoint(mx,my):
                fullScreen = True
                start = False
            if helpRect.collidepoint(mx,my):
                start = False
                helpScreen = True
                
    if helpScreen:
        screen.blit(startBackground,[0,0])
        pygame.draw.rect(screen,BLACK,(800,30,450,650),1)
        screen.blit(back,[25,30])
        screen.blit(infoPic,[800,30])
        if backRect.collidepoint(mx,my) and mouseDown[0]:
            start = True
            helpScreen = False
        
            
        
        

    if fullScreen or normalScreen:
        resetBoxCol()



        # Fullscreen Mechanics/changes
        if fullScreen and oneTime:
            screen.blit(background,[0,0])
            screen.blit(background,[550,0])
            screen.blit(background,[1000,0])
            oneTime = False
            canvas = pygame.Rect(0,100,1280,720)
            pygame.draw.rect(screen, WHITE, canvas)
            
            pencilRect = pygame.Rect(25,15,35,35)
            pygame.draw.rect(screen, BLACK, pencilRect,2)
            screen.blit(miniPencilButton,[32,20])

            paintBrushRect = pygame.Rect(65,15,35,35)
            pygame.draw.rect(screen, BLACK, paintBrushRect,2)
            screen.blit(miniBrushButton,[72,20])

            clearRect = pygame.Rect(105,15,35,35)
            pygame.draw.rect(screen,BLACK,clearRect,2)
            screen.blit(miniBucketButton,(108,20))

            eraserRect = pygame.Rect(25,60,35,35)
            pygame.draw.rect(screen, BLACK, eraserRect,2)
            screen.blit(miniEraserButton,[30,65])

            polygonRect = pygame.Rect(105,60,35,35)
            pygame.draw.rect(screen, BLACK,polygonRect,2)
            screen.blit(miniPolygonButton,(110,65))

            sprayPaintRect = pygame.Rect(65,60,35,35)
            pygame.draw.rect(screen, BLACK, sprayPaintRect,2)
            screen.blit(miniSprayPaintButton,[72,65])

            thicknessUpRect = pygame.Rect (300,15,35,35)
            pygame.draw.rect(screen, BLACK, thicknessUpRect,2)
            thickText1 = smallFont.render("Size",True,BLACK)
            thickText2 = smallFont.render("+",True,BLACK)
            screen.blit(thickText1,[304,15])
            screen.blit(thickText2,[314,30])

            thicknessDownRect = pygame.Rect(300,60,35,35)
            pygame.draw.rect(screen, BLACK, thicknessDownRect,2)
            thickText3 = smallFont.render("Size",True,BLACK)
            thickText4 = smallFont.render("_",True,BLACK)
            screen.blit(thickText3,[304,60])
            screen.blit(thickText4,[314,65])

            fillRect = pygame.Rect(260,15,35,35)
            pygame.draw.rect(screen, BLACK, fillRect,2)
            pygame.draw.rect(screen, BLACK, (270,20,15,23))

            noFillRect = pygame.Rect(260,60,35,35)
            pygame.draw.rect(screen, BLACK, noFillRect,2)
            pygame.draw.rect(screen, BLACK, (270,65,15,23),1)

            undoButtonRect = pygame.Rect(1230,20,30,30)
            screen.blit(undoButton, [1230,20])

            redoButtonRect = pygame.Rect(1230,50,30,30)
            screen.blit(redoButton,[1230,50])

            textBoxRect = pygame.Rect(185,15,35,35)
            pygame.draw.rect(screen, BLACK,textBoxRect,2)
            screen.blit(miniTextButton,[190,20])
            
            saveButtonRect = pygame.Rect(360,15,32,32)
            screen.blit(saveButton,[360,15])

            loadButtonRect = pygame.Rect(400,15,32,32)
            screen.blit(loadButton,[400,15])

            lineRect = pygame.Rect(145,15,35,35)
            pygame.draw.rect(screen, BLACK, lineRect,2)
            pygame.draw.line(screen, BLACK, (155,22),(170,42))
            
            rectangleRect = pygame.Rect(145,60,35,35)
            pygame.draw.rect(screen, BLACK, rectangleRect,2)
            pygame.draw.rect(screen, BLACK, (151,67,23,23),2)

            circleRect = pygame.Rect(185,60,35,35)
            pygame.draw.rect(screen, BLACK, circleRect,2)
            pygame.draw.circle(screen, BLACK, [202,80],10,2)

            colourRect = pygame.Rect(850,0, 150, 100)
            colourSelect = pygame.transform.scale(colourSelect,[150,100])
            screen.blit(colourSelect,[850,0])

            stamp1 = pygame.Rect(440,45,50,50)
            stamp2 = pygame.Rect(500,45,50,50)
            stamp3 = pygame.Rect(560,45,50,50)
            stamp4 = pygame.Rect(620,45,50,50)
            stamp5 = pygame.Rect(680,45,50,50)
            stamp6 = pygame.Rect(740,45,50,50)

            screen.blit(fullStampList[0],[445,50])
            screen.blit(fullStampList[1],[505,50])
            screen.blit(fullStampList[2],[565,50])
            screen.blit(fullStampList[3],[625,50])
            screen.blit(fullStampList[4],[685,50])
            screen.blit(fullStampList[5],[743,48])

            stampRects = [stamp1,stamp2,stamp3,stamp4,stamp5,stamp6]
            for i in stampRects:
                pygame.draw.rect(screen,BLACK,i,2)
                

            

           
        if fullScreen:
            colourText = mediumFont.render("Current Colour ---> ", True, col)
            pygame.draw.rect(screen, col, (1200,25,15,15))
            screen.blit(colourText,[1025,20])
            
        
            
        if normalScreen and oneTime:
            oneTime = False
            screen.blit(background,[0,0])
            screen.blit(background2,[0,467])
            screen.blit(background2,[550,467])
            screen.blit(background2,[800,467])
            canvas = pygame.Rect(300,0,width-300,600)
            subCanvas = screen.subsurface(canvas)
            pygame.draw.rect(screen, WHITE, canvas)

            pencilRect = pygame.Rect(30,30,50,50)
            pygame.draw.rect(screen, BLACK, pencilRect,2)
            screen.blit(pencilButton,[35,40])

            paintBrushRect = pygame.Rect(90,30,50,50)
            pygame.draw.rect(screen, BLACK, paintBrushRect,2)
            screen.blit(paintBrushButton,[95,35])

            eraserRect = pygame.Rect(30,90,50,50)
            pygame.draw.rect(screen, BLACK, eraserRect,2)
            screen.blit(eraserButton,[33,100])

            sprayPaintRect = pygame.Rect(90,90,50,50)
            pygame.draw.rect(screen, BLACK, sprayPaintRect,2)
            screen.blit(sprayPaintButton, [95,95])

            textBoxRect = pygame.Rect(90,210,50,50)
            pygame.draw.rect(screen, BLACK, textBoxRect,2)
            screen.blit(textButton,[95,216])

            clearRect = pygame.Rect(150,350,50,50)
            pygame.draw.rect(screen,BLACK,clearRect,2)
            screen.blit(bucketButton,(155,352))

            thicknessUpRect = pygame.Rect (90,410,50,50)
            pygame.draw.rect(screen, BLACK, thicknessUpRect,2)
            thickText1 = mediumFont.render("Size",True,BLACK)
            thickText2 = mediumFont.render("+",True,BLACK)
            screen.blit(thickText1,[97,417])
            screen.blit(thickText2,[107,433])

            thicknessDownRect = pygame.Rect(30,410,50,50)
            pygame.draw.rect(screen, BLACK, thicknessDownRect,2)
            thickText3 = mediumFont.render("Size",True,BLACK)
            thickText4 = mediumFont.render("_",True,BLACK)
            screen.blit(thickText3,[37,417])
            screen.blit(thickText4,[48,425])

            colourRect = pygame.Rect(30,540,200,150)

            undoButtonRect = pygame.Rect(200,60,30,30)
            screen.blit(undoButton, [200,60])

            redoButtonRect = pygame.Rect(236,60,30,30)
            screen.blit(redoButton,[236,60])
            

            lineRect = pygame.Rect(30,150,50,50)
            pygame.draw.rect(screen, BLACK, lineRect,2)
            pygame.draw.line(screen,BLACK,(40,155),(75,190),3)

            rectangleRect = pygame.Rect(90,150,50,50)
            pygame.draw.rect(screen, BLACK, rectangleRect,2)
            pygame.draw.rect(screen, BLACK, (100,160,30,30),1)

            
            fillRect = pygame.Rect(90,350,50,50)
            pygame.draw.rect(screen, BLACK, fillRect, 2)
            pygame.draw.rect(screen, BLACK,(100,355,30,40))


            noFillRect = pygame.Rect(30,350,50,50)
            pygame.draw.rect(screen, BLACK, noFillRect,2)
            pygame.draw.rect(screen, BLACK, (40,355,30,40),2)

           
            circleRect = pygame.Rect(30,210,50,50)
            pygame.draw.rect(screen, BLACK, circleRect,2)
            pygame.draw.circle(screen, BLACK, [55,235],15,2)

            polygonRect = pygame.Rect(30,270,50,50)
            pygame.draw.rect(screen,BLACK,polygonRect,2) 
            screen.blit(polygonButton,(36,275))
                        
            screen.blit(saveButton,[200,20])
            screen.blit(loadButton,[240,20])
            
            stamp1 = pygame.Rect(280,620,80,80)
            stamp2 = pygame.Rect(380,620,80,80)
            stamp3 = pygame.Rect(480,620,80,80)
            stamp4 = pygame.Rect(580,620,80,80)
            stamp5 = pygame.Rect(680,620,80,80)
            stamp6 = pygame.Rect(780,620,80,80)
            stampRects = [stamp1,stamp2,stamp3,stamp4,stamp5,stamp6]

            for i in stampRects:
                pygame.draw.rect(screen,BLACK,i,2)

            screen.blit(normalStampList[0],[280,620])
            screen.blit(normalStampList[1],[380,620])
            screen.blit(normalStampList[2],[480,620])
            screen.blit(normalStampList[3],[580,620])
            screen.blit(normalStampList[4],[680,620])
            screen.blit(normalStampList[5],[783,623])

        # Showing what colour is selected
        if normalScreen:
            screen.blit(colourSelect,[30,540])
            pygame.draw.rect(screen, col, (205,512,15,15))
            colourText = mediumFont.render("Current Colour --->", True, col)
            screen.blit(colourText, [30,510])
        
        # To show the type of tool being used
        if normalScreen:
            pygame.draw.rect(screen, (0,200,255),(950,610,300,100))
        else:
            pygame.draw.rect(screen, (0,200,255),(1025,50,200,40))
        toolDialogBox(mx,my,fillRect,noFillRect,fullScreen,normalScreen,toolText)
            
            
        # Checks to see if the mouse is on the canvas
        if canvas.collidepoint(mx,my):
            onCanvas = True
        else:
            onCanvas = False    
        
        # Selecting a Tool/Command
        if mouseDown[0]:
            # Tool Select
            if pencilRect.collidepoint(mx,my):
                tool = "pencil"
                thickness = 1
                toolSelected = True
            if paintBrushRect.collidepoint(mx,my):
                tool = "paint brush"
                thickness = 40
                toolSelected = True
            if eraserRect.collidepoint(mx,my):
                tool = "eraser"
                thickness = 5
                toolSelected = True
            if sprayPaintRect.collidepoint(mx,my):
                tool = "spray paint"
                thickness = 9
                toolSelected = True
            if lineRect.collidepoint(mx,my):
                tool = "line"
                thickness = 1
                toolSelected = True
            if rectangleRect.collidepoint(mx,my):
                tool = "rectangle"
                thickness = 10
                toolSelected = True
            if circleRect.collidepoint(mx,my):
                tool = "circle"
                thickness = 1
                toolSelected = True
            if textBoxRect.collidepoint(mx,my):
                tool = "text box"
                toolSelected = True
                thickness = 21
            if polygonRect.collidepoint(mx,my):
                tool = "polygon"
                toolSelected = True
                thickness = 1
                
            for i in range(len(stampRects)):
                if stampRects[i].collidepoint(mx,my):
                    tool = "stamp " + str(i)
                    toolSelected = True
                
            # Tool manipulations   
            if thicknessUpRect.collidepoint(mx,my):
                thickness += 1
                pygame.draw.rect(screen, BLUE, thicknessUpRect,2)
            if thicknessDownRect.collidepoint(mx,my):
                thickness -= 1
                pygame.draw.rect(screen, BLUE, thicknessDownRect,2)
            if fillRect.collidepoint(mx,my):
                pygame.draw.rect(screen, BLUE, fillRect,2)
                fill = True
            if noFillRect.collidepoint(mx,my):
                pygame.draw.rect(screen, BLUE,noFillRect,2)
                fill = False
            if colourRect.collidepoint(mx,my):
                col = screen.get_at((mx,my))
                colourText = mediumFont.render("Current Colour ---> ", True, col)
                if normalScreen:
                    screen.blit(colourText, [30,510])
                    pygame.draw.rect(screen, col, (205,512,15,15))
                if fullScreen:
                    screen.blit(colourText,[1025,20])
                    pygame.draw.rect(screen, col, (1200,22,15,15))
            if clearRect.collidepoint(mx,my):
                tool = "fill"
                pygame.draw.rect(screen,BLUE,clearRect,2)
                fillScreen(canvas,col)
                tool = "no tool"
                
                    
        # Makes sure the thickness is controlled
            if tool == "pencil":
                if thickness >= 10:
                        thickness = 9
            elif tool == "paint brush":
                if thickness <= 30:
                        thickness = 31
            elif tool == "line":
                if thickness >= 20:
                    thickness = 19
            elif tool == "spray paint":
                if thickness <= 5:
                    thickness = 5
            elif tool == "polygon":
                if thickness >= 15:
                    thickness = 15
            elif tool == "text box":
                if thickness >= 40:
                    thickness = 40
            if thickness <= 1:
                thickness = 1

                
        if normalScreen:
            subCanvas = screen.subsurface(canvas)
        if fullScreen:
            subCanvas = screen.subsurface(0,100,1280,620)
        limitArea(onCanvas)
        drawing(mouseDown,omx,omy,mx,my,tool,onCanvas,screenShot,thickness,col,startX,startY,fill,selectList)
        if tool == "polygon":
            if onCanvas:
                if rightClick:
                    try:
                        finishPolygon(startPoints,col,thickness)
                    except:
                        pass
                    startPoints = []
                if leftClick:
                    drawPolygon(startX,startY,mx,my,screenShot,startPoints,rightClick,col,thickness)
        selectTool(tool)
        highlightTool()
        save(mouseDown,mx,my,subCanvas)
        load(mouseDown,mx,my,loadImage)
        textBox(startX,startY,userText,mediumFont,canType,tool,col,onCanvas,textboxPos,thickness)
    
    
    omx = mx
    omy = my
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
