from tkinter import *
import os

def Ekip():
        #créer une fenetre
        ekip = Tk()
        #donner un titre a la ekip
        ekip.title("ekips")
        #donner une taille a la ekip
        ekip.geometry("1920x1080")
        #creer une zone de texte pour les ekips
        zone_ekips = Text(ekip, height=1, width=75)
        zone_ekips.grid(row=3, column=2)
        #créer une liste de ekips et les afficher 
        liste_ekips = ["ekip 1", "ekip 2", "ekip 3", "ekip 4", "ekip 5"]
        liste_ekips_afficher = Listbox(ekip, height=5, width=80)
        for i in range(len(liste_ekips)):
            liste_ekips_afficher.insert(i, liste_ekips[i])
        liste_ekips_afficher.grid(row=6, column=2)
    
        def retour():
            # bouton_retour.destroy()
            ekip.destroy()
            os.system("python Interface/Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(ekip, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.grid(row=18, column=2)

    
        #afficher la fenetre
        ekip.attributes('-fullscreen', True)
        ekip.mainloop()

#afficher la fenetre
Ekip()