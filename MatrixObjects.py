import pygame

class MatrixObjects:
    def __init__(self,ligne,colonne):
        self.x=ligne
        self.y=colonne


if __name__ == "__main__":
    M1=MatrixObjects(1,2)
    print M1.x
    print M1.y
