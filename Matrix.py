import pygame
import numpy
import random

class Matrix:
    def __init__(self):
        self.grid=creatematrice(10,10)
    def creatematrice(ligne,colonne):
     return [[0 for q in range(0,ligne)] for p in range(0,colonne)]
    def getvalue(self,ligne,colonne):
     return self.grid[ligne][colonne]
    def setvalue (self,ligne,colonne,value):
        self.grid[ligne][colonne]=value
    def createrandommatrice (self):
        for i in range(10):


if __name__ == "__main__":
    M1=Matrix()
    print M1
    print M1.grid
    print M1.getvalue(1,2)
    M1.setvalue(1,2,1)
    print M1.getvalue(1,2)