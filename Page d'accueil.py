# Créé par Céleste, le 03/03/2015
from __future__ import division
from lycee import *
from Tkinter import*
import tkFont

def action():
    if quitter :
        fenetre.destroy()
def actions():
    if jouer :
        fenetre2=Tk()
        fenetre2.title("jeu")
        fenetre2.geometry("960x768")
        fenetre2.mainloop()
        fenetre.destroy()


fenetre=Tk()
fenetre.title("BOMBERMAN ~ Page d'Accueil")
fenetre.geometry("960x768")

img = PhotoImage(file="pagedaccueil2.gif")
bg = Label(fenetre, image=img).pack(side="right")

texte = Label(fenetre,justify=LEFT,padx = 10,text="Bienvenue. Que voulez faire ?").pack(side="left")
texte.place(x=405,y=200)

jouer=Button(fenetre, text="JOUER",width=20,command=actions)
jouer.place(x=410,y=240)

quitter = Button(fenetre, text="QUITTER",width=20, command=action)
quitter.place(x=410,y=270)

fenetre.mainloop()
