from tkinter import *
import os

from setuptools import Command

def Affectation():
        #créer une fenetre
        Affectation = Tk()
        #donner un titre a la Affectation
        Affectation.title("Affectations")
        #donner une taille a la Affectation
        Affectation.geometry("1920x1080")
        #creer une zone de texte pour les Affectations
        zone_Affectations = Text(Affectation, height=1, width=75)
        zone_Affectations.grid(row=3, column=2)
        #créer une liste de Affectations et les afficher 
        liste_Affectations = ["Affectation 1", "Affectation 2", "Affectation 3", "Affectation 4", "Affectation 5"]
        liste_Affectations_afficher = Listbox(Affectation, height=5, width=80)
        for i in range(len(liste_Affectations)):
            liste_Affectations_afficher.insert(i, liste_Affectations[i])
        liste_Affectations_afficher.grid(row=6, column=2)
    
        def retour():
            # bouton_retour.destroy()
            Affectation.destroy()
            os.system("python Interface/Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(Affectation, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.grid(row=18, column=2)

    
        #afficher la fenetre
        Affectation.mainloop()

#afficher la fenetre
Affectation()