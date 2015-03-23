from Tkinter import*
from Matrix import*

class GameWindow:
    def __init__(self):
        self.window=Tk()
        self.window.title("jeu")
        self.window.geometry("960x768")

        self.matrix=Matrix()
        self.matrix.CreateRandomMatrice()
        self.matrix.CreateRandomPosition1()
        self.matrix.CreateRandomPosition2()

        self.window.bind("<KeyPress-z>",self.Bomby1Up)
        self.window.bind("<KeyPress-q>",self.Bomby1Left)
        self.window.bind("<KeyPress-s>",self.Bomby1Down)
        self.window.bind("<KeyPress-d>",self.Bomby1Right)
        self.window.bind("<KeyPress-Up>",self.Bomby2Up)
        self.window.bind("<KeyPress-Left>",self.Bomby2Left)
        self.window.bind("<KeyPress-Down>",self.Bomby2Down)
        self.window.bind("<KeyPress-Right>",self.Bomby2Right)
        self.window.bind("<KeyPress-Escape>",self.Quitter)
        self.window.bind("<KeyPress-F5>",self.Reinitialiser)

    def Bomby1Up(self,event):
        print "Bomby1Up.window"
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
    W1.Mainloop()
