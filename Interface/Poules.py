import os
from tkinter import *
from tkinter.ttk import Combobox
from utils import *

#window_height : 701
#window_width : 1284
#faire un tableau avec des listes déroulantes pour choisir l"équipe

class Poules():
    def __init__(self):
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        
        #créer une fenetre
        self.main_window = Tk()
        #donner un titre a la fenetre
        self.main_window.title("Poules")
        #donner une taille a la fenetre
        #self.main_window.geometry("1920x1080")
        #taille de la fenetre s'adapte a la taille de l'écran
        self.main_window.geometry("{0}x{1}+0+0".format(self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()))

        self.choiceniveau = Combobox()
        self.choicepoule = Combobox()
        self.inputannee = Entry()
        self.inputphase = Entry()

        #créer une liste d'équipes et les afficher 
        self.liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5", "EXEMPT"]

        self.add_buttons()
        #self.add_phat_table()

        #afficher la fenetre
        self.main_window.attributes('-fullscreen', True)
        self.main_window.mainloop()


    def retour(self):
        # bouton_retour.destroy()
        self.main_window.destroy()
        os.system("python Interface/Accueil.py")
    

    def quitter(self):
        self.main_window.destroy()


    def creer(self):
        print("Creation de la poule")
        self.main_window.destroy()


    def add_phat_table(self, liste_des_equipes):
        for j in range(8): 
            self.e = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
            self.e.place(x = 0, y = 0)
            
            self.e2 = Entry(self.main_window, font=("Arial", 12), width=3, justify=CENTER)
            self.e2.place(x = 0, y = 0)
            self.e2.insert(END, j+1)      
            self.e2.config(state="disabled")
            self.e3 = Combobox(self.main_window, values=[1,2,3,4,5], font=("Arial", 12), width=3)
            self.e3.place(x = 0, y = 0)

            self.main_window.update()
            #definitely placesx=self.main_window.winfo_width()/2-txt.winfo_width()/2
            self.e.place(x=self.main_window.winfo_width()/2-self.e.winfo_width()/2, y=205+j*20)
            self.e2.place(x=self.main_window.winfo_width()/2-self.e2.winfo_width()-self.e.winfo_width()/2, y=205+j*20)
            self.e3.place(x=self.main_window.winfo_width()/2+self.e.winfo_width()/2, y=205+j*20)


    def add_buttons(self):   
        txt = Label(self.main_window, text="Sélectionnez les équipes pour créer une poule :", font=("Arial", 15))
        txttab = Label(self.main_window, text="      N                   Nom équipe                N°e", font=("Arial", 12))
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_creer = Button(self.main_window, text="Créer", command=self.creer, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
        #on crée un bouton valider
        bouton_valider = Button(self.main_window, text="Valider", bg='#AF7AC5', fg='#000000', font=('Arial', 12),command = self.Valider)
        self.choiceniveau = Combobox(self.main_window, font=("Arial", 12), values=["N1","N2","N3","R1","R2","R3","D1","D2","D3","D4","D5"], width=5, justify=CENTER)
        textniveau = Label(self.main_window, text="Niveau", font=("Arial", 12))
        #poules allant de A à P
        self.choicepoule = Combobox(self.main_window, values=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"], font=("Arial", 12), width=5, justify=CENTER)
        textpoule = Label(self.main_window, text="Poule", font=("Arial", 12))
        self.inputannee = Entry(self.main_window, font=("Arial", 12), width=7, justify=CENTER)
        textannee = Label(self.main_window, text="Année", font=("Arial", 12))
        self.inputphase = Entry(self.main_window, font=("Arial", 12), width=7, justify=CENTER)
        textphase = Label(self.main_window, text="Phase", font=("Arial", 12))

        #pre-place objects
        txt.place(x=0, y=0)
        bouton_creer.place(x=0, y=0)
        bouton_retour.place(x=0, y=0)
        bouton_quitter.place(x=0, y=0)
        bouton_valider.place(x=0, y=0)
        txttab.place(x=0, y=0)
        self.choiceniveau.place(x=0, y=0)
        textniveau.place(x=0, y=0)
        self.choicepoule.place(x=0, y=0)
        textpoule.place(x=0, y=0)
        self.inputannee.place(x=0, y=0)
        textannee.place(x=0, y=0)
        self.inputphase.place(x=0, y=0)
        textphase.place(x=0, y=0)
        
        
        
        self.main_window.update()
        
        #definitely places widgets
        #top text
        txt.place(x=self.main_window.winfo_width()/2-txt.winfo_width()/2, y= 40)

        #bottom buttons
        bouton_creer.place(x=self.main_window.winfo_width()/2-bouton_creer.winfo_width()/2, y=680)
        bouton_retour.place(x=25, y=680)
        bouton_quitter.place(x=1200, y= 680)
        bouton_valider.place(x=1000, y=100)

        #input boxes au dessus du tableau
        #niveau
        self.choiceniveau.place(x=self.main_window.winfo_width()/2-self.choiceniveau.winfo_width()/2-50, y= 100)
        textniveau.place(x=self.main_window.winfo_width()/2-textniveau.winfo_width()/2-self.choiceniveau.winfo_width()-textniveau.winfo_width(), y= 100)
        #poule
        self.choicepoule.place(x=self.main_window.winfo_width()/2-self.choicepoule.winfo_width()/2-50, y= 130)
        textpoule.place(x=self.main_window.winfo_width()/2-textpoule.winfo_width()/2-self.choicepoule.winfo_width()-textpoule.winfo_width()-4, y= 130)
        #Année
        textannee.place(x=self.main_window.winfo_width()/2+self.inputannee.winfo_width()/2-30, y= 100)
        self.inputannee.place(x=self.main_window.winfo_width()/2+self.inputannee.winfo_width()/2+textannee.winfo_width()-20, y= 100)
        #Phase
        textphase.place(x=self.main_window.winfo_width()/2+self.inputannee.winfo_width()/2-30, y= 130)
        self.inputphase.place(x=self.main_window.winfo_width()/2+self.inputannee.winfo_width()/2+textannee.winfo_width()-20, y= 130)

        #tableau central
        txttab.place(x=self.main_window.winfo_width()/2-txttab.winfo_width()/2, y= 178)


    def Valider(self):
        #on recupere les valeurs des champs
        niveau = self.choiceniveau.get()
        poule = self.choicepoule.get()
        annee = self.inputannee.get()
        phase = self.inputphase.get()
        #on affiche les valeurs des champs
        print("Niveau : ", niveau)
        print("Poule : ", poule)
        print("Année : ", annee)
        print("Phase : ", phase)
        ListePoule = getListRow(self.conn, self.cursor,"EquipeClub",["Division","Poule"],[niveau,poule])
        print(ListePoule)
        a = getValues(self.conn, self.cursor, "CLUB","NomClub","NumClub",getValuesFromList(ListePoule,1))
        while (len(a) != 8):
            a.append("EXEMPT")
        print(a)
        self.add_phat_table(a)
        return a