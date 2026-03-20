import pygame

class Character():
    def __init__(self):
        pass
    
    def drawchar(self, screen, x, y,):
        pygame.draw.rect(screen, (255, 0, 255), (x, y, 30, 30))
    
    def movechar(self, event, x, y, speed):
        if event.key == pygame.K_LEFT:
            x -= speed
        elif event.key == pygame.K_RIGHT:
            x += speed
        elif event.key == pygame.K_UP:
            y -= speed
        elif event.key == pygame.K_DOWN:
            y += speed

        return x, y