##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2020, John McNamara, jmcnamara@cpan.org
#
import sqlite3
import xlsxwriter
import sys
from datetime import date,time

def format_copy_add(fmt,param=dict()):
    '''
    Réalise la copie d'un format (fmt) avec ajout de propriétés (param)
    '''
    # Récupération des propriétés spécifiques au format
    properties = [f[4:] for f in dir(fmt) if f[0:4] == 'set_']
    # Création d'un format de base pour récupérer les paramètres initiaux
    dft_fmt = workbook.add_format()
    dict_param = {k : v for k, v in fmt.__dict__.items() if k in properties and dft_fmt.__dict__[k] != v}
    for k, v in param.items():
        dict_param[k] = v
    return workbook.add_format(dict_param)

def preparation_convocation_rapport(donnees):
    '''
    Prépare le fichier xlsx pour le JA contenant convocation et rapport sur deux feuilles différentes POUR UNE SEULE RENCONTRE
    '''

    ############################################################################
    #
    #             CREATION DU FICHIER ET DES FORMATS DE CELLULES
    #
    ############################################################################
    
# (1, 1, 'R3', 'B', 'TT SUD CHER', 1, 'BEAUJARDIN BDC', 1, '26/09/2021', '9:30:00', 'Salle polyvalente de la République,56 av de la République', '18370', 'Chateaumeillant', 'UNG-BILLAULT Florian', '07 81 45 48 06', '9115229', 'BERTHOME', 'Pascal', 'TT GERMINOIS', '11, rue Iouri Gagarine', '18390', 'Saint Germain du Puy', '06 33 17 34 38', 28)
    global workbook

# Indication journée
    phase      = donnees[0]
    journee    = donnees[1]
    if (phase == 2 ):
        journee = journee -7
    dateRenc   = donnees[8]
    heureRenc  = donnees[9]
# Indications Rencontre
    division   = donnees[2]
    poule      = donnees[3]
    club1      = donnees[4]
    numeq1     = donnees[5]
    equipe1    = club1 + ' ' + str(numeq1)
    club2      = donnees[6]
    numeq2     = donnees[7]
    equipe2    = club2 + ' ' + str(numeq2)
# Indications lieu rencontre
    salleRenc  = donnees[10]
    CPRenc     = donnees[11]
    VilleRenc  = donnees[12]
    Corres     = donnees[13]
    TelCorr    = donnees[14]
