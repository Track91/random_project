from player import Player
from comete import Comet
import pygame
from comet_event import CometFallEvent

class Game(pygame.sprite.Sprite):
    def __init__(self):
        self.player = Player()
        self.comet_event = CometFallEvent(self)
        self.comet = Comet()




