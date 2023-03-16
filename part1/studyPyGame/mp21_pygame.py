import pygame

pygame.init()
wind = pygame.display.set_mode((1000, 500))

bg_img = pygame.image.load('./studyPygame/Assets/background.png')
BG = pygame.transform.scale(bg_img, (1000, 500)) # size up

pygame.display.set_caption('make game')
icon = pygame.image.load('./studyPyGame/game.png')
pygame.display.set_icon(icon)

width = 1000 
loop = 0 
run = True

while run : 
    wind.fill((0,0,0)) 

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            run = False

    wind.blit(BG, (loop,0))
    wind.blit(BG, (width + loop, 0))
    if loop == -width :                    
        loop = 0

    loop -= 1 

    pygame.display.update()
