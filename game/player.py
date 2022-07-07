import pygame

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

