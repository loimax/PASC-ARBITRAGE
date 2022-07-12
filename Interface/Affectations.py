from tkinter import *
import os
from tkinter.ttk import Combobox
from utils import *
from re import split

#tableau de 3 colonnes, les deux premieres normales (avec les équipes) et la 3e listes déroulantes pour sélectionner un JA

class Affectation():
    def __init__(self, list_from_matchs):
        self.liste_Rencontres = list_from_matchs
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        #créer une fenetre

        # création des différentes listes
        self.liste_domicile = []
        self.liste_exterieur = []
        self.liste_NumRencontre =[]
        for row in self.liste_Rencontres:
            self.liste_domicile.append(row[0])
            self.liste_exterieur.append(row[1])
            self.liste_NumRencontre.append(row[2])
        
        self.main_window = Tk()
        #donner un titre a la window
        self.main_window.title("Affectations")
        #donner une taille a la Affectation
        self.main_window.geometry("1920x1080")

        self.final_JA_list = []

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
                if i < 1 :
                    self.e.insert(END, self.liste_domicile[j]) 
                else :
                    self.e.insert(END, self.liste_exterieur[j])     
                self.e.config(state="disabled")
                self.final_JA_list.append(Combobox(self.main_window, values=self.liste_JA, font=("Arial", 12)))
                self.final_JA_list[j].place(x=642+184*0.5, y=105+j*20)
                if i%2:
                    self.final_JA_list[j].insert(END, "Juge Arbitre")
                

    def setup_texte(self):
        txt = Label(self.main_window, text="Affectez un arbitre à chaque match :", font=("Arial", 15))
        txt.place(x=642-162, y= 40)
        
        
    def setup_boutons(self):
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_generer = Button(self.main_window, text="Générer", command=self.generer, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
               
        bouton_retour.place(x=0, y=0)
        bouton_generer.place(x=0, y=0)
        bouton_quitter.place(x=0, y=0)

        self.main_window.update()
        bouton_generer.place(x = self.main_window.winfo_width()/2 - bouton_generer.winfo_width()/2, y = 680)
        bouton_retour.place(x = 0.02*self.main_window.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_quitter.place(x = 0.98*self.main_window.winfo_width()-bouton_retour.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())


    def quitter(self):
        close_connection(self.conn)
        self.main_window.destroy()

    def generer(self):
        
        for i in range(len(self.liste_Rencontres)):
            print(self.final_JA_list[i].get())
        
            splitingResultJA = split(' ',self.final_JA_list[i].get())
            splitingResultJA.pop()
            licenceJA = splitingResultJA.pop()
            modify_one_entry(self.conn,self.cursor,"Rencontres","JA",licenceJA,self.liste_NumRencontre[i])
        print("Génération des convocations en cours")
        self.main_window.destroy()

    def retour(self):
        self.main_window.destroy()
        os.system("python Interface/main.py")