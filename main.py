import pygame

pygame.init()

pygame.display.set_caption('Agent Game')
screen = pygame.display.set_mode((1080, 920))
playersheet = pygame.image.load("player.png").convert_alpha()

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False




    pygame.display.update()

pygame.quit()
