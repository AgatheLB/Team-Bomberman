from threading import Timer
import time
import Matrix
import Man
from constantes import*
from MatrixObjects import*

class Bombe(MatrixObjects):
    def __init__(self,ligne,colonne,matrix):
         MatrixObjects.__init__(self,ligne,colonne)
#         self.timer = Timer(constantes.CONST_CountDown,self.Explode)
         self.timer = Timer(3,self.Explode)
         self.timer.start()
         self.matrix=matrix

    def Explode(self):
        print 'bombe explose en ligne',self.ligne,'et en colonne',self.colonne
        self.matrix.DeleteBombe(self.ligne,self.colonne)

if __name__ == '__main__':
    print 'Got to main'
    x=Bombe(1,1)
    time.sleep(5)
    y=Bombe(2,2)