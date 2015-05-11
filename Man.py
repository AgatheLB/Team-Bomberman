from Tkinter import*
from MatrixObjects import *


class Man(MatrixObjects):
    def __init__(self,ligne,colonne,sens):
        MatrixObjects.__init__(self,ligne,colonne)
        self.sens=sens


    def SetImages(self,FileUp,FileDown,FileRight,FileLeft):
        self.ImageUp=PhotoImage(FileUp)
        self.ImageDown=PhotoImage(FileDown)
        self.ImageRight=PhotoImage(FileRight)
        self.ImageLeft=PhotoImage(FileLeft)



if __name__ == "__main__":
    
    from constantes import *
    import os

    M1=Man(1,2,CONST_Haut)
    print M1.ligne
    print M1.colonne
    fenetre=Tk()
    M1.SetImages(os.getcwd()+CONST_ImageDirectory+"BombyB.gif",os.getcwd()+CONST_ImageDirectory+"BombyBackB.gif",os.getcwd()+CONST_ImageDirectory+"BombyRightB.gif",os.getcwd()+CONST_ImageDirectory+"BombyLeftB.gif")
    print M1.ImageUp
    print M1.ImageDown
    print M1.ImageRight
    print M1.ImageLeft
