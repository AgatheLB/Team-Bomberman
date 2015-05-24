from threading import Timer
import time
from  MatrixObjects import*
from constantes import*
import Matrix

class Bombe(MatrixObjects):
    def __init__(self,ligne,colonne, matrix):
         MatrixObjects.__init__(self, ligne,colonne)
         self.matrix=matrix
         self.timer = Timer(CONST_CountDownBombes,self.Explode)
         self.timer.start()


    def Explode(self):
        self.matrix.BombeExplodeAt(self.ligne,self.colonne)

class Explosion(MatrixObjects):
    def __init__(self,ligne,colonne, matrix):
        MatrixObjects.__init__(self, ligne,colonne)
        self.matrix=matrix
        self.timer = Timer(CONST_CountDownExplosion,self.Disappear)
        self.timer.start()

    def Disappear(self):
        self.matrix.EndOfExplosion(self.ligne,self.colonne)

