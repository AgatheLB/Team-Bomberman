import pygame
import Matrix
import Man
from MatrixObjects import*


class Bombe(MatrixObjects):
    def __init__(self,ligne,colonne):
         MatrixObjects.__init__(self,ligne,colonne)
