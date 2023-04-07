import tkinter as tk
import PIL as pil
from PIL import Image
import random
from time import *
import tkinter.font as font
from tkinter import messagebox

#fonctions interface

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

def hit(carte):
    affichage_carte1(charger_image(carte))

def remake():
    pass

def stand():
    pass

def affichage_carte1(img_carte):
    label = tk.Label(fenetre, image = img_carte)
    label.place(x=613,y=500)

def charger_image(carte):
    return tk.PhotoImage(file="cartes/"+str(carte)+".png")


#fonctions jeu
def conditions():
    global Fin
    global joueur
    global croupier
    if joueur == croupier:
        print("Le croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nC'est une égalité")
        Fin = True
        return
    if (joueur > croupier) or (croupier > 22):
        if joueur > 21:
            if croupier > 21:
                print("Le croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nC'est une égalité")
                Fin = True
                return
            else:
                print("\nLe croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nvous avez perdu")
                Fin = True
                return
        else:
            print("\nLe croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nvous avez gagné")
            Fin = True
            return
    if croupier > joueur and croupier < 22:
        if joueur > 21:
            print("Le croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nC'est une égalité")
            Fin = True
            return
        else:
            print("\nLe croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nvous avez perdu")
            Fin = True
            return
    return


def tour_croupier(numservicecroupier):
    global joueur
    global croupier
    retourner = True
    distribution(retourner)
    if (carte[cartealeatoire[3]] == As and carte[cartealeatoire[1]] == 6) or (carte[cartealeatoire[3]] == 6 and carte[cartealeatoire[1]] == As):
        if croupier == 17 or croupier == 7:
            conditions()
            return
    retourner = False
    if croupier <= 16:
        while croupier <= 16:
            distribution(retourner)
            numservicecroupier += 1     
        conditions()
        return
    else:
        conditions()
        return


def tour_joueur(servicecroupier):
    global tour
    global carte
    global cartealeatoire
    global Fin
    global joueur
    global croupier
    if joueur >= 22:
        print("\nLe croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nvous avez perdu")
        Fin = True
    elif joueur < 22:
        print("\nLe croupier possède " + str(croupier), "+ une carte retourné.\nVous avez " + str(joueur))
        # abandonner = str(input("Voulez vous abandonner et perdre la moitié de votre mise : yes or no: "))
        # reste = str(input("Reste : yes or no: "))
        abandonner = "no"
        reste = "no"
        if abandonner == "yes":
            Fin = True
            # on arrête le jeu (on met cette condition en premier comme ça on peut pas appuyer sur deux boutons)
            return
        else:
            if reste == "yes":
                tour_croupier(servicecroupier)
                pass
                # si c'est non on regarde les autres boutons
            else:
                hit = str(input("Voulez vous hit: yes or no: "))
                if hit == "yes":
                    distribution(hit)
                    servicecroupier += 1
                    tour_croupier(servicecroupier)
                    return
                if hit == "no":
                    tour_croupier(servicecroupier)
                    return
    return


def afficher_carte():
    symboles = ['trèfle', 'coeur', 'carreau', 'pique']
    valeur = random.choice(cartealeatoire)
    symbole = random.choice(symboles)
    carte = str(valeur) + ' de ' + str(symbole)
    print(carte)
    return

def distribution(condi):
    global joueur
    global croupier
    global croupierhit
    if joueur == 0:  #joueur == 0, est le début de la partie avec la distribution des cartes.
        joueur += carte[cartealeatoire[0]]
        afficher_carte()
        sleep(2)
        croupier += carte[cartealeatoire[1]]
        afficher_carte()
        sleep(2)
        joueur += carte[cartealeatoire[2]]
        afficher_carte()
        sleep(2)
        return joueur, croupier
    if condi == 'yes':  #condition == 'yes', est le moment où le joueur décide de hit ou non. Condi étant égal à 'yes' ou 'no'
        joueur += carte[cartealeatoire[croupierhit]]
        afficher_carte()
        sleep(2)
        return
    elif condi == True:  #la condition = True, est le moment où la carte du croupier est retournée, et on la retourne (la carte étant déjà distribué son numéro est déjà défini)
        croupier += carte[cartealeatoire[3]]
        afficher_carte()
        sleep(2)
        return
    if croupier <= 16 and condi == False :  #le croupier <= 16, est le moment où le croupier doit piocher toutes ses cartes. 
        croupier += carte[cartealeatoire[condi]]
        afficher_carte()
        sleep(2)
        return
    return


Fin = False
while Fin is not True:
    
    play = menu()
    #play = True  # bouton avec play booléen oui ou non
    if play is True:


        fenetre= tk.Tk()
        fenetre.title("blackjack")
        background= tk.PhotoImage(file="background.png")
        background_label = tk.Label(fenetre, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        fenetre.geometry('1280x732')

        bouton_hit= tk.Button(fenetre, text="HIT", command=hit, width=10, bg='green')
        bouton_hit.place(x=600, y=705)

        bouton_stand= tk.Button(fenetre, text="STAND", command=stand, width=10, bg='green')
        bouton_stand.place(x=680, y=705)

        bouton_remake= tk.Button(fenetre, text="REMAKE", command=remake, width=10, bg='green')
        bouton_remake.place(x=520, y=705)
        fenetre.mainloop()

    As = int(input("Quelle est la valeur de l'AS ? (1 ou 11): "))
    carte = [As, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if play is True:
        # peut être ajouter le bet
        Fin = False
        croupierhit = 4  # carte retourné sur la table
        cartealeatoire = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        joueur = 0
        croupier = 0
        hit = ''
        random.shuffle(cartealeatoire)
        tour = 0
        if tour == 0 and joueur == (As+10):
            messagebox.info("BLACKJACK! Vous avez gagné!")
            Fin = True
            break
        distribution(joueur)
        while Fin is not True:
            tour += 1
            tour_joueur(croupierhit)
