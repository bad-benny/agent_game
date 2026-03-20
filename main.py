import pygame
from characterplayer import Character

pygame.init()

pygame.display.set_caption('Agent Game')
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
player = Character()


running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    playerdraw = Character.drawchar(player, screen, 50, 50)


    pygame.display.update()

pygame.quit()
