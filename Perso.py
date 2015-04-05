# Cr???? par mlefort, le 24/03/2015
from __future__ import division
from lycee import *
from Tkinter import *


bomberman=PhotoImage(file=os.getcwd()+"\Images\Bombermanbleu.gif")
bombe=PhotoImage(file=os.getcwd()+"\Images\bombe.gif")
mur=PhotoImage(file=os.getcwd()+"\Images\mur.gif")



class Perso(object):
   def __init__(self):
      self.bas=PhotoImage(file=os.getcwd()+"\Images\Bombermandevantbleu.gif")
      self.basmarche1=PhotoImage(file=os.getcwd()+"\Images\Bombermandevantmarche1bleu.gif")
      self.basmarche2=PhotoImage(file=os.getcwd()+"\Images\Bombermandevantmarche2bleu.gif")
      self.haut=PhotoImage(file=os.getcwd()+"\Images\Bombermanderrierebleu.gif")
      self.hautmarche1=PhotoImage(file=os.getcwd()+"\Images\Bombermanderrieremarche1bleu.gif")
      self.hautmarche2=PhotoImage(file=os.getcwd()+"\Images\Bombermanderrieremarche2bleu.gif")
      self.gauche=PhotoImage(file=os.getcwd()+"\Images\Bombermangauchebleu.gif")
      self.gauchemarche1=PhotoImage(file=os.getcwd()+"\Images\Bombermangauchemarche1bleu.gif")
      self.gauchemarche2=PhotoImage(file=os.getcwd()+"\Images\Bombermangauchemarche2bleu.gif")
      self.droite=PhotoImage(file=os.getcwd()+"\Images\Bombermandroitebleu.gif")
      self.droitemarche1=PhotoImage(file=os.getcwd()+"\Images\Bombermandroitemarche1bleu.gif")
      self.droitemarche2=PhotoImage(file=os.getcwd()+"\Images\Bombermandroitemarche2bleu.gif")
