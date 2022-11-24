import os
from tkinter import *

from pandas import wide_to_long
from Matchs import Matchs
from Poules import Poules
from JA import JA
from Equipes import Equipes
from Clubs import Clubs
from Affectations import Affectation


class Accueil:
    def __init__(self):
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
        bouton_clubs = Button(self.main_window, text="Clubs", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 15, 'bold'), command=self.open_clubs, height=3, width=50)
        bouton_JA = Button(self.main_window, text="JA", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 15, 'bold'), command=self.open_JA, height=3, width=50)
        bouton_Équipes = Button(self.main_window, text="Équipes", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 15, 'bold'), command=self.open_teams, height=3, width=50)
        # bouton_Rencontres = Button(self.main_window, text="Matchs", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 15, 'bold'), command=self.open_matchs, height=3, width=50)
        # bouton_Affectation = Button(self.main_window, text="Affectation JA", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 15, 'bold'), command=self.open_affectation, height=3, width=50)
        bouton_Poules = Button(self.main_window, text="Poules", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 15, 'bold'), command=self.open_poule, height=3, width=50)
        bouton_Quitter = Button(self.main_window, text="Quitter", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 15, 'bold'), command=self.quit, height=3, width=50)

        #placer les boutons dans la fenetre
        bouton_clubs.place(x = 0, y = 0)
        bouton_JA.place(x = 0, y = 0)
        bouton_Équipes.place(x = 0, y = 0)
        # bouton_Rencontres.place(x = 0, y = 0)
        # bouton_Affectation.place(x = 0, y = 0)
        bouton_Poules.place(x = 0, y = 0)
        bouton_Quitter.place(x = 0, y = 0)


        self.main_window.update()

        bouton_clubs.place(x = 10, y = 10)
        bouton_JA.place(x = 10, y = 10 + bouton_clubs.winfo_height() + 20)
        bouton_Équipes.place(x = 10, y = 10 + bouton_clubs.winfo_height() + bouton_JA.winfo_height() + 40)
        bouton_Poules.place(x = 10, y = 10 + bouton_clubs.winfo_height() + bouton_JA.winfo_height() + bouton_Équipes.winfo_height() + 60)
        bouton_Quitter.place(x = 10, y = self.main_window.winfo_height() - bouton_Quitter.winfo_height()- 10)




    def open_clubs(self):
        self.main_window.destroy()
        Clubs()


    def open_JA(self):
        self.main_window.destroy()
        JA()


    def open_teams(self):
        self.main_window.destroy()
        Equipes()

    
    # def open_matchs(self):
    #     self.main_window.destroy()
    #     Matchs()
    

    # def open_affectation(self):
    #     self.main_window.destroy()
    #     Affectation()


    def open_poule(self):
        self.main_window.destroy()
        Poules()
                    
    
    def quit(self):
        self.main_window.destroy()