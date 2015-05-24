#import pygame

class MatrixObjects:
    def __init__(self,ligne,colonne):
        self.SetPosition(ligne,colonne)

    def SetPosition(self,ligne,colonne):
        self.ligne=ligne
        self.colonne=colonne

    def GetPosition(self):
        return self.ligne,self.colonne


