from Tkinter import *

fenetre=Tk()
fenetre.title("Go !")
fenetre.geometry("1000x680")
Fond=Canvas(fenetre,width=4000,height=1000,bg="#080001")
Fond.place(x=0,y=0)

F_bloc = PhotoImage(file="mur.gif")
F_vide = PhotoImage(file="vide.gif")
F_perso1 = PhotoImage(file="Bombermanbleu.gif")
F_perso2=PhotoImage(file="Bombermandevant.gif")
F_bombe=PhotoImage(file="bombe.gif")



x, y = 0, 0
fichier = open("niveau.txt")
for ligne in fichier :
    for i in range(25) :
        case = ligne[i]
        if case == '9' :
            Fond.create_image(x,y,image=F_perso2,anchor="nw")
        if case == '8' :
            Fond.create_image(x,y,image=F_perso1,anchor="nw")
        if case == '6' :
            Fond.create_image(x,y,image=F_bombe,anchor="nw")
        if case == '1' :
            Fond.create_image(x,y,image=F_bloc,anchor="nw")
        if case == '0' :
            Fond.create_image(x,y,image=F_vide,anchor="nw")



        x = x + 50
    x = 0
    y = y + 50
fichier.close()

fenetre.mainloop()