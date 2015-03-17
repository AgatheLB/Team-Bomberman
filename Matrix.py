import pygame
import random

#Valeurs du dimensionnement de la grille
CONST_NbLignes=10+2
CONST_NbColonnes=10+2
CONST_NbBlocsParLigne=3
# Valeurs du contenu des cases
CONST_VideValue=0

class Matrix:
    def __init__(self):
        self.grid=self.creatematrice(CONST_NbLignes,CONST_NbColonnes)
    def creatematrice(self,ligne,colonne):
     return [[1 for q in range(0,ligne)] for p in range(0,colonne)]
    def getvalue(self,ligne,colonne):
     return self.grid[ligne][colonne]
    def setvalue (self,ligne,colonne,value):
        self.grid[ligne][colonne]=value
    def createrandommatrice (self):
        for ligne in range (CONST_NbLignes):
            ListCompleted=True
            ListColonnes=[]
            while ListCompleted:
                colonne=random.randint(1,CONST_NbColonnes-2)
                if not colonne in ListColonnes :
                    ListColonnes.append(colonne)
                    self.setvalue(ligne,colonne,CONST_VideValue)
                if len(ListColonnes)==7 :
                    ListCompleted=False
    def CreateRandomPosition(self):
        for i in range (CONST_NbColonnes):
            if self.setvalue.value==0 :
                ListColonnes[0]=8
            else:
                ligne=ligne+1

if __name__ == "__main__":
    M1=Matrix()
    print M1
    print M1.grid
    print M1.getvalue(1,2)
    M1.setvalue(1,2,1)
    print M1.getvalue(1,2)
    M1.createrandommatrice()
    print M1.grid
    M1.CreateRandomPosition()
    print M1.grid