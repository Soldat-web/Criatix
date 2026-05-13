from maxime_class import *
from random import randint
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
    while criatix_joueur.pv>0 and criatix_adversaire.pv>0:
        print("pv de votre criatix : ", criatix_joueur.pv,"\npv du criatix adverse : ", criatix_adversaire.pv)
        if tour == 0:
            tour = 1
            attaque = int(input(f"A vous de jouer ! Attaque 1 : {criatix_joueur.attaque1[0]} ({criatix_joueur.attaque1[1]} dégats) ou attaque 2 : {criatix_joueur.attaque2[0]} ({criatix_joueur.attaque2[1]} dégats) ? (écrivez 1 ou 2) : "))
            if attaque == 1:
                criatix_joueur.attaquer(criatix_joueur.attaque1, criatix_adversaire)
            elif attaque == 2:
                criatix_joueur.attaquer(criatix_joueur.attaque2, criatix_adversaire)
                
        elif tour == 1:
            tour = 0
            attaque = randint(1,2)
            if attaque == 1:
                criatix_adversaire.attaquer(criatix_adversaire.attaque1, criatix_joueur)
            elif attaque == 2:
                criatix_adversaire.attaquer(criatix_adversaire.attaque2, criatix_joueur)
    
combat(pyronix, aquaryx)