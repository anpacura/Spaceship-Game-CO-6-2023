import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH


class spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2)  - WIDTH
    Y_POS = 500
    UP = 0
    DOWN = 0

    def __init__(self):
        self.imagen = SPACESHIP
        self.imagen = pygame.transform.scale(self.imagen, (self.WIDTH, self.HEIGHT))
        self.rect = self.imagen.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, game_speed, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)

        if user_input[pygame.K_RIGHT]:
            self.move_right(game_speed)   

        if user_input[pygame.K_UP]:
            self.move_up(game_speed)

        if user_input[pygame.K_DOWN]:
            self.move_down(game_speed)

    def dram(self, screen):
                screen.blit(self.imagen, self.rect)

    def move_left(self, game_speed):
                    if self.rect.left >= self.rect.right:
                        self.rect.x -= game_speed

    def move_right(self, game_speed):
                    if self.rect.right <= self.rect.left:
                        self.rect.x += game_speed

    def move_up(self, game_speed):
                    if self.rect.up > 0:
                        self.rect.y -= game_speed

    def move_down(self, game_speed):
                    if self.rect.down < 0:
                        self.rect.y += game_speed                                        