# Indications JA
    licJA      = donnees[15]
    NomJA      = donnees[16]
    PrenomJA   = donnees[17]
    ClubJA     = donnees[18]
    AdrJA      = donnees[19]
    CPJA       = donnees[20]
    VilleJA    = donnees[21]
    TelJA      = donnees[22]    

    titreWBK = NomJA+"-"+ PrenomJA +"-P"+str(phase)+"J"+str(journee)+"-"+ division+"-"+ club1+"-"+str(numeq1)+".xlsx"
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(titreWBK)
    
    # Par défaut, c'est de l'Arial, on souhaite mettre du 'Times New Roman', donc tous les
    # styles auront cet attribut changé.
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    # style de base 
    normal_format = workbook.add_format({'align': 'left','valign':'vcenter',
                                         'font_name':'Times New Roman','font_size':8})
    # Cellules avec taille 10
    normal10_format = format_copy_add(normal_format,{'font_size':10})
    # Cellules centrées
    center_format = format_copy_add(normal_format,{'align':'center'})
    # Cellules alignées à droite
    right_format = format_copy_add(normal_format,{'align':'right'})
    right10_format = format_copy_add(right_format,{'font_size':10})

    # Cellules pour mettre en gras
    bold_format = format_copy_add(normal_format,{'bold':True})
    # Cellules pour mettre en gras taille 9
    bold9_format = format_copy_add(bold_format,{'font_size':9})
    bold9I_format = format_copy_add(bold9_format,{'italic':True,'align':'center'})
    # Cellules pour mettre en gras taille 10
    bold10_format = format_copy_add(bold_format,{'font_size':10})
    bold12_format = format_copy_add(bold_format,{'font_size':12,'align':'center'})

    # Cellules encadrées fin
    squared1_format = format_copy_add(normal_format,{'border':1,'align':'center','border_color':'#3A3A3A'})
    # Cellules encadrées Gras
    squared1B_format = format_copy_add(squared1_format,{'bold':True})
    # Cellules encadrées épais HGD
    squared2TLR_format = format_copy_add(squared1_format,{'top':2,'left':2,'right':2,'bottom':0})
    # Cellules encadrées épais BGD
    squared2BLR_format = format_copy_add(squared1_format,{'top':0,'left':2,'right':2,'bottom':2})
    # Cellules pointillés droite
    squared3_format = format_copy_add(squared1_format,{'top':0,'left':0,'right':3,'bottom':0,'font_size':10})
    # Cellules encadrées titre
    squared6_format = format_copy_add(squared1_format,{'border':6,'bold':True})
    # Cellules du bas de feuille
    merge_bottom_format = format_copy_add(squared1_format,{'top':6,'left':0,'right':0,'bottom':0,'align':'center','valign':'bottom','bold':True})
    # Cellules pour mettre en gras centré encadré (éventuellement italique)
    squared2BC_format = format_copy_add(squared1_format,{'top':0,'left':2,'right':2,'bottom':0,'align':'center','bold':True})
    squared2BIC_format = format_copy_add(squared2BC_format,{'italic':True})
    squared2BC_format.set_font_size(10)
    # Encadrement Frais
    squared2Black_format = format_copy_add(squared1_format,{'border_color':'black','border':2})
    # Cellules encadrées titre rempli
    squared6BG_format = format_copy_add(squared6_format,{'pattern':17,'bold':False,'border_color':'black','font_size':10})
    
    # Cellules COVID (en rouge)
    red_bold_format = format_copy_add(bold_format, {'font_color':'red'})

    # Cellules grises....
    gray_cells = workbook.add_format()
    gray_cells.set_bg_color('gray')

    date_format = workbook.add_format({'align': 'left'})
    date_format.set_num_format('dd/mm/yyyy')
    date_format.set_font_name('Times New Roman')
    date_format.set_font_size(10)
    date8_format = format_copy_add(date_format,{'align':'right','font_size':8})

    hour_format = workbook.add_format({'align': 'left'})
    hour_format.set_num_format('hh" heures "mm')
    hour_format.set_font_name('Times New Roman')
    hour_format.set_font_size(10)



    #############################################################################
    #
    #             MISE EN PAGE DE LA CONVOCATION
    #
    ##############################################################################

    # Niveau de la compétition 
    niveau = str(donnees[2])[0:1]
    # print (niveau)
    print('Rencontre : '+ equipe1 +  '/' + equipe2 + ' par ' + NomJA +' '+ PrenomJA)

    # Mise en page (impression)
    worksheet = workbook.add_worksheet("Convocation-JA-Régionale")
    worksheet.set_landscape()
    worksheet.set_margins(left=0.4,right=0.4,top=0.4,bottom=0.4)
    worksheet.set_paper(9)
    worksheet.center_vertically()
    worksheet.center_horizontally()
    worksheet.print_area(0,0,40,16)
    worksheet.hide_gridlines(2)

    # Format the column to make the text clearer.
    worksheet.set_column('A:A', 9.57)
    worksheet.set_column('B:C', 11.43)
    worksheet.set_column('D:D',2.57)
    worksheet.set_column('E:E', 13.71)
    worksheet.set_column('F:F', 11.71)
    worksheet.set_column('G:H', 1.71)
    for i in range(43):
        worksheet.set_row(i, 12.75)

    for l in ['A','B','C','D','E','F']:
        worksheet.write_blank( l+'1', '', gray_cells)
        worksheet.write_blank( l+'7', '', gray_cells)

    # Write some simple text.
    worksheet.write('A2', 'LIGUE DU CENTRE VAL DE LOIRE',bold_format)
    worksheet.write('A3', 'DE TENNIS DE TABLE', bold_format)
    worksheet.write('A4', '40, RUE DU GÉNÉRAL LECLERC', bold_format)
    worksheet.write('A5', '41300 SALBRIS', bold_format)
    worksheet.write('A6', 'TÉL : 02 54 96 14 28', bold_format)
    worksheet.write('F2', 'SAISON '+saison, right10_format)
    # Insert an image.
    worksheet.insert_image('D2', 'logo.png', {'x_scale':1.65, 'y_scale':1.65})

    worksheet.write('F9', 'CONVOCATION', format_copy_add(bold10_format,{'underline':True,'align':'right'}))
    worksheet.write('A10', 'NOM du JUGE-ARBITRE', normal_format)

    worksheet.merge_range('B12:E12', "COMMISSION RÉGIONALE D'ARBITRAGE", squared6_format)
    worksheet.write('A13', 'LIGUE', normal_format)
    worksheet.write('C13', 'CENTRE VAL DE LOIRE', bold10_format)
    worksheet.write('A14', "J'ai l'avantage de vous informer que vous êtes désigné(e) pour diriger la rencontre suivante du", normal_format)
    worksheet.write('A15', 'CHAMPIONNAT DE FRANCE PAR ÉQUIPES', normal_format)
    worksheet.write('E15', 'MESSIEURS -', format_copy_add(normal_format,{'align':'right'}))
    worksheet.write('F15', 'DAMES', format_copy_add(normal_format,{'font_strikeout':True}))

    worksheet.write('A17', 'Journée n°', normal_format)
    worksheet.write('C17', 'Division', normal_format)
    worksheet.write('E17', 'Poule', center_format)
    worksheet.write('A18', 'Opposant', normal_format)
    worksheet.write('D18', 'à', normal_format)
    worksheet.write('A19', 'Le', normal_format)
    worksheet.write('D19', 'à', normal_format)

    # Spécificité des rencontres nationales
    if niveau == 'N':
        worksheet.merge_range('A20:E20', 'Rappel : Être présent 1 heure au moins avant le début de la rencontre', normal_format)
        worksheet.write('A30', "Vos frais de dépl. + div. + 20 € seront réglés par l'association qui reçoit.", normal_format)
        worksheet.write('A32', '20 €', center_format)
    else:
    # Pour les régionales
        worksheet.merge_range('A20:E20', 'Rappel : Être présent 30 minutes au moins avant le début de la rencontre', normal_format)
        worksheet.write('A30', "Vos frais de dépl. + div. + 12,50 € seront réglés par l'association qui reçoit et 12,50 € par l'équipe adverse.", normal_format)
        worksheet.write('A32', '25 €', center_format)
    # Fin des spécificités
    
    worksheet.write('A21', 'ADRESSE DE LA SALLE', normal_format)
    worksheet.write('A25', 'NOM-PRÉNOM et ADRESSE du CORRESPONDANT du CLUB RECEVANT :', normal_format)

    worksheet.write('A28', 'NOM-PRÉNOM et Téléphone du référent COVID :', red_bold_format)
    worksheet.write('A31', 'INDEMNITÉ FIXE', normal_format)
    worksheet.write('C31', 'DÉPLACEMENT', normal_format)
    worksheet.write('E31', 'DIVERS', center_format)
    worksheet.write('F31', 'TOTAL', center_format)

    worksheet.write('C32', 'km X 0,25 €', center_format)
