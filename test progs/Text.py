import pygame


# Colors

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255 ,255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)

PI = 3.141592653

pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
mediumFont = pygame.font.SysFont('Calibri',21,True,False)
sx = 0
sy = 0
canType = False
rightClick = False
keyList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space','caps lock','return','backspace','tab',1,2,3,4,5,6,7,8,9]
startPoints = []
currentKey = None
polygonFinished = False
userText = ""
pygame.display.set_caption("Re_run")

#Loop until the close button is clicked
done = False

#Used to manage the framerate
clock = pygame.time.Clock()

def textBox(sx,sy,userText,font,canType):
    if canType:
        screenText = font.render(userText,True,BLACK)
        screen.blit(screenText,[sx,sy])
    else:
        pass

def drawPolygon(sx,sy,mx,my,screenShot,startPoints,rightClick,polygonFinished):
    screen.blit(screenShot,[0,0])
    pygame.draw.line(screen,BLACK,(sx,sy),(mx,my),1)
    startPoints.append((sx,sy))
    try:
        if rightClick:
            pygame.draw.line(screen,BLACK,(startPoints[0]),(startPoints[-1]),1)
            polygonFinished = False
            startPoints = []
    except:
        pass
        
        
    
    

    
    
    
    

#_______Main program loop__________

while not done:
    #_____Main event loop_______

    for event in pygame.event.get(): #The user did something
        if event.type == pygame.QUIT:#If the user attempts to close the window
            done = True #Telling us to exit the loop and therefore the window
        elif event.type == pygame.KEYDOWN:
            for i in keyList:
                if i == pygame.key.name(event.key):
                    currentKey = pygame.key.name(event.key)
                    if currentKey == "space":
                        currentKey = " "
                        userText += str(currentKey)
                    elif currentKey == "caps lock":
                        userText += ""
                    elif currentKey == "return":
                        currentKey = None
                        canType = False
                    elif currentKey == "backspace":
                        """
                        undo redo code here
                        """
                    elif currentKey == "tab":
                        currentKey = "          "
                        userText += str(currentKey)
                    else:
                        userText += str(currentKey)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sx,sy = pygame.mouse.get_pos()
            screenShot = screen.copy()
            if event.button == 3:
                rightClick = True
                polygonFinished = True
            if not canType:
                canType = True
                userText = ""
            
            
    #_______Game logic goes here________
    mb = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()
    

    #screen.fill(WHITE) #Clears the screen to white. DO NOT put drawing code above this
    
    #_______Drawing code goes here_____
    textBox(sx,sy,userText,mediumFont,canType)
    try:
        drawPolygon(sx,sy,mx,my,screenShot,startPoints,rightClick,polygonFinished)
    except:
        pass
    
    print(polygonFinished)
    pygame.display.flip() #Updates the screen with what was drawn


    clock.tick(200)# This sets framerate to 60
    

pygame.quit()
