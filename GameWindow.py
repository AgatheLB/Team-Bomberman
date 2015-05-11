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

        self.matrix=Matrix.Matrix(self)
        self.matrix.CreateRandomMatrice()
        self.matrix.CreateRandomPosition1()
        self.matrix.CreateRandomPosition2()


        self.ImageBloc = PhotoImage(file=os.getcwd()+"\Images\Wall.gif")
        self.ImageVide = PhotoImage(file=os.getcwd()+"\Images\Vide.gif")
        self.ImageBomby1=PhotoImage(file=os.getcwd()+"\Images\BombyB.gif")
        self.ImageBomby1Left=PhotoImage(file=os.getcwd()+"\Images\BombyLeftB.gif")
        self.ImageBomby1Right=PhotoImage(file=os.getcwd()+"\Images\BombyRightB.gif")
        self.ImageBomby1Back=PhotoImage(file=os.getcwd()+"\Images\BombyBackB.gif")
        self.ImageBomby2=PhotoImage(file=os.getcwd()+"\Images\BombyR.gif")
        self.ImageBomby2Left=PhotoImage(file=os.getcwd()+"\Images\BombyLeftR.gif")
        self.ImageBomby2Right=PhotoImage(file=os.getcwd()+"\Images\BombyRightR.gif")
        self.ImageBomby2Back=PhotoImage(file=os.getcwd()+"\Images\BombyBackR.gif")
        self.ImageBombe=PhotoImage(file=os.getcwd()+"\Images\Bombe.gif")


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
        self.PrintImages()
    def Bomby1Left(self,event):
        self.matrix.Bomby1Left()
        self.PrintImages()
    def Bomby1Down(self,event):
        self.matrix.Bomby1Down()
        self.PrintImages()
    def Bomby1Right(self,event):
        self.matrix.Bomby1Right()
        self.PrintImages()
    def Bomby2Up(self,event):
        self.matrix.Bomby2Up()
        self.PrintImages()
    def Bomby2Left(self,event):
        self.matrix.Bomby2Left()
        self.PrintImages()
    def Bomby2Down(self,event):
        self.matrix.Bomby2Down()
        self.PrintImages()
    def Bomby2Right(self,event):
        self.matrix.Bomby2Right()
        self.PrintImages()

    def Bomby1SetBombe(self,event):
        self.matrix.SetBombes(self.matrix.Bomby1)
#        self.Countdown()
        self.PrintImages()
    def Bomby2SetBombe(self,event):
        self.matrix.SetBombes(self.matrix.Bomby2)
#        self.Countdown()
        self.PrintImages()

    def PrintImages (self):
        for l in range(CONST_NbLignes) :
            for c in range (CONST_NbColonnes):
                case = self.matrix.grid[l][c]
                if case == 6 :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageBombe,anchor="nw")
                if case == 1 :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageBloc,anchor="nw")
                if case == 0 :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageVide,anchor="nw")
        #Affichage Bomby1:
        posBomby1=self.matrix.Bomby1.GetPosition()
        if self.matrix.Bomby1.sens==CONST_Bas:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1,anchor="nw")
        if self.matrix.Bomby1.sens==CONST_Haut:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1Back,anchor="nw")
        if self.matrix.Bomby1.sens==CONST_Droit:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1Right,anchor="nw")
        if self.matrix.Bomby1.sens==CONST_Gauche:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1Left,anchor="nw")
        #Affiche Bomby2
        posBomby2=self.matrix.Bomby2.GetPosition()
        if self.matrix.Bomby2.sens==CONST_Bas:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2,anchor="nw")
        if self.matrix.Bomby2.sens==CONST_Haut:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2Back,anchor="nw")
        if self.matrix.Bomby2.sens==CONST_Droit:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2Right,anchor="nw")
        if self.matrix.Bomby2.sens==CONST_Gauche:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2Left,anchor="nw")

    def CalculPositionCase(self,ligne,colonne):
        x=colonne*CONST_ImageSizeInPixels
        y=ligne*CONST_ImageSizeInPixels
        return x,y

    def CalculPositionCaseX(self,colonne):
        x=colonne*CONST_ImageSizeInPixels
        return x

    def CalculPositionCaseY(self,ligne):
        y=ligne*CONST_ImageSizeInPixels
        return y

    def Reinitialiser(self):
        self.matrix.Reinitialisation()
        self.PrintImages()

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
    W1.PrintImages()
    W1.Mainloop()