#    worksheet.write('E32', '2,00 € (COVID)', format_copy_add(red_bold_format,{'align':'center'}))
    # worksheet.write('E31', '2,00 €', format_copy_add(normal_format,{'align':'center'}))
    worksheet.write('F32', '', squared2TLR_format)
    worksheet.write('F33', '', squared2BLR_format)
    #worksheet.write('A32', "DIVERS : Frais spécifiques COVID = 2€", normal_format)
    worksheet.write('A35', 'Veuillez agréer mes meilleurs sentiments.', normal_format)
    worksheet.write('E36', 'Le responsable des nominations', normal_format)
    worksheet.write('E37', 'Pascal Berthomé (06 33 17 34 38)', normal_format)

    worksheet.set_row(38, 15)
    worksheet.write('A38', 'FRAIS RÉGLÉS', normal_format)
    worksheet.write('C38', 'Montant', center_format)
    worksheet.write('A39', 'OUI', squared1_format)
    worksheet.write('B39', 'NON', squared1_format)
    worksheet.write('C39', '', squared1_format)

    worksheet.set_row(40, 20)
    worksheet.merge_range('A41:F41', "L'ensemble de cette feuille doit être adressée à la Ligue du Centre Val de Loire", merge_bottom_format)




    #############################################################################
    #
    #             MISE EN PAGE DE L'ETAT DE FRAIS
    #
    ##############################################################################

    # Format the column to make the text clearer.
    worksheet.set_column('I:I', 9.57)
    worksheet.set_column('J:L', 6.71)
    worksheet.set_column('M:O', 4.57)
    worksheet.set_column('P:P', 12)
    worksheet.set_column('Q:Q', 7.43)

    for l in ['I','J','K','L','M','N','O','P','Q']:
        worksheet.write_blank( l+'1', '', gray_cells)
        worksheet.write_blank( l+'7', '', gray_cells)

    # Write some simple text.
    worksheet.write('I2', 'LIGUE DU CENTRE VAL DE LOIRE',bold_format)
    worksheet.write('I3', 'DE TENNIS DE TABLE', bold_format)
    worksheet.write('I4', '40, RUE DU GÉNÉRAL LECLERC', bold_format)
    worksheet.write('I5', '41300 SALBRIS', bold_format)
    worksheet.write('I6', 'TÉL : 02 54 96 14 28', bold_format)
    worksheet.write('Q2', 'SAISON '+saison, right10_format)
    worksheet.write('P3', 'Destinataire', normal_format)
    worksheet.write('P4', 'La C.R.A.', normal10_format)
    # Insert an image.
    worksheet.insert_image('M2', 'logo.png', {'x_scale':1.65, 'y_scale':1.65})

    worksheet.write('I9', 'FICHE DE RENSEIGNEMENTS', format_copy_add(bold10_format,{'underline':True}))
    worksheet.write('I10', '(à remplir par le Juge arbitre)', normal_format)

    worksheet.write('I12', 'NOM', normal_format)
    worksheet.write('N12', 'PRÉNOM', normal_format)
    worksheet.write('I13', 'ADRESSE', normal_format)
    worksheet.write('I14', 'CODE POSTAL', normal_format)
    worksheet.write('M14', 'VILLE', normal_format)
    worksheet.write('I15', 'TÉLÉPHONE', normal_format)

    worksheet.write('I17', 'LICENCIÉ au CLUB de : ', normal_format)
    worksheet.write('I18', 'Numéro de licence :', normal_format)

    worksheet.write('I20', 'Distance ALLER et RETOUR (domicile <=> Salle) :', normal_format)

    worksheet.write('K26', 'Fait à', normal_format)
    worksheet.write('O26', 'Le', normal_format)
    worksheet.write('O27', 'Signature', format_copy_add(squared2BIC_format,{'top':0,'bottom':0,'left':0,'right':0}))

    worksheet.merge_range('I31:Q31', "L'ensemble de cette feuille (recto-verso) doit être retourné", squared2TLR_format)
    worksheet.merge_range('I32:Q32', "avec la feuille de match", squared2BIC_format)
    worksheet.merge_range('I33:Q33', "A", format_copy_add(squared2TLR_format,{'top':0}))
    worksheet.merge_range('I34:Q34', "", squared2BIC_format)
    worksheet.merge_range('I35:Q35', "LIGUE CENTRE VAL DE LOIRE", squared2BIC_format)
    worksheet.merge_range('I36:Q36', "TENNIS DE TABLE", squared2BIC_format)
    worksheet.merge_range('I37:Q37', "40, Rue du Général Leclerc", squared2BIC_format)
    worksheet.merge_range('I38:Q38', "41300 SALBRIS", squared2BIC_format)
    worksheet.merge_range('I39:Q39', "liguecentre.tt@wanadoo.fr", squared2BLR_format)

    worksheet.merge_range('I41:Q41', "L'ensemble de cette feuille doit être adressée à la Ligue du Centre Val de Loire", merge_bottom_format)



    #############################################################################
    #
    #             REMPLISSAGE DES DONNEES
    #
    ##############################################################################

    worksheet.write('B17', str(journee) + " Ph. " + str(phase), bold12_format)
    worksheet.write('D17', division, format_copy_add(bold12_format,{'align':'left'}))
    worksheet.write('F17', poule, bold12_format)
    worksheet.write('B18', equipe1 , normal10_format)
    worksheet.write('E18', equipe2, normal10_format)
    d = dateRenc.split('/')
    day = date(int(d[2]), int(d[1]), int(d[0]))
    worksheet.write('B19', day, date_format)
    worksheet.write('P26', day, format_copy_add(date_format,{'bold':True,'italic':True}))
    h = heureRenc.split(':')
    hour = time(int(h[0]), int(h[1]))
    worksheet.write('E19', hour, hour_format)
    adresse = salleRenc.split(',')
    worksheet.write('B22', adresse[0], normal10_format)
    try:
        worksheet.write('B23', adresse[1], normal10_format)
    except:
        None
    worksheet.write('B24', CPRenc+" "+ VilleRenc.upper(), normal10_format)
    worksheet.write('B26', Corres,normal10_format)
    worksheet.write('L26', VilleRenc, format_copy_add(bold10_format,{'italic':True}))
    try:
        worksheet.write('B27', "Tél : "+ TelCorr,normal10_format)
    except:
        None
    worksheet.write('K18', licJA, normal10_format)
    worksheet.write('K12', NomJA, normal10_format)
    worksheet.write('P12', PrenomJA, normal10_format)
    worksheet.write('C10', NomJA+' '+ PrenomJA, normal10_format)
    worksheet.write('K17', ClubJA, normal10_format)
    worksheet.write('K13', AdrJA, normal10_format)
    worksheet.write('K14', CPJA,normal10_format)
    try:
        worksheet.write('O14', VilleJA.upper(),normal10_format)
    except:
        None
    worksheet.write('K15', TelJA,normal10_format)


    #############################################################################
    #
    #             MISE EN PAGE DES FRAIS
    #
    ##############################################################################

    # Mise en page (impression)
    worksheet = workbook.add_worksheet("Etat Frais")
    worksheet.set_margins(left=0.4,right=0.4,top=0.4,bottom=0.4)
    worksheet.set_paper(9)
    worksheet.set_print_scale(130)
    worksheet.center_vertically()
    worksheet.center_horizontally()
    worksheet.print_area(0,0,42,8)
    worksheet.hide_gridlines(2)

    # Format the column to make the text clearer.
    worksheet.set_column('A:A', 13.57)
    worksheet.set_column('B:B', 10)
    worksheet.set_column('C:C', 9)
    worksheet.set_column('D:D', 1.71)
    worksheet.set_column('E:E', 8)
    worksheet.set_column('F:F', 1.71)
    worksheet.set_column('G:H', 7)
    worksheet.set_column('I:I', 8)
    for i in range(43):
        worksheet.set_row(i, 12.75)
    worksheet.set_row(3,16)
    worksheet.set_row(13,24)
    worksheet.set_row(17,24)
    worksheet.set_row(25,16)
    worksheet.set_row(35,24)
    worksheet.set_row(39,24)

    #############################################################################
    #
    #             FRAIS DU RECEVANT
    #
    ##############################################################################
    
    worksheet.write('A1', 'CHAMPIONNAT DE FRANCE PAR ÉQUIPES',bold10_format)
    if niveau != 'N':
        worksheet.write('A2', 'Divisions régionales', bold9_format)
    else:
        worksheet.write('A2', 'Divisions nationales', bold9_format)
    worksheet.merge_range('A4:I4', "FRAIS DE JUGE-ARBITRAGE", squared6BG_format)
    worksheet.write('A6', 'NOM et Prénom :', normal_format)
    worksheet.write('A8', 'Rencontre :', normal_format)
    worksheet.write('H8', 'Date :', normal_format)
    
    worksheet.write('A10', 'Allocation Forfaitaire de Fonction :', normal_format)
    worksheet.write('D10', " =", normal_format)
    if niveau == 'N':
        worksheet.write('E10', '20 €', right_format)
    else:
        worksheet.write('E10', '12,50 €', right_format)
    worksheet.write('A12', 'Déplacement :', normal_format)
    worksheet.write('B12', '0,25 € x', right_format)
    worksheet.write('C12', '_ _ _ _ _ km', normal_format)
    worksheet.write('D12', " =", normal_format)
    worksheet.write('E12', '_ _ _ _ _ €', right_format)

    # prime COVID
