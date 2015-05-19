# -*- coding: utf-8 -*-
from Tkinter import*
from Matrix import*
from Man import*
from Bombes import*
from constantes import*
import os
import pygame.mixer


class GameWindow:
    def __init__(self):
        self.window=Tk()
        self.window.title("jeu")
        self.window.geometry("800x600")
        self.ImageWindow=Canvas(self.window,width=600, height=600)
        self.ImageWindow.place(x=0,y=0)
        self.ImageWindow.pack()

        self.matrix=Matrix.Matrix(self.ImageWindow)

        self.window.bind("<KeyPress-z>",self.Bomby1Up)
        self.window.bind("<KeyPress-q>",self.Bomby1Left)
        self.window.bind("<KeyPress-s>",self.Bomby1Down)
        self.window.bind("<KeyPress-d>",self.Bomby1Right)
        self.window.bind("<KeyPress-r>",self.Bomby1SetBombe)
        self.window.bind("<KeyPress-Up>",self.Bomby2Up)
        self.window.bind("<KeyPress-Left>",self.Bomby2Left)
        self.window.bind("<KeyPress-Down>",self.Bomby2Down)
        self.window.bind("<KeyPress-Right>",self.Bomby2Right)
        self.window.bind("<KeyPress-0>",self.Bomby2SetBombe)
        self.window.bind("<KeyPress-Escape>",self.QuitterByESC)
        self.window.bind("<KeyPress-F5>",self.ReinitialiserByF5)

        reinitialiser=Button(self.window, text="REINITIALISER",bg="white",fg="black",width=20,command=self.Reinitialiser)
        reinitialiser.place(x=0,y=0)

        pygame.mixer.init()
        pygame.mixer.music.load("music1.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.fadeout(300)
        pygame.mixer.music.play(-1,0.0)
        self.window.protocol("WM_DELETE_WINDOW",self.Quitter)

    def Bomby1Up(self,event):
        self.matrix.Bomby1Up()
    def Bomby1Left(self,event):
        self.matrix.Bomby1Left()
    def Bomby1Down(self,event):
        self.matrix.Bomby1Down()
    def Bomby1Right(self,event):
        self.matrix.Bomby1Right()
    def Bomby2Up(self,event):
        self.matrix.Bomby2Up()
    def Bomby2Left(self,event):
        self.matrix.Bomby2Left()
    def Bomby2Down(self,event):
        self.matrix.Bomby2Down()
    def Bomby2Right(self,event):
        self.matrix.Bomby2Right()

    def Bomby1SetBombe(self,event):
        self.matrix.SetBombe(self.matrix.Bomby1)

    def Bomby2SetBombe(self,event):
        self.matrix.SetBombe(self.matrix.Bomby2)

    def Reinitialiser(self):
        self.matrix.Reinitialisation()

    def ReinitialiserByF5(self,event):
        self.Reinitialiser()

    def Mainloop(self):
        self.window.mainloop()

    def Quitter(self):
        self.Destroy()

    def QuitterByESC(self,event):
        self.Quitter()

    def Destroy(self):
        pygame.mixer.music.stop()
        self.window.destroy()


if __name__ == "__main__":
    W1=GameWindow()
    W1.Mainloop()

