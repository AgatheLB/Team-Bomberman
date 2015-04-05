from Tkinter import*
from Matrix import*
from Man import*
from constantes import*
import os

class GameWindow:
    def __init__(self):
        self.window=Tk()
        self.window.title("jeu")
        self.window.geometry("960x768")
        self.ImageWindow=Canvas(self.window)
        self.ImageWindow.place(x=0,y=0)
        self.ImageWindow.pack()

        self.matrix=Matrix()
        self.matrix.CreateRandomMatrice()
        self.matrix.CreateRandomPosition1()
        self.matrix.CreateRandomPosition2()


        self.Bloc = PhotoImage(file=os.getcwd()+"\Images\Wall.gif")
        self.Vide = PhotoImage(file=os.getcwd()+"\Images\Vide.gif")
        self.Bomby1=PhotoImage(file=os.getcwd()+"\Images\BombyB.gif")
        self.Bomby2=PhotoImage(file=os.getcwd()+"\Images\BombyB.gif")
        self.Bombe=PhotoImage(file=os.getcwd()+"\Images\Bombe.gif")



        self.window.bind("<KeyPress-z>",self.Bomby1Up)
        self.window.bind("<KeyPress-q>",self.Bomby1Left)
        self.window.bind("<KeyPress-s>",self.Bomby1Down)
        self.window.bind("<KeyPress-d>",self.Bomby1Right)
#        self.window.bind("<KeyPress-r>",self.Bomby1SetBombe)
        self.window.bind("<KeyPress-Up>",self.Bomby2Up)
        self.window.bind("<KeyPress-Left>",self.Bomby2Left)
        self.window.bind("<KeyPress-Down>",self.Bomby2Down)
        self.window.bind("<KeyPress-Right>",self.Bomby2Right)
#        self.window.bind("<KeyPress-0>",self.Bomby2SetBombe)
        self.window.bind("<KeyPress-Escape>",self.Quitter)
        self.window.bind("<KeyPress-F5>",self.Reinitialiser)

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
#    def Bomby1SetBombe(self):
#    def Bomby2SelBombe(self):

    def PrintImages (self):
        for l in range(CONST_NbLignes) :
            for c in range (CONST_NbColonnes):
                case = self.matrix.grid[l][c]
                print case
                if case == 9 :
                    pos=self.CalculPositionCase(l,c)
                    print pos
                    print self.Bomby2
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseX(l),image=self.Bomby2,anchor="nw")
                if case == 8 :
                    pos=self.CalculPositionCase(l,c)
                    print pos
                    print self.Bomby1
                    self.ImageWindow.create_image(self.CalculPositionCase(l,c),self.Bomby1,anchor="nw")
                if case == 6 :
                    pos=self.CalculPositionCase(l,c)
                    print pos
                    print self.Bombe
                    self.ImageWindow.create_image(self.CalculPositionCase(l,c),self.Bombe,anchor="nw")
                if case == 1 :
                    pos=self.CalculPositionCase(l,c)
                    print pos
                    print self.Bloc
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseX(l),image=self.Bloc,anchor="nw")
                if case == 0 :
                    pos=self.CalculPositionCase(l,c)
                    print pos
                    print self.Vide
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseX(l),image=self.Vide,anchor="nw")

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


    def Quitter(self,event):
        print "Quitter"

    def Reinitialiser(self,event):
        print "Reinitialiser"

    def Mainloop(self):
        self.window.mainloop()

    def Destroy(self):
        self.window.destroy()


if __name__ == "__main__":
    W1=GameWindow()
    W1.PrintImages()
    W1.Mainloop()
