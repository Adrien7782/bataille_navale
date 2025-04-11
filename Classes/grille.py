#classe grille pour les deux joueurs 
import sys
import os
import numpy as np
# Ajouter le dossier parent au path d'importation
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from constantes import *
from ship import ship

class grille():

    def __init__ (self, X = XGrille, Y = YGrille, color = "blue"):
        self.X = X
        self.Y = Y
        self.color = color
        self.grille = np.zeros((YGrille, XGrille), dtype = int)

    def afficher(self):
        print(self.grille)
        print("\n")

    def check_coordinates(self, X, Y):
        if X < 0 or X >= self.X or Y < 0 or Y >= self.Y:
            print("Coordonnées impossibles")
            return False
        return True
        
    def place_ship(self, ship, X, Y, orientation):
        if X <= 0 or X > XGrille or Y <= 0 or Y > YGrille:
            print("Vous devez rentrer des coordonnees valides !")
            
            return False

        # Décalage pour l'indexation à partir de 0
        X, Y = X - 1, Y - 1

        # On prépare la liste des coordonnées à vérifier
        coords = [(X, Y)]

        for _ in range(ship.taille - 1):
            match orientation:
                case "N":
                    Y -= 1
                case "S":
                    Y += 1
                case "E":
                    X += 1
                case "O":
                    X -= 1
                case _:
                    print("\nOrientation invalide !")
                    return False
                
            coords.append((X, Y))


            # Vérifie que les coordonnées sont valides
        for x, y in coords:
            if not self.check_coordinates(x, y):
                return False
            if self.grille[y][x] != 0:
                print("Case deja occupee")
                return False

        # Si tout est OK, on place le bateau
        for x, y in coords:
            self.grille[y][x] = ship.val

        self.afficher()
        return True
        
    def reinitialiser_grille(self):
        self.grille = np.zeros((self.Y, self.X), dtype = int)

    def tirer(self, X, Y):
        X, Y = X-1, Y-1
        if self.grille[Y][X] == 0:
            print("RAS !\n")
            self.grille[Y][X] = 11
            return False, 0
        if self.grille[Y][X] == 11:
            print ("Vous avez déja tiré ici !\n")
            return False, 11
        else:
            val = self.grille[Y][X]
            self.grille[Y][X] = 11
            print ("Touché !")
            return True, val

    def check_ship(self, val):

        for i in range (XGrille):
            for j in range (YGrille):
                if self.grille[j][i] == val:
                    return True
        print(f"Vous avez coulé le bateau : {val}")
        return False


# myShip = ship(2, "red", 1)
# magrille = grille(color = "red")
# magrille.afficher()
# magrille.place_ship(myShip, 1,1, "S")
# magrille.afficher()
# magrille.tirer(1,1)
# magrille.afficher()
# magrille.check_ship(myShip)
# magrille.tirer(1,2)
# magrille.check_ship(myShip)