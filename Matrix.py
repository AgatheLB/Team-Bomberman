# -*- coding: utf-8 -*-
#import pygame
import random
import time
import os
from Tkinter import*
from constantes import*
from Man import*
from GameWindow import*
from Bombes import*


class Matrix:
    def __init__(self, gamewindow):
        self.grid=self.CreateMatrice(CONST_NbLignes,CONST_NbColonnes)
        self.ImageWindow=gamewindow.ImageWindow
        self.gamewindow=gamewindow
        self.ImageBloc = PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"Wall.gif")
        self.ImageVide = PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"Vide.gif")
        self.ImageBomby1=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyB.gif")
        self.ImageBomby1Left=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyLeftB.gif")
        self.ImageBomby1Right=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyRightB.gif")
        self.ImageBomby1Back=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyBackB.gif")
        self.ImageBomby2=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyR.gif")
        self.ImageBomby2Left=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyLeftR.gif")
        self.ImageBomby2Right=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyRightR.gif")
        self.ImageBomby2Back=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"BombyBackR.gif")
        self.ImageBombe=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"Bombe.gif")
        self.ImageExplosionMilieu=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"explosionmilieu.gif")
        self.ImageExplosionHorizontal=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"explosionhorizontal.gif")
        self.ImageExplosionVertical=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"explosionvertical.gif")
        self.ImageExplosionFinDroit=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"explosionfindroit.gif")
        self.ImageExplosionFinGauche=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"explosionfingauche.gif")
        self.ImageExplosionFinHaut=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"explosionfinhaut.gif")
        self.ImageExplosionFinBas=PhotoImage(file=os.getcwd()+CONST_ImageDirectory+"explosionfinbas.gif")
        self.CreateRandomMatrice()
        self.CreateRandomPosition1()
        self.CreateRandomPosition2()
        self.PrintImages()


    def CreateMatrice(self,ligne,colonne):
     return [[1 for q in range(0,ligne)] for p in range(0,colonne)]

    def GetValue(self,ligne,colonne):
        if ligne>=0 and ligne<CONST_NbLignes:
            if colonne>=0 and colonne<CONST_NbColonnes:
                 return self.grid[ligne][colonne]
        return CONST_VideAbsolu

    def SetValue (self,ligne,colonne,value):
        self.grid[ligne][colonne]=value

    def CreateRandomMatrice (self):
        for ligne in range (1,CONST_NbLignes-1):
            ListCompleted=True
            ListColonnes=[]
            while ListCompleted:
                colonne=random.randint(1,CONST_NbColonnes-2)
                if not colonne in ListColonnes :
                    ListColonnes.append(colonne)
                    self.SetValue(ligne,colonne,CONST_VideValue)
                if len(ListColonnes)==7 :
                    ListCompleted=False

    def CreateRandomPosition1(self):
        for c in range(CONST_NbColonnes):
            for l in range (CONST_NbLignes):
                if self.grid[l][c]==CONST_VideValue :
                    self.Bomby1=Man(l,c,CONST_Bas)
                    self.Bomby1.SetImages(os.getcwd()+CONST_ImageDirectory+"BombyB.gif",os.getcwd()+CONST_ImageDirectory+"BombyBackB.gif",os.getcwd()+CONST_ImageDirectory+"BombyRightB.gif",os.getcwd()+CONST_ImageDirectory+"BombyLeftB.gif")
                    return

    def CreateRandomPosition2(self):
        for c in range(CONST_NbColonnes-1,0,-1):
            for l in range (CONST_NbLignes-1,0,-1):
                if self.GetValue(l, c)==CONST_VideValue :
                    self.Bomby2=Man(l,c,CONST_Bas)
                    self.Bomby2.SetImages(os.getcwd()+CONST_ImageDirectory+"BombyR.gif",os.getcwd()+CONST_ImageDirectory+"BombyBackR.gif",os.getcwd()+CONST_ImageDirectory+"BombyRightR.gif",os.getcwd()+CONST_ImageDirectory+"BombyLeftR.gif")
                    return

    def Reinitialisation(self):
       self.grid=self.CreateMatrice(CONST_NbLignes,CONST_NbColonnes)
       self.CreateRandomMatrice()
       self.CreateRandomPosition1()
       self.CreateRandomPosition2()
       self.PrintImages()


    def IsEmptyCase (self,ligne,colonne):
        if self.GetValue(ligne,colonne)==0 :
            posBomby1=self.Bomby1.GetPosition()
            posBomby2=self.Bomby2.GetPosition()
            if posBomby1[0]!=ligne or posBomby1[1]!=colonne:
                if posBomby2[0]!=ligne or posBomby2[1]!=colonne:
                    return True
        return False

    def IsBombyHere(self,ligne,colonne,man):
        if man.ligne==ligne :
            if abs(man.ligne-ligne)>2:
                return False
        if man.colonne==colonne:
            if abs(man.colonne-colonne)>2:
                return False
        return True

    def Bomby1Up(self):
        if self.IsEmptyCase(self.Bomby1.ligne-1,self.Bomby1.colonne):
            self.Bomby1.SetPosition(self.Bomby1.ligne-1,self.Bomby1.colonne)
            self.Bomby1.sens=CONST_Haut
        self.PrintImages()


    def Bomby1Left(self):
        if self.IsEmptyCase(self.Bomby1.ligne,self.Bomby1.colonne-1):
            self.Bomby1.SetPosition(self.Bomby1.ligne,self.Bomby1.colonne-1)
            self.Bomby1.sens=CONST_Gauche
        self.PrintImages()

    def Bomby1Down(self):
        if self.IsEmptyCase(self.Bomby1.ligne+1,self.Bomby1.colonne):
            self.Bomby1.SetPosition(self.Bomby1.ligne+1,self.Bomby1.colonne)
            self.Bomby1.sens=CONST_Bas
        self.PrintImages()

    def Bomby1Right(self):
        if self.IsEmptyCase(self.Bomby1.ligne,self.Bomby1.colonne+1):
            self.Bomby1.SetPosition(self.Bomby1.ligne,self.Bomby1.colonne+1)
            self.Bomby1.sens=CONST_Droit
        self.PrintImages()


    def Bomby2Up(self):
        if self.IsEmptyCase(self.Bomby2.ligne-1,self.Bomby2.colonne):
            self.Bomby2.SetPosition(self.Bomby2.ligne-1,self.Bomby2.colonne)
            self.Bomby2.sens=CONST_Haut
        self.PrintImages()


    def Bomby2Left(self):
        if self.IsEmptyCase(self.Bomby2.ligne,self.Bomby2.colonne-1):
            self.Bomby2.SetPosition(self.Bomby2.ligne,self.Bomby2.colonne-1)
            self.Bomby2.sens=CONST_Gauche
        self.PrintImages()

    def Bomby2Down(self):
        if self.IsEmptyCase(self.Bomby2.ligne+1,self.Bomby2.colonne):
            self.Bomby2.SetPosition(self.Bomby2.ligne+1,self.Bomby2.colonne)
            self.Bomby2.sens=CONST_Bas
        self.PrintImages()

    def Bomby2Right(self):
        if self.IsEmptyCase(self.Bomby2.ligne,self.Bomby2.colonne+1):
            self.Bomby2.SetPosition(self.Bomby2.ligne,self.Bomby2.colonne+1)
            self.Bomby2.sens=CONST_Droit
        self.PrintImages()

    def SetBombe(self,aBomby):
        if aBomby.sens==CONST_Gauche:
            targetLigne=aBomby.ligne
            targetColonne=aBomby.colonne-1
        if aBomby.sens==CONST_Droit:
            targetLigne=aBomby.ligne
            targetColonne=aBomby.colonne+1
        if aBomby.sens==CONST_Haut:
            targetLigne=aBomby.ligne-1
            targetColonne=aBomby.colonne
        if aBomby.sens==CONST_Bas:
            targetLigne=aBomby.ligne+1
            targetColonne=aBomby.colonne

        if self.IsEmptyCase(targetLigne,targetColonne):
            self.grid[targetLigne][targetColonne]=CONST_Bombe
            bombe=Bombe(targetLigne,targetColonne,self)
        self.PrintImages()


    def BombeExplodeAt(self,ligne,colonne):

        #ici, il faut placer :
        # - l'affichage de l'explosion sur plusieurs cases
        # - la vérification qu'un Bomberman aurait été tué
        # - le retour à l'affichage normal
        # la fin du jeu si un Bomberman est mort --> Réinitialiser ??

        self.grid[ligne][colonne]=CONST_ExplosionMilieu
        if self.IsEmptyCase(ligne,colonne-1):
            self.grid[ligne][colonne-1]=CONST_ExplosionHorizontal
            if self.IsEmptyCase(ligne,colonne-2):
                self.grid[ligne][colonne-2]=CONST_ExplosionFinGauche
        if self.IsEmptyCase(ligne,colonne+1):
            self.grid[ligne][colonne+1]=CONST_ExplosionHorizontal
            if self.IsEmptyCase(ligne,colonne+2):
                self.grid[ligne][colonne+2]=CONST_ExplosionFinDroit
        if self.IsEmptyCase(ligne-1,colonne):
            self.grid[ligne-1][colonne]=CONST_ExplosionVertical
            if self.IsEmptyCase(ligne-2,colonne):
                self.grid[ligne-2][colonne]=CONST_ExplosionFinHaut
        if self.IsEmptyCase(ligne+1,colonne):
            self.grid[ligne+1][colonne]=CONST_ExplosionVertical
            if self.IsEmptyCase(ligne+2,colonne):
                self.grid[ligne+2][colonne]=CONST_ExplosionFinBas
        self.PrintImages()
        explosion=Explosion(ligne,colonne,self)


    def EndOfExplosion(self,ligne,colonne):
        if self.GetValue(ligne,colonne) in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne][colonne]=CONST_VideValue
        if self.GetValue(ligne,colonne-1)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne][colonne-1]=CONST_VideValue
        if self.GetValue(ligne,colonne+1)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne][colonne+1]=CONST_VideValue
        if self.GetValue(ligne-1,colonne)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne-1][colonne]=CONST_VideValue
        if self.GetValue(ligne+1,colonne)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne+1][colonne]=CONST_VideValue
        if self.GetValue(ligne-2,colonne)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne-2][colonne]=CONST_VideValue
        if self.GetValue(ligne+2,colonne)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne+2][colonne]=CONST_VideValue
        if self.GetValue(ligne,colonne-2)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne][colonne-2]=CONST_VideValue
        if self.GetValue(ligne,colonne+2)in (CONST_ExplosionMilieu,CONST_ExplosionVertical,CONST_ExplosionHorizontal,CONST_ExplosionFinHaut,CONST_ExplosionFinBas,CONST_ExplosionFinGauche,CONST_ExplosionFinDroit):
            self.grid[ligne][colonne+2]=CONST_VideValue

        self.PrintImages()
