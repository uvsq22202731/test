#interface graphique

import tkinter as tk
import PIL as pil
from PIL import Image
import random
import tkinter.font as font
from tkinter import messagebox

#fonctions

def menu():
    def etat_quit():
        fenetre.destroy()
        return etat_play.set(1)
    
    fenetre= tk.Tk()
    fenetre.title("menu blackjack")
    background= tk.PhotoImage(file="menu.png")
    background_label = tk.Label(fenetre, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    fenetre.geometry('1280x737')
    etat_play = tk.BooleanVar(fenetre) # creation variable booleen 
    etat_play.set(0) # intialisation de la variable a False
    bouton_quitter = tk.Button(fenetre, text="QUITTER", command=fenetre.destroy, width=20,height=2,bg='white') # ferme la fenetre, fin du jeu
    bouton_quitter.place(x=680,y=300)
    bouton_play = tk.Button(fenetre, text="JOUER", command=lambda:etat_quit(), width=20, height=2,bg='white') #si le boutton jouer est clické, on ferme le menu et retourne la valeur True
    bouton_play.place(x=400,y=300)
    myFont = font.Font(family='Comic Sans MS', size=15, weight='bold')
    bouton_quitter['font'] = myFont
    bouton_play['font'] = myFont
    fenetre.mainloop()
    return etat_play.get() # retourne True si JOUER est clické sinon reste False

def quitter():
    fenetre.destroy()

def remake():
    pass

def stand():
    pass


def affichage_carte1(img_carte):
    label = tk.Label(fenetre, image = img_carte)
    label.place(x=597,y=483)

def affichage_carte2(img_carte):
    label = tk.Label(fenetre, image = img_carte)
    label.place(x=618,y=505)

def affichage_carte_hit(img_carte):
    label = tk.Label(fenetre, image = img_carte)
    label.place(x=640,y=540)

def charger_image(carte):
    global img
    img = tk.PhotoImage(file="cartes/"+str(carte)+".png")
    return img

def hit(nom_carte):
    affichage_carte_hit(charger_image(str(nom_carte)))


fenetre_menu = menu()

if fenetre_menu == True:
    #creation de la fenetre

    fenetre= tk.Tk()
    fenetre.title("blackjack")
    background= tk.PhotoImage(file="background.png")
    background_label = tk.Label(fenetre, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    fenetre.geometry('1280x732')


    #deck de carte

    def nom_carte():
        symboles = ['trefle', 'coeur', 'carreau', 'pique']
        carte = ['As', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'reine', 'roi']
        valeur = random.choice(carte)
        symbole = random.choice(symboles)
        carte = str(valeur) + '_' + str(symbole)
        return carte
    
    
    #label1 = tk.Label(fenetre, image = charger_image(nom_carte()))
    #label1.place(x=597,y=483)
    #label2 = tk.Label(fenetre, image = charger_image(nom_carte()))
    #label2.place(x=618,y=505)
    affichage_carte1(charger_image(str(nom_carte())))
    affichage_carte2(charger_image(str(nom_carte())))


    #creation des boutons

    bouton_quitter = tk.Button(fenetre, text="X", command=quitter, width=5)
    bouton_quitter.grid(column=0,row=0)

    bouton_hit= tk.Button(fenetre, text="HIT", command=hit(nom_carte()), width=10, bg='green')
    bouton_hit.place(x=600, y=705)

    bouton_stand= tk.Button(fenetre, text="STAND", command=stand, width=10, bg='green')
    bouton_stand.place(x=680, y=705)

    bouton_remake= tk.Button(fenetre, text="REMAKE", command=remake, width=10, bg='green')
    bouton_remake.place(x=520, y=705)
    fenetre.mainloop()


#my_img = tk.PhotoImage(file="cartes/2_carreau.png")
#label = tk.Label(fenetre, image = my_img)
#label.place(x=613,y=500)



#affichage_carte1(charger_image("2_carreau"))

