from Tkinter import*
from MatrixObjects import *


class Man(MatrixObjects):
    def __init__(self,ligne,colonne,sens):
        MatrixObjects.__init__(self,ligne,colonne)
        self.sens=sens



