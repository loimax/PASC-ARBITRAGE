
import os
from tkinter import *
from Matchs import Matchs
from Poules import Poules
from JA import JA
from Equipes import Equipes
from Clubs import Clubs
from utils import *


class Accueil:
    def __init__(self):
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        #creer une fenetre
        self.main_window = Tk()

        #donner un titre a la fenetre
        self.main_window.title("Arbitrage")

        #donner une taille a la fenetre
        #self.main_window.geometry("1920x1080")
        #taille de la fenetre s'adapte a la taille de l'ecran
        self.main_window.geometry("{0}x{1}+0+0".format(self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()))

        #mettre un logo a la fenetre
        self.main_window.iconbitmap('Interface/img/logo2.ico')

        self.comite = PhotoImage(file="Interface/img/comite.png")
        self.background_image = PhotoImage(file="Interface/img/pingpong.png")


        # couleur de fond de la fenetre
        # fenetre.configure(background='#DADAD7')

        # setup du contenu
        self.main_window.attributes('-fullscreen', True)
        self.setup_images()
        self.setup_buttons()
        self.main_window.mainloop()







    def setup_images(self):
        #ajouter l'image comite.png a la fenetre en bas à droite
        comite_label = Label(self.main_window, image=self.comite)
        comite_label.place(x = 0, y = 0)
        self.main_window.update()
        comite_label.place(x = self.main_window.winfo_width()-comite_label.winfo_width(),y = self.main_window.winfo_height()-comite_label.winfo_height())
        
        #mettre une image en background a la fenetre
        background_label = Label(self.main_window, image=self.background_image)
        background_label.place(x = 0, y = 0)
        self.main_window.update()
        background_label.place(x = self.main_window.winfo_width()/2+50, y = self.main_window.winfo_height()/2-background_label.winfo_height()/2, relheight=0.5, relwidth=0.5)
            

    def setup_buttons(self):
        #creer 6 boutons
        bouton_clubs = Button(self.main_window, text="Clubs", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=self.open_clubs)
        bouton_JA = Button(self.main_window, text="JA", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=self.open_JA)
        bouton_Équipes = Button(self.main_window, text="Équipes", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=self.open_teams)
        bouton_Rencontres = Button(self.main_window, text="Matchs", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=self.open_matchs)
        bouton_Affectation = Button(self.main_window, text="Affectation JA", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=self.open_affectation)
        bouton_Poules = Button(self.main_window, text="Poules", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=self.open_poule)
        bouton_Quitter = Button(self.main_window, text="Quitter", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=self.quit)

        #placer les boutons dans la fenetre
        bouton_clubs.grid(row=3, column=2)
        bouton_JA.grid(row=6, column=2)
        bouton_Équipes.grid(row=9, column=2)
        bouton_Rencontres.grid(row=12, column=2)
        bouton_Affectation.grid(row=15, column=2)
        bouton_Poules.grid(row=18, column=2)
        bouton_Quitter.grid(row=21, column=2)

        #taille des boutons
        bouton_clubs.config(height=5, width=80)
        bouton_JA.config(height=5, width=80)
        bouton_Équipes.config(height=5, width=80)
        bouton_Rencontres.config(height=5, width=80)
        bouton_Affectation.config(height=5, width=80)
        bouton_Poules.config(height=5, width=80)
        bouton_Quitter.config(height=5, width=80)

        #mettre un espace entre les boutons
        bouton_clubs.grid(padx=10, pady=10)
        bouton_JA.grid(padx=10, pady=10)
        bouton_Équipes.grid(padx=10, pady=10)
        bouton_Rencontres.grid(padx=10, pady=10)
        bouton_Affectation.grid(padx=10, pady=10)
        bouton_Poules.grid(padx=10, pady=10)
        bouton_Quitter.grid(padx=10, pady=10)


    def open_clubs(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, False, True)
        Clubs()


    def open_JA(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, False, True)
        JA()


    def open_teams(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, False, True)
        Equipes()

    
    def open_matchs(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, False, True)
        Matchs()
    

    def open_affectation(self):
        self.main_window.destroy()
        os.system("python Interface/Affectations.py")


    def open_poule(self):
        self.main_window.destroy()
        Poules()
                    
    
    def quit(self):
        self.main_window.destroy()