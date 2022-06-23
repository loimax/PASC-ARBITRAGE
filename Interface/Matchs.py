import os
from tkinter import *
from tkinter.ttk import Combobox
from utils import *


#window_height : 701, nope, dépends de la taille réelle de l'écran
#window_width : 1284, ça aussi

#faire un tableau avec des listes déroulantes pour choisir l"équipe

class Matchs():
    def __init__(self, liste_from_poules):
        self.liste_debase_equipes = liste_from_poules
        print("match list = " + str(self.liste_debase_equipes))
        conn = create_connection("Interface/testdb/GestionRegionale.db")
        cursor = conn.cursor()
        #créer une fenetre
        self.main_window = Tk()
        #donner un titre a la Matchs
        self.main_window.title("Matchs")

        self.main_window.attributes('-fullscreen', True)
        #donner une taille a la Matchs
        #self.main_window.geometry("1920x1080")
        #taille de la fenetre s'adapte a la taille de l'écran
        self.main_window.geometry("{0}x{1}+0+0".format(self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()))

        #créer une liste d'équipes et les afficher 
        self.dates_rencontres = ["25/09/2021", "02/10/2021", "23/10/2021", "06/11/2021", "13/11/2021", "27/11/2021", "11/12/2021"]


        # self.main_window.update()
        # print(txt.winfo_width())
        self.create_UI()
        #afficher la fenetre
        self.main_window.mainloop()



    def create_UI(self):
        #créer tableau qui hold les équipes
        self.add_phat_table()
        self.add_txt()


    def retour(self):
            # bouton_retour.destroy()
            self.main_window.destroy()
            os.system("python Interface/Accueil.py")


    def quitter(self):
        self.main_window.destroy()


    def mix_teams(self, list, i):
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
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                tmp_list.append(list[7])
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[3])
                return tmp_list

            case 2:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[7])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                tmp_list.append(list[3])
                tmp_list.append(list[6])
                return tmp_list

            case 3:
                tmp_list.append(list[4])
                tmp_list.append(list[3])
                tmp_list.append(list[2])
                tmp_list.append(list[5])
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                return tmp_list

            case 4:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[6])
                tmp_list.append(list[7])
                tmp_list.append(list[3])
                tmp_list.append(list[2])
                tmp_list.append(list[4])
                tmp_list.append(list[5])
                return tmp_list

            case 5:
                tmp_list.append(list[2])
                tmp_list.append(list[1])
                tmp_list.append(list[3])
                tmp_list.append(list[4])
                tmp_list.append(list[0])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                return tmp_list

            case 6:
                tmp_list.append(list[0])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[7])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[3])
                tmp_list.append(list[4])
                return tmp_list


    def add_phat_table(self):
        nb_rencontres = 7
        nb_matchs_jour = 4
        self.eref = Entry(self.main_window, font=("Arial", 12), width=12, justify=CENTER)
        self.eref2 = Entry(self.main_window, font=("Arial", 12), width=5, justify=CENTER)
        self.eref.place(x=0, y=0)
        self.eref2.place(x=0, y=0)
        self.main_window.update()
        self.e_size = self.eref.winfo_width()
        self.e_sizeh = self.eref.winfo_height()
        self.e2_size = self.eref2.winfo_width()
        self.eref.destroy()
        self.eref2.destroy()
        for i in range(nb_rencontres):
            for j in range(nb_matchs_jour):
                if (j == 0):
                    self.e = Entry(self.main_window, font=("Arial", 12), width=12, justify=CENTER)
                    self.e.place(x=0, y=0)
                    self.e.insert(END,self.dates_rencontres[i])
                    #self.e.config(state="disabled")
                    self.e2 = Entry(self.main_window, font=("Arial", 12), width=5, justify=CENTER)
                    self.e2.place(x=0, y=0)
                    self.e2.insert(END,i+1)
                    self.e2.config(state="disabled")

                self.e3 = Combobox(self.main_window, values=self.liste_debase_equipes, font=("Arial", 12))
                self.e3.place(x=0, y=0)
                self.e3.insert(END,self.mix_teams(self.liste_debase_equipes,i)[j])
                # self.e3.config(state='disabled')

                self.e4 = Combobox(self.main_window, values=self.liste_debase_equipes, font=("Arial", 12))
                self.e4.place(x=0, y=0)
                self.e4.insert(END,self.mix_teams(self.liste_debase_equipes,i)[j+4])
                # self.e4.config(state='disabled')


                self.main_window.update()
                tab_len = self.e_size + self.e2_size + self.e3.winfo_width() + self.e4.winfo_width()+50
                start_array = self.main_window.winfo_width()/2-(tab_len)+25
                offset_top = 100
                if(i >= 4):
                    if (j == 0):
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



    def add_txt(self):
        txt = Label(self.main_window, text="Voici la feuille de match pour la poule X de X/X/XX", font=("Arial", 18))
        bouton_creer = Button(self.main_window, text="Créer", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))

        #pre-place objects
        txt.place(x = 0, y = 0)
        bouton_creer.place(x = 0, y = 0)
        bouton_retour.place(x = 0, y = 0)
        bouton_quitter.place(x = 0, y = 0)

        self.main_window.update()

        #placement des widgets en fonction de la fenetre
        txt.place(x = self.main_window.winfo_width()/2-txt.winfo_width()/2, y = 40)
        bouton_creer.place(x = self.main_window.winfo_width()/2-bouton_creer.winfo_width()/2, y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_retour.place(x = 0.02*self.main_window.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_quitter.place(x = 0.98*self.main_window.winfo_width()-bouton_retour.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
