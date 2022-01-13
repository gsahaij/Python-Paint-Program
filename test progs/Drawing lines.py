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
sx = 0
sy = 0

#Loop until the close button is clicked
done = False

#Used to manage the framerate
clock = pygame.time.Clock()

#_______Main program loop__________

while not done:
    #_____Main event loop_______

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            screenShot = screen.copy() # Screen Shot
            sx,sy = pygame.mouse.get_pos() # starting position
            
       

    #_______Game logic goes here________

    mb = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()
    print(sx,sy,mx,my)

    if mb[0]:
        screen.blit(screenShot,(0,0))
        pygame.draw.line(screen, GREEN, (sx,sy),(mx,my))
    

    #_______Drawing code goes here______

    pygame.display.flip() #Updates the screen with what was drawn


    clock.tick(200)# This sets framerate to 60
    

pygame.quit()
