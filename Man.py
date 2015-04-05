from Tkinter import*
from MatrixObjects import *
from Matrix import*


class Man(MatrixObjects):
    def __init__(self,ligne,colonne):
        MatrixObjects.__init__(self,ligne,colonne)



    def SetImages(self,FileUp,FileDown,FileRight,FileLeft):
        self.ImageUp=PhotoImage(FileUp)
        self.ImageDown=PhotoImage(FileDown)
        self.ImageRight=PhotoImage(FileRight)
        self.ImageLeft=PhotoImage(FileLeft)




if __name__ == "__main__":
    M1=Man(1,2)
    print M1.ligne
    print M1.colonne
    fenetre=Tk()
    M1.SetImages(os.getcwd()+"\Images\BombyB.gif",os.getcwd()+"\Images\BombyBackB.gif",os.getcwd()+"\Images\BombyRightB.gif",os.getcwd()+"\Images\BombyLeftB.gif")
    print M1.ImageUp
    print M1.ImageDown
    print M1.ImageRight
    print M1.ImageLeft