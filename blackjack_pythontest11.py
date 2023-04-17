"""Appel de librairies"""
import tkinter as tk
import PIL as pil
from PIL import Image
import random
from time import *
import tkinter.font as font

"""Fonctions interface"""

def menu():
    """affiche le menu, propose 2 bouttons : quitter et jouer, jouer ammene le joueur sur une nouvelle fenetre jeu et ferme l'ancienne"""
    def etat_quit():
        """ferme la fenetre et retourne l'etat du boutton jouer"""
        fenetrem.destroy()
        return etat_play.set(1)
    
    fenetrem= tk.Tk()
    fenetrem.title("menu blackjack")
    # fenetrem.bind('<Escape>', lambda e: fenetrem.destroy())
    background= tk.PhotoImage(file="menu.png")
    background_label = tk.Label(fenetrem, image=background)
    background_label.place(x=0, y=0)
    fenetrem.attributes("-fullscreen",True)
    etat_play = tk.BooleanVar(fenetrem) # creation variable booleen 
    etat_play.set(0) # intialisation de la variable a False
    bouton_quitter = tk.Button(fenetrem, text="QUITTER", command=fenetrem.destroy, width=20,height=2,bg='white') # ferme la fenetre, fin du jeu
    bouton_quitter.place(x=680,y=300)
    bouton_play = tk.Button(fenetrem, text="JOUER", command=lambda:etat_quit(), width=20, height=2,bg='white') #si le boutton jouer est clické, on ferme le menu et retourne la valeur True
    bouton_play.place(x=400,y=300)
    myFont = font.Font(family='Comic Sans MS', size=15, weight='bold')
    bouton_quitter['font'] = myFont
    bouton_play['font'] = myFont
    fenetrem.mainloop()
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
    label1.place(x=618,y=67)

def affichage_carte2_joueur(img_carte):
    """affiche la 2ere carte du joueur"""
    label2 = tk.Label(fenetre, image = img_carte)
    label2.place(x=618,y=505)

def affichage_carte_hit(img_carte,x,y):
    """affiche les cartes hit du joueur"""
    label3 = tk.Label(fenetre, image = img_carte)
    label3.place(x=x,y=y)

def charger_image(carte):
    """charge les images rentrées en paramètre"""
    global img
    global liste_images_cartes
    img = tk.PhotoImage(file="cartes/"+str(carte)+".png")
    liste_images_cartes.append(img)

def hit():
    """affiche la carte du hit"""
    global joueur
    global liste_images_cartes
    global etat_hit
    global bouton_hit
    global compteur
    global compteur_hit

    compteur_hit+=1
    x,y=640,540
    
    if compteur_hit == 1:
        sleep(0.2)
        # affichage_carte_hit(liste_images_cartes[8],x,y)
        compteur.config(text='score : '+str(joueur))
        x+=22
        y+=35
    elif compteur_hit == 2:
        sleep(0.2)
        print(liste_images_cartes)
        # affichage_carte_hit(liste_images_cartes[10],x,y)
        compteur.config(text='score : '+str(joueur))
        x+=22
        y+=35
    elif compteur_hit == 3:
        sleep(0.2)
        print(liste_images_cartes)
        # affichage_carte_hit(liste_images_cartes[12],x,y)
        compteur.config(text='score : '+str(joueur))
        x+=22
        y+=35
    etat_hit.set(1)
    
    
    return

#fonctions jeu
def conditions():
    """Fonction qui permet de définir qui va gagner la partie, elle ne retourne que des variables globales"""
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
                print("\nLe croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nVous avez perdu")
                Fin = True
                return
        else:
            print("\nLe croupier possède " + str(croupier), "\nVous avez " + str(joueur), "\nVous avez gagné")
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
    """ Fonction qui permet au croupier de jouer de manière automatique, elle prend en paramètre 'numservicecroupier' qui correspond au numéro de la prochaine carte à piocher"""
    global joueur
    global croupier
    global etat_hit
    retourner = etat_hit.get()
    distribution(retourner)
    if (carte[cartealeatoire[3]] == As and carte[cartealeatoire[1]] == 6) or (carte[cartealeatoire[3]] == 6 and carte[cartealeatoire[1]] == As):
        if croupier == 17 or croupier == 7:
            croupier = 17
            conditions()
            return
    retourner = etat_hit.get()
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
    """Fonction qui permet au joueur de jouer de manière automatique, elle prend en paramètre 'servicecroupier' qui correspond au numéro de la prochaine carte à piocher"""
    global tour
    global carte
    global cartealeatoire
    global Fin
    global joueur
    global croupier
    global etat_hit
    global fenetre
    global compteur_hit
    
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
                
                if etat_hit.get() == 0 and compteur_hit == 0:
                    tour_croupier(servicecroupier)
                    return
    return