#        if self.IsBombyHere(ligne,colonne,self.Bomby1) or self.IsBombyHere(ligne,colonne,self.Bomby2) :
#            self.gamewindow.EndOfGame()

    def PrintImages (self):
        for l in range(CONST_NbLignes) :
            for c in range (CONST_NbColonnes):
                case = self.GetValue(l, c)
                if case == CONST_Bombe :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageBombe,anchor="nw")
                if case == CONST_Bloc :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageBloc,anchor="nw")
                if case == CONST_VideValue :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageVide,anchor="nw")
                if case == CONST_ExplosionMilieu :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageExplosionMilieu,anchor="nw")
                if case == CONST_ExplosionHorizontal :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageExplosionHorizontal,anchor="nw")
                if case == CONST_ExplosionVertical :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageExplosionVertical,anchor="nw")
                if case == CONST_ExplosionFinHaut :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageExplosionFinHaut,anchor="nw")
                if case == CONST_ExplosionFinBas :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageExplosionFinBas,anchor="nw")
                if case == CONST_ExplosionFinGauche :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageExplosionFinGauche,anchor="nw")
                if case == CONST_ExplosionFinDroit :
                    self.ImageWindow.create_image(self.CalculPositionCaseX(c),self.CalculPositionCaseY(l),image=self.ImageExplosionFinDroit,anchor="nw")

        #Affichage Bomby1:
        posBomby1=self.Bomby1.GetPosition()
        if self.Bomby1.sens==CONST_Bas:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1,anchor="nw")
        if self.Bomby1.sens==CONST_Haut:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1Back,anchor="nw")
        if self.Bomby1.sens==CONST_Droit:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1Right,anchor="nw")
        if self.Bomby1.sens==CONST_Gauche:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby1[1]),self.CalculPositionCaseY(posBomby1[0]),image=self.ImageBomby1Left,anchor="nw")
        #Affiche Bomby2
        posBomby2=self.Bomby2.GetPosition()
        if self.Bomby2.sens==CONST_Bas:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2,anchor="nw")
        if self.Bomby2.sens==CONST_Haut:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2Back,anchor="nw")
        if self.Bomby2.sens==CONST_Droit:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2Right,anchor="nw")
        if self.Bomby2.sens==CONST_Gauche:
            self.ImageWindow.create_image(self.CalculPositionCaseX(posBomby2[1]),self.CalculPositionCaseY(posBomby2[0]),image=self.ImageBomby2Left,anchor="nw")

    def CalculPositionCase(self,ligne,colonne):
        x=colonne*CONST_ImageSizeInPixels
        y=ligne*CONST_ImageSizeInPixels
        return x,y

    def CalculPositionCaseX(self,colonne):
        x=colonne*CONST_ImageSizeInPixels
        return x

    def CalculPositionCaseY(self,ligne):
        y=ligne*CONST_ImageSizeInPixels
        return y

if __name__ == "__main__":

    from GameWindow import*

    root=Tk()
    gw = GameWindow()
    M1=gw.matrix
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
    M1.SetBombe(M1.Bomby1)
    time.sleep(5)
    M1.SetBombe(M1.Bomby2)


