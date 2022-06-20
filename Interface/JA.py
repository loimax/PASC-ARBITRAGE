from tkinter import *
import os

def JA():
        #créer une fenetre
        Arb = Tk()
        #donner un titre
        Arb.title("JA")
        #donner une taille 
        Arb.geometry("1920x1080")

         #uptade de la liste des JA
        def update(data):
            #clear the listbox
            club_list.delete(0, END)

            #ajpouter les JA dans la listbox
            for item in data:
                club_list.insert(END, item)
        #afficher le club séléctionné
        def fillout(e):
            entry_JA.delete(0, END)
            entry_JA.insert(0, club_list.get(ANCHOR))

        #créer fonction entrée vs liste de JA
        def check(e):
            #grab what typed
            typed = entry_JA.get()

            if typed == '':
                data = liste_JA
            else:
                data = []
                for item in liste_JA:
                    if typed.lower() in item.lower():
                        data.append(item)

            update(data)
        #creer une zone de texte pour la recherche de JA
        entry_JA = Entry(Arb, font=("Helvetica", 20))
        entry_JA.place(x=600, y=150)

        #créer une zone pour la liste de JA
        club_list = Listbox(Arb, width=50)
        club_list.place(x=600, y=200)

        #créer une liste de JA 
        liste_JA = ["Nom 1", "Nom 2", "Nom 3", "Nom 4", "Nom 5", "Nom 6", "Nom 7", "Nom 8", "Nom 9", "Nom 10", "Nom 11", "Nom 12", "Nom 13", "Nom 14", "Nom 15", "Nom 16", "Nom 17", "Nom 18", "Nom 19", "Nom 20", "Nom 21", "Nom 22", "Nom 23", "Nom 24", "Nom 25", "Nom 26", "Nom 27", "Nom 28", "Nom 29", "Nom 30", "Nom 31", "Nom 32", "Nom 33", "Nom 34", "Nom 35", "Nom 36"]
        #Ajouter JA dans la liste
        update(liste_JA)

        #afficher le club selectionné
        club_list.bind("<<ListboxSelect>>", fillout)

        #create a binding to the entry box
        entry_JA.bind("<KeyRelease>", check)


        
           

        bouton_modifier = Button(Arb, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'))
        bouton_modifier.place(x=600, y=400)
        bouton_ajouter = Button(Arb, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'))
        bouton_ajouter.place(x=725, y=400)
        bouton_supprimer = Button(Arb, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'))
        bouton_supprimer.place(x=850, y=400)
            

    
        def retour():
            # bouton_retour.destroy()
            Arb.destroy()
            os.system("python Interface\Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(Arb, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.place(x=725, y=700)

    
        #afficher la fenetre
        Arb.mainloop()

#afficher la fenetre
JA()