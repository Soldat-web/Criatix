# import Adrien_class
import pygame
import sys
import pytmx




#import de la map


# Initialisation de pygame
pygame.init()
# Création de la fenêtre lal
taille_case = 32

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
fullscreen = False  # Mettre False pour fenêtre normale
if fullscreen:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((800, 600))

map = pytmx.load_pygame("C:/Users/adrie/Desktop/projet Criatix/Criatix/criatixmap.tmx")

pygame.display.set_caption("CRIATIX")


def draw_map(screen, tmx_data):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, surface in layer.tiles():
                screen.blit(surface, (x * taille_case, y * taille_case))



# Horloge pour contrôler les FPS
clock = pygame.time.Clock()
FPS = 60

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # --- AFFICHAGE ---
    screen.fill((0, 0, 0))  # fond noir
    draw_map(screen,map)



    pygame.display.flip()
    # Limite les FPS
    clock.tick(FPS)

 
