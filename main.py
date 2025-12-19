import Adrien_class

import pygame

import sys
 
# Initialisation de pygame

pygame.init()
 
# Création de la fenêtre
taille_case = 32
x = 00
y = 800

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

fullscreen = False  # Mettre False pour fenêtre normale

if fullscreen:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((800, 600))

screen = pygame.display.set_mode((x, y))

pygame.display.set_caption("CRIATIX")



 
# Horloge pour contrôler les FPS
clock = pygame.time.Clock()
FPS = 60
 
# Boucle principale

while True:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    # --- AFFICHAGE ---

    screen.fill((0, 0, 0))  # fond noir

    pygame.display.flip()
 
    # Limite les FPS

    clock.tick(FPS)

# Nettoyage

pygame.quit()

sys.exit()

 