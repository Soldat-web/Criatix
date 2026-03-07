class Inventaire:
    def __init__(self):
        self.objets = {}

    def ajouter_objet(self, objet):
        self.objets[objet]+=1
        return self.objets
    def retirer_objet(self, objet):
        self.objets[objet]-=1
        return self.objets
class Personnage:
    def __init__(self, nom, prenom, inventaire:Inventaire):
        self.nom = nom
        self.prenom = prenom
        self.inventaire:Inventaire = inventaire
    
