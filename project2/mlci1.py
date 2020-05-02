import tkinter
from tkinter import ttk
from tkinter import *

from datetime import datetime
import time
import random
import site_db
from site_db import *
from tkinter import messagebox



time1=""
class mlci1:
    def __init__(self,root,pro_name,site_name,bsite1):
            self.bsite1 = bsite1
            self.site_name = site_name


            self.pro_name=pro_name
            self.mlci_db = site_db.mlci()
            self.mlci_db.ctex(self.pro_name)

            self.root = root
            self.wroot = self.root.winfo_screenwidth() - 6
            self.hroot = self.root.winfo_screenheight() - 74

            self.root.geometry("%dx%d" % (self.wroot, self.hroot))

            vwidth_b = 100 / 1530 * 28 * self.wroot / 100
            wframe_widthb_1 = round(vwidth_b, 0)
            wframe_widthb_2 = str(wframe_widthb_1)[:-2]
            self.wbutton = int(wframe_widthb_2)

            topwidth_b = 100 / 1530 * 800 * self.wroot / 100
            wframe_widthb_1 = round(topwidth_b, 0)
            wframe_widthb_2 = str(wframe_widthb_1)[:-2]
            self.topwidth = int(wframe_widthb_2)

            vwidth2 = 100 / 1530 * 1330 * self.wroot / 100
            wframe_width2_1 = round(vwidth2, 0)
            wframe_width2_2 = str(wframe_width2_1)[:-2]
            self.wframe22 = int(wframe_width2_2)

            vwidth3 = 100 / 1530 * 510 * self.wroot / 100
            wframe_width3_1 = round(vwidth3, 0)
            wframe_width3_2 = str(wframe_width3_1)[:-2]
            self.wframe3 = int(wframe_width3_2)

            vwidth5 = 100 / 1530 * 42 * self.wroot / 100
            wframe_width5_1 = round(vwidth5, 0)
            wframe_width5_2 = str(wframe_width5_1)[:-2]
            self.wframe5 = int(wframe_width5_2)

            vwidth4 = 100 / 1530 * 200* self.wroot / 100
            wframe_width4_1 = round(vwidth4, 0)
            wframe_width4_2 = str(wframe_width4_1)[:-2]
            self.wframe4= int(wframe_width4_2)

            vheight1 = 100 / 790 * 30 * self.hroot / 100
            hframe1_1 = round(vheight1, 0)
            hframe1_2 = str(hframe1_1)[:-2]
            self.hframe1 = int(hframe1_2)

            vheight2 = 100 / 790 * 720 * self.hroot / 100
            hframe2_1 = round(vheight2, 0)
            hframe2_2 = str(hframe2_1)[:-2]
            self.hframe2 = int(hframe2_2)

            vheight2_button = 100 / 790 * 10 * self.hroot / 100
            hframe2_1_button = round(vheight2_button, 0)
            hframe2_2_button = str(hframe2_1_button)[:-2]
            self.hframe2button = int(hframe2_2_button)

            vheight22 = 100 / 790 * 100 * self.hroot / 100
            hframe22_1 = round(vheight22, 0)
            hframe22_2 = str(hframe22_1)[:-2]
            self.hframe22 = int(hframe22_2)

            vheight3 = 100 / 790 * 40 * self.hroot / 100
            hframe3_1 = round(vheight3, 0)
            hframe3_2 = str(hframe3_1)[:-2]
            self.hframe3 = int(hframe3_2)

            vheight4 = 100 / 790 * 620 * self.hroot / 100
            hframe_canvas1 = round(vheight4, 0)
            hframe_canvas2 = str(hframe_canvas1)[:-2]
            self.hframe_canvas = int(hframe_canvas2)

            big_frame = Frame(self.root, width=self.wroot, height=self.hroot, bg="red")
            big_frame.grid(row=0, column=0)
            big_frame.grid_propagate(0)

            self.frame1 = Frame(big_frame, width=self.wroot, height=self.hframe1, bg="#055E33")
            self.frame1.grid(row=0, column=0, columnspan=2)
            self.frame1.grid_propagate(0)

            self.frame2 = Frame(big_frame, width=self.wroot, height=self.hframe2, bg="#F1F1F2")
            self.frame2.grid(row=1, column=0)
            self.frame2.grid_propagate(0)

            self.frame22 = Frame(self.frame2, width=self.wroot, height=self.hframe22, bg="#38B449")
            self.frame22.grid(row=0, column=0)
            self.frame22.grid_propagate(0)

            self.frame23 = Frame(self.frame2, width=self.wroot, height=self.hframe_canvas, bg="#38B449")
            self.frame23.grid(row=1, column=0)
            self.frame23.grid_propagate(0)


            self.frame_job=Frame(self.frame23,width=self.wframe4,height=self.hframe_canvas,bg="#27A9E1")
            self.frame_job.grid(row=0,column=0)
            self.frame_job.grid_propagate(0)

            frame_canvas = Frame(self.frame_job, width=self.wframe4 - 10, height=self.hframe_canvas, bg="#27A9E1")
            frame_canvas.grid(row=0, column=0)

            vsb = Scrollbar(frame_canvas, orient=VERTICAL)
            vsb.grid(row=0, column=1, rowspan=2, sticky=N + S)
            hsb = Scrollbar(frame_canvas, orient=HORIZONTAL)
            hsb.grid(row=1, column=0, columnspan=2, sticky=W + E)
            canvas_site = Canvas(frame_canvas, yscrollcommand=vsb.set, xscrollcommand=hsb.set, bg="#27A9E1",width=self.wframe4 -20, height=self.hframe_canvas-20)
            canvas_site.grid(row=0, column=0, sticky="news")
            canvas_site.grid_propagate(0)

            vsb.config(command=canvas_site.yview)
            hsb.config(command=canvas_site.xview)

            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)

            frame_canvas2 = Frame(canvas_site)
            #####################################################################################^vvvvvvvvvv
            self.bper = Button(frame_canvas2, text="personnel", width=self.wbutton,command=self.go_per)
            self.bper.grid(row=0, column=0)

            self.bmlci=Button(frame_canvas2,text="MLCI",width=self.wbutton,bg='green')
            self.bmlci.grid(row=1,column=0)

            self.benv = Button(frame_canvas2, text="environnement", width=self.wbutton)
            self.benv.grid(row=2, column=0)
            #################################################################################^^^^^^^^^^^^^^^^^^^^

            canvas_site.create_window(0, 0, window=frame_canvas2)
            frame_canvas2.update_idletasks()

            canvas_site.config(scrollregion=canvas_site.bbox("all"))

            self.frame_show=Frame(self.frame23,width=self.wframe22,height=self.hframe_canvas)
            self.frame_show.grid(row=0,column=1)
            self.frame_show.grid_propagate(0)

            self.frame3 = Frame(big_frame, width=self.wroot, height=self.hframe3, bg="#BBBDC0")
            self.frame3.grid(row=2, column=0, sticky=S)
            self.frame3.grid_propagate(0)

            self.frame11 = Frame(self.frame1, width=self.wframe3, height=self.hframe1, bg="#055E33")
            self.frame11.grid(row=0, column=0)
            self.frame11.grid_propagate(0)

            self.frame12 = Frame(self.frame1, width=self.wframe3, height=self.hframe1, bg="#055E33")
            self.frame12.grid(row=0, column=1)
            self.frame12.grid_propagate(0)

            self.frame13 = Frame(self.frame1, width=self.wframe3, height=self.hframe1, bg="#055E33")
            self.frame13.grid(row=0, column=2)
            self.frame13.grid_propagate(0)
    def go_per(self):
        import personnel
        go = personnel.personnel(self.root, self.pro_name, self.bsite1, self.site_name)
        go.all_items()
        go.b()
        """import mlci
        go=mlci.part_mlci(self.root,self.pro_name,self.bsite1,self.site_name)
        go.all_mlci()"""
    def b(self):
        btex=Button(self.frame22,text='tableau des extincteurs',command=self.jobex)
        btex.grid(row=0,column=0)
        biex = Button(self.frame22, text='ajouter extincteur', command=self.iex)
        biex.grid(row=0, column=1)
        bsiex = Button(self.frame22, text='signaler', command=self.jobria)
        bsiex.grid(row=0, column=2)
        bpex = Button(self.frame22, text='plan des extincteur', command=self.jobex)
        bpex.grid(row=1, column=0)
        bfex = Button(self.frame22, text='filter', command=self.jobria)
        bfex.grid(row=1, column=1)
    def all_items(self):
        lname_pro=Label(self.frame12,text=self.pro_name,bg="#055E33",fg="white")
        lname_pro.grid(row=0,column=0)
        ldate = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ldate.grid(row=0, column=0)
        ltime = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ltime.grid(row=0, column=1)
        ltime.grid_rowconfigure(100, weight=1)
        bretour=Button(self.frame11,text='retour')
        bretour.grid(row=0,column=0)

        def tick():

            global time1
            date_now = time.strftime('%Y-%m-%d')
            time_now = time.strftime('%H:%M:%S')
            if time_now != time1:
                time1 = time_now

                ltime.config(text=time_now)
                ldate.config(text=date_now)
            ltime.after(200, tick)
        tick()
        def retour():
            import part_3
            go=part_3.part_3(self.root,self.pro_name,self.site_name,self.bsite1)
            go.all_items()
            """import mlci
            go=mlci.part_mlci(self.root,self.pro_name,self.bsite1,self.site_name)
            go.all_mlci()"""

        bretour.config(command=retour)
    def iex(self):
                top=Toplevel()
                #top.geometry=('%dx%d'%(self.topwidth,500))
                frame2 = Frame(top, width=1400, height=100) #?????????????????????????????????????????????????????????? regler le width and height
                frame2.grid(row=0, column=0)
                frame2.grid_propagate(0)
                lbl = Label(frame2, text="numéro", width=self.wbutton)
                lbl.grid(row=0, column=0)
                lbl = Label(frame2, text="type", width=self.wbutton)
                lbl.grid(row=0, column=1)
                lbl = Label(frame2, text="poid", width=self.wbutton)
                lbl.grid(row=0, column=2)
                lbl = Label(frame2, text="lieu", width=self.wbutton)
                lbl.grid(row=0, column=3)
                lbl = Label(frame2, text="verification", width=self.wbutton)
                lbl.grid(row=0, column=4)
                lbl = Label(frame2, text="recharge", width=self.wbutton)
                lbl.grid(row=0, column=5)
                self.ent_num = Entry(frame2, width=self.wbutton, validate='key')
                self.ent_num.grid(row=1, column=0)
                self.entt_type = Entry(frame2, width=self.wbutton)
                self.entt_type.grid(row=1, column=1)
                self.ent_poid = Entry(frame2, width=self.wbutton, validate='key')
                self.ent_poid.grid(row=1, column=2)
                self.ent_lieu = Entry(frame2, width=self.wbutton)
                self.ent_lieu.grid(row=1, column=3)
                self.ent_v = Entry(frame2, width=self.wbutton)
                self.ent_v.grid(row=1, column=4)
                self.ent_r = Entry(frame2, width=self.wbutton)
                self.ent_r.grid(row=1, column=5)
                btn_valider = Button(frame2, text="valider", width=self.wbutton)
                btn_valider.grid(row=2, column=1, columnspan=3, pady=20)
                btn_annuler2 = Button(frame2, text="anuuler", width=self.wbutton)
                btn_annuler2.grid(row=2, column=3, pady=20)
                def i():

                    num = self.ent_num.get()
                    type = self.entt_type.get()
                    poid = self.ent_poid.get()
                    lieu = self.ent_lieu.get()
                    v = self.ent_v.get()
                    r = self.ent_r.get()
                    self.mlci_db.iex(num,type,poid,lieu,v,r,self.pro_name)
                    top.destroy()
                    self.jobex()
                btn_valider.config(command=i)



    def uex(self,num,type,poid,lieu,v,r,lnum1,proname):
        go=site_db.mlci()

        go.uex(num,type,poid,lieu,v,r,lnum1,proname)
        self.jobex()
        print('herrre num'+str(lnum1))
        print(proname)

    def jobex(self):

            frame_canvas = Frame(self.frame_show, width=self.wframe22 - 10, height=self.hframe_canvas, bg="#2C2206")
            frame_canvas.grid(row=0, column=0)

            vsb = Scrollbar(frame_canvas, orient=VERTICAL)
            vsb.grid(row=0, column=1, rowspan=2, sticky=N + S)
            hsb = Scrollbar(frame_canvas, orient=HORIZONTAL)
            hsb.grid(row=1, column=0, columnspan=2, sticky=W + E)
            canvas_site = Canvas(frame_canvas, yscrollcommand=vsb.set, xscrollcommand=hsb.set, bg="#F1F1F2",width=self.wframe22 - 20, height=self.hframe_canvas-20)
            canvas_site.grid(row=0, column=0, sticky="news")
            canvas_site.grid_propagate(0)

            vsb.config(command=canvas_site.yview)
            hsb.config(command=canvas_site.xview)

            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)

            frame_canvas3 = Frame(canvas_site)
            ########################vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            #############################vvvvvvvvvvvvvvvvvvvvvvvvvvv

            ls_numéro.clear()
            ls_type.clear()
            ls_poid.clear()
            ls_lieu.clear()
            ls_v.clear()
            ls_r.clear()
            self.mlci_db.lsex(self.pro_name)
            lnum = Label(frame_canvas3,text='numéro', width=int(self.wbutton/2),border='1px',bg='#C3F4E5')
            lnum.grid(row=0, column=0)
            ltype = Label(frame_canvas3, text='type', width=self.wbutton,border='1px',bg='#C3F4E5')
            ltype.grid(row=0, column=1)
            lpoid = Label(frame_canvas3, text='poid', width=self.wbutton,border='1px',bg='#C3F4E5')
            lpoid.grid(row=0, column=2)
            llieu = Label(frame_canvas3, text='lieu', width=self.wbutton,border='1px',bg='#C3F4E5')
            llieu.grid(row=0, column=3)
            lv = Label(frame_canvas3, text='v', width=self.wbutton,border='1px',bg='#C3F4E5')
            lv.grid(row=0, column=4)
            lr = Label(frame_canvas3, text='r', width=self.wbutton,border='1px',bg='#C3F4E5')
            lr.grid(row=0, column=5)
            def modifier( ii,lnum1):
                enum= Entry(frame_canvas3, width=int(self.wbutton/2))
                enum.grid(row=ii + 1, column=0)
                etype=Entry(frame_canvas3,width=self.wbutton)
                etype.grid(row=ii+1,column=1)
                epoid = Entry(frame_canvas3, width=self.wbutton)
                epoid.grid(row=ii + 1, column=2)
                elieu = Entry(frame_canvas3, width=self.wbutton)
                elieu.grid(row=ii + 1, column=3)
                ev = Entry(frame_canvas3, width=self.wbutton)
                ev.grid(row=ii + 1, column=4)
                er= Entry(frame_canvas3, width=self.wbutton)
                er.grid(row=ii + 1, column=5)
                bval=Button(frame_canvas3,text='valider', width=self.wbutton,command=lambda:self.uex(enum.get(),etype.get(),epoid.get(),elieu.get(),ev.get(),er.get(),lnum1['text'],self.pro_name))
                bval.grid(row=ii+1,column=6)
                print(enum.get())
            for i in range(len(ls_numéro)):
                        num=StringVar()
                        type=StringVar()
                        poid=StringVar()
                        lieu=StringVar()
                        v=StringVar()
                        r=StringVar()
                        num.set(ls_numéro[i])
                        type.set(ls_type[i])
                        poid.set(ls_poid[i])
                        lieu.set(ls_lieu[i])
                        v.set(ls_v[i])
                        r.set(ls_r[i])
                        lnum=Label(frame_canvas3,textvariable=num,width=int(self.wbutton/2),bg='#AAAFAE',border='1px')
                        lnum.grid(row=i+1,column=0)
                        ltype = Label(frame_canvas3, textvariable=type, width=self.wbutton,bg='#AAAFAE',border='1px')
                        ltype.grid(row=i+1, column=1)
                        lpoid = Label(frame_canvas3, textvariable=poid, width=self.wbutton,bg='#AAAFAE',border='1px')
                        lpoid.grid(row=i+1, column=2)
                        llieu = Label(frame_canvas3, textvariable=lieu, width=self.wbutton,bg='#AAAFAE',border='1px')
                        llieu.grid(row=i+1, column=3)
                        lv = Label(frame_canvas3, textvariable=v, width=self.wbutton,bg='#AAAFAE',border='1px')
                        lv.grid(row=i+1, column=4)
                        lr = Label(frame_canvas3, textvariable=r, width=self.wbutton,bg='#AAAFAE',border='1px')
                        lr.grid(row=i+1, column=5)
                        bmodifier=Button(frame_canvas3,text='modifier',width=self.wbutton,bg='#AAAFAE',border='1px')
                        bmodifier.grid(row=i+1,column=6)
                        #bmodifier["command"] = lambda bmodifier=bmodifier1 lnum=lnum1,ltype=ltype1,lpoid=lpoid1,llieu=llieu1,lv=lv1,lr=lr1: bmodifier1.configure(command=self.modifier( lnum1, ltype1, lpoid1, llieu1,  lv1,er1, lr1, btn_supprimer1, btn_modifier1))
                        bmodifier["command"] = lambda bmodifier1=bmodifier ,ii=i,lnum1=lnum: bmodifier1.configure(command=modifier(ii,lnum1))
            #############^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ##############^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            canvas_site.create_window(0, 0, window=frame_canvas3)
            frame_canvas3.update_idletasks()
            canvas_site.config(scrollregion=canvas_site.bbox("all"))

    def jobria(self):

            frame_canvas = Frame(self.frame_show, width=self.wframe22 - 10, height=self.hframe_canvas, bg="#2C2206")
            frame_canvas.grid(row=0, column=0)
            vsb = Scrollbar(frame_canvas, orient=VERTICAL)
            vsb.grid(row=0, column=1, rowspan=2, sticky=N + S)
            hsb = Scrollbar(frame_canvas, orient=HORIZONTAL)
            hsb.grid(row=1, column=0, columnspan=2, sticky=W + E)
            canvas_site = Canvas(frame_canvas, yscrollcommand=vsb.set, xscrollcommand=hsb.set, bg="#F1F1F2",width=self.wframe22 - 20, height=self.hframe_canvas-20)
            canvas_site.grid(row=0, column=0, sticky="news")
            canvas_site.grid_propagate(0)
            vsb.config(command=canvas_site.yview)
            hsb.config(command=canvas_site.xview)
            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)
            frame_canvas3 = Frame(canvas_site)
            ########################vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            #############################vvvvvvvvvvvvvvvvvvvvvvvvvvv


            btria= Button(frame_canvas3, text='tableau des ria', command=self.all_items)
            btria.grid(row=0, column=0)


            #############^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ##############^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

            canvas_site.create_window(0, 0, window=frame_canvas3)
            frame_canvas3.update_idletasks()
            canvas_site.config(scrollregion=canvas_site.bbox("all"))