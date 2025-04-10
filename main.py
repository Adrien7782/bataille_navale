from Classes.grille import *
from Classes.joueur import joueur
from utils import *

#Point d'entrée du jeu 

def main():

    joueur1 = joueur("Adrien")
    joueur2 = joueur("Victor")

    joueur1.initialisation_grille(joueur1, "blue")

    joueur2.initialisation_grille(joueur2, "red")

    Fin_partie = False

  
    tour(joueur1)

        

main()