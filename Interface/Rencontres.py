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
    Rencontre.geometry("1920x1080")
    Rencontre.update()
    print(Rencontre.winfo_width())
    #creer une zone de texte pour les Rencontres
    # zone_Rencontres = Text(Rencontre, height=1, width=75)
    # zone_Rencontres.grid(row=3, column=2)
    # #créer une liste de Rencontres et les afficher 
    liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5"]
    # liste_Rencontres_afficher = Listbox(Rencontre, height=5, width=80)
    # for i in range(len(liste_Rencontres)):
    #     liste_Rencontres_afficher.insert(i, liste_Rencontres[i])
    # liste_Rencontres_afficher.grid(row=6, column=2)

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
                        self.e2 = Combobox(Rencontre, values=liste_Rencontres, font=("Arial", 12))
                        self.e2.place(x=642-203+i*203, y=105+j*20) 
                        #self.e2.insert(END, "Equipe")
                        Rencontre.update()
        
        Table(Rencontre)

    #init objects
    txt = Label(Rencontre, text="Entrez le nombre de rencontres : ", font=("Arial", 15))
    inputbox = Entry(Rencontre, font=("Arial", 15), width=5, justify=CENTER)
    bouton_retour = Button(Rencontre, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_valider = Button(Rencontre, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_creer = Button(Rencontre, text="Créer", command=print_tab, bg='#AF7AC5', fg='#000000', font=('Arial', 12))

    #place objects
    txt.place(x=642-150, y= 40)
    inputbox.place(x=642-30, y= 70)
    bouton_creer.place(x=642-27, y=110)
    bouton_retour.place(x=25, y=680)
    bouton_valider.place(x=1200, y= 680)

    Rencontre.update()
    print(bouton_creer.winfo_width())
    print(inputbox.winfo_width())

    #afficher la fenetre
    Rencontre.attributes('-fullscreen', True)
    Rencontre.mainloop()

#afficher la fenetre
Rencontre()
