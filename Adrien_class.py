import pygame
import pytmx
import pyscroll
import os
from maxime_class import *

class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Carte(self.screen)
        self.char = Personnage(0, "Larue", "Kevino", 1, i, 0, c)
        print(self.char.image.get_size())
        self.map.zoom_sur_personnage(self.char)
        
    def run(self):
        self.map.group.add(self.char)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
            
            # Centre automatiquement la caméra sur le personnage à chaque frame
            self.map.group.center(self.char.rect.center)
            
            self.map.group.draw(self.screen.get_display())
            self.char.update()
            self.screen.update()
            
        

class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1366, 768))#fenetre en 1280 par 720
        pygame.display.set_caption("CRIATIX") #nom de la fenetre criatix
        self.clock = pygame.time.Clock() #controle de la vitesse boucle jeu
        self.frame = 60 #le jeu tourne en 60 fps

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.frame)
        self.display.fill((0, 0, 0))

    def size(self):
       return self.display.get_size()

    def get_display(self):
        return self.display

class Carte:
    def __init__(self, screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        self.switch_map("map0")
        
    def switch_map(self, name: str):
        base_path = os.path.dirname(__file__)
        path = os.path.join(base_path, "assets", "map", f"{name}.tmx")

        self.tmx_data = pytmx.util_pygame.load_pygame(path)

        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

        
    def update(self):
        self.group.draw(self.screen.get_display())
        
    def zoom_sur_personnage(self, personnage):
        self.group.center(personnage.rect.center)
        self.map_layer.zoom = 4.0





class Batiments:
    def __init__(self):
        self.porte = 0

    def porte_ouverte(self):

        if self.porte > 1:
            self.porte = 1
        elif self.porte < 0:
            self.porte = 0

        if self.porte_ouverte == 0:
            print("Porte fermée")
        else:
            print("porte ouverte")

    def porte_ouvrir(self):
        self.porte = 1

    def porte_fermer(self):
        self.porte = 0

class Maison(Batiments):
    pass
class Hopital(Batiments):
    pass
class Magasins(Batiments):
    pass




