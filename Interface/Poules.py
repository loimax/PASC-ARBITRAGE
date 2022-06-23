import os
from tkinter import *
from tkinter.ttk import Combobox
from webbrowser import get
from Matchs import Matchs
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


        self.liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5", "EXEMPT"]

        self.choiceniveau = Combobox()
        self.choicepoule = Combobox()
        self.inputannee = Entry()
        self.inputphase = Entry()

        #créer les combobox
        self.menuderoulant1 = Combobox()
        self.menuderoulant2 = Combobox()
        self.menuderoulant3 = Combobox()
        self.menuderoulant4 = Combobox()
        self.menuderoulant5 = Combobox()
        self.menuderoulant6 = Combobox()
        self.menuderoulant7 = Combobox()
        self.menuderoulant8 = Combobox()    

        # self.liste_combobox = []
        # self.liste_combobox.append(self.menuderoulant1)
        # self.liste_combobox.append(self.menuderoulant2)
        # print(self.liste_combobox)
        # print(self.liste_combobox[0])

        self.liste_combobox[0]=Combobox(self.main_window, values=self.liste_Rencontres, font=("Arial", 12))
        self.liste_combobox[0].place(x = 0, y = 0)

        #créer une liste d'équipes et les afficher 

        #liste des noms des clubs correspondant a la division et la poule
        self.liste_nom_club = []

        self.add_buttons()
        #self.add_phat_table()

        #afficher la fenetre
        self.main_window.attributes('-fullscreen', True)
        self.main_window.mainloop()


    def retour(self):
        # bouton_retour.destroy()
        self.main_window.destroy()
        os.system("python Interface/main.py")
    

    def quitter(self):
        self.main_window.destroy()


    def creer(self):
        print("Creation de la poule")
        Equipe1 = self.menuderoulant1.get()
        Equipe2 = self.menuderoulant2.get()
        Equipe3 = self.menuderoulant3.get()
        Equipe4 = self.menuderoulant4.get()
        Equipe5 = self.menuderoulant5.get()
        Equipe6 = self.menuderoulant6.get()
        Equipe7 = self.menuderoulant7.get()
        Equipe8 = self.menuderoulant8.get()
        print(Equipe1, Equipe2, Equipe3, Equipe4, Equipe5, Equipe6, Equipe7, Equipe8)
        #faire une liste avec les valeurs des champs
        Matchs([Equipe1, Equipe2, Equipe3, Equipe4, Equipe5, Equipe6, Equipe7, Equipe8])

    def add_phat_table(self, liste_des_equipes):
    
        self.menuderoulant1 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
        # print(self.menuderoulant1.get())
        # print(liste_des_equipes)
        self.menuderoulant1.bind("<<ComboboxSelected>>", self.updatemenuderoulant(self.menuderoulant1))
        #liste_des_equipes.remove(self.menuderoulant1.get())
        self.menuderoulant2 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
        self.menuderoulant2.bind("<<ComboboxSelected>>", self.updatemenuderoulant(self.menuderoulant2))
        self.menuderoulant3 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
        self.menuderoulant3.bind("<<ComboboxSelected>>", self.updatemenuderoulant)
        self.menuderoulant4 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
        self.menuderoulant4.bind("<<ComboboxSelected>>", self.updatemenuderoulant)
        self.menuderoulant5 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
        self.menuderoulant5.bind("<<ComboboxSelected>>", self.updatemenuderoulant)
        self.menuderoulant6 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
        self.menuderoulant6.bind("<<ComboboxSelected>>", self.updatemenuderoulant)
        self.menuderoulant7 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))
        self.menuderoulant7.bind("<<ComboboxSelected>>", self.updatemenuderoulant)
        self.menuderoulant8 = Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12))  
        self.menuderoulant8.bind("<<ComboboxSelected>>", self.updatemenuderoulant)

        self.menuderoulant1.place(x=0, y=0)
        self.menuderoulant2.place(x=0, y=0)
        self.menuderoulant3.place(x=0, y=0)
        self.menuderoulant4.place(x=0, y=0)
        self.menuderoulant5.place(x=0, y=0)
        self.menuderoulant6.place(x=0, y=0)
        self.menuderoulant7.place(x=0, y=0)
        self.menuderoulant8.place(x=0, y=0)


        #definitely placesx=self.main_window.winfo_width()/2-txt.winfo_width()/2
        #self.e.place(x=self.main_window.winfo_width()/2-self.e.winfo_width()/2, y=205+j*20)
        for j in range(8): 
            self.e2 = Entry(self.main_window, font=("Arial", 12), width=3, justify=CENTER)
            self.e2.place(x = 0, y = 0)
            self.e2.insert(END, j+1)      
            self.e2.config(state="disabled")
            self.e3 = Combobox(self.main_window, values=[1,2,3,4,5], font=("Arial", 12), width=3)
            self.e3.place(x = 0, y = 0)
            self.main_window.update()
            self.e2.place(x=self.main_window.winfo_width()/2-self.e2.winfo_width()-self.menuderoulant5.winfo_width()/2, y=205+j*24)
            self.e3.place(x=self.main_window.winfo_width()/2+self.menuderoulant5.winfo_width()/2, y=205+j*24)
            
        self.main_window.update()

        self.menuderoulant1.place(x=self.main_window.winfo_width()/2-self.menuderoulant1.winfo_width()/2, y=205+0*self.menuderoulant1.winfo_height())
        self.menuderoulant2.place(x=self.main_window.winfo_width()/2-self.menuderoulant2.winfo_width()/2, y=205+1*self.menuderoulant2.winfo_height())
        self.menuderoulant3.place(x=self.main_window.winfo_width()/2-self.menuderoulant3.winfo_width()/2, y=205+2*self.menuderoulant3.winfo_height())
        self.menuderoulant4.place(x=self.main_window.winfo_width()/2-self.menuderoulant4.winfo_width()/2, y=205+3*self.menuderoulant4.winfo_height())
        self.menuderoulant5.place(x=self.main_window.winfo_width()/2-self.menuderoulant5.winfo_width()/2, y=205+4*self.menuderoulant5.winfo_height())
        self.menuderoulant6.place(x=self.main_window.winfo_width()/2-self.menuderoulant6.winfo_width()/2, y=205+5*self.menuderoulant6.winfo_height())
        self.menuderoulant7.place(x=self.main_window.winfo_width()/2-self.menuderoulant7.winfo_width()/2, y=205+6*self.menuderoulant7.winfo_height())
        self.menuderoulant8.place(x=self.main_window.winfo_width()/2-self.menuderoulant8.winfo_width()/2, y=205+7*self.menuderoulant8.winfo_height())

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
        self.liste_nom_club = getValues(self.conn, self.cursor, "CLUB","NomClub","NumClub",getValuesFromList(ListePoule,1))
        
        self.liste_nom_club.append("EXEMPT")
        print(self.liste_nom_club)
        self.add_phat_table(self.liste_nom_club)
    
    def updatemenuderoulant(self,combobox):
        club_select = combobox.get()
        print('club_select = ', club_select)
        if club_select != "EXEMPT" and club_select != "":
            self.liste_nom_club.remove(club_select)
        print("Oh ! Selected")
      
    

        

