from player import Player
from comete import Comet
from comet_event import CometFallEvent

class Game:
    def __init__(self):
        self.player = Player()
        self.comet_event = CometFallEvent(self)
        self.comet = Comet()

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.comet_event.update_bar(screen)

        self.comet_event.all_comets.draw(screen)
        for comet in self.comet_event.all_comets:
            comet.fall()




