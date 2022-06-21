from tkinter import *
import os

def Ekip():
    #créer une fenetre
    window = Tk()
    #donner un titre a la ekip
    window.title("ekips")
    #donner une taille a la ekip
    #window.geometry("1920x1080")
    #taille de la fenetre s'adapte a la taille de l'ecran
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    #creer une zone de texte pour les ekips
    # zone_ekips = Text(ekip, height=1, width=75)
    # zone_ekips.grid(row=3, column=2)
    # #créer une liste de ekips et les afficher 
    # liste_ekips = ["ekip 1", "ekip 2", "ekip 3", "ekip 4", "ekip 5"]
    # liste_ekips_afficher = Listbox(ekip, height=5, width=80)
    # for i in range(len(liste_ekips)):
    #     liste_ekips_afficher.insert(i, liste_ekips[i])
    # liste_ekips_afficher.grid(row=6, column=2)

    def quitter():
        # bouton_retour.destroy()
        window.destroy()

    def retour():
        # bouton_retour.destroy()
        window.destroy()
        os.system("python Interface/Accueil.py")


    liste_Rencontres = ["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4", "Equipe 5", "Equipe 6", "Equipe 7", "Equipe 8", "Equipe 9", "Equipe 10"]
    liste_clubs = ["Club 1", "Club 2", "Club 3", "Club 4", "Club 5", "Club 6", "Club 7", "Club 8", "Club 9", "Club 10"]
    
    nb_equipes = 10

    class Table: #Pour faire un tableau
        def __init__(self,Rencontre):
            for i in range(2): 
                for j in range(nb_equipes):
                    self.e = Entry(Rencontre, font=("Arial", 12))
                    self.e.place(x=642-184*1.5+i*184, y=105+j*20)
                    self.e.insert(END, liste_Rencontres[j])      
                    self.e.config(state="disabled")

            for j in range(nb_equipes):
                self.e = Entry(Rencontre, font=("Arial", 12))
                self.e.place(x=642-0.5*184+i*184, y=105+j*20)
                self.e.insert(END, liste_clubs[j])      
                self.e.config(state="disabled")

    Table(window)

    #creer bouton retour vers l'accueil
    bouton_retour = Button(window, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_quitter = Button(window, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    
    
    bouton_retour.place(x=25, y=680)
    bouton_quitter.place(x=1200, y=680)

    #afficher la fenetre
    window.attributes('-fullscreen', True)
    window.mainloop()

#afficher la fenetre
Ekip()