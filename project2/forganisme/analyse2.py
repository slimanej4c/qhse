from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("300x300")
import forganisme
from forganisme import analyseenjeux



def analyseenjjeux(event):
    if event=="enjeux externe":
            top=Toplevel()
            top.geometry("800x600")
            lstype=['politique','social']
            lspolitique=['here is politique ','jsdvjksbdvkjbk sfvnskjvbkjb jsdvjksbdvkjbk sfvnskjvbkjb slivhsflvhsfvh sjfn jsdvjksbdvkjbk sfvnskjvbkjb slivhsflvhsfvh sjfn slivhsflvhsfvh sjfnv']
            vtype=StringVar()
            f1=Frame(top,width=800,height=45,relief=GROOVE,border='2px',bg='#031F3A')
            f1.grid(row=0,column=0)
            f1.grid_propagate(0)
            f1.grid_columnconfigure(0,weight=1)
            f2 = Frame(top, width=800, height=190, relief=GROOVE)
            f2.grid(row=1, column=0)
            f2.grid_propagate(0)
            f21 = Frame(f2, width=400, height=190, relief=GROOVE)
            f21.grid(row=0, column=0)
            f21.grid_propagate(0)
            f22 = Frame(f2, width=400, height=190, relief=GROOVE)
            f22.grid(row=0, column=1)
            f22.grid_propagate(0)
            f22.grid_columnconfigure(0,weight=1)

            f3 = Frame(top, width=800, height=30, relief=GROOVE)
            f3.grid(row=2, column=0)
            f3.grid_propagate(0)
            f4 = Frame(top, width=800, height=230, relief=GROOVE, border='2px')
            f4.grid(row=3, column=0)
            f4.grid_propagate(0)
            f4.grid_rowconfigure(1,weight=2)
            f4.grid_rowconfigure(2, weight=1)
            f5 = Frame(top, width=800, height=60, relief=GROOVE)
            f5.grid(row=4, column=0)
            f5.grid_propagate(0)
            f5.grid_columnconfigure(0,weight=1)
            f5.grid_columnconfigure(1, weight=1)
            f5.grid_columnconfigure(2, weight=1)
            f5.grid_columnconfigure(3, weight=1)
            f6= Frame(top, width=800, height=45, relief=GROOVE, border='2px')
            f6.grid(row=5, column=0)
            f6.grid_propagate(0)
            f6.grid_columnconfigure(0,weight=1)
            f6.grid_columnconfigure(1, weight=1)
            def afficher(event1):
                ldetail = Label(f22, text='détail:',font=('arial',11))
                ldetail.grid(row=0, column=0)
                lafficher = Label(f22, wraplength=450,justify=LEFT)
                lafficher.grid(row=1, column=0,sticky='w',padx=5)
                listbox=Listbox(f21,width=70)
                listbox.grid(row=1,column=0)
                if event1.widget.get()=='politique':
                    for i in lspolitique:
                        listbox.insert(END,i)
                else:None
                def afficher2(event2):
                    vsign=StringVar()
                    vlie= StringVar()
                    lafficher.config(text="")
                    lafficher.config(text=str(listbox.get(listbox.curselection())))

                    label3=Label(f3,text="l'analyse de l'enjeux")
                    label3.grid(row=0,column=0)

                    text3=Text(f4,width=70)
                    text3.grid(row=0,column=0,rowspan=4)
                    cbnigative=Radiobutton(f4,text='nigative(risque)',variable=vsign,value='nigative')
                    cbnigative.grid(row=1,column=1,sticky='w')
                    cbpositive = Radiobutton(f4, text='positive(opportunité)',variable=vsign,value='positive')
                    cbpositive.grid(row=2, column=1,sticky='n'+'w')

                    cbsst = Radiobutton(f5, text='lie à SST', variable=vlie, value='sst')
                    cbsst.grid(row=0, column=0)
                    cbenv = Radiobutton(f5, text="lie à l'environnement", variable=vlie, value='env')
                    cbenv.grid(row=0, column=1)
                    cbqualité = Radiobutton(f5, text='lie à la qualité ', variable=vlie, value='qualité')
                    cbqualité.grid(row=0, column=2)
                    cbautre = Radiobutton(f5, text="lie à l'autre ", variable=vlie, value='autre')
                    cbautre.grid(row=0, column=3)

                    bajouter=Button(f6,text='ajouter')
                    bajouter.grid(row=0,column=0,sticky='e',padx=10)
                    bannuler = Button(f6, text='annuler')
                    bannuler.grid(row=0, column=1,sticky='w',padx=10)




                listbox.bind('<<ListboxSelect>>',afficher2)

            ltitre=Label(f1,text='analyse les '+event,font=('arial',15),fg='white',bg='#031F3A')
            ltitre.grid(row=0,column=0)
            cb=ttk.Combobox(f21,textvariable=vtype)
            cb.grid(row=0,column=0)
            cb.current()
            cb['values']=lstype
            cb.bind('<<ComboboxSelected>>',afficher)


    else:

        pass
def go(event):
    go = analyseenjeux.analyseenjeux()

    if event=="analyse externe":
        go.analyseexterne(event)

    else:
        go.analyseinterne(event)




b1=Button(root,text='add enjeux',command=lambda:go("analyse externe"))
b1.grid(row=0,column=0)
root.mainloop()
