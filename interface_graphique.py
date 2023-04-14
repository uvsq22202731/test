#interface graphique

import tkinter as tk
import PIL as pil
from PIL import Image
import random
import tkinter.font as font
from tkinter import messagebox

#fonctions

def menu():
    """affiche le menu, propose 2 bouttons : quitter et jouer, jouer ammene le joueur sur une nouvelle fenetre jeu et ferme l'ancienne"""
    def etat_quit():
        """ferme la fenetre et retourne l'etat du boutton jouer"""
        fenetre.destroy()
        return etat_play.set(1)
    
    fenetre= tk.Tk()
    fenetre.title("menu blackjack")
    background= tk.PhotoImage(file="menu.png")
    background_label = tk.Label(fenetre, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    fenetre.attributes("-fullscreen",True)
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
    """ferme la fenetre"""
    fenetre.destroy()

def remake():
    """permet de relancer une nouvelle partie"""
    pass

def stand():
    pass


def affichage_carte1_joueur(img_carte):
    """affiche la 1ere carte du joueur"""
    label1 = tk.Label(fenetre, image = img_carte)
    label1.place(x=597,y=483)

def affichage_carte1_croupier(img_carte):
    """affiche la 1ere carte du croupier"""
    label1 = tk.Label(fenetre, image = img_carte)
    label1.place(x=597,y=45)

def affichage_carte_retournee_croupier(img_carte):
    """affiche la 2eme carte du croupier"""
    label1 = tk.Label(fenetre, image = img_carte)
    label1.place(x=618,y=90)

def affichage_carte2_joueur(img_carte):
    """affiche la 2ere carte du joueur"""
    label2 = tk.Label(fenetre, image = img_carte)
    label2.place(x=618,y=505)

def affichage_carte_hit(img_carte):
    """affiche la 3ere carte du joueur"""
    label3 = tk.Label(fenetre, image = img_carte)
    label3.place(x=640,y=540)

def charger_image(carte):
    """charge les images rentrées en paramètre"""
    global img
    global liste_images_cartes
    img = tk.PhotoImage(file="cartes/"+str(carte)+".png")
    liste_images_cartes.append(img)

def hit():
    """affiche la carte du hit"""
    affichage_carte_hit(liste_images_cartes[3])

    
fenetre_menu = menu()

if fenetre_menu == True:
    #creation de la fenetre

    fenetre= tk.Tk()
    fenetre.title("blackjack")
    background= tk.PhotoImage(file="background.png")
    background_label = tk.Label(fenetre, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    fenetre.attributes("-fullscreen",True)


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
    liste_images_cartes=[]
    for i in range(6):
        charger_image(nom_carte())
    charger_image("dos")
    affichage_carte1_joueur(liste_images_cartes[0])
    affichage_carte2_joueur(liste_images_cartes[1])
    affichage_carte1_croupier(liste_images_cartes[2])
    affichage_carte_retournee_croupier(liste_images_cartes[-1])

    #creation des boutons

    bouton_quitter = tk.Button(fenetre, text="X", command=quitter, width=5, bg="red")
    bouton_quitter.grid(column=0,row=0)

    bouton_hit= tk.Button(fenetre, text="HIT", command=hit, width=20, bg='green')
    bouton_hit.place(x=640, y=838)

    bouton_stand= tk.Button(fenetre, text="STAND", command=stand, width=20, bg='green')
    bouton_stand.place(x=800, y=838)

    bouton_remake= tk.Button(fenetre, text="REMAKE", command=remake, width=20, bg='green')
    bouton_remake.place(x=480, y=838)
    fenetre.mainloop()


#my_img = tk.PhotoImage(file="cartes/2_carreau.png")
#label = tk.Label(fenetre, image = my_img)
#label.place(x=613,y=500)



#affichage_carte1(charger_image("2_carreau"))

