import random
import tkinter as tk

#liste de mot prédéfini
liste_de_mot = ["bulle","proteger","edulcorant","panier","pelicule","remorque"]

#nombre d'essai
nb_de_chance = 7

#génération du mot
def generation_mot():
    Mot = random.choice(liste_de_mot)
    return Mot

#mot du joueur
mot_joueur = []

#le joueur joue
def jouer():
    mot=generation_mot()
    while nb_de_chance!=0 :
        lettre = input("Ecrivez une lettre")
        if lettre in mot:
            if lettre not in mot_joueur:
                mot_joueur.append(lettre)
            elif lettre in mot_joueur:
                print("vous avez déjà entrez cette lettre")
    #modifier l'affichage (enlever les astérix)
            continue
        elif lettre not in mot:
            nb_de_chance -=1
    