def afficher_carte(nb): 
    """Fonction qui permet d'afficher les cartes, et qui return le nom de la carte de cette façon : '1_trèfle' ainsi que la variable 'qui' qui permet de savoir qui joue. Elle prend en paramètre 'nb' qui correspond au numéro de la carte pioché """
    global carte
    global cartealeatoire
    global symboles
    global deck 
    global joueur
    global croupier
    qui = ""
    valeur = carte[cartealeatoire[nb]]
    if nb == 0 or nb == 2 or nb == 4:
        qui = "joueur"
    else:
        qui = "croupier"
    if valeur == 12 or valeur == 13 or valeur == 14:
        if qui == "joueur":
            joueur = joueur + 10 - valeur
        elif qui == "croupier":
            croupier = croupier + 10 - valeur
    symbole = random.choice(symboles)
    current_card= valeur,symbole
    if (valeur,"coeur") and (valeur,"trefle") and (valeur,'carreau') and (valeur,'pique') not in deck:
        nb += 1
    while current_card not in deck:
        valeur = carte[cartealeatoire[nb]]
        symbole = random.choice(symboles)
        current_card= valeur,symbole
    if current_card[0]==1:
        valeur='As'
        carte_affich = str(valeur) + '_' + str(symbole)
    if current_card[0] == 12 or current_card[0] == 13 or current_card[0] == 14:
        if current_card[0] == 12:
            valeur = "valet"
        elif current_card[0] == 13:
            valeur = "reine"
        elif current_card[0] == 14:
            valeur = "roi"
        deck.remove(current_card)
        current_card = (10,symbole)
        carte_affich = str(valeur) + '_' + str(symbole)
        return carte_affich #, qui
    
    deck.remove(current_card)    
    carte_affich = str(valeur) + '_' + str(symbole)
    return carte_affich #, qui

def etat_11():
    global as_11
    bouton_11.destroy()
    valeur_as.destroy()
    return as_11.set(1)

def etat_1():
    global as_1
    bouton_1.destroy()
    valeur_as.destroy()
    return as_1.set(1)

def distribution(condi):
    """Fonction qui permet de distribuer chaque carte dans chaque situation, elle prend en paramètre 'condi' qui nous permet de déterminer dans quelle situation de jeu nous nous trouvons"""
    global joueur
    global croupier
    global croupierhit
    global cartealeatoire
    global liste_images_cartes
    global carte
    global etat_hit
    global compteur_hit
    global valeur_as
    global bouton_11
    global bouton_1
    def update():
        return compteur.config(text='score : '+str(joueur))
    # compteur_hit = 0
    if joueur == 0:  #joueur == 0, est le début de la partie avec la distribution des cartes.
        c1= carte[cartealeatoire[0]]
        if c1 == 1:
            valeur_as.place(x=1000,y=300)
            bouton_11.place(x=1000, y= 320)
            bouton_1.place(x=1020, y= 320)
            if as_11.get() == 1:
                c1 = 11
            elif as_11.get()== 1:
                c1= 1
            return
        joueur+= c1
        update()
        # c=afficher_carte(0)
        liste_images_cartes.append(charger_image(afficher_carte(0)))
        affichage_carte1_joueur(liste_images_cartes[0])
        croupier += carte[cartealeatoire[1]]
        # c1=afficher_carte(1)
        liste_images_cartes.append(charger_image(afficher_carte(1)))
        affichage_carte1_croupier(liste_images_cartes[2])
        c2= carte[cartealeatoire[2]]
        if c2 == 1:
            valeur_as.place(x=1000,y=300)
            bouton_11.place(x=1000, y= 320)
            bouton_1.place(x=1020, y= 320)
            if as_11.get() == 1:
                c2 = 11
            elif as_1.get()== 1:
                c2= 1
            return
        joueur += c2
        update()
        # c2=afficher_carte(2)
        liste_images_cartes.append(charger_image(afficher_carte(2)))
        affichage_carte2_joueur(liste_images_cartes[4])
        liste_images_cartes.append(charger_image('dos'))
        affichage_carte_retournee_croupier(liste_images_cartes[6])
        # print(c,c1,c2, liste_images_cartes)
        # cartehit= carte[cartealeatoire[croupierhit]]
        # joueur += cartehit
        
        while joueur < 21:
            if joueur >= 21:
                    bouton_hit.config(state="disabled")
                    return
            if etat_hit.get()==1:
                cartehit= carte[cartealeatoire[croupierhit]]
                liste_images_cartes.append(charger_image(afficher_carte(croupierhit)))
                croupierhit+=1
                if cartehit == 1:
                    valeur_as.place(x=800,y=300)
                    bouton_11.place(x=1000, y= 320)
                    bouton_1.place(x=1020, y= 320)
                    if as_11.get() == 1:
                        cartehit = 11
                    elif as_1.get()== 1:
                        cartehit= 1
                    return
                joueur += cartehit
                hit()

                return etat_hit.set(0)
            
        return joueur, croupier

    # if etat_hit.get() == 1:  #condition == 'yes', est le moment où le joueur décide de hit ou non. Condi étant égal à 'yes' ou 'no'
    #     hit()
    #     return
    elif condi == True:  #la condition = True, est le moment où la carte du croupier est retournée, et on la retourne (la carte étant déjà distribué son numéro est déjà défini)
        croupier += carte[cartealeatoire[3]]
        liste_images_cartes.append(charger_image(afficher_carte(3)))
        affichage_carte_retournee_croupier(liste_images_cartes[8])
        return
    if croupier <= 16 and condi == False :  #le croupier <= 16, est le moment où le croupier doit piocher toutes ses cartes. 
        croupier += carte[cartealeatoire[condi]]
        afficher_carte(condi)
        return
    return

