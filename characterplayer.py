import pygame

class Character():
    def __init__(self):
        pass
    
    def drawchar(self, screen, x, y,):
        pygame.draw.rect(screen, (255, 0, 255), (30, 30, x, y))
    