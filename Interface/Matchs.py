from tkinter import *
import os
from functools import partial
from tkinter.ttk import Combobox

#window_height : 701
#window_width : 1284
#faire un tableau avec des listes déroulantes pour choisir l"équipe

def Matchs():

    #créer une fenetre
    window = Tk()
    #donner un titre a la Matchs
    window.title("Matchs")
    #donner une taille a la Matchs
    #window.geometry("1920x1080")
    #taille de la fenetre s'adapte a la taille de l'écran
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

    #créer une liste d'équipes et les afficher 
    liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5"]

    def retour():
        # bouton_retour.destroy()
        window.destroy()
        os.system("python Interface/Accueil.py")

    def quitter():
        window.destroy()


    #créer tableau qui hold les équipes
    class Table:
        def __init__(self,window):
            for i in range(2): 
                for j in range(8): 
                    self.e = Combobox(window, values=liste_Rencontres, font=("Arial", 12))
                    self.e.place(x=642-203+i*203, y=105+j*20)

    Table(window)

    #init objects
    txt = Label(window, text="Voici la feuille de match pour la poule X de X/X/XX", font=("Arial", 15))
    # inputbox = Entry(window, font=("Arial", 15), width=5, justify=CENTER)
    bouton_retour = Button(window, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_valider = Button(window, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_creer = Button(window, text="Créer", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 12))

    #place objects
    txt.place(x=642-189, y= 40)
    # inputbox.place(x=642-30, y= 70)
    bouton_creer.place(x=642-27, y=680)
    bouton_retour.place(x=25, y=680)
    bouton_valider.place(x=1200, y= 680)

    # window.update()
    # print(txt.winfo_width())

    #afficher la fenetre
    window.attributes('-fullscreen', True)
    window.mainloop()

#afficher la fenetre
Matchs()
