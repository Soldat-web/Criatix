
from Adrien_class import Game




import pygame
import sys
import pytmx
from player import Player

# Initialisation de pygame
pygame.init()
if __name__ == "__main__":
    jeu = Game()
    jeu.run()















#import image map
tmx_map = pytmx.load_pygame("./criatixmap.tmx")


def draw_map(screen, tmx_data):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, surface in layer.tiles():
                screen.blit(surface, (x * taille_case, y * taille_case))




# création Personnage
joueur = Player()


#systeme de déplacement
x,y = 400, 300 
speed = 1
size = 40
#dict de touches
controls = {
     "left" : pygame.K_q,
     "right" : pygame.K_d,
     "haut" : pygame.K_z,   
     "bas" : pygame.K_s
}


# Horloge pour contrôler les FPS
clock = pygame.time.Clock()
FPS = 60





# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
#pour les déplacements (z,q,s,d)
    if keys[controls["left"]]:  # gauche
            joueur.rect.x -= speed
    if keys[controls["right"]]:  # droite
            joueur.rect.x += speed
    if keys[controls["haut"]]:  # haut
            joueur.rect.y -= speed
    if keys[controls["bas"]]:  # bas
            joueur.rect.y += speed


    # --- AFFICHAGE ---
    screen.fill((0, 0, 0))
    draw_map(screen, map)
    screen.blit(joueur.image, joueur.rect)  # joueur ici
    pygame.display.flip()


