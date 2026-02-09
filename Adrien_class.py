import pygame
import pytmx
import pyscroll
import os


class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()

    def run(self):
        while self.running:
            pass


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1200, 720))
        pygame.display.set_caption("CRIATIX")
        self.clock = pygame.time.Clock()
        self.frame = 60

    def update(self):
        pygame.display.flip()
        pygame.display.update()
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

    def switch_map(self, name: str):
        base_path = os.path.dirname(__file__)
        path = os.path.join(base_path, "assets", "maps", f"{name}.tmx")

        self.tmx_data = pytmx.util_pygame.load_pygame(path)
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)











class Foret:
    pass
class Arbre(Foret):
    pass
class Chemin(Foret):
    pass


class Arene:
    pass



class Defis:
    pass


class Coffre:
    pass
class Criatix:
    pass






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




