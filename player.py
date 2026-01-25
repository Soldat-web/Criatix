import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("C:/Users/adrie/Desktop/projet Criatix/Criatix/personnage.png")
        self.rect = self.image.get_rect()

        #la position max du perso en x = 769px et en y = 569px
        self.rect.x = 384
        self.rect.y = 284