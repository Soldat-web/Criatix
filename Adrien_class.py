import pygame



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




