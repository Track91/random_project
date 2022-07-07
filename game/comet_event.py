import pygame

class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 100
        self.game = game

        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += 1

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        pass

    def attenmpt_fall(self):
        if self.is_full_loaded():
            print('Pluie de cometes')
            self.meteor_fall()
            self.reset_percent()

    def update_bar(self, surface):
        self.add_percent()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
        ])

        pygame.draw.rect(surface, (255, 0, 0), [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * 10,
            10
        ])