from threading import Timer
import time
from  MatrixObjects import*
from constantes import*
import Matrix

class Bombe(MatrixObjects):
    def __init__(self,ligne,colonne, matrix):
         MatrixObjects.__init__(self, ligne,colonne)
         self.timer = Timer(CONST_CountDownBombes,self.Explode)
         self.timer.start()
         self.matrix=matrix

    def Explode(self):
        self.matrix.BombeExplodeAt(self.ligne,self.colonne)

class Explosion(MatrixObjects):
    def __init__(self,ligne,colonne, matrix):
         MatrixObjects.__init__(self, ligne,colonne)
         self.timer = Timer(CONST_CountDownExplosion,self.Disappear)
         self.timer.start()
         self.matrix=matrix

    def Disappear(self):
        self.matrix.EndOfExplosion(self.ligne,self.colonne)


if __name__ == '__main__':

    from GameWindow import*
    window=GameWindow()
    x=Bombe(1,1, window.matrix)
    time.sleep(5)
    y=Bombe(2,2, window.matrix)
