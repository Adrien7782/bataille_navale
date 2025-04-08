class ship():

    def __init__ (self, taille, joueur = 1, color ="blue", val = 1):
        self.taille = taille
        self.joueur = joueur
        self.color = color
        self.val = val

    def afficher():
        print("bateau appartenant au joueur {joueur} de couleur {color} et de taille {taille}")

