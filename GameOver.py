from Tkinter import*
import tkFont
from GameWindow import*
import pygame.mixer
import os
import threading

class GameOver():

    def __init__(self):
        self.window=Tk()
        self.window.title("BOMBERMAN ~ Game Over")
        self.window.geometry("960x768")
        self.window.protocol("WM_DELETE_WINDOW",self.Quitter)
        self.img = PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"Gameover.gif")
        bg = Label(self.window, image=self.img).pack(side="left")
        self.gameOver = False
        
        pygame.mixer.init()
        pygame.mixer.music.load("music2.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.fadeout(300)
        pygame.mixer.music.play(-1,0.0)

        jouer=Button(self.window, text="REJOUER",bg="black",fg="white",width=20,command=self.Jouer)
        jouer.place(x=360,y=340)

        quitter = Button(self.window, text="QUITTER",bg="black",fg="white",width=20, command=self.Quitter)
        quitter.place(x=360,y=370)

    def Mainloop(self):
        self.window.mainloop()

    def Quitter(self):
        pygame.mixer.music.stop()
        self.gameOver = True
        self.window.destroy()

    def Jouer(self):
        pygame.mixer.music.stop()
        self.window.destroy()

if __name__ == "__main__":
    W1=GameOver()
    W1.Mainloop()




