from tkinter import *
import os
from tkinter.ttk import Combobox
from utils import *

#tableau de 3 colonnes, les deux premieres normales (avec les équipes) et la 3e listes déroulantes pour sélectionner un JA

class Affectation():
    def __init__(self, list_from_matchs):
        self.liste_Rencontres = list_from_matchs
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        #créer une fenetre

        print(self.liste_Rencontres)
        
        self.main_window = Tk()
        #donner un titre a la window
        self.main_window.title("Affectations")
        #donner une taille a la Affectation
        self.main_window.geometry("1920x1080")

        #créer une liste de Affectations et les afficher 

        #liste_JA = ["Damien le Gamin", "Zemmour la pute", "Nezuko-chan", "Arthur le 5e", "LeDave"]
        self.liste_JA = creation_liste(self.conn, self.cursor, "JA", ["PrenomJA","NomJA","NumLic"])

        self.setup_texte()
        self.setup_boutons()
        self.creation_tableau()

        self.main_window.attributes('-fullscreen', True)
        self.main_window.mainloop()




        
    def creation_tableau(self):
        for i in range(2): 
            for j in range(len(self.liste_Rencontres)):
                self.e = Entry(self.main_window, font=("Arial", 12))
                self.e.place(x=642-184*1.5+i*184, y=105+j*20)
                self.e.insert(END, self.liste_Rencontres[j])      
                self.e.config(state="disabled")
                self.f = Combobox(self.main_window, values=self.liste_JA, font=("Arial", 12))
                self.f.place(x=642+184*0.5, y=105+j*20)
                self.f.insert(END, "Juge Arbitre")
                

    def setup_texte(self):
        txt = Label(self.main_window, text="Affectez un arbitre à chaque match :", font=("Arial", 15))
        txt.place(x=642-162, y= 40)
        
        
    def setup_boutons(self):
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_generer = Button(self.main_window, text="Générer", command=self.generer, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
               
        bouton_retour.place(x=25, y=680)
        bouton_generer.place(x=642-38, y=680)
        bouton_quitter.place(x=1200, y=680)


    def quitter(self):
        self.main_window.destroy()

    def generer(self):
        print("Génération des convocations en cours")
        self.main_window.destroy()

    def retour(self):
        self.main_window.destroy()
        os.system("python Interface/main.py")