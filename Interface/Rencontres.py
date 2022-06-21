from tkinter import *
import os
from functools import partial
from tkinter.ttk import Combobox

#window_height : 701
#window_width : 1284
#faire un tableau avec des listes déroulantes pour choisir l"équipe

def Rencontre():

    #créer une fenetre
    Rencontre = Tk()
    #donner un titre a la Rencontre
    Rencontre.title("Rencontres")
    #donner une taille a la Rencontre
    #Rencontre.geometry("1920x1080")
    #taille de la fenetre s'adapte a la taille de l'écran
    Rencontre.geometry("{0}x{1}+0+0".format(Rencontre.winfo_screenwidth(), Rencontre.winfo_screenheight()))

    #créer une liste de Rencontres et les afficher 
    liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5"]

    def retour():
        # bouton_retour.destroy()
        Rencontre.destroy()
        os.system("python Interface/Accueil.py")

    def quitter():
        Rencontre.destroy()

    def print_tab():
        val = inputbox.get()

        #créer tableau qui hold les équipes
        class Table:
            def __init__(self,Rencontre):
                for i in range(2): 
                    for j in range(int(val)): 
                        self.e = Combobox(Rencontre, values=liste_Rencontres, font=("Arial", 12))
                        self.e.place(x=642-203+i*203, y=105+j*20)
                        #self.e2.insert(END, "Equipe")
        if int(val) <= 27:        
            Table(Rencontre)

    #init objects
    txt = Label(Rencontre, text="Entrez le nombre de rencontres : (max 27)", font=("Arial", 15))
    inputbox = Entry(Rencontre, font=("Arial", 15), width=5, justify=CENTER)
    bouton_retour = Button(Rencontre, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_valider = Button(Rencontre, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_creer = Button(Rencontre, text="Créer", command=print_tab, bg='#AF7AC5', fg='#000000', font=('Arial', 12))

    #place objects
    txt.place(x=642-189, y= 40)
    inputbox.place(x=642-30, y= 70)
    bouton_creer.place(x=642-27, y=680)
    bouton_retour.place(x=25, y=680)
    bouton_valider.place(x=1200, y= 680)

    # Rencontre.update()
    # print(txt.winfo_width())

    #afficher la fenetre
    Rencontre.attributes('-fullscreen', True)
    Rencontre.mainloop()

#afficher la fenetre
Rencontre()
