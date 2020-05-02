import tkinter
from tkinter import ttk
from tkinter import *
import forganisme
from forganisme import organise_db
from forganisme.organise_db import *
go=organise_db.all_db1()





class analyseenjeux:
    def __init__(self):
        self.top = Toplevel()
        self.top.geometry("800x600")

        self.f1 = Frame(self.top, width=800, height=45, relief=GROOVE, border='2px', bg='#031F3A')
        self.f1.grid(row=0, column=0)
        self.f1.grid_propagate(0)
        self.f1.grid_columnconfigure(0, weight=1)
        self.f2 = Frame(self.top, width=800, height=190, relief=GROOVE)
        self.f2.grid(row=1, column=0)
        self.f2.grid_propagate(0)
        self.f21 = Frame(self.f2, width=400, height=190, relief=GROOVE)
        self.f21.grid(row=0, column=0)
        self.f21.grid_propagate(0)
        self.f22 = Frame(self.f2, width=400, height=190, relief=GROOVE)
        self.f22.grid(row=0, column=1)
        self.f22.grid_propagate(0)
        self.f22.grid_columnconfigure(0, weight=1)

        self.f3 = Frame(self.top, width=800, height=30, relief=GROOVE)
        self.f3.grid(row=2, column=0)
        self.f3.grid_propagate(0)
        self.f4 = Frame(self.top, width=800, height=230, relief=GROOVE, border='2px')
        self.f4.grid(row=3, column=0)
        self.f4.grid_propagate(0)
        self.f4.grid_rowconfigure(1, weight=2)
        self.f4.grid_rowconfigure(2, weight=1)
        self.f5 = Frame(self.top, width=800, height=60, relief=GROOVE)
        self.f5.grid(row=4, column=0)
        self.f5.grid_propagate(0)
        self.f5.grid_columnconfigure(0, weight=1)
        self.f5.grid_columnconfigure(1, weight=1)
        self.f5.grid_columnconfigure(2, weight=1)
        self.f5.grid_columnconfigure(3, weight=1)
        self.f6 = Frame(self.top, width=800, height=45, relief=GROOVE, border='2px')
        self.f6.grid(row=5, column=0)
        self.f6.grid_propagate(0)
        self.f6.grid_columnconfigure(0, weight=1)
        self.f6.grid_columnconfigure(1, weight=1)



    def add_analyse_interne(self):
        vmode = 'externe'
        vtype = self.vtype
        venjeux = self.lafficher['text']
        vanalyse = self.text3.get('1.0', END)
        vvaleur = self.vsign.get()
        vlie = 'autre'
        vdate = '12/12/2020'
        vpro = self.pro
        go.ianalyse(vmode, vtype, venjeux, vanalyse, vvaleur, vlie, vdate, vpro)
        self.top.destroy()

    def annuler(self):
        self.top.destroy()
    def afficher_interne2(self,event2):
        self.vsign = StringVar()
        self.vlie = StringVar()
        self.lafficher.config(text="")
        self.lafficher.config(text=str(self.listbox.get(self.listbox.curselection())))

        label3 = Label(self.f3, text="l'analyse de l'enjeux")
        label3.grid(row=0, column=0)

        self.text3 = Text(self.f4, width=50)
        self.text3.grid(row=0, column=0, rowspan=4)
        cbnigative = Radiobutton(self.f4, text='nigative(faiblaisse)', variable=self.vsign, value='nigative')
        cbnigative.grid(row=1, column=1, sticky='w')
        cbpositive = Radiobutton(self.f4, text='positive(force)', variable=self.vsign, value='positive')
        cbpositive.grid(row=2, column=1, sticky='n' + 'w')

        bajouter = Button(self.f6, text='ajouter',command=self.add_analyse_interne)
        bajouter.grid(row=0, column=0, sticky='e', padx=10)
        bannuler = Button(self.f6, text='annuler',command=self.annuler)
        bannuler.grid(row=0, column=1, sticky='w', padx=10)

    def afficher_interne(self,event1):
        self.vtype = event1.widget.get()
        ldetail = Label(self.f22, text='détail:', font=('arial', 11))
        ldetail.grid(row=0, column=0)
        self.lafficher= Label(self.f22, wraplength=450, justify=LEFT)
        self.lafficher.grid(row=1, column=0, sticky='w', padx=5)
        self.listbox = Listbox(self.f21, width=70)
        self.listbox.grid(row=1, column=0)
        ls_enjeux_bytype.clear()
        go.lsenjeux_bt(self.vtype)
        for i in ls_enjeux_bytype:
            self.listbox.insert(END, i[0])
        self.listbox.bind('<<ListboxSelect>>', self.afficher_interne2)
        pass




    def analyseinterne(self,event,proname):
        self.pro=proname
        self.lstype = ["Gouvernance de l’entreprise", "Conformité réglementaire", "Culture de l’entreprise",
                       "Compétences", "Environnement interne", "Système d'information"]

        self.lspolitique = ['here is politique ','jsdvjksbdvkjbk sfvnskjvbkjb jsdvjksbdvkjbk sfvnskjvbkjb slivhsflvhsfvh sjfn jsdvjksbdvkjbk sfvnskjvbkjb slivhsflvhsfvh sjfn slivhsflvhsfvh sjfnv']

        self.vtype = StringVar()
        ltitre = Label(self.f1, text='analyse les ' + event, font=('arial', 15), fg='white', bg='#031F3A')
        ltitre.grid(row=0, column=0)
        cb = ttk.Combobox(self.f21, textvariable=self.vtype)
        cb.grid(row=0, column=0)
        cb.current()
        cb['values'] = self.lstype
        cb.bind('<<ComboboxSelected>>', self.afficher_interne)

        #####################################################################################################################
        #####################################################################################################################
        #####################################################################################################################
        #####################################################################################################################

    def analyseexterne(self, event, proname):
        self.pro = proname
        self.lstype = ['politique', 'social', 'culturel', 'financier', 'économique', 'technologique',
                       "Gestion de la chaîne  d'approvisionnement", "demande du marché et public",
                       "Météorologiques, géologiques, hydrologiques et écologiques", "liés aux catastrophes"]

        self.lspolitique = ['here is politique ',
                            'jsdvjksbdvkjbk sfvnskjvbkjb jsdvjksbdvkjbk sfvnskjvbkjb slivhsflvhsfvh sjfn jsdvjksbdvkjbk sfvnskjvbkjb slivhsflvhsfvh sjfn slivhsflvhsfvh sjfnv']

        self.vtype = StringVar()
        ltitre = Label(self.f1, text='analyse les ' + event, font=('arial', 15), fg='white', bg='#031F3A')
        ltitre.grid(row=0, column=0)
        cb = ttk.Combobox(self.f21, textvariable=self.vtype)
        cb.grid(row=0, column=0)
        cb.current()
        cb['values'] = self.lstype
        cb.bind('<<ComboboxSelected>>', self.afficher_externe)


    def add_analyse_externe(self):
        vmode='externe'
        vtype=self.vtype
        venjeux=self.lafficher['text']
        vanalyse=self.text3.get('1.0',END)
        vvaleur=self.vsign.get()
        vlie=self.vlie.get()
        vdate='12/12/2020'
        vpro=self.pro
        go.ianalyse(vmode,vtype,venjeux,vanalyse,vvaleur,vlie,vdate,vpro)
        self.top.destroy()





    def afficher_externe2(self,event2):
        self.vsign = StringVar()
        self.vlie = StringVar()
        self.lafficher.config(text="")
        self.lafficher.config(text=str(self.listbox.get(self.listbox.curselection())))

        label3 = Label(self.f3, text="l'analyse de l'enjeux")
        label3.grid(row=0, column=0)

        self.text3 = Text(self.f4, width=65)
        self.text3.grid(row=0, column=0, rowspan=4)
        cbnigative = Radiobutton(self.f4, text='nigative(risque)', variable=self.vsign, value='nigative')
        cbnigative.grid(row=1, column=1, sticky='w')
        cbpositive = Radiobutton(self.f4, text='positive(opportunité)', variable=self.vsign, value='positive')
        cbpositive.grid(row=2, column=1, sticky='n' + 'w')

        cbsst = Radiobutton(self.f5, text='lie à SST', variable=self.vlie, value='sst')
        cbsst.grid(row=0, column=0)
        cbenv = Radiobutton(self.f5, text="lie à l'environnement", variable=self.vlie, value='env')
        cbenv.grid(row=0, column=1)
        cbqualité = Radiobutton(self.f5, text='lie à la qualité ', variable=self.vlie, value='qualité')
        cbqualité.grid(row=0, column=2)
        cbautre = Radiobutton(self.f5, text="lie à l'autre ", variable=self.vlie, value='autre')
        cbautre.grid(row=0, column=3)

        bajouter = Button(self.f6, text='ajouter',command=self.add_analyse_externe)
        bajouter.grid(row=0, column=0, sticky='e', padx=10)
        bannuler = Button(self.f6, text='annuler',command=self.annuler)
        bannuler.grid(row=0, column=1, sticky='w', padx=10)
    def afficher_externe(self,event1):
        self.vtype=event1.widget.get()
        ldetail = Label(self.f22, text='détail:', font=('arial', 11))
        ldetail.grid(row=0, column=0)
        self.lafficher = Label(self.f22, wraplength=450, justify=LEFT)
        self.lafficher.grid(row=1, column=0, sticky='w', padx=5)
        self.listbox = Listbox(self.f21, width=70)
        self.listbox.grid(row=1, column=0)
        ls_enjeux_bytype.clear()
        go.lsenjeux_bt(self.vtype)
        for i in ls_enjeux_bytype:
            self.listbox.insert(END, i[0])
        self.listbox.bind('<<ListboxSelect>>', self.afficher_externe2)


