import sys, math, random, pygame

# PARAMETRES DU JEU
WIDTH = 640
HEIGHT = 480
FPS = 60
TITLE = "Mon jeu"

# INITIALISATION DU JEU
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE);
rectScreen = screen.get_rect()

# ... A COMPLETER AVEC LE CODE DE VOS INITIALISATIONS ...

police = pygame.font.Font(None, 72)
texte = police.render("Game Over", True, pygame.Color("#FFFF00"))
rectTexte = texte.get_rect()
rectTexte.center = rectScreen.center

# BOUCLE DE JEU
clock = pygame.time.Clock()
while True:
    time = clock.tick(FPS)

    # GESTION DES EVENEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # ... A COMPLETER AVEC LE CODE DE VOTRE JEU ...

    screen.fill(pygame.Color("#FF0000"))
    screen.blit(texte, rectTexte)

    # MAJ DE L'AFFICHAGE
    pygame.display.update()