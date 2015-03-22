from Tkinter import*
import tkFont

def Quitter():
    fenetre.destroy()
def Jouer():
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
#texte.place(x=405,y=200)

jouer=Button(fenetre, text="JOUER",width=20,command=Jouer)
jouer.place(x=410,y=240)

quitter = Button(fenetre, text="QUITTER",width=20, command=Quitter)
quitter.place(x=410,y=270)

fenetre.mainloop()


