import pygame


class Inventaire:
    def __init__(self):
        # bibliothèque d'objets avec leur quantité
        self.objets = {"test":0}

    # ajout d'un objet à l'inventaire
    def ajouter_objet(self, objet):
        self.objets[objet]+=1
        return self.objets
    
    # retrait d'un objet de l'inventaire
    def retirer_objet(self, objet):
        if self.objets[objet]>0:
            self.objets[objet]-=1
        return self.objets
    
    # affichage de l'inventaire
    def afficher_inv(self):
        print(self.objets)



# test class inv avec "test":0
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
        # bibliothèque de criatix avec leur id
        self.completion = {}
        # affichage du criadex (menu, combat, etc)
        self.affichage = affichage
    
    # ajout d'un criatix au criadex
    def ajouter(self, criatix):
        self.completion[criatix] = 1

c = Criadex("menu")

#decoupage d'une image en plusieurs pour les animations
def load_spritesheet(filename, num_lignes, num_cols):
    # Chargement de l'image et recupération de ses dimensions
    sheet = pygame.image.load(filename).convert_alpha()
    largeur, hauteur = sheet.get_size()
    
    # Taille d'une sous-image
    frame_l = largeur // num_cols  # Largeur totale / 3 colonnes
    frame_h = hauteur // num_lignes # Hauteur totale / 4 lignes
    
    sprites = []
    
    # On parcourt d'abord les lignes, puis les colonnes
    for ligne in range(num_lignes):
        line_frames = []
        for col in range(num_cols):
            # On définit un rectangle pour extraire la sous-image correspondante
            rect = pygame.Rect(col * frame_l, ligne * frame_h, frame_l, frame_h)
            # On extrait la sous-image et on la redimensionne à 32x24
            sprite = sheet.subsurface(rect)
            sprite = pygame.transform.scale(sprite, (32, 24))
            line_frames.append(sprite)
        sprites.append(line_frames) # On stocke par lignes pour plus de clarté
            
    return sprites


class Personnage(pygame.sprite.Sprite):
    def __init__(self, id, nom, prenom, speed, inventaire:Inventaire, credits, criadex:Criadex):
        super().__init__()
        
        self.animations = load_spritesheet("character\Characters_free\main_character_1.png", 4, 3)

        self.image = self.animations[0][0]
        self.image = pygame.transform.scale(self.image, (32, 24))
        #la position max du perso en x = 769px et en y = 569px
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.i_anim = 0
        self.n_dir = 0 # 0 : bas, 1 : gauche, 2 : droite, 3 : haut
        self.a_dir = 0
        self.nb_frame = 0
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.inventaire:Inventaire = inventaire
        self.speed = speed
        self.credits = credits
        self.equipe = []
        self.criadex:Criadex = criadex


    def ajouter_equipe(self, criatix):
        if len(self.equipe)<6:
            return self.equipe.append(criatix)

    def retirer_equipe(self, criatix):
        if criatix in self.equipe and len(self.equipe)>0:
            return self.equipe.remove(criatix)
        
    def update(self):
        
        keys = pygame.key.get_pressed()
        
        # Si aucune touche de déplacement n'est pressée, réinitialiser l'animation
        if not keys[pygame.K_q] and not keys[pygame.K_LEFT] and not keys[pygame.K_d] and not keys[pygame.K_RIGHT] and not keys[pygame.K_z] and not keys[pygame.K_UP] and not keys[pygame.K_s] and not keys[pygame.K_DOWN]:
            self.i_anim = 0
        # Déterminer la direction du personnage en fonction des touches pressées
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.n_dir = 1
            self.rect.x -= self.speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.n_dir = 2
            self.rect.x += self.speed
        elif keys[pygame.K_z] or keys[pygame.K_UP]:
            self.n_dir = 3
            self.rect.y -= self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.n_dir = 0
            self.rect.y += self.speed
        # update de l'animation seulement si la direction actuelle est la même que la direction précédente
        if self.n_dir == self.a_dir:
            self.a_dir = self.n_dir
            if self.i_anim < 3:
                self.i_anim += 1
            elif self.i_anim == 3:
                self.i_anim = 0

        self.image = self.animations[self.n_dir][self.i_anim]

        
        # Limites de l'écran (Contraintes)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1366:
            self.rect.right = 1366

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 768:
            self.rect.bottom = 768

        pygame.display.flip() #voir le rendu actuel
        self.image = self.image.convert_alpha()
                
    


"""#test personnage
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

"""
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



"""a = Criatix(0, "a", "feu", 50, "a", "b", 0.1, 0, 1)
print(a.id, a.nom, a.type, a.pv, a.attaque1, a.attaque2, a.defense, a.exp, a.niveau)

b = Criatix(0, "a", "feu", 50, "a", "b", 0.1, 0, 1)
print(a.id, a.nom, a.type, a.pv, a.attaque1, a.attaque2, a.defense, a.exp, a.niveau)

"""