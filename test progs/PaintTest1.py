import pygame
import random
# Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

PI = 3.141592653

pygame.init()
size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paint Test 1")

# Loop until the close button is clicked
done = False
screen.fill(WHITE)
# ________ Defining Globals _________
leftClick = False
start = True

""" Fonts """
bigFont = pygame.font.SysFont('Calibri', 50, True, False)
mediumFont = pygame.font.SysFont('Calibri', 25, True, False)
smallFont = pygame.font.SysFont('Calibri', 15, True, False)

""" Images """
rocketImage = pygame.image.load("Rocket.png").convert()
rocketImage.set_colorkey(BLACK)
rocketY = 600
starImage = pygame.image.load("stars.png").convert()
starImage.set_colorkey(WHITE)
starPosList = []
for i in range(100):
    pos = [random.randint(1,1000),random.randint(1,600)]
    starPosList.append(pos)




# _______ Defining Functions_________
"""Start screen"""
def startScreen(screen):
    pygame.draw.rect(screen, BLACK, [0,0,1000,600])
def startText(x1,x2,y):
    startAlert = bigFont.render("Welcome to Space Paint", True, WHITE)
    spaceAlert = mediumFont.render("Press Space to Enter the Paint Program", True, WHITE)
    screen.blit(startAlert, [250, 20])
    screen.blit(spaceAlert, [280, 200])
    for star in starPosList:
        screen.blit(starImage,star)
    screen.blit(rocketImage, [x1,y])
    screen.blit(rocketImage, [x2,y])








def eraseText():
    eraseAlert = smallFont.render('Press Space to Erase the Canvas', True, BLACK)
    screen.blit(eraseAlert,[30,510])




"""Brushes"""
def brush1(screen,x,y):
    pygame.draw.circle(screen, RED, [x,y],5)

def brush2(screen,x,y):
    pygame.draw.circle(screen, RED, [x, y], 5)




# _______Main program loop__________

while not done:
    # _____Main event loop_______

    for event in pygame.event.get():  # The user did something
        if event.type == pygame.QUIT:  # If the user attempts to close the window
            done = True  # Telling us to exit the loop and therefore the window
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = False
                screen.fill(WHITE)



# _________Globals__________
    if not start:
        mouseButton = pygame.mouse.get_pressed()
        if mouseButton[0] == 1:
            leftClick = True
        elif mouseButton[0] == 0:
            leftClick = False
        mouseX,mouseY = pygame.mouse.get_pos()



# _________Calling Functions_________
    if start:
        startScreen(screen)
        rocketY -= 5
        pygame.time.wait(60)
        startText(50, 850, rocketY)
        if rocketY < -75:
            rocketY = 600
    else:
        eraseText()
        if leftClick:
            brush1(screen, mouseX, mouseY)









    # _______Drawing code goes here______

    pygame.display.flip()  # Updates the screen with what was drawn



pygame.quit()
