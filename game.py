import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
running = True
image = pygame.image.load('maxime.jpg')
image = pygame.transform.scale(image, (250, 400))
x, y = 0, 0
clock = pygame.time.Clock()

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and x < 1920 - 250:
                x -= 1
        if pressed[pygame.K_RIGHT] and x < 1920 - 250:
                x += 1

        if pressed[pygame.K_UP] and y < + 1080 +400:
                y -= 1

        if pressed[pygame.K_DOWN] and y < 1080+ 400:
                y += 1
        if x > 1920:
                print('oui')
        screen.fill((0, 0, 0))
        screen.blit(image, (x, y))
        pygame.display.flip()
        clock.tick(800)

pygame.quit()
