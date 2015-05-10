from Tkinter import*
import tkFont
from GameWindow import*
import pygame.mixer
import os

from Tkinter import*
import tkFont
from GameWindow import*
import pygame.mixer

def Quitter():
    pygame.mixer.music.stop()
    fenetre.destroy()
def Jouer():
    pygame.mixer.music.stop()
    fenetre.destroy()
    GameWindow()


fenetre=Tk()
fenetre.title("BOMBERMAN ~ Page d'Accueil")
fenetre.geometry("960x768")
fenetre.protocol("WM_DELETE_WINDOW",Quitter)

img = PhotoImage(file=os.getcwd()+"\Images\pagedaccueil2.gif")
bg = Label(fenetre, image=img).pack(side="left")

pygame.mixer.init()
pygame.mixer.music.load("music.ogg")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
pygame.mixer.fadeout(300)
pygame.mixer.music.play(-1,0.0)

jouer=Button(fenetre, text="JOUER",bg="black",fg="white",width=20,command=Jouer)
jouer.place(x=360,y=340)

quitter = Button(fenetre, text="QUITTER",bg="black",fg="white",width=20, command=Quitter)
quitter.place(x=360,y=370)

fenetre.mainloop()


