#import pygame

class MatrixObjects:
    def __init__(self,ligne,colonne):
        self.SetPosition(ligne,colonne)

    def SetPosition(self,ligne,colonne):
        self.ligne=ligne
        self.colonne=colonne

    def GetPosition(self):
        return self.ligne,self.colonne

if __name__ == "__main__":
    M1=MatrixObjects(1,2)
    print M1.ligne
    print M1.colonne
    print M1.GetPosition()
