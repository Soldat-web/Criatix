from maxime_class import *
from random import randint
import time 

def Combat(criatix_joueur:Criatix, criatix_adversaire:Criatix):
    tour = 0
    while criatix_joueur.pv>0 and criatix_adversaire.pv>0:
        time.sleep(1)
        print(f"\nPV de votre criatix : {criatix_joueur.pv}\nPV du criatix adverse : {criatix_adversaire.pv}")
        time.sleep(1)
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
"""pret = "non"
while pret != "oui":
    criatix_joueur = input("Choisissez votre criatix : Florix (Plante), Pyronix (Feu) ou Aquaryx (Eau) ? (écrivez le nom du criatix) : ")
    if criatix_joueur == "Florix":
        criatix_joueur = florix
    elif criatix_joueur == "Pyronix":
        criatix_joueur = pyronix
    elif criatix_joueur == "Aquaryx":
        criatix_joueur = aquaryx
    criatix_adversaire = [florix, pyronix, aquaryx]
    criatix_adversaire.remove(criatix_joueur)
    criatix_adversaire = criatix_adversaire[randint(0,1)]
    pret = input(f"Vous avez choisi {criatix_joueur.nom} ! Votre adversaire sera {criatix_adversaire.nom} ! Cela vous convient il ? (écrivez oui ou non) : ")
combat(criatix_joueur, criatix_adversaire)
    """