"""Programme principal"""
Fin = False
while Fin is not True:
    
    fenetre_menu = menu()
    #play = True  # bouton avec play booléen oui ou non
    if fenetre_menu == True:
    #creation de la fenetre
        fenetre= tk.Tk()
        fenetre.title("blackjack")
        fenetre.bind('<Escape>', lambda e: fenetre.destroy())
        background= tk.PhotoImage(file="background.png")
        background_label = tk.Label(fenetre, image=background)
        background_label.place(x=0, y=0)
        fenetre.attributes("-fullscreen",True)
        liste_images_cartes=[]
        #creation des boutons

        bouton_quitter = tk.Button(fenetre, text="X", command=quitter, width=5, bg="red")
        bouton_quitter.grid(column=0,row=0)

        bouton_stand= tk.Button(fenetre, text="STAND", command=stand, width=20, bg='green')
        bouton_stand.place(x=800, y=838)

        bouton_remake= tk.Button(fenetre, text="REMAKE", command=remake, width=20, bg='green')
        bouton_remake.place(x=480, y=838)

        valeur_as= tk.Label(fenetre,text="quelle est la valeur de l'as?",font=("Lithograph", 14),bg='#228B00')
        bouton_11 = tk.Button(fenetre, text="AS = 11", command=etat_11, width=20, bg='green')
        bouton_1 = tk.Button(fenetre, text="AS = 1", command=etat_1, width=20, bg='green')
        as_11 = tk.BooleanVar(fenetre) # creation variable booleen
        as_11.set(0)
        as_1 = tk.BooleanVar(fenetre) # creation variable booleen
        as_1.set(0)

        compteur= tk.Label(fenetre,text='',font=("Lithograph", 14),bg='#228B00')
        compteur.place(x=500,y=700)

        compteur_hit=0
        
        etat_hit = tk.BooleanVar(fenetre) # creation variable booleen 
        etat_hit.set(0) # intialisation de la variable a False
        bouton_hit= tk.Button(fenetre, text="HIT", command= hit, width=20, bg='green')
        bouton_hit.place(x=640, y=838)

        As = 1
        carte = [As, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
        symboles = ['trefle', 'coeur', 'carreau', 'pique']
        deck = [(card,suit) for card in carte for suit in symboles]
        # peut être ajouter le bet
        Fin = False
        croupierhit = 4  # carte retourné sur la table
        cartealeatoire = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        joueur = 0
        croupier = 0
        random.shuffle(cartealeatoire)
        tour = 0
        distribution(joueur)
        if tour == 0 and joueur == (As+10):
            print("BLACKJACK ! \nVous avez gagné !")
            Fin = True
            break
        while Fin is not True:
            tour += 1
            tour_joueur(croupierhit)


fenetre.mainloop()
