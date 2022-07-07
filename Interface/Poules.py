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


        self.choiceniveau = Combobox()
        self.choicepoule = Combobox()
        self.inputannee = Entry()
        self.inputphase = Entry()

        #créer les combobox   

        self.liste_menuderoulant = []

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
        close_connection(self.conn)
        os.system("python Interface/main.py")
    

    def quitter(self):
        close_connection(self.conn)
        self.main_window.destroy()

    def add_phat_table(self, liste_des_equipes):
        for i in range(8):
            txttab = Label(self.main_window, text="      N                   Nom équipe", font=("Arial", 12))
            txttab.place(x=0, y=0)
            self.num_equipe = Entry(self.main_window, font=("Arial", 12), width=3, justify=CENTER)
            self.num_equipe.place(x = 0, y = 0)
            self.num_equipe.insert(END, i+1)      
            self.num_equipe.config(state="disabled")


            self.liste_menuderoulant.append(Combobox(self.main_window, values=liste_des_equipes, font=("Arial", 12)))
            self.liste_menuderoulant[i].bind("<<ComboboxSelected>>", self.updatemenuderoulant(self.liste_menuderoulant[i]))
            self.liste_menuderoulant[i].place(x = 0, y = 0)
            self.liste_menuderoulant[i].insert(END, liste_des_equipes[i])

            self.main_window.update()
            txttab.place(x=self.main_window.winfo_width()/2-txttab.winfo_width()/2 - 50, y= 178)
            self.num_equipe.place(x=self.main_window.winfo_width()/2-self.num_equipe.winfo_width()-self.liste_menuderoulant[i].winfo_width()/2, y=205+i*24)
            self.liste_menuderoulant[i].place(x=self.main_window.winfo_width()/2 - self.liste_menuderoulant[i].winfo_width()/2, y=205+i*24)


            
            

 
    def add_buttons(self):   
        txt = Label(self.main_window, text="Sélectionnez les équipes pour créer une poule :", font=("Arial", 15))
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_creer = Button(self.main_window, text="Créer", command=self.creer, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
        #on crée un bouton valider
        bouton_valider = Button(self.main_window, text="Valider", bg='#AF7AC5', fg='#000000', font=('Arial', 12),command = self.Valider)
        self.choiceniveau = Combobox(self.main_window, font=("Arial", 12), values=["N1", "N2", "N3","PN","R1","R2","R3","PR"], width=5, justify=CENTER)
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
        self.choiceniveau.place(x=0, y=0)
        textniveau.place(x=0, y=0)
        self.choicepoule.place(x=0, y=0)
        textpoule.place(x=0, y=0)
        self.inputannee.place(x=0, y=0)
        textannee.place(x=0, y=0)
        self.inputphase.place(x=0, y=0)
        textphase.place(x=0, y=0)
        self.choiceniveau.insert(END, "R1")
        self.choicepoule.insert(END, "A")
        self.inputannee.insert(END, "2022")
        self.inputphase.insert(END, "1")
        
        
        
        self.main_window.update()
        
        #definitely places widgets
        #top text
        txt.place(x=self.main_window.winfo_width()/2-txt.winfo_width()/2, y= 40)

        #bottom buttons
        bouton_creer.place(x=self.main_window.winfo_width()/2-bouton_creer.winfo_width()/2, y=680)
        bouton_valider.place(x=self.main_window.winfo_width()/2-bouton_creer.winfo_width()/2 + 220, y=112)

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

        bouton_retour.place(x = 0.02*self.main_window.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_quitter.place(x = 0.98*self.main_window.winfo_width()-bouton_retour.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())


    def Valider(self):
        #on recupere les valeurs des champs
        niveau = self.choiceniveau.get()
        poule = self.choicepoule.get()
        annee = self.inputannee.get()
        phase = self.inputphase.get()
        #on affiche les valeurs des champs
        self.liste_equipes = join_table_where_4(self.conn, self.cursor, ["CLUB", "EquipeClub"],
                                              ["CLUB.NumClub", "EquipeClub.numClub"], ["NomClub", "RangEq", "NumEq"], ["Phase", "Année","Poule","Division"],
                                              [phase, annee,poule,niveau])
        self.final_liste_team = []
        for tuple in self.liste_equipes:
            one_team =f"{tuple[0]} {tuple[1]} ({tuple[2]})"
            self.final_liste_team.append(one_team)

        self.final_liste_team.append("EXEMPT")
        self.add_phat_table(self.final_liste_team)
    
    def updatemenuderoulant(self,combobox):
        club_select = combobox.get()
        if club_select != "EXEMPT" and club_select != "":
            self.liste_nom_club.remove(club_select)

    
    def creer(self):
        #faire une liste avec les valeurs des champs
        list_to_send = []
        for i in range(8):
            list_to_send.append(self.liste_menuderoulant[i].get() + " ")
        
        #recup les autres champs
        niveau = self.choiceniveau.get()
        poule = self.choicepoule.get()
        année = self.inputannee.get()
        phase = self.inputphase.get()
        self.main_window.destroy()
        Matchs(list_to_send, niveau, poule, année, phase)