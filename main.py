import Adrien_class

import pygame

import sys
 
# Initialisation de pygame

pygame.init()
 
# Création de la fenêtre

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Mon jeu Pokémon-like")
 
# Horloge pour contrôler les FPS

clock = pygame.time.Clock()

FPS = 60
 
# Boucle principale

running = True

while running:

    # Gestion des événements

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
 
    # --- LOGIQUE DU JEU ICI ---
 
    # --- AFFICHAGE ---

    screen.fill((0, 0, 0))  # fond noir

    pygame.display.flip()
 
    # Limite les FPS

    clock.tick(FPS)
 
# Nettoyage

pygame.quit()

sys.exit()

 