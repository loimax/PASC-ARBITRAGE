from tkinter import *
import os
from tkinter.ttk import Combobox

from setuptools import Command

def Affectation():
    #créer une fenetre
    window = Tk()
    #donner un titre a la window
    window.title("Affectations")
    #donner une taille a la Affectation
    window.geometry("1920x1080")
    
    def quitter():
        window.destroy()

    def generer():
        print("Génération des convocations en cours")
        window.destroy()

    #créer une liste de Affectations et les afficher 
    nb_rencontres = 10
    liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5", "Equipe 6", "Equipe 7", "Equipe 8", "Equipe 9", "Equipe 10"]
    liste_JA = ["Damien le Gamin", "Zemmour la pute", "Nezuko-chan", "Arthur le 5e", "LeDave"]
    
    class Table: #Pour faire un tableau
        def __init__(self,Rencontre):
            for i in range(2): 
                for j in range(nb_rencontres):
                    self.e = Entry(Rencontre, font=("Arial", 12))
                    self.e.place(x=642-184*1.5+i*184, y=105+j*20)
                    self.e.insert(END, liste_Rencontres[j])      
                    self.e.config(state="disabled")


            for j in range(nb_rencontres):
                    self.f = Combobox(Rencontre, values=liste_JA, font=("Arial", 12))
                    self.f.place(x=642+184*0.5, y=105+j*20)
                    self.f.insert(END, "Juge Arbitre")
    Table(window)
    
    def retour():
        # bouton_retour.destroy()
        window.destroy()
        os.system("python Interface/Accueil.py")

    #creer UI
    txt = Label(window, text="Affectez un arbitre à chaque match :", font=("Arial", 15))
    bouton_retour = Button(window, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_generer = Button(window, text="Générer", command=generer, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
    bouton_quitter = Button(window, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    

    #afficher UI
    txt.place(x=642-162, y= 40)
    bouton_retour.place(x=25, y=680)
    bouton_generer.place(x=642-38, y=680)
    bouton_quitter.place(x=1200, y=680)

    # window.update()
    # print(bouton_generer.winfo_width())

    #afficher la fenetre
    window.attributes('-fullscreen', True)
    window.mainloop()

#afficher la fenetre
Affectation()