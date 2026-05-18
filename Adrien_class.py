import pygame
import pytmx
import pyscroll
import os
from maxime_class import *
from random import *
from combat import *

banque_criatix = {
#criatix plante
"florix" : Criatix(
    id=0,
    nom="Florix",
    type="Plante",
    pv=95,
    attaque1=["Fleur de Vie", 15],
    attaque2=["Tempête Végétale", 20],
    defense=1,
    experience=0,
    niveau=1
),
# Criatix feu
"pyronix" : Criatix(
    id=1,
    nom="Pyronix",
    type="Feu",
    pv=85,
    attaque1=["Flamme Vive", 15],
    attaque2=["Explosion Solaire", 20],
    defense=1,
    experience=0,
    niveau=1
),
# Criatix eau
"aquaryx" : Criatix(
    id=2,
    nom="Aquaryx",
    type="Eau",
    pv=100,
    attaque1=["Jet Marin", 15],
    attaque2=["Vague Gelée", 20],
    defense=1,
    experience=0,
    niveau=1
)}


class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Carte(self.screen)
        self.player_animations = load_spritesheet("character/Characters_free/main_character_1.png", 4, 3)
        print(self.player_animations[0][0].get_size())
        self.char = Personnage(0, "Larue", "Kevino", 1, 0, c, self.player_animations)
        print(self.char.image.get_size())
        for criatix in banque_criatix.values():
            self.char.ajouter_equipe(criatix)
            
    def run(self):
        self.map.group.add(self.char)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.map.group.draw(self.screen.get_display())
            self.char.update(self.map.collisions_rects)
            self.map.group.center(self.char.rect.center)
            self.screen.update()
            combat = randint(1, 5000)
            if combat == 942:
                criatix_joueur = self.char.equipe[0]
                criatix_adversaire = [criatix for criatix in banque_criatix.values() if criatix != criatix_joueur]
                criatix_adversaire = criatix_adversaire[randint(0, len(criatix_adversaire) - 1)]
                print(f'criatix_joueur: {criatix_joueur}, criatix_adversaire: {criatix_adversaire}')
                Combat(criatix_joueur, criatix_adversaire)

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
        self.collisions_rects = []

        self.switch_map("map0")

    def switch_map(self, name: str):
        base_path = os.path.dirname(__file__)
        path = os.path.join(base_path, "assets", "map", f"{name}.tmx")

        self.tmx_data = pytmx.util_pygame.load_pygame(path)

        self.collisions_rects = []
        for obj in self.tmx_data.get_layer_by_name("collisions"):
            self.collisions_rects.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.size(), zoom= 5.0)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)


    def update(self):
        self.group.draw(self.screen.get_display())







