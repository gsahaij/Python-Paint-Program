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
pygame.display.set_caption("Re_run")

marker = pygame.Surface((20,20),pygame.SRCALPHA)
pygame.draw.circle(marker,(255,255,255,5),(10,10),10)

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

    #screen.fill(WHITE) #Clears the screen to white. DO NOT put drawing code above this
    mx,my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    if mb[0]:
        screen.blit(marker,[mx,my])
    
    

    #_______Drawing code goes here______

    pygame.display.flip() #Updates the screen with what was drawn


    clock.tick(60)# This sets framerate to 60
    

pygame.quit()
    
