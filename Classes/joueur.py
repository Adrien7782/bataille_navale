
import sys
import os
import numpy as np
# Ajouter le dossier parent au path d'importation
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from constantes import *
from Classes.ship import ship
from grille import grille

class joueur():

    def __init__ (self, nom, myColor):
        self.nom = nom
        self.color = myColor
        self.grille = grille(color = self.color)

    def afficher_joueur(self):
        print(f"nom du joueur: {self.nom}, couleur du joueur: {self.color}")
    
    def afficher_grille_joueur(self):
        print(f"\n {self.grille} \n")

    # def message_fin_de_partie():
    #     message = str(input("Si vous le souhaitez vous pouvez communiquer avec votre adversaire : "))

    #     print(message) #temporaire utile pour le jeu en réseau local

    def initialisation_grille(self, myColor):

        myGrille = self.grille

        ship1 = ship(2, color = myColor, val = 1)
        ship2 = ship(3, color = myColor, val = 2)
        ship3 = ship(3, color = myColor, val = 3)
        ship4 = ship(4, color = myColor, val = 4)
        ship5 = ship(5, color = myColor, val = 5)

        ships = {ship1 :False, ship2: False, ship3: False, ship4: False, ship5: False}
        print(f"{self.nom} il vous reste a placer :\n")
        
        T2 = True
        while (T2):
            i = 1
            for key in ships:
                if ships[key] == False : print(f"- {i} bateau de taille : {key.taille} ")
                i+=1
        
            try:
                numero = int(input(f"\n{self.nom} - Quel bateau voulez-vous placer ? "))
                if numero < 1 or numero > 5:
                    print("Vous devez choisir parmi les 5 bateaux")
                    continue
            except ValueError:
                print("Entrée invalide !")
                continue

            try:
                X = int(input(f"\n{self.nom} - Rentrez les coordonnées X de votre premier bateau : "))
                Y = int(input(f"\n{self.nom}  Rentrez les coordonnées Y de votre premier bateau : "))
                orientation = str(input("\nJ2 - Rentrez l'orientation désiré : (N,S,E,O)"))
            except:
                print(f"{self.nom}  Vous devez rentrez des valeurs !")

            try:
                match numero:
                    case 1:
                        myGrille.place_ship(ship1, X, Y, orientation)
                        ships[ship1] = True
                    case 2:
                        myGrille.place_ship(ship2,X,Y, orientation)
                        ships[ship2] = True
                    case 3:
                        myGrille.place_ship(ship3,X,Y, orientation)
                        ships[ship3] = True
                    case 4:
                        myGrille.place_ship(ship4,X,Y, orientation)
                        ships[ship4] = True
                    case 5:
                        myGrille.place_ship(ship5,X,Y, orientation)
                        ships[ship5] = True

                # print(f"{self.nom} Vous avez placé votre bateau {numero} \n")
                # myGrille.afficher()
            except:
                print(f"{self.nom}  Erreur lors du placement du bateau :")

            if all(ships.values()):
                T2 = False


        print(f"{self.nom}, vous avez placé tous vos bateaux\n")

# joueur1 = joueur ("Adrien", "blue")
# joueur1.afficher_joueur()
# joueur1.afficher_grille_joueur()
# joueur1.initialisation_grille("blue")


# grilleTest = joueur1.grille
# grilleTest.afficher()
# grilleTest.tirer(3,3)
# grilleTest.afficher()

