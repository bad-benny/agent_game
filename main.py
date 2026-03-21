import pygame
from characterhandler import Character

pygame.init()

pygame.display.set_caption('Agent Game')
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
player = Character()
npc = Character()
speed = 1

playercol = (100, 255, 50)
npccol = (50, 255, 150)

x = 50
y = 50


running = True

while running:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    x, y = player.moveplayer(keys, x, y, speed)

    
    screen.fill((0, 0, 0))
    
    npc.drawnpc(screen, 600, 400, npccol)
    player.drawplayer(screen, x, y, playercol)

    pygame.display.update()

pygame.quit()
