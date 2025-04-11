#toutes les fonctions utilitaires du jeu 


from Classes.grille import grille
from Classes.ship import ship
from jeu_sans_reseau_sans_ihm import *
from Classes.joueur import joueur 


def victoire(joueur):
    for i in range (XGrille):
        for j in range (YGrille):
            if joueur.grille[j][i] != 11 or joueur.grille[j][i] != 0:
                return False
    print(f"{joueur.nom} Vous avez gagné !")
    return True

def tour(joueur):

    print(f"Quels sont vos ordres {joueur.nom} !\n")

    T = False
    while (not T):
        try:
            X = int(input("Où voulez-vous tirer ? (X)"))
            Y = int(input("Où voulez-vous tirer ? (Y)"))
        except X == None and Y == None :
            print("Vous devez entrer des coordonnées valides !")

        if (joueur.grille.check_coordinates(X, Y)): T = True
    

    touche, val = joueur.grille.tirer(X,Y)
    
    if touche == True: 
        joueur.grille.check_ship(val)
            

    











