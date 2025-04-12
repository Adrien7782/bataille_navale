from Classes.grille import *
from Classes.joueur import *
from Classes.ship import *
from utils import *

#Point d'entrée du jeu 

def main():

    joueur1 = joueur("Adrien", "blue")
    joueur2 = joueur("Victor", "red")

    joueur1.initialisation_grille()

    joueur2.initialisation_grille()
  


    nb_tour = 0
    fin_de_partie = False

    while (fin_de_partie == False):
        if nb_tour % 2 == 0:
            joueur_adverse = joueur2

            tour(joueur1, joueur_adverse)
            if check_bateaux(joueur_adverse) == True:
                fin_de_partie = True

        else: 
            joueur_adverse = joueur1

            tour(joueur2, joueur_adverse)
            if check_bateaux(joueur_adverse) == True:
                fin_de_partie = True

        nb_tour +=1
        print(fin_de_partie)

        
        

        

main()