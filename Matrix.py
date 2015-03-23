import pygame
import random
import constantes
from Man import*

class Matrix:
    def __init__(self):
        self.grid=self.CreateMatrice(constantes.CONST_NbLignes,constantes.CONST_NbColonnes)

    def CreateMatrice(self,ligne,colonne):
     return [[1 for q in range(0,ligne)] for p in range(0,colonne)]

    def GetValue(self,ligne,colonne):
     return self.grid[ligne][colonne]

    def SetValue (self,ligne,colonne,value):
        self.grid[ligne][colonne]=value

    def CreateRandomMatrice (self):
        for ligne in range (1,constantes.CONST_NbLignes-1):
            ListCompleted=True
            ListColonnes=[]
            while ListCompleted:
                colonne=random.randint(1,constantes.CONST_NbColonnes-2)
                if not colonne in ListColonnes :
                    ListColonnes.append(colonne)
                    self.SetValue(ligne,colonne,constantes.CONST_VideValue)
                if len(ListColonnes)==7 :
                    ListCompleted=False

    def CreateRandomPosition1(self):
        for c in range(constantes.CONST_NbColonnes):
            for l in range (constantes.CONST_NbLignes):
                if self.grid[l][c]==constantes.CONST_VideValue :
                    self.grid[l][c]=constantes.CONST_Perso1
                    self.Bomby1=Man(l,c)
                    return

    def CreateRandomPosition2(self):
        for c in range(constantes.CONST_NbColonnes-1,0,-1):
            for l in range (constantes.CONST_NbLignes-1,0,-1):
                if self.grid[l][c]==constantes.CONST_VideValue :
                    self.grid[l][c]=constantes.CONST_Perso2
                    self.Bomby2=Man(l,c)
                    return

    def Bomby1Up(self):
        print "Bomby1Up"
    def Bomby1Left(self):
        print "Bomby1Left"
    def Bomby1Down(self):
        print "Bomby1Down"
    def Bomby1Right(self):
        print "Bomby1Right"
    def Bomby2Up(self):
        print "Bomby2Up"
    def Bomby2Left(self):
        print "Bomby2Left"
    def Bomby2Down(self):
        print "Bomby2Down"
    def Bomby2Right(self):
        print "Bomby2Right"

if __name__ == "__main__":
    M1=Matrix()
    print 'initialisation'
    print M1.grid
    print M1.GetValue(1,2)
    M1.SetValue(1,2,1)
    print M1.GetValue(1,2)
    print 'initialisation blocs et cases vides'
    M1.CreateRandomMatrice()
    print M1.grid
    print 'initilisation personnage'
    M1.CreateRandomPosition1()
    M1.CreateRandomPosition2()
    print M1.grid