#classe grille pour les deux joueurs 
import numpy as np
from constantes import *
from ship import ship

class grille():

    def __init__ (self, X = XGrille, Y = YGrille, joueur = 1, color = "blue"):
        self.X = X
        self.Y = Y
        self.color = color
        self.grille = np.zeros((self.Y, self.X), dtype=int)
        self.joueur = joueur

    def afficher(self):
        print(f'\nGrille du Joueur {self.joueur} :\n')
        print(self.grille)
        print("\n")

    def check_coordinates(self, X, Y):
        if X < 0 or X >= self.X or Y < 0 or Y >= self.Y:
            print("Vous ne pouvez pas placer votre bateau ici, il depasse de la grille !")
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

        return True
        
    def reinitialiser_grille(self):
        self.grille = np.zeros((self.Y, self.X), dtype = int)

            


        





