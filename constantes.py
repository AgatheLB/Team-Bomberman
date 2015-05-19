import sys

#Valeurs du dimensionnement de la grille
CONST_NbLignes=10+2
CONST_NbColonnes=10+2
CONST_NbBlocsParLigne=3
CONST_ImageSizeInPixels=50

#Valeurs du contenu des cases
CONST_VideAbsolu=100
CONST_VideValue=0
CONST_Bloc=1
CONST_Perso1=8
CONST_Perso2=9
CONST_Bombe=6
CONST_ExplosionMilieu=20
CONST_ExplosionHorizontal=21
CONST_ExplosionVertical=22
CONST_ExplosionFinHaut=23
CONST_ExplosionFinBas=24
CONST_ExplosionFinGauche=25
CONST_ExplosionFinDroit=26

#Valeurs du sens du personnage
CONST_Haut=10
CONST_Bas=11
CONST_Droit=12
CONST_Gauche=13

#Timeur Bombes
CONST_CountDownBombes=3
CONST_CountDownExplosion=2

#Répertoire des Images
if sys.platform.startswith('win32'):
    CONST_ImageDirectory="\\Images\\" ## for windows developper
elif sys.platform.startswith('linux'):
    CONST_ImageDirectory="/Images/"  ## for linux developper


