from Adrien_class import Game
import pygame
import sys
import pytmx
from maxime_class import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("musique_pas_du_tout_copyright.mp3")
pygame.mixer.music.play(-1)

if __name__ == "__main__":
    jeu = Game()
    jeu.run()
