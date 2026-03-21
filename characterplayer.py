import pygame

class Character():
    def __init__(self):
        pass
    
    def drawchar(self, screen, x, y,):
        pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))
    
    def movechar(self, key, x, y, speed):
        if key[pygame.K_w] or key[pygame.K_UP]:
            y -= speed
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            y += speed
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            x += speed
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            x -= speed
        return x, y