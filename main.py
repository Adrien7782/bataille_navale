from grille import *

#Point d'entrée du jeu 

def main():
    bateau1 = ship(5,val = 2)
    bateau2 = ship(3)

    magrille = grille(9,7)

    magrille.place_ship(bateau1, 3,3,"S")
    magrille.afficher()
    magrille.place_ship(bateau2, 4,4, "E")
    magrille.afficher()

main()