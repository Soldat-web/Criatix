from maxime_class import *

# Criatix feu
pyronix = Criatix(
    id=1,
    nom="Pyronix",
    type="Feu",
    pv=85,
    attaque1=["Flamme Vive", 15],
    attaque2=["Explosion Solaire", 20],
    defense=0.2,
    experience=0,
    niveau=1
)

# Criatix eau
aquaryx = Criatix(
    id=2,
    nom="Aquaryx",
    type="Eau",
    pv=100,
    attaque1=["Jet Marin", 15],
    attaque2=["Vague Gelée", 20],
    defense=0.18,
    experience=0,
    niveau=1
)

def combat(criatix_joueur:Criatix, criatix_adversaire:Criatix):
    tour = 0
    while criatix_joueur.pv>0 or criatix_adversaire.pv>0:
        print("pv de votre criatix : ", criatix_joueur.pv, "pv du criatix adverse : ", criatix_adversaire)
        if tour == 0:
            tour = 1
            attaque = input("A vous de jouer ! Attaque 1", criatix_joueur.attaque1, "ou 2", criatix_joueur.attaque2, "? (écrivez 1 ou 2) : ")
            if attaque == 1:
                criatix_joueur.attaquer(criatix_joueur.attaque1, criatix_adversaire)
            elif attaque == 2:
                criatix_joueur.attaquer(criatix_joueur.attaque2, criatix_adversaire)
                
        elif tour == 1:
            tour = 0
            attaque = input("A vous de jouer ! Attaque 1", criatix_adversaire.attaque1, "ou 2", criatix_adversaire.attaque2, "? (écrivez 1 ou 2) : ")
            if attaque == 1:
                criatix_adversaire.attaquer(criatix_adversaire.attaque1, criatix_joueur)
            elif attaque == 2:
                criatix_adversaire.attaquer(criatix_adversaire.attaque2, criatix_joueur)
                
combat(pyronix, aquaryx)