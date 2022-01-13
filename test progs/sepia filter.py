import pygame


# Colors

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255 ,255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)

PI = 3.141592653

pygame.init()
size = (900,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Re_run")
masseyPic = pygame.image.load("images/grass.jpg")
screen.blit(masseyPic,[10,10])

for x in range(864):
    for y in range(576):
        r,g,b,a = screen.get_at((x,y))
        r2 = min(255,int(0.393 * r + 0.769 * g + 0.189 * b))
        g2 = min(255,int(0.349 * r + 0.686 * g + 0.169 * b))
        b2 = min(255,int(0.272 * r + 0.534 * g + 0.131 * b))
        screen.set_at((x,y),(r2,g2,b2))
    
        
        

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
    

    #_______Drawing code goes here______

    pygame.display.flip() #Updates the screen with what was drawn


    clock.tick(60)# This sets framerate to 60
    

pygame.quit()
