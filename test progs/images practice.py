import pygame


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

pos = 0

canvasRect = pygame.Rect(100,50, 400,400)
screen.fill(RED)
pygame.draw.rect(screen, WHITE, canvasRect)

stringList = ["images/brick.jpg", "images/dirt.jpg", "images/grass.jpg"]
textures = []

for i in stringList:
    image = pygame.image.load(i)
    textures.append(image)
    

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
            if event.button == 4:
                pos = (pos + 1) % n
                
            if event.button == 5:
                pos = (pos - 1) % n
        

    #_______Game logic goes here________

    sub = textures[pos].subsurface((0,0),(50,50))
    n = len(textures)

    mb = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()

    screen.blit(sub,(25,50))
    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if mb[0]:
            pygame.draw.line(screen, RED, (omx,omy),(mx,my))

        if mb[2]:
            sample = textures[pos].subsurface((mx,my,30,30))
            screen.blit(sample, (mx-25,my-25))
            

    
    #_______Drawing code goes here______

    pygame.display.flip() #Updates the screen with what was drawn
    
    omx = mx
    omy = my
    clock.tick(60)# This sets framerate to 60
    

pygame.quit()
