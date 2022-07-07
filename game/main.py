import pygame
from game import Game

import random

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


class Game:
    def __init__(self):
        self.player = Player()
        self.comet = Comet()

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.comet_event.update_bar(screen)

        self.comet_event.all_comets.draw(screen)
        for comet in self.comet_event.all_comets:
            comet.fall()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.max_heath = 10
        self.velocity = 4
        self.image = pygame.image.load('maxime2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = 720-280

        self.image = pygame.transform.scale(self.image, (190, 280))

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity
    def move_up(self):
        self.rect.y -= self.velocity



class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bite.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
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


pygame.init()
colors = {
    'BLACK': (0, 0, 0),
    'GRAY': (127, 127, 127),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'CYAN': (0, 255, 255),
    'MAGENTA': (255, 0, 255)
}

pygame.display.set_caption('Maxime game')
screen = pygame.display.set_mode((1080, 720))
score = 0
def check_collide():
    global score
    rect1 = game.comet.rect
    rect2 = game.player.rect

    collide = rect1.colliderect(rect2)
    if collide:
        game.comet.reset_fall()
        score += 1


game = Game()


rectScreen = screen.get_rect()
running = True
clock = pygame.time.Clock()
while running:

    police = pygame.font.Font(None, 72)
    texte = police.render("score : {}".format(str(score)), True, pygame.Color("#FFFF00"))
    rectTexte = texte.get_rect()
    rectTexte.center = rectScreen.center
    screen.fill(colors['GREEN'])
    screen.blit(game.player.image, game.player.rect)
    screen.blit(texte, rectTexte )
    screen.blit(game.comet.image, game.comet.rect)

    pygame.display.flip()


    for event in pygame.event.get():
        if game.comet.lose() or event.type == pygame.QUIT:

            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and game.player.rect.x > -75:
        game.player.move_left()
    if pressed[pygame.K_RIGHT] and game.player.rect.x < 1080 - 190:
        game.player.move_right()

    if pressed[pygame.K_UP] and game.player.rect.y > 0:
        game.player.move_up()

    if pressed[pygame.K_DOWN] and game.player.rect.y < 720 - 280:
        game.player.move_down()
    game.comet.fall()

    if game.comet.rect.y == 720:
        break

    check_collide()


pygame.quit()
