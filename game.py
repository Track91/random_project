import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
running = True
image = pygame.image.load('maxime.jpg')
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        screen.blit(image, (0, 0))
        pygame.display.flip()

pygame.quit()
