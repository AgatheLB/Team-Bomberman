from Tkinter import*
import tkFont
from GameWindow import*
from GameOver import *
import pygame.mixer
import os

class HomeWindow:
    def __init__(self):
        self.window=Tk()
        self.window.title("BOMBERMAN ~ Page d'Accueil")
        self.window.geometry("960x768")
        self.window.protocol("WM_DELETE_WINDOW",self.Quitter)
        
        self.img = PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"pagedaccueil2.gif")
        bg = Label(self.window, image=self.img).pack(side="left")
        
        pygame.mixer.init()
        pygame.mixer.music.load("music.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.fadeout(300)
        pygame.mixer.music.play(-1,0.0)
        
        self.goToGameWindow=False
        self.jouer=Button(self.window, text="JOUER",bg="black",fg="white",width=20,command=self.Jouer)
        self.jouer.place(x=360,y=340)
        
        self.quitter = Button(self.window, text="QUITTER",bg="black",fg="white",width=20, command=self.Quitter)
        self.quitter.place(x=360,y=370)

    def Quitter(self):
        pygame.mixer.music.stop()
        self.window.destroy()
        
    def Jouer(self):
        pygame.mixer.music.stop()
        self.goToGameWindow=True
        self.window.destroy()

    def Mainloop(self):
        self.window.mainloop()

pageAccueil=HomeWindow()
pageAccueil.Mainloop()

if pageAccueil.goToGameWindow:
    continueGame = True
    while continueGame:
        gameWindow=GameWindow()
        gameWindow.Mainloop()
        
        # si l'un des joueurs a perdu 
        if gameWindow.gameOver:
            
            #on affiche la fenêtre GameOver
            gameOverWindow=GameOver()
            gameOverWindow.Mainloop()
            
            #si on quitte, fin du jeu sinon on rejoue
            if gameOverWindow.gameOver:
                continueGame=False
        # l'un des joueurs a appuyé sur ESC, on retourne à la page d'accueil
        else:
            pageAccueil=HomeWindow()
            pageAccueil.Mainloop()
            if not pageAccueil.goToGameWindow:
                continueGame = False
       
