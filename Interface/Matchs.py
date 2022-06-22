from tkinter import *
import os
from functools import partial
from tkinter.ttk import Combobox

from numpy import datetime_as_string

#window_height : 701, nope, dépends de la taille réelle de l'écran
#window_width : 1284, ça aussi

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
    dates_rencontres = ["25/09/2021", "02/10/2021", "23/10/2021", "06/11/2021", "13/11/2021", "27/11/2021", "11/12/2021"]

    def retour():
        # bouton_retour.destroy()
        window.destroy()
        os.system("python Interface/Accueil.py")

    def quitter():
        window.destroy()


    #créer tableau qui hold les équipes
    class Table:
        def __init__(self,window):
            for j in range(7):
                self.e = Entry(window, font=("Arial", 12), width=12, justify=CENTER)
                self.e.place(x=0, y=0)
                self.e.insert(END,dates_rencontres[j])
                #self.e.config(state="disabled")

                self.e2 = Entry(window, font=("Arial", 12), width=5, justify=CENTER)
                self.e2.place(x=0, y=0)
                self.e2.insert(END,j+1)
                self.e2.config(state="disabled")

                self.e3 = Combobox(window, values=liste_Rencontres, font=("Arial", 12))
                self.e3.place(x=0, y=0)

                self.e4 = Combobox(window, values=liste_Rencontres, font=("Arial", 12))
                self.e4.place(x=0, y=0)

                window.update()

                start_array = window.winfo_width()/2-(self.e.winfo_width() + self.e2.winfo_width() + self.e3.winfo_width() + self.e4.winfo_width())/2
                offset_top = 100
                self.e.place(x=start_array, y=offset_top+j*self.e.winfo_height())
                self.e2.place(x=start_array+self.e.winfo_width(), y=offset_top+j*self.e.winfo_height())
                self.e3.place(x=start_array+self.e.winfo_width()+self.e2.winfo_width(), y=offset_top+j*self.e.winfo_height())
                self.e4.place(x=start_array+self.e.winfo_width()+self.e2.winfo_width()+self.e3.winfo_width(), y=offset_top+j*self.e.winfo_height())

    Table(window)

    #init objects
    txt = Label(window, text="Voici la feuille de match pour la poule X de X/X/XX", font=("Arial", 15))
    bouton_creer = Button(window, text="Créer", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
    bouton_retour = Button(window, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_quitter = Button(window, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))

    #pre-place objects
    txt.place(x = 0, y = 0)
    bouton_creer.place(x = 0, y = 0)
    bouton_retour.place(x = 0, y = 0)
    bouton_quitter.place(x = 0, y = 0)

    window.update()

    #placement des widgets en fonction de la fenetre
    txt.place(x = window.winfo_width()/2-txt.winfo_width()/2, y = 50)
    bouton_creer.place(x = window.winfo_width()/2-bouton_creer.winfo_width()/2, y = window.winfo_height()-0.04*window.winfo_height())
    bouton_retour.place(x = 0.02*window.winfo_width(), y = window.winfo_height()-0.04*window.winfo_height())
    bouton_quitter.place(x = 0.98*window.winfo_width()-bouton_retour.winfo_width(), y = window.winfo_height()-0.04*window.winfo_height())

    # window.update()
    # print(txt.winfo_width())

    #afficher la fenetre
    window.attributes('-fullscreen', True)
    window.mainloop()

#afficher la fenetre
Matchs()
