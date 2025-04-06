from grille import *
#Point d'entrée du jeu 

def main():
    magrille = grille(9,7, name = 1)
    magrille.afficher()
    magrille.place_ship(3, 5, 4, "N")
    magrille.afficher()
    magrille.place_ship(2, 4,4, "E")
    magrille.afficher()

main()