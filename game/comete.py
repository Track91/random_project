import pygame
import random
import game

from comet_event import CometFallEvent

class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bite.png")
        self.rect = self.image.get_rect()
        self.velocity = 1

    def lose(self):
        print('')
    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y == 720:
            self.remove()
            self.lose()




    def reset_fall(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, 1080-200)
        self.velocity = random.randint(3, 5)





