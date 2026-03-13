import pygame


class Inventaire:
    def __init__(self):
        self.objets = {"test":0}

    def ajouter_objet(self, objet):
        self.objets[objet]+=1
        return self.objets
    
    def retirer_objet(self, objet):
        if self.objets[objet]>0:
            self.objets[objet]-=1
        return self.objets
    
    def afficher_inv(self):
        print(self.objets)



#test class inv avec "test":0
i = Inventaire()
i.afficher_inv()
i.ajouter_objet("test")
i.afficher_inv()
i.retirer_objet("test")
i.afficher_inv()
i.retirer_objet("test")
i.afficher_inv()


class Criadex():
    def __init__(self, affichage):
        self.completion = {}
        self.affichage = affichage
        
    def ajouter(self, criatix):
        self.completion[criatix] = 1

c = Criadex("menu")


class Personnage(pygame.sprite.Sprite):
    def __init__(self, id, nom, prenom, speed, inventaire:Inventaire, credits, criadex:Criadex, image):
        super().__init__()
        self.image = pygame.image.load(".\perso1.png")
        self.rect = self.image.get_rect()

        #la position max du perso en x = 769px et en y = 569px
        self.rect.x = 384
        self.rect.y = 284

        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.inventaire:Inventaire = inventaire
        self.speed = speed
        self.credits = credits
        self.equipe = []
        self.criadex:Criadex = criadex
        self.sprite = image


    def ajouter_equipe(self, criatix):
        if len(self.equipe)<6:
            return self.equipe.append(criatix)

    def retirer_equipe(self, criatix):
        if criatix in self.equipe and len(self.equipe)>0:
            return self.equipe.remove(criatix)
        
    def update(self):
        
        keys = pygame.key.get_pressed()

        # Déplacement horizontal
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Déplacement vertical
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Limites de l'écran (Contraintes)
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 769:
            self.rect.x = 769

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 569:
            self.rect.y = 569

        
    


#test personnage
p = Personnage(0, "Larue", "Kevino", 10000000, i, 0, c, "image")
#print(p, p.nom, p.prenom, p.speed, p.inventaire, p.credits, p.criadex, p.sprite, p.ajouter_equipe("Noham"), p.equipe, p.retirer_equipe("Alex"),p.equipe, p.retirer_equipe("Noham"),p.equipe, p.retirer_equipe("Noham"),p.equipe)
p.ajouter_equipe("Noham")
print(p.equipe)
p.retirer_equipe("Alex")
print(p.equipe)
p.retirer_equipe("Noham")
print(p.equipe)
#fleche de Noham (fleche aberrante !)
for i in range(6):
    p.ajouter_equipe("Noham")
    print(p.equipe)
for i in range(6):
    p.retirer_equipe("Noham")
    print(p.equipe)


class Criatix:
    def __init__(self, id, nom, type, pv, attaque1, attaque2, defense, experience, niveau):
        self.id = id
        self.nom = nom
        self.type = type
        self.pv = pv
        self.attaque1 = attaque1
        self.attaque2 = attaque2
        self.defense = defense
        self.exp = experience
        self.niveau = niveau



a = Criatix(0, "a", "feu", 50, "a", "b", 0.1, 0, 1)
print(a.id, a.nom, a.type, a.pv, a.attaque1, a.attaque2, a.defense, a.exp, a.niveau)

b = Criatix(0, "a", "feu", 50, "a", "b", 0.1, 0, 1)
print(a.id, a.nom, a.type, a.pv, a.attaque1, a.attaque2, a.defense, a.exp, a.niveau)
