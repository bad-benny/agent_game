import pygame
from characterplayer import Character

pygame.init()

pygame.display.set_caption('Agent Game')
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
player = Character()
speed = 1

x = 50
y = 50


running = True

while running:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    x, y = Character.movechar(player, keys, x, y, speed)

    
    screen.fill((0, 0, 0))
    
    playerdraw = Character.drawchar(player, screen, x, y)

    pygame.display.update()

pygame.quit()
