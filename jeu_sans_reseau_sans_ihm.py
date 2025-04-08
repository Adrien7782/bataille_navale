#logique du jeu 
from grille import *
from ship import *
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def initialisation_jeu():
    
    grille1 = grille(joueur = 1, color = "blue")
    grille2 = grille(joueur = 2, color = "red")

    J1_ship1 = ship(2, joueur = 1, color = "blue", val = 1)
    J1_ship2 = ship(3, joueur = 1, color = "blue", val = 2)
    J1_ship3 = ship(3, joueur = 1, color = "blue", val = 3)
    J1_ship4 = ship(4, joueur = 1, color = "blue", val = 4)
    J1_ship5 = ship(5, joueur = 1, color = "blue", val = 5)

    J2_ship1 = ship(2, 2, color = "red")
    J2_ship2 = ship(3, 2,color = "red")
    J2_ship3 = ship(3, 2,color = "red")
    J2_ship4 = ship(4, 2,color = "red")
    J2_ship5 = ship(5, 2,color = "red")

    J1ships = {J1_ship1 :False, J1_ship2: False, J1_ship3: False, J1_ship4: False, J1_ship5: False}
    J2ships = {J2_ship1 :False, J2_ship2: False, J2_ship3: False, J2_ship4: False, J2_ship5: False}


    print("\nPour commencer la partie vous devez placer tous vos bateau !")
    print("Joueur 1 il vous reste a placer :\n")

    T1 = True

    while (T1):
        i = 1
        for key in J1ships:
            if J1ships[key] == False : print(f"- {i} bateau de taille : {key.taille} ") 
            i+=1
    
        try:
            numero = int(input("\nJ1 - Quel bateau voulez-vous placer ? "))
            if numero < 1 or numero > 5:
                print("Vous devez choisir parmi les 5 bateaux")
                continue
        except ValueError:
            print("Entrée invalide !")
            continue

        try:
            X = int(input("\nJ1 - Rentrez les coordonnées X de votre premier bateau : "))
            Y = int(input("\nJ1 - Rentrez les coordonnées Y de votre premier bateau : "))
            orientation = str(input("\nJ1 - Rentrez l'orientation désiré : (N,S,E,O)"))
        except:
            print("Vous devez  rentrez des valeurs !")

        try:
            match numero:
                case 1:
                    grille1.place_ship(J1_ship1,X,Y, orientation)
                    J1ships[J1_ship1] = True
                case 2:
                    grille1.place_ship(J1_ship2,X,Y, orientation)
                    J1ships[J1_ship2] = True
                case 3:
                    grille1.place_ship(J1_ship3,X,Y, orientation)
                    J1ships[J1_ship3] = True
                case 4:
                    grille1.place_ship(J1_ship4,X,Y, orientation)
                    J1ships[J1_ship4] = True
                case 5:
                    grille1.place_ship(J1_ship5,X,Y, orientation)
                    J1ships[J1_ship5] = True
            
            
            grille1.afficher()
            print(f"J1 - Vous avez placé votre bateau {numero} \n")
        except:
            print("J1 - Erreur lors du placement du bateau :")

        if all(J1ships.values()):
            T1 = False


    clear_console()

    print("Joueur 1, vous avez placé tous vos bateaux\n")

    print("Joueur 2 il vous reste a placer :\n")
    
    
    T2 = True
    while (T2):
        i = 1
        for key in J2ships:
            if J2ships[key] == False : print(f"- bateau de taille : {key.taille} ") 
    
        try:
            numero = int(input("\nJ2 - Quel bateau voulez-vous placer ? "))
            if numero < 1 or numero > 5:
                print("Vous devez choisir parmi les 5 bateaux")
                continue
        except ValueError:
            print("Entrée invalide !")
            continue

        try:
            X = int(input("\nJ2 - Rentrez les coordonnées X de votre premier bateau : "))
            Y = int(input("\nJ2 - Rentrez les coordonnées Y de votre premier bateau : "))
            orientation = str(input("\nJ2 - Rentrez l'orientation désiré : (N,S,E,O)"))
        except:
            print("J2 - Vous devez rentrez des valeurs !")

        try:
            match numero:
                case 1:
                    grille2.place_ship(J2_ship1,X,Y, orientation)
                    J2ships[J2_ship1] = True
                case 2:
                    grille2.place_ship(J2_ship2,X,Y, orientation)
                    J2ships[J2_ship2] = True
                case 3:
                    grille2.place_ship(J2_ship3,X,Y, orientation)
                    J2ships[J2_ship3] = True
                case 4:
                    grille2.place_ship(J2_ship4,X,Y, orientation)
                    J2ships[J2_ship4] = True
                case 5:
                    grille2.place_ship(J2_ship5,X,Y, orientation)
                    J2ships[J2_ship5] = True
            print(f"J2 - Vous avez placé votre bateau {numero} \n")
            grille2.afficher()
        except:
            print("J2 - Erreur lors du placement du bateau :")

        if all(J1ships.values()):
            T2 = False


    print("Joueur 2, vous avez placé tous vos bateaux\n")


    

initialisation_jeu()
        