import pygame
import random


screen_x = 1080
screen_y = 720


class Game1(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.player = Player()
        self.comet = Comet()
        self.sunny = Sunny()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.max_heath = 10
        self.velocity = 4
        self.image = pygame.image.load('assets/maxime2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = screen_y- 280

        self.image = pygame.transform.scale(self.image, (190, 280))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity


class Sunny(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sunny.png")
        self.image = pygame.transform.scale(self.image, (120, 150))
        self.rect = self.image.get_rect()
        self.velocity = 4

    def lose(self):
        print('')

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y == screen_y:
            self.remove()
            self.lose()

    def reset_fall(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, screen_x - 200)
        self.velocity = 4



class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/bite.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.velocity = 4

    def lose(self):
        print('')

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y == screen_y:
            self.remove()
            self.lose()

    def reset_fall(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, screen_x - 200)
        self.velocity = random.randint(2, 3)


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
screen = pygame.display.set_mode((screen_x, screen_y))
score = 0


def check_bite_collide():
    global score
    rect1 = game.comet.rect
    rect2 = game.player.rect

    collide = rect1.colliderect(rect2)
    if collide:
        game.comet.reset_fall()
        score += 1


def check_sunny_collide():
    rect1 = game.sunny.rect
    rect2 = game.player.rect
    collide = rect1.colliderect(rect2)

    if collide:
        game.sunny.reset_fall()

        
    if game.sunny.rect.y == screen_y:
        game.sunny.reset_fall()



game = Game1()

rectScreen = screen.get_rect()
running = True

while running:
    police = pygame.font.Font(None, 72)
    texte = police.render("score : {}".format(str(score)), True, pygame.Color("#FFFF00"))
    rectTexte = texte.get_rect()
    rectTexte.center = rectScreen.center
    screen.fill(colors['CYAN'])
    screen.blit(texte, rectTexte)
    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.comet.image, game.comet.rect)
    screen.blit(game.sunny.image, game.sunny.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if game.comet.lose() or event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and game.player.rect.x > -75:
        game.player.move_left()
    if pressed[pygame.K_RIGHT] and game.player.rect.x < screen_x - 190:
        game.player.move_right()

    if pressed[pygame.K_UP] and game.player.rect.y > 0:
        game.player.move_up()

    if pressed[pygame.K_DOWN] and game.player.rect.y < screen_y - 280:
        game.player.move_down()
    game.comet.fall()
    game.sunny.fall()

    if game.comet.rect.y == screen_y:
        break

    check_bite_collide()
    check_sunny_collide()

pygame.quit()
