import pygame
import numpy
import random
import constantes

class Matrix:
    def __init__(self):
        self.grid=self.creatematrice(constantes.CONST_NbLignes,constantes.CONST_NbColonnes)
    def creatematrice(self,ligne,colonne):
     return [[0 for q in range(0,ligne)] for p in range(0,colonne)]
    def getvalue(self,ligne,colonne):
     return self.grid[ligne][colonne]
    def setvalue (self,ligne,colonne,value):
        self.grid[ligne][colonne]=value
    def createrandommatrice (self):
        for ligne in range (constantes.CONST_NbLignes):
            ListCompleted=True
            ListColonnes=[]
            while ListCompleted:
                colonne=random.randint(0,constantes.CONST_NbColonnes-1)
                if not colonne in ListColonnes :
                    ListColonnes.append(colonne)
                    self.setvalue(ligne,colonne,constantes.CONST_BlocValue)
                if len(ListColonnes)==3 :
                    ListCompleted=False

if __name__ == "__main__":
    M1=Matrix()
    print M1
    print M1.grid
    print M1.getvalue(1,2)
    M1.setvalue(1,2,1)
    print M1.getvalue(1,2)
    M1.createrandommatrice()
    print M1.grid