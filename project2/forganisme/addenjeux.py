import  tkinter
from tkinter import ttk
from tkinter import *
from forganisme import organise_db
go=organise_db.all_db1()
import time


class addenjeux:
    def __init__(self,pro_name,site_name):
        self.pro_name=pro_name
        self.site_name=site_name
        self.top = Toplevel()
        self.top.geometry("800x600")


        self.lstypeexterne = ['politique', 'social', 'culturel', 'financier', 'économique', 'technologique',
                       "Gestion de la chaîne  d'approvisionnement", "demande du marché et public",
                       "Météorologiques, géologiques, hydrologiques et écologiques", "liés aux catastrophes"]

        self.lstypeinterne = ["Gouvernance de l’entreprise", "Conformité réglementaire", "Culture de l’entreprise",
                              "Compétences", "Environnement interne", "Système d'information"]
        self.vtype = StringVar()
        self.f1 = Frame(self.top, width=800, height=60, relief=GROOVE, border='2px')
        self.f1.grid(row=0, column=0)
        self.f1.grid_propagate(0)
        self.f1.grid_rowconfigure(0, weight=1)
        self.f1.grid_columnconfigure(0, weight=1)

        self.f2 = Frame(self.top, width=800, height=60, relief=GROOVE, border='2px')
        self.f2.grid(row=1, column=0, sticky='n')
        self.f2.grid_propagate(0)
        self.f2.grid_rowconfigure(0, weight=1)
        self.f2.grid_columnconfigure(0, weight=1)
        self.f2.grid_columnconfigure(1, weight=1)

        self.f3 = Frame(self.top, width=800, height=180, relief=GROOVE, border='2px')
        self.f3.grid(row=2, column=0, sticky='n')
        self.f3.grid_propagate(0)
        self.f4 = Frame(self.top, width=800, height=240, relief=GROOVE, border='2px')
        self.f4.grid(row=3, column=0, sticky='n')
        self.f4.grid_propagate(0)

        self.f5 = Frame(self.top, width=800, height=60, relief=GROOVE, border='2px')
        self.f5.grid(row=4, column=0)
        self.f5.grid_propagate(0)
        self.f5.grid_rowconfigure(0, weight=1)
        self.f5.grid_columnconfigure(0, weight=2)
        self.f5.grid_columnconfigure(1, weight=2)
        self.lexemple = Label(self.f3, width=110, wraplength=750)
        self.lexemple.grid(row=0, column=0, padx=10, pady=5)

    def afficher_exemple_externe(self,event):
        self.f4.grid_columnconfigure(0,weight=1)
        self.f4.grid_columnconfigure(1, weight=8)
        vdate=StringVar()
        date_now = time.strftime('%d/%m/%Y')
        vdate.set(str(date_now))

        ldate=Label(self.f4,text='date:')
        ldate.grid(row=0,column=0,sticky=E)
        edate=Entry(self.f4,textvariable=vdate)
        edate.grid(row=0,column=1,sticky=W)

        tenjeux = Text(self.f4, width=65)
        tenjeux.grid(row=1, column=0,columnspan=2,padx=20)

        v=str(event.widget.get()[0])


        if event.widget.get() == 'politique':
            self.lexemple['text'] = " "
            self.lexemple['text'] = " -Pays dictatorial ou démocratique - Entreprise dont un site clé est situé en zone de conflit armé - Ingérence politique dans le développement économique" \
                                    " - Respect des réglementations locales - Lobbying écologique et industriel sur les Politique questions environnementales - Aide de l'État aux entreprises dans leur démarche" \
                                    " environnementale (promotion des économies d'énergie, par exemple) - Exigence de démarche environnementale" \
                                    " pour l'obtention de contrats auprès des collectivités - Normes et exigences environnementales actuelles et futures " \
                                    "sur la zone d'exploitation et tout le long du cycle de vie (dans d'autres régions ou pays)"


        elif event.widget.get() == 'social':
            self.lexemple['text'] = " "
            self.lexemple['text'] = " Subordination et corruption - Niveau de criminalité - Niveau d'éducation de la population active " \
                                    "- Langue utilisée - Valeurs ethniques - Questions de genre - Disponibilité au sein " \
                                    "de la population active  - Accès aux infrastructures scolaires et médicales"

        elif event.widget.get() == 'culturel':
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Monuments historiques, sites archéologiques à proximité " \
                                    "- Disponibilité de  ressources spécifiques telles que des plantes endémiques, de l'eau, du bois, des matéiaux"


        elif event.widget.get() == 'financier':
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Système financier reconnu - Disponibilité et accès aux ressources financières pour des investissements" \
                                    "dans des meilleures technologies plus  respectueuses de l'environnement " \
                                    "- Investissement possible et fiable sur des projets environnementaux auprès de banques solides" \
                                    "- Organismes de contrôle financier reconnus"

        elif event.widget.get() == 'économique':
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Disponibilité des services publics : gaz, eau, électricité, infrastructures,routes, installations de transport, etc. " \
                                    "permettant un approvisionnement, une fabrication et  une distribution efficaces et en toute sécurité environnementale"

        elif event.widget.get() == 'technologique':
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Disponibilité et accès à la technologie pertinente pour l'organisme  " \
                                    "- Collaboration avec des centres de recherche à proximité  - Risque technologique (explosion, incendie etc.)"

        elif event.widget.get() == "Gestion de la chaîne  d'approvisionnement":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Disponibilité des matières premières dans le respect des législations environnementales " \
                                    "- Capacité et aptitude des fournisseurs à proposer des produits innovants respectueux de l'environnement " \
                                    "- Personnel de sous-traitance, fournisseurs qualifiés dans l'application des bonnes pratiques environnementales " \
                                    " - Fournisseurs et sous-traitants  engagés dans des démarches environnementales " \
                                    "- Niveau de technologie et exigence des clients dans le domaine de la protection de l'environnement"

        elif event.widget.get() == "demande du marché et public":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Tendances actuelles et futures du marché pour les produits et services  " \
                                    "-Consommateur orienté vers des produits à faible impact environnemental :" \
                                    " bois issus de forêts gérées écologiquement, vêtements fabriqués sans" \
                                    " utilisation excessive de produits dangereux, recyclabilité des produits en" \
                                    " fin de vie, équipements moins énergivores " \
                                    "- Riverains et associations en attente de performances environnementales " \
                                    "élevées de la part de l'entreprise accueillie sur le territoire, etc"

        elif event.widget.get() == "Météorologiques, géologiques, hydrologiques et écologiques":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Pluviosité, climatologie (températures extrêmes ou écarts de température), neige, brouillard, verglas," \
                                    " chaleur extrême, perméabilité du sol, présence d'une nappe vulnérable, espèces animales et végétales " \
                                    "remarquables, cours d'eau classé, qualité de l'air atmosphérique, etc. :" \
                                    " éléments pouvant impacter ou être impactés par les produits et les activités exercées sur le site" \
                                    " (pollution, contamination, etc.)*."

        elif event.widget.get() == "liés aux catastrophes":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "Inondation, foudre, glissement de terrain, changement climatique,accidents technologiques," \
                                    "  pouvant engendrer des pollutions, explosions ou incendies, destruction des habitats naturels, " \
                                    "destruction\ de la biodiversité (perte des services écosystémiques)" \
                                    ", etc. Situations d'urgence relevées dans  le cadre du système de management environnemental**."

        else:

            self.lexemple['text'] = " "
            self.lexemple['text'] = ""


        def addd():
            print(self.pro_name)
            mode='externe'
            type=event.widget.get()
            enjeux=tenjeux.get('1.0',END)
            date=str(edate.get())

            a=str(self.pro_name)
            b=str(self.site_name)
            go.ienjeux(mode,type,enjeux,date,a,b)
            self.top.destroy()
        bajouter = Button(self.f5, text='ajouter',command=addd)
        bajouter.grid(row=0, column=0)
        bcancel = Button(self.f5, text='annuler',command=self.annuler)
        bcancel.grid(row=0, column=1)

    def enjeuxexterne(self):
        ltitre = Label(self.f1, text='ajouter un enjeux ', relief=GROOVE, font=('aria', 14), fg='green')
        ltitre.grid(row=0, column=0)
        ltype = Label(self.f2, text="type d'enjeux", relief=GROOVE)
        ltype.grid(row=0, column=0, sticky='e' + 's')
        cbtype = ttk.Combobox(self.f2, textvariable=self.vtype)
        cbtype.grid(row=0, column=1, sticky='w' + 's')
        cbtype.current()
        cbtype['values'] = self.lstypeexterne
        cbtype.bind('<<ComboboxSelected>>', self.afficher_exemple_externe)




    def afficher_exemple_interne(self,event):
        self.f4.grid_columnconfigure(0, weight=1)
        self.f4.grid_columnconfigure(1, weight=8)
        vdate = StringVar()
        date_now = time.strftime('%d/%m/%Y')
        vdate.set(str(date_now))

        ldate = Label(self.f4, text='date:')
        ldate.grid(row=0, column=0, sticky=E)
        edate = Entry(self.f4, textvariable=vdate)
        edate.grid(row=0, column=1, sticky=W)

        tenjeux = Text(self.f4, width=65)
        tenjeux.grid(row=1, column=0, columnspan=2, padx=10)





        if event.widget.get() == "Système d'information":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "- Flux d'informations et processus décisionnels (formels et informels) et temps nécessaire à leur achèvement" \
                                    "-Relations internes avec les parties intéressées, ainsi que leurs perceptions et leurs valeurs"


        elif event.widget.get() == "Gouvernance de l’entreprise":
            self.lexemple['text'] = " "
            self.lexemple['text'] = " - Développement de la sécurité au niveau de l'entreprise" \
                                    " -Système au moyen duquel une organisation prend et applique des décisions dans le but d'atteindre ses objectifs"

        elif event.widget.get() == "Conformité réglementaire":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "- Exigences à laquelle l'organisme doit se conformer "

        elif event.widget.get() == "Culture de l’entreprise":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "- Culture SST -Entreprise familiale, entreprise privée ou publique, style de management et de leadership," \
                                   "ouvert et libre, culture du secret et fermé et processus décisionnels"


        elif event.widget.get() == "Compétences":
            self.lexemple['text'] = " "
            self.lexemple['text'] ="- Développement de compétences spécifiques Capacité, aptitude et connaissance de " \
                                   "l'organismeen termes de ressourceset de " \
                                    " compétences(par exemple: capital,temps, personnes, langue,processus, système ettechnologies ainsi que leurmaintenance)"

        elif event.widget.get() == "Environnement interne":
            self.lexemple['text'] = " "
            self.lexemple['text'] = "- Communication efficace"
        else:
            self.lexemple['text'] = " "
            self.lexemple['text'] = "jkkbkbhb"

        def addd():

            mode = 'interne'
            type = event.widget.get()
            enjeux = tenjeux.get('1.0', END)
            date = '29012020'

            a = str(self.pro_name)
            b = str(self.site_name)
            go.ienjeux(mode, type, enjeux, date, a, b)
            self.top.destroy()

        bajouter = Button(self.f5, text='ajouter', command=addd)
        bajouter.grid(row=0, column=0)
        bcancel = Button(self.f5, text='annuler',command=self.annuler)
        bcancel.grid(row=0, column=1)

    def annuler(self):
        self.top.destroy()
    def enjeuxinterne(self):
        ltitre = Label(self.f1, text='ajouter un enjeux ', relief=GROOVE, font=('aria', 14), fg='green')
        ltitre.grid(row=0, column=0)
        ltype = Label(self.f2, text="type d'enjeux", relief=GROOVE)
        ltype.grid(row=0, column=0, sticky='e' + 's')
        cbtype = ttk.Combobox(self.f2, textvariable=self.vtype)
        cbtype.grid(row=0, column=1, sticky='w' + 's')
        cbtype.current()
        cbtype['values'] = self.lstypeinterne
        cbtype.bind('<<ComboboxSelected>>', self.afficher_exemple_interne)
