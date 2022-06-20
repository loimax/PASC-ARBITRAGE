from tkinter import *
import os

def JA():
        #créer une fenetre
        Arb = Tk()
        #donner un titre
        Arb.title("JA")
        #donner une taille 
        Arb.geometry("1920x1080")
        #creer une zone de texte pour les JA
        zone_Arbs = Text(Arb, height=1, width=75)
        zone_Arbs.grid(row=3, column=2)
        #créer une liste de JA et les afficher 
        liste_Arbs = ["JA 1", "JA 2", "JA 3", "JA 4", "JA 5"]
        liste_Arbs_afficher = Listbox(Arb, height=5, width=80)
        for i in range(len(liste_Arbs)):
            liste_Arbs_afficher.insert(i, liste_Arbs[i])
        liste_Arbs_afficher.grid(row=6, column=2)


        #créer fonction ajouter qui ajoute un JA à la liste liste_Arbs après avoir rentré le nom du JA
        def ajouter():
            liste_Arbs.append(zone_Arbs.get("1.0", END))
            liste_Arbs_afficher.insert(END, zone_Arbs.get("1.0", END))
            zone_Arbs.delete("1.0", END)
            print(liste_Arbs)
        
           

        #creer 3 boutons pour les JA : modifier ajouter supprimer
        # creer bouton modifier
        bouton_modifier = Button(Arb, text="Modifier", bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_modifier.grid(row=8, column=2)
        # creer bouton ajouter
        bouton_ajouter = Button(Arb, text="Ajouter", bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'),command=ajouter)
        bouton_ajouter.grid(row=9, column=2)
        # creer bouton supprimer
        bouton_supprimer = Button(Arb, text="Supprimer", bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_supprimer.grid(row=10, column=2)
        #placer les boutons dans la fenetre
        bouton_modifier.place(x=700, y=10)
        bouton_ajouter.place(x=700, y=50)
        bouton_supprimer.place(x=700, y=90)

      
            

    
        def retour():
            # bouton_retour.destroy()
            Arb.destroy()
            os.system("python Interface\Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(Arb, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.grid(row=18, column=2)

    
        #afficher la fenetre
        Arb.mainloop()

#afficher la fenetre
JA()
