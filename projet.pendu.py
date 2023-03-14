import random
import tkinter as tk

def aide():
    fenetre = tk.Toplevel(root)
    fenetre.title("Aide")
    text = tk.Label(fenetre, text='Les règles du jeux')
    text.grid()
    fenetre.mainloop()
root = tk.Tk()
root.title("Pendu")

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
 
#dessin et boutton aide 
dessin=tk.Canvas(root, bg="ivory", width=500, height=500)
button=tk.Button(root, text="Aide",command=aide)
dessin.pack(side="left", padx=20, pady=20)
button.pack(side='bottom')

#Etapes pendu 
#1
#dessin.create_line(50,400,450,400,fill='black', width=5)
#dessin.create_line(100,400,100,100,fill='black', width=5)
#dessin.create_line(100,150,150,100,fill='black', width=5)
#dessin.create_line(98,100,300,100,fill='black', width=5)
#dessin.create_line(300,100,300,150,fill='black', width=5)
#2
#dessin.create_oval(270,150,330,210, fill='red', width=5)

#3
#dessin.create_line(300,210,300,300, fill='black', width=5)
#4
#dessin.create_line(300,230,260,220, fill='black', width=5)

#5
#dessin.create_line(300,230,340,220, fill='black', width=5)

#6
#dessin.create_line(300,300,260,320, fill='black', width=5)

#7
#dessin.create_line(300,300,340,320, fill='black', width=5)

#8
#dessin.create_oval(50,50,450,450, fill='red', width=5)
#dessin.create_oval(100,150,200,250, fill='black', width=5)
#dessin.create_oval(300,150,400,250, fill='black', width=5)
#dessin.create_line(150,380,250,280, fill='black' ,width=30, capstyle='round')
#dessin.create_line(250,280,350,380, fill='black', width=30, capstyle='round')

root.mainloop()
    
