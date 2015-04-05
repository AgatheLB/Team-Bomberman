# -*- coding: utf-8 -*-
import pygame
import random
import constantes
from Man import*
from Tkinter import*
import os


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
                    self.Bomby1.SetImages(os.getcwd()+"\Images\BombyB.gif",os.getcwd()+"\Images\BombyBackB.gif",os.getcwd()+"\Images\BombyRightB.gif",os.getcwd()+"\Images\BombyLeftB.gif")
                    return

    def CreateRandomPosition2(self):
        for c in range(constantes.CONST_NbColonnes-1,0,-1):
            for l in range (constantes.CONST_NbLignes-1,0,-1):
                if self.grid[l][c]==constantes.CONST_VideValue :
                    self.grid[l][c]=constantes.CONST_Perso2
                    self.Bomby2=Man(l,c)
                    self.Bomby2.SetImages(os.getcwd()+"\Images\BombyB.gif",os.getcwd()+"\Images\BombyBackB.gif",os.getcwd()+"\Images\BombyRightB.gif",os.getcwd()+"\Images\BombyLeftB.gif")
                    return

    def Bomby1Up(self):
        if self.grid[self.Bomby1.ligne-1][self.Bomby1.colonne]==0:
            self.Bomby1.SetPosition(self.Bomby1.ligne-1,self.Bomby1.colonne)
        else :
            print "Bomby1 ne peut pas se deplacer(monter)"
    def Bomby1Left(self):
        if self.grid[self.Bomby1.ligne][self.Bomby1.colonne-1]==0:
            self.Bomby1.SetPosition(self.Bomby1.ligne,self.Bomby1.colonne-1)
        else :
            print "Bomby1 ne peut pas se deplacer(gauche)"
    def Bomby1Down(self):
        if self.grid[self.Bomby1.ligne+1][self.Bomby1.colonne]==0:
            self.Bomby1.SetPosition(self.Bomby1.ligne+1,self.Bomby1.colonne)
        else :
            print "Bomby1 ne peut pas se deplacer(descendre)"
    def Bomby1Right(self):
        if self.grid[self.Bomby1.ligne][self.Bomby1.colonne+1]==0:
            self.Bomby1.SetPosition(self.Bomby1.ligne,self.Bomby1.colonne+1)
        else :
            print "Bomby1 ne peut pas se deplacer(droit)"
    def Bomby2Up(self):
        if self.grid[self.Bomby2.ligne-1][self.Bomby2.colonne]==0:
            self.Bomby2.SetPosition(self.Bomby2.ligne-1,self.Bomby2.colonne)
        else :
            print "Bomby2 ne peut pas se deplacer(monter)"
    def Bomby2Left(self):
        if self.grid[self.Bomby2.ligne][self.Bomby2.colonne-1]==0:
            self.Bomby2.SetPosition(self.Bomby2.ligne,self.Bomby2.colonne-1)
        else :
            print "Bomby2 ne peut pas se deplacer(gauche)"
    def Bomby2Down(self):
        if self.grid[self.Bomby2.ligne+1][self.Bomby2.colonne]==0:
            self.Bomby2.SetPosition(self.Bomby2.ligne+1,self.Bomby2.colonne)
        else :
            print "Bomby2 ne peut pas se deplacer(descendre)"
    def Bomby2Right(self):
        if self.grid[self.Bomby2.ligne][self.Bomby2.colonne+1]==0:
            self.Bomby2.SetPosition(self.Bomby2.ligne,self.Bomby2.colonne+1)
        else :
            print "Bomby2 ne peut pas se deplacer(droite)"

#    def Bomby1SetBombe(self):
#    def Bomby2SetBombe(self):

if __name__ == "__main__":
    root=Tk()
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
    print (__file__)
    print os.path.join(os.getcwd(),__file__)
    print os.getcwd()