#    worksheet.write('A11', 'Divers : Frais COVID 19 ', red_bold_format)
#    worksheet.write('D11', " =", red_bold_format)
#    worksheet.write('E11', ' 2 €', format_copy_add(red_bold_format, {'align':'right'}))
    
    worksheet.write('C14', 'Somme à régler :', bold_format)
    worksheet.write('G14', '', format_copy_add(squared2Black_format,{'right':0}))
    worksheet.write('H14', '€   ', format_copy_add(squared2Black_format,{'left':0,'align':'right'}))
    worksheet.write('A16', "Somme payée par M..............................................................", normal_format)
    worksheet.write('E16', "Association :", normal_format)
    worksheet.merge_range('A18:C18', "Signature du Juge-Arbitre :", center_format)
    worksheet.merge_range('D18:H18', "", squared2Black_format)
    worksheet.merge_range('A20:I20', "Frais de Juge-arbitrage à la charge du club recevant", bold9I_format)

    worksheet.merge_range('A21:I21', "", format_copy_add(squared2Black_format,{'top':0,'left':0,'right':0,'bottom':3}))

    

    #############################################################################
    #
    #             FRAIS DU VISITEUR
    #
    ##############################################################################
    
    if niveau != 'N':
        worksheet.write('A23', 'CHAMPIONNAT DE FRANCE PAR ÉQUIPES',bold10_format)
        worksheet.write('A24', 'Divisions régionales', bold9_format)
        worksheet.merge_range('A26:I26', "FRAIS DE JUGE-ARBITRAGE", squared6BG_format)
        worksheet.write('A28', 'NOM et Prénom :', normal_format)
        worksheet.write('A30', 'Rencontre :', normal_format)
        worksheet.write('H30', 'Date :', normal_format)
    
        worksheet.write('A32', 'Allocation Forfaitaire de Fonction :', normal_format)
        worksheet.write('D32', " =", normal_format)
        worksheet.write('E32', '12,50 €', right_format)
    
        worksheet.write('C36', 'Somme à régler :', bold_format)
        worksheet.merge_range('G36:H36', '12,50 €', squared2Black_format)
        worksheet.write('A38', "Somme payée par M..............................................................", normal_format)
        worksheet.write('E38', "Association :", normal_format)
        worksheet.merge_range('A40:C40', "Signature du Juge-Arbitre :", center_format)
        worksheet.merge_range('D40:H40', "", squared2Black_format)
        worksheet.merge_range('A42:I42', "Frais de Juge-arbitrage à la charge du club visiteur", bold9I_format)

    

    #############################################################################
    #
    #             REMPLISSAGE DES DONNEES
    #
    ##############################################################################

    worksheet.write('B6', NomJA+' '+PrenomJA, normal_format)
    worksheet.write('B8', equipe1 + ' / '+ equipe2, normal_format)
    worksheet.write('I8', day, date8_format)
    worksheet.write('G16', equipe1, normal_format)
    if niveau != 'N':
        worksheet.write('B28', NomJA+' '+ PrenomJA,normal_format)
        worksheet.write('B30', equipe1+' / '+equipe2,normal_format)
        worksheet.write('I30', day, date8_format)
        worksheet.write('G38', equipe2, normal_format)

    workbook.close()





#############################################################################
#
#             RECUPERATION DES DONNEES DES RENCONTRES
#
#   format de l'appel:
#   python3.8 testXlsxWriter.py optNumJournee optNumRencontre
#          - optNumJournee: pour sortir les rencontres de la journée en question
#                           par défaut 1
#          - optNumRencontre: pour sélectioner une rencontre précise 
#                           par défaut toutes
#
##############################################################################



# Par défaut la première journée : on peut préciser le numero de journée 
# en premier argument
if (len(sys.argv)>1):
    numjournee = sys.argv[1]
else:
    numjournee = 1

req = """
SELECT * FROM DonneesRencontres
WHERE journee = """ + str(numjournee) 

# 2ème argument : numéro de la rencontre quand on veut éditer une seule convocation
if (len(sys.argv)>2):
    req = req + """
AND NumRenc = """ + sys.argv[2]

# Il faut terminer la requête comme il faut
req = req + """;"""

# Vérification de la requête.
# print(req)

saison = "2021/2022"
cnx = sqlite3.connect("GestionRegionale.db")
cur = cnx.cursor()
cur.execute(req)

rows = cur.fetchall()
for row in rows:
#    print (row)
    preparation_convocation_rapport(row)
print(len(rows)," convocations réalisées.")


    
