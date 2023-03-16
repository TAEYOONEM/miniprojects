#Python Game - PyGame Game Framework
import pygame

pygame.init() # essential - 1 initiate game 
width = 500; height = 500

wind = pygame.display.set_mode((width, height)) # window 500 x 500
pygame.display.set_caption('make game')
icon = pygame.image.load('./studyPyGame/game.png')
pygame.display.set_icon(icon)

# set object
x = 250
y = 250
radius = 10
vel_x = 10
vel_y = 10
jump = False

run = True

while run : 
    wind.fill((0,0,0)) # fill background blak
    pygame.draw.circle(wind, (255,255,255), (x, y), radius)

    # event = signal
    for event in pygame.event.get() : # 2 get event
        if event.type == pygame.QUIT :
            run = False

    # movement object
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 10 :
        x -= vel_x # move left by vel_x
    if userInput[pygame.K_RIGHT] and  x < width - 10:
        x += vel_x # move right by vel_x
    
    # if userInput[pygame.K_UP] and y > 10 :
    #     y -= vel_y # move up by vel_y
    # if userInput[pygame.K_DOWN] and y < height - 10:
    #     y += vel_y # move down by vel_y

    # Jump Object
    if jump == False and userInput[pygame.K_SPACE] :
        jump = True
    
    if jump == True :
        y -= vel_y * 3
        vel_y -= 1
        if vel_y < - 10 :
            jump = False
            vel_y = 10


    pygame.time.delay(10)
    pygame.display.update() # 3 update display (transform)
