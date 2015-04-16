# -*- coding: utf-8 -*-
from Tkinter import*
from Matrix import*
from Man import*
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

        self.matrix=Matrix()
        self.matrix.CreateRandomMatrice()
        self.matrix.CreateRandomPosition1()
        self.matrix.CreateRandomPosition2()


        self.Bloc = PhotoImage(file=os.getcwd()+"\Images\Wall.gif")
        self.Vide = PhotoImage(file=os.getcwd()+"\Images\Vide.gif")
        self.Bomby1=PhotoImage(file=os.getcwd()+"\Images\BombyB.gif")
        self.Bomby1Left=PhotoImage(file=os.getcwd()+"\Images\BombyLeftB.gif")
        self.Bomby1Right=PhotoImage(file=os.getcwd()+"\Images\BombyRightB.gif")
        self.Bomby1Back=PhotoImage(file=os.getcwd()+"\Images\BombyBacktB.gif")
        self.Bomby2=PhotoImage(file=os.getcwd()+"\Images\BombyR.gif")
        self.Bomby2Left=PhotoImage(file=os.getcwd()+"\Images\BombyLeftR.gif")
        self.Bomby2Right=PhotoImage(file=os.getcwd()+"\Images\BombyRightR.gif")
        self.Bomby2Back=PhotoImage(file=os.getcwd()+"\Images\BombyBacktR.gif")
        self.Bombe=PhotoImage(file=os.getcwd()+"\Images\Bombe.gif")


        self.window.bind("<KeyPress-z>",self.Bomby1Up)
        self.window.bind("<KeyPress-q>",self.Bomby1Left)
        self.window.bind("<KeyPress-s>",self.Bomby1Down)
        self.window.bind("<KeyPress-d>",self.Bomby1Right)
        self.window.bind("<KeyPress-r>",self.Bomby1SetBombe)
        self.window.bind("<KeyPress-Up>",self.Bomby2Up)
        self.window.bind("<KeyPress-Left>",self.Bomby2Left)
        self.window.bind("<KeyPress-Down>",self.Bomby2Down)
        self.window.bind("<KeyPress-Right>",self.Bomby2Right)
#        self.window.bind("<KeyPress-0>",self.Bomby2SetBombe)
        self.window.bind("<KeyPress-Escape>",self.Quitter)
        self.window.bind("<KeyPress-F5>",self.Reinitialiser)

        reinitialiser=Button(self.window, text="REINITIALISER",width=20,command=self.Reinitialiser)
        reinitialiser.place(x=650,y=0)

        pygame.mixer.init()
        pygame.mixer.music.load("music1.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.fadeout(300)
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
        self.matrix.Bomby1.SetBombe()
#        self.Countdown()
        self.PrintImages()
    def Bomby2SelBombe(self,event):
        self.matrix.Bomby2.SetBombe()
#        self.Countdown()
        self.PrintImages()

    def PrintImages (self):
        for l in range(CONST_NbLignes) :
            for c in range (CONST_NbColonnes):
                case = self.matrix.grid[l][c]
                if case == 9 :
                    if Bomby2.sens==CONST_Bas:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby2,anchor="nw")
                    if Bomby2.sens==CONST_Haut:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby2Back,anchor="nw")
                    if Bomby2.sens==CONST_Droit:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby2Right,anchor="nw")
                    if Bomby2.sens==CONST_Gauche:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby2Left,anchor="nw")
                if case == 8 :
                    pos=self.CalculPositionCase(l,c)
                    if Bomby1.sens==CONST_Bas:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby1,anchor="nw")
                    if Bomby1.sens==CONST_Haut:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby1Back,anchor="nw")
                    if Bomby1.sens==CONST_Droit:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby1Right,anchor="nw")
                    if Bomby1.sens==CONST_Gauche:
                        self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bomby1Left,anchor="nw")
                if case == 6 :
                    pos=self.CalculPositionCase(l,c)
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bombe,anchor="nw")
                if case == 1 :
                    pos=self.CalculPositionCase(l,c)
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Bloc,anchor="nw")
                if case == 0 :
                    pos=self.CalculPositionCase(l,c)
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.Vide,anchor="nw")

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


    def Quitter(self):
        print "Quitter"
        self.Destroy()

    def Reinitialiser(self):
        self.matrix.CreateRandomMatrice()
        self.matrix.CreateRandomPosition1()
        self.matrix.CreateRandomPosition2()
        self.PrintImages()
        print "Reinitialisation"

    def Mainloop(self):
        self.window.mainloop()

    def Destroy(self):
        pygame.mixer.music.stop()
        self.window.destroy()


if __name__ == "__main__":
    W1=GameWindow()
    W1.PrintImages()
    W1.Mainloop()
