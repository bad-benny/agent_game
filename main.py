import pygame
from characterplayer import Character

pygame.init()

pygame.display.set_caption('Agent Game')
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
player = Character()
speed = 5

x = 50
y = 50


running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            x, y = Character.movechar(player, event, x, y, speed)

    
    screen.fill((0, 0, 0))
    
    playerdraw = Character.drawchar(player, screen, x, y)

    pygame.display.update()

pygame.quit()
