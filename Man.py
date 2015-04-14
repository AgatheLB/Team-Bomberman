from Tkinter import*
from MatrixObjects import *
from Matrix import*
from GameWindow import*


class Man(MatrixObjects):
    def __init__(self,ligne,colonne,sens):
        MatrixObjects.__init__(self,ligne,colonne)
        self.sens=sens


    def SetImages(self,FileUp,FileDown,FileRight,FileLeft):
        self.ImageUp=PhotoImage(FileUp)
        self.ImageDown=PhotoImage(FileDown)
        self.ImageRight=PhotoImage(FileRight)
        self.ImageLeft=PhotoImage(FileLeft)

    def SetBombe(self):
        if self.sens==constantes.CONST_Gauche:
#            if self.grid[self.ligne][self.colonne-1]==0:
#                Bombe.SetPosition(self.ligne,self.colonne-1)
            print "to do"


        if self.sens==constantes.CONST_Bas:
#            if self.grid[self.ligne+1][self.colonne]==0:
#                Bombe.SetPosition(self.ligne+1,self.colonne)
            print "to do"


        if self.sens==constantes.CONST_Droit:
#            if self.grid[self.ligne][self.Bomby1.colonne+1]==0:
#                Bombe.SetPosition(self.ligne,self.colonne+1)
            print "to do"


        if self.sens==constantes.CONST_Haut:
#            if self.grid[self.ligne-1][self.colonne]==0:
#                Bombe.SetPosition(self.ligne-1,self.colonne)
            print "to do"




if __name__ == "__main__":
    M1=Man(1,2,CONST_Haut)
    print M1.ligne
    print M1.colonne
    fenetre=Tk()
    M1.SetImages(os.getcwd()+"\Images\BombyB.gif",os.getcwd()+"\Images\BombyBackB.gif",os.getcwd()+"\Images\BombyRightB.gif",os.getcwd()+"\Images\BombyLeftB.gif")
    print M1.ImageUp
    print M1.ImageDown
    print M1.ImageRight
    print M1.ImageLeft
    M1.SetBombe()