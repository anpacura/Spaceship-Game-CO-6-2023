import pygame
class PowerUp:
    WIDTH = 30
    HEIGHT = 30
    POS_Y = 0

    def __init__(self, image):
        self.image = image
        self.image = pygame.transform.scale(self, image, (self.WIDTH, self.HEIGHT))
        self.rect = self,image