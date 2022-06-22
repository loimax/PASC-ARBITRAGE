from tkinter import *
import os
from tkinter.ttk import Combobox
from utils import *

from numpy import datetime_as_string

#window_height : 701, nope, dépends de la taille réelle de l'écran
#window_width : 1284, ça aussi

#faire un tableau avec des listes déroulantes pour choisir l"équipe

def Matchs():
    conn = create_connection("Interface/testdb/GestionRegionale.db")
    cursor = conn.cursor()
    #créer une fenetre
    window = Tk()
    #donner un titre a la Matchs
    window.title("Matchs")

    window.attributes('-fullscreen', True)
    #donner une taille a la Matchs
    #window.geometry("1920x1080")
    #taille de la fenetre s'adapte a la taille de l'écran
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

    #créer une liste d'équipes et les afficher 
    liste_debase_equipes = ["UN", "DEUX", "TROIS", "QUATRE", "CINQ", "SIX", "SEPT", "HUIT"]
    dates_rencontres = ["25/09/2021", "02/10/2021", "23/10/2021", "06/11/2021", "13/11/2021", "27/11/2021", "11/12/2021"]

    def retour():
        # bouton_retour.destroy()
        window.destroy()
        os.system("python Interface/Accueil.py")

    def quitter():
        window.destroy()

    def mix_teams(list, i):
        tmp_list = []
        match i:
            case 0:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[3])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                return tmp_list
            
            case 1:
                tmp_list.append(list[5])
                tmp_list.append(list[6])
                tmp_list.append(list[7])
                tmp_list.append(list[4])
                tmp_list.append(list[3])
                tmp_list.append(list[2])
                tmp_list.append(list[1])
                tmp_list.append(list[0])
                return tmp_list

            case 2:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[4])
                tmp_list.append(list[5])
                tmp_list.append(list[3])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                return tmp_list

            case 3:
                tmp_list.append(list[7])
                tmp_list.append(list[3])
                tmp_list.append(list[2])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                tmp_list.append(list[1])
                tmp_list.append(list[0])
                return tmp_list

            case 4:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                tmp_list.append(list[6])
                tmp_list.append(list[7])
                tmp_list.append(list[2])
                tmp_list.append(list[3])
                return tmp_list

            case 5:
                tmp_list.append(list[2])
                tmp_list.append(list[1])
                tmp_list.append(list[3])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                tmp_list.append(list[0])
                return tmp_list

            case 6:
                tmp_list.append(list[0])
                tmp_list.append(list[5])
                tmp_list.append(list[6])
                tmp_list.append(list[4])
                tmp_list.append(list[7])
                tmp_list.append(list[3])
                tmp_list.append(list[2])
                tmp_list.append(list[1])
                return tmp_list


    #créer tableau qui hold les équipes
    class Table:
        def __init__(self,window):

            nb_rencontres = 7
            nb_matchs_jour = 4
            self.eref = Entry(window, font=("Arial", 12), width=12, justify=CENTER)
            self.eref2 = Entry(window, font=("Arial", 12), width=5, justify=CENTER)
            self.eref.place(x=0, y=0)
            self.eref2.place(x=0, y=0)
            window.update()
            self.e_size = self.eref.winfo_width()
            self.e_sizeh = self.eref.winfo_height()
            self.e2_size = self.eref2.winfo_width()
            self.eref.destroy()
            self.eref2.destroy()
            for i in range(nb_rencontres):
                for j in range(nb_matchs_jour):
                    if (j == 0):
                        self.e = Entry(window, font=("Arial", 12), width=12, justify=CENTER)
                        self.e.place(x=0, y=0)
                        self.e.insert(END,dates_rencontres[i])
                        #self.e.config(state="disabled")
                        self.e2 = Entry(window, font=("Arial", 12), width=5, justify=CENTER)
                        self.e2.place(x=0, y=0)
                        self.e2.insert(END,i+1)
                        self.e2.config(state="disabled")

                    self.e3 = Combobox(window, values=liste_debase_equipes, font=("Arial", 12))
                    self.e3.place(x=0, y=0)
                    self.e3.insert(END,mix_teams(liste_debase_equipes,i)[j])
                    # self.e3.config(state='disabled')

                    self.e4 = Combobox(window, values=liste_debase_equipes, font=("Arial", 12))
                    self.e4.place(x=0, y=0)
                    self.e4.insert(END,mix_teams(liste_debase_equipes,i)[-j-1])
                    # self.e4.config(state='disabled')


                    window.update()
                    tab_len = self.e_size + self.e2_size + self.e3.winfo_width() + self.e4.winfo_width()+50
                    start_array = window.winfo_width()/2-(tab_len)+25
                    offset_top = 100
                    if(i >= 4):
                        if (j == 0):
                            print("ligne > 4")
                            self.e.place(x=start_array+tab_len, y=offset_top+j*self.e_sizeh+(i-4)*140)
                            self.e2.place(x=start_array+self.e_size+tab_len, y=offset_top+j*self.e_sizeh+(i-4)*140)
                        self.e3.place(x=start_array+self.e_size+self.e2_size+tab_len, y=offset_top+j*self.e_sizeh+(i-4)*140)
                        self.e4.place(x=start_array+self.e_size+self.e2_size+self.e3.winfo_width()+tab_len, y=offset_top+j*self.e_sizeh+(i-4)*140)
                    else:
                        if (j == 0): 
                            self.e.place(x=start_array, y=offset_top+j*self.e_sizeh+i*140)
                            self.e2.place(x=start_array+self.e_size, y=offset_top+j*self.e_sizeh+i*140)
                        self.e3.place(x=start_array+self.e_size+self.e2_size, y=offset_top+j*self.e_sizeh+i*140)
                        self.e4.place(x=start_array+self.e_size+self.e2_size+self.e3.winfo_width(), y=offset_top+j*self.e_sizeh+i*140)


    #init objects
    txt = Label(window, text="Voici la feuille de match pour la poule X de X/X/XX", font=("Arial", 18))
    bouton_creer = Button(window, text="Créer", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
    bouton_retour = Button(window, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_quitter = Button(window, text="Quitter", command=quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))

    #pre-place objects
    txt.place(x = 0, y = 0)
    bouton_creer.place(x = 0, y = 0)
    bouton_retour.place(x = 0, y = 0)
    bouton_quitter.place(x = 0, y = 0)

    window.update()

    #placement des widgets en fonction de la fenetre
    txt.place(x = window.winfo_width()/2-txt.winfo_width()/2, y = 40)
    bouton_creer.place(x = window.winfo_width()/2-bouton_creer.winfo_width()/2, y = window.winfo_height()-0.04*window.winfo_height())
    bouton_retour.place(x = 0.02*window.winfo_width(), y = window.winfo_height()-0.04*window.winfo_height())
    bouton_quitter.place(x = 0.98*window.winfo_width()-bouton_retour.winfo_width(), y = window.winfo_height()-0.04*window.winfo_height())

    Table(window)

    # window.update()
    # print(txt.winfo_width())

    #afficher la fenetre
    window.mainloop()

#afficher la fenetre
Matchs()
