from tkinter import *
import os
from tkinter.ttk import Combobox

#window_height : 701
#window_width : 1284
#faire un tableau avec des listes déroulantes pour choisir l"équipe

def Poules():

    #créer une fenetre
    window = Tk()
    #donner un titre a la fenetre
    window.title("Poules")
    #donner une taille a la fenetre
    window.geometry("1920x1080")

    #créer une liste d'équipes et les afficher 
    liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5", "EXEMPT"]

    def retour():
        # bouton_retour.destroy()
        window.destroy()
        os.system("python Interface/Accueil.py")

    def quitter():
        window.destroy()

    def creer():
        print("Creation de la poule")
        window.destroy()

    #créer tableau pour hold les équipes de la poule
    class Table:
        def __init__(self,window):
            for j in range(8): 
                self.e = Combobox(window, values=liste_Rencontres, font=("Arial", 12))
                self.e.place(x = 0, y = 0)
                
                self.e2 = Entry(window, font=("Arial", 12), width=3, justify=CENTER)
                self.e2.place(x = 0, y = 0)
                self.e2.insert(END, j+1)      
                self.e2.config(state="disabled")

                self.e3 = Combobox(window, values=[1,2,3,4,5], font=("Arial", 12), width=3)
                self.e3.place(x = 0, y = 0)

                window.update()
                #definitely placesx=window.winfo_width()/2-txt.winfo_width()/2
                self.e.place(x=window.winfo_width()/2-self.e.winfo_width()/2, y=205+j*20)
                self.e2.place(x=window.winfo_width()/2-self.e2.winfo_width()-self.e.winfo_width()/2, y=205+j*20)
                self.e3.place(x=window.winfo_width()/2+self.e.winfo_width()/2, y=205+j*20)
                    
                    


    #init objects
    txt = Label(window, text="Sélectionnez les équipes pour créer une poule :", font=("Arial", 15))
    txttab = Label(window, text="      N                   Nom équipe                N°e", font=("Arial", 12))

    
    bouton_retour = Button(window, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_valider = Button(window, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_creer = Button(window, text="Créer", command=creer, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
    choiceniveau = Combobox(window, font=("Arial", 12), values=["N1","N2","N3","R1","R2","R3","D1","D2","D3","D4","D5"], width=5, justify=CENTER)
    textniveau = Label(window, text="Niveau", font=("Arial", 12))
    choicepoule = Combobox(window, values=["Poule 1", "Poule 2", "Poule 3"], font=("Arial", 12), width=5, justify=CENTER)
    textpoule = Label(window, text="Poule", font=("Arial", 12))
    inputannee = Entry(window, font=("Arial", 12), width=7, justify=CENTER)
    textannee = Label(window, text="Année", font=("Arial", 12))
    inputphase = Entry(window, font=("Arial", 12), width=7, justify=CENTER)
    textphase = Label(window, text="Phase", font=("Arial", 12))

    #pre-place objects
    txt.place(x=0, y=0)
    bouton_creer.place(x=0, y=0)
    bouton_retour.place(x=0, y=0)
    bouton_valider.place(x=0, y=0)
    txttab.place(x=0, y=0)
    choiceniveau.place(x=0, y=0)
    textniveau.place(x=0, y=0)
    choicepoule.place(x=0, y=0)
    textpoule.place(x=0, y=0)
    inputannee.place(x=0, y=0)
    textannee.place(x=0, y=0)
    inputphase.place(x=0, y=0)
    textphase.place(x=0, y=0)


    window.update()

    #definitely places widgets
    #top text
    txt.place(x=window.winfo_width()/2-txt.winfo_width()/2, y= 40)

    #bottom buttons
    bouton_creer.place(x=window.winfo_width()/2-bouton_creer.winfo_width()/2, y=680)
    bouton_retour.place(x=25, y=680)
    bouton_valider.place(x=1200, y= 680)

    #input boxes au dessus du tableau
    #niveau
    choiceniveau.place(x=window.winfo_width()/2-choiceniveau.winfo_width()/2-50, y= 100)
    textniveau.place(x=window.winfo_width()/2-textniveau.winfo_width()/2-choiceniveau.winfo_width()-textniveau.winfo_width(), y= 100)
    #poule
    choicepoule.place(x=window.winfo_width()/2-choicepoule.winfo_width()/2-50, y= 130)
    textpoule.place(x=window.winfo_width()/2-textpoule.winfo_width()/2-choicepoule.winfo_width()-textpoule.winfo_width()-4, y= 130)
    #Année
    textannee.place(x=window.winfo_width()/2+inputannee.winfo_width()/2-30, y= 100)
    inputannee.place(x=window.winfo_width()/2+inputannee.winfo_width()/2+textannee.winfo_width()-20, y= 100)
    #Phase
    textphase.place(x=window.winfo_width()/2+inputannee.winfo_width()/2-30, y= 130)
    inputphase.place(x=window.winfo_width()/2+inputannee.winfo_width()/2+textannee.winfo_width()-20, y= 130)

    #tableau central
    txttab.place(x=window.winfo_width()/2-txttab.winfo_width()/2, y= 178)
    Table(window)

    
    # window.update()
    # print(txt.winfo_width())

    #afficher la fenetre
    window.attributes('-fullscreen', True)
    window.mainloop()

#afficher la fenetre
Poules()
