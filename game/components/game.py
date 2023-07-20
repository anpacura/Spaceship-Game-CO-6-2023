import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.utils import 
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.key = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = spaceship()
        self.enemy_handler = EnemyHandler()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            Points = 0
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.key = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(self.game_speed, user_input)
        self.enemy_handler.update(self.bullet_handler)
        self.bullet_handler.update(self.player)
        if not self.player.is_alive:
            pygame.time.delay(300)
            self.playing = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        self.bullet_handler.draw(self.screen)
        points_box.text = "Points: {}".format(points)
        top_score_box.text = "Max score: {}".format(top_score)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw menu(self):
        if self.number_deaths == 0:
           text, text_rect = text_utils.get_message('Press any key to start', 30, WHITE)
           self.screen.blit(text, tex_rect)
           self.screen.blit(score, score_rect)
        else:
            text, text_rect = tex_utils.getmessage('Press any key to Restart', 30, WHITE)
            score, score_rect = text_utils.get.message('Your score is: {self.score}', 30, WHITE, height-SCREEN_HEIGHT//2 + 50)
            self.screen_rect.blit(text, text_rect)
            self.screen,blit(score, score_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(F'Your score is: {self.score}', 20, WHITE, 1000, 40)
        self.screen.blit(score, score_rect)


    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.score = 0    