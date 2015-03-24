# Créé par mlefort, le 24/03/2015
from __future__ import division
from lycee import *
from Tkinter import *


bomberman=PhotoImage(file="Bombermanbleu.gif")
bombe=PhotoImage(file="bombe.gif")
mur=PhotoImage(file="mur.gif")



class Perso(object):
   def __init__(self):
      self.bas=PhotoImage(file="Bombermandevantbleu.gif")
      self.basmarche1=PhotoImage(file="Bombermandevantmarche1bleu.gif")
      self.basmarche2=PhotoImage(file="Bombermandevantmarche2bleu.gif")
      self.haut=PhotoImage(file="Bombermanderrierebleu.gif")
      self.hautmarche1=PhotoImage(file="Bombermanderrieremarche1bleu.gif")
      self.hautmarche2=PhotoImage(file="Bombermanderrieremarche2bleu.gif")
      self.gauche=PhotoImage(file="Bombermangauchebleu.gif")
      self.gauchemarche1=PhotoImage(file="Bombermangauchemarche1bleu.gif")
      self.gauchemarche2=PhotoImage(file="Bombermangauchemarche2bleu.gif")
      self.droite=PhotoImage(file="Bombermandroitebleu.gif")
      self.droitemarche1=PhotoImage(file="Bombermandroitemarche1bleu.gif")
      self.droitemarche2=PhotoImage(file="Bombermandroitemarche2bleu.gif")
