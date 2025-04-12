#toutes les fonctions utilitaires du jeu 


from Classes.grille import grille
from Classes.ship import ship
from jeu_sans_reseau_sans_ihm import *
from Classes.joueur import joueur 


def check_bateaux(joueur):
    count = 0
    for ligne in joueur.grille.grille:
        for case in ligne:
            if case in [1,2,3,4,5]:
                return False
    print(f"{joueur.nom} Vous avez gagné !")
    return True

def tour(joueur, joueur_adverse):

    joueur_adverse.grille.afficher()

    print(f"Quels sont vos ordres {joueur.nom} !\n")
    T = False
    while (not T):
        try:
            X = int(input("Où voulez-vous tirer (X) ? :"))
            Y = int(input("Où voulez-vous tirer (Y) ? :"))
        except X == None and Y == None :
            print("Vous devez entrer des coordonnées valides !")

        # if (joueur.grille.check_coordinates(X, Y)):
        T = True
    

    touche, val = joueur_adverse.grille.tirer(X,Y)
    
    if touche == True: 
        joueur_adverse.grille.check_ship(val)
    
    joueur_adverse.grille.afficher()
    return True
    
        

 




