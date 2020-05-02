from tkinter import *
from tkinter import ttk

import time
import site_db
import forganisme
from forganisme import analyseenjeux
from forganisme import  addenjeux
from forganisme import organise_db
from forganisme.organise_db import *
go=organise_db.all_db1()

time1=""
class organisme:
    def __init__(self,root,pro_name,site_name,bsite1):
            self.bsite1 = bsite1
            self.site_name = site_name
            self.pro_name=pro_name

            self.root = root
            self.wroot = self.root.winfo_screenwidth() - 6
            self.hroot = self.root.winfo_screenheight() - 74

            self.root.geometry("%dx%d" % (self.wroot, self.hroot))

            vwidth_b = 100 / 1530 * 28 * self.wroot / 100
            wframe_widthb_1 = round(vwidth_b, 0)
            wframe_widthb_2 = str(wframe_widthb_1)[:-2]
            self.wbutton = int(wframe_widthb_2)

            vwidth_bi = 100 / 1530 * 30 * self.wroot / 100
            wframe_widthb_1 = round(vwidth_bi, 0)
            wframe_widthb_2 = str(wframe_widthb_1)[:-2]
            self.wbuttoni = int(wframe_widthb_2)

            vwidth_bi = 100 / 1530 * 200 * self.wroot / 100
            wframe_widthb_1 = round(vwidth_bi, 0)
            wframe_widthb_2 = str(wframe_widthb_1)[:-2]
            self.wcanvas1 = int(wframe_widthb_2)

            vwidth_bi = 100 / 1530 * 1330 * self.wroot / 100
            wframe_widthb_1 = round(vwidth_bi, 0)
            wframe_widthb_2 = str(wframe_widthb_1)[:-2]
            self.wcanvas2 = int(wframe_widthb_2)



            vheight_bi = 100 / 790 * 2 * self.hroot / 100
            hframe1_1 = round(vheight_bi, 0)
            hframe1_2 = str(hframe1_1)[:-2]
            self.hbuttoni = int(hframe1_2)

            vheight_bm = 100 / 790 * 2 * self.hroot / 100
            hframe1_1 = round(vheight_bm, 0)
            hframe1_2 = str(hframe1_1)[:-2]
            self.hbuttonm = int(hframe1_2)


            topwidth_b = 100 / 1530 * 800 * self.wroot / 100
            wframe_widthb_1 = round(topwidth_b, 0)
            wframe_widthb_2 = str(wframe_widthb_1)[:-2]
            self.topwidth = int(wframe_widthb_2)



            vwidth3 = 100 / 1530 * 510 * self.wroot / 100
            wframe_width3_1 = round(vwidth3, 0)
            wframe_width3_2 = str(wframe_width3_1)[:-2]
            self.wframe3 = int(wframe_width3_2)

            vheight1 = 100 / 790 * 30 * self.hroot / 100
            hframe1_1 = round(vheight1, 0)
            hframe1_2 = str(hframe1_1)[:-2]
            self.hframe1 = int(hframe1_2)

            vheight2_button = 100 / 790 * 10 * self.hroot / 100
            hframe2_1_button = round(vheight2_button, 0)
            hframe2_2_button = str(hframe2_1_button)[:-2]
            self.hframe2button = int(hframe2_2_button)

            vheight22 = 100 / 790 * 50 * self.hroot / 100
            hframe22_1 = round(vheight22, 0)
            hframe22_2 = str(hframe22_1)[:-2]
            self.hframe2 = int(hframe22_2)

            vheight4 = 100 / 790 * 710 * self.hroot / 100
            hframe_canvas1 = round(vheight4, 0)
            hframe_canvas2 = str(hframe_canvas1)[:-2]
            self.hframe_canvas = int(hframe_canvas2)

            big_frame = Frame(self.root, width=self.wroot, height=self.hroot, bg="green")
            big_frame.grid(row=0, column=0)
            big_frame.grid_propagate(0)

            self.frame1 = Frame(big_frame, width=self.wroot, height=self.hframe1, bg="#055E33")
            self.frame1.grid(row=0, column=0, columnspan=2)
            self.frame1.grid_propagate(0)

            self.frame2 = Frame(big_frame, width=self.wroot, height=self.hframe2, bg="#055E33")
            self.frame2.grid(row=1, column=0, columnspan=2)

            self.frame2.grid_columnconfigure(0,weight=1)
            self.frame2.grid_columnconfigure(1,weight=6)
            self.frame2.grid_columnconfigure(2,weight=1)

            self.frame3 = Frame(big_frame, width=self.wroot, height=self.hframe_canvas, bg="#F1F1F2")
            self.frame3.grid(row=2, column=0)
            self.frame3.grid_propagate(0)


            frame_canvas = Frame(self.frame3, width=self.wcanvas1 - 10, height=self.hframe_canvas-30, bg="#27A9E1")
            frame_canvas.grid(row=0, column=0,rowspan=2)

            vsb = Scrollbar(frame_canvas, orient=VERTICAL)
            vsb.grid(row=0, column=1, rowspan=2, sticky=N + S)
            hsb = Scrollbar(frame_canvas, orient=HORIZONTAL)
            hsb.grid(row=1, column=0, columnspan=2, sticky=W + E)

            canvas_site = Canvas(frame_canvas, yscrollcommand=vsb.set, xscrollcommand=hsb.set, bg="#27A9E1",width=self.wcanvas1 -20, height=self.hframe_canvas-20)
            canvas_site.grid(row=0, column=0, sticky="news")
            canvas_site.grid_propagate(0)

            vsb.config(command=canvas_site.yview)
            hsb.config(command=canvas_site.xview)

            frame_canvas.grid_rowconfigure(0, weight=1)
            frame_canvas.grid_columnconfigure(0, weight=1)

            frame_canvas2 = Frame(canvas_site)
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

            self.borg = Button(frame_canvas2, text="contexte de l'organisme", width=self.wbutton,height=self.hbuttonm, bg='#38B449')
            self.borg.grid(row=0, column=0)

            self.bleader = Button(frame_canvas2, text="leadership", width=self.wbutton,height=self.hbuttonm)
            self.bleader.grid(row=1, column=0)

            self.bplan = Button(frame_canvas2, text="planification", width=self.wbutton,height=self.hbuttonm)
            self.bplan.grid(row=2, column=0)

            self.bsupp = Button(frame_canvas2, text="support", width=self.wbutton,height=self.hbuttonm)
            self.bsupp.grid(row=3, column=0)

            self.bréal = Button(frame_canvas2, text="réalisation", width=self.wbutton,height=self.hbuttonm)
            self.bréal.grid(row=4, column=0)

            self.béval = Button(frame_canvas2, text="évaluation des perfermancen", width=self.wbutton,height=self.hbuttonm)
            self.béval.grid(row=5, column=0)

            self.bamé = Button(frame_canvas2, text="amélioration", width=self.wbutton,height=self.hbuttonm)
            self.bamé.grid(row=6, column=0)


# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

            canvas_site.create_window(0, 0, window=frame_canvas2)
            frame_canvas2.update_idletasks()

            canvas_site.config(scrollregion=canvas_site.bbox("all"))







#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

    def b(self):
        f1 = Frame(self.frame2,height=self.hframe2)
        f1.grid(row=0, column=0)
        f2 = Frame(self.frame2,height=self.hframe2)
        f2.grid(row=0, column=1)
        f3 = Frame(self.frame2, height=self.hframe2)
        f3.grid(row=0, column=2)

        bpro=Button(f2,text='processus –procédure / instruction',width=self.wbuttoni,height=self.hbuttoni)
        bpro.grid(row=0,column=0)
        bpartie = Button(f2, text='les  parties intéressées et travailleur ',width=self.wbuttoni,height=self.hbuttoni)
        bpartie.grid(row=0, column=1)
        bexigence = Button(f2, text='exigence légal et réglementaire et autre',width=self.wbuttoni,height=self.hbuttoni)
        bexigence.grid(row=0, column=2)

        self.benjeux = Button(f2, text=' enjeux internes et externes', width=self.wbuttoni,height=self.hbuttoni,command=self.depart)
        self.benjeux.grid(row=0, column=3)

# IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII




#fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

    def analyse(self,event):
        go=analyseenjeux.analyseenjeux()
        if event=='analyse externe':
               go.analyseexterne(event,self.pro_name)
        else: go.analyseinterne(event,self.pro_name)

    def add(self,event):
         go=addenjeux.addenjeux(self.pro_name,self.site_name)

         if event=='enjeux externe':
            go.enjeuxexterne()
         else:
             go.enjeuxinterne()






    def depart(self):
        frame_option = Frame(self.frame3, width=self.wcanvas2, height=20, bg='green')
        frame_option.grid(row=0, column=1,sticky=N)
        frame_option.grid_propagate(0)
        frame_option.grid_columnconfigure(0,weight=1)
        frame_option.grid_columnconfigure(1,weight=6)
        frame_option.grid_columnconfigure(2,weight=1)


        frame_option1 = Frame(self.frame3, height=20, bg='green')
        frame_option1.grid(row=0, column=0, sticky=N)
        frame_option2 = Frame(self.frame3, height=20, bg='green')
        frame_option2.grid(row=0, column=1, sticky=N)
        frame_option3 = Frame(self.frame3, height=20, bg='green')
        frame_option3.grid(row=0, column=2, sticky=N)


        badd_interne = Button(frame_option2, text='ajouter enjeux interne', width=self.wbutton,
                              command=lambda: self.add("enjeux interne"))
        badd_interne.grid(row=1, column=0, sticky=W)
        badd_externe = Button(frame_option2, text='ajouter enjeux externe', width=self.wbutton,
                              command=lambda: self.add("enjeux externe"))
        badd_externe.grid(row=1, column=1, sticky=W)

        bfort = Button(frame_option2, text='analyse les enjeux interne',
                       command=lambda: self.analyse("analyse interne"))
        bfort.grid(row=1, column=2)
        bfaib = Button(frame_option2, text='analyse les enjeux externe',
                       command=lambda: self.analyse("analyse externe"))
        bfaib.grid(row=1, column=3)

        bfort = Button(frame_option2, text='afficher les enjeux',
                       command=self.job)
        bfort.grid(row=1, column=4)
        bfaib = Button(frame_option2, text='aficher analyse swot',
                       command=lambda: self.analyse("analyse externe"))
        bfaib.grid(row=1, column=5)






    def job(self):

        frame_canvas = Frame(self.frame3, width=self.wcanvas2, height=self.hframe_canvas - 30, bg="#2C2206")
        frame_canvas.grid(row=1, column=1)

        vsb = Scrollbar(frame_canvas, orient=VERTICAL)
        vsb.grid(row=0, column=1, rowspan=2, sticky=N + S)



        hsb = Scrollbar(frame_canvas, orient=HORIZONTAL)
        hsb.grid(row=1, column=0, columnspan=2, sticky=W + E)


        canvas_site = Canvas(frame_canvas, yscrollcommand=vsb.set,takefocus=0,highlightthickness=0, xscrollcommand=hsb.set, bg="#F1F1F2",
                             width=self.wcanvas2 - 20, height=self.hframe_canvas - 20)
        canvas_site.grid(row=0, column=0, sticky=N)
        canvas_site.grid_propagate(0)

        canvas_site.yview_moveto(1)

        vsb.config(command=canvas_site.yview)
        hsb.config(command=canvas_site.xview)

        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)

        frame_canvas3 = Frame(canvas_site)
        ########################vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        #############################vvvvvvvvvvvvvvvvvvvvvvvvvvv

        self.frame_one=Frame(frame_canvas3,width=self.wcanvas2,height=self.hframe_canvas - 20)
        self.frame_one.grid(row=0,column=0,pady=20)
        self.frame_one.grid_columnconfigure(0,weight=1)
        self.frame_one.grid_columnconfigure(1, weight=1)

        self.frame_one1 = Frame(self.frame_one,width=self.wbutton+50, relief=GROOVE, border='2px')
        self.frame_one1.grid(row=0, column=0,sticky=N+S)
        self.frame_one1.grid_columnconfigure(0,weight=1)

        self.frame_one2= Frame(self.frame_one,width=self.wbutton+50, relief=GROOVE, border='2px')
        self.frame_one2.grid(row=0, column=1,sticky=N+S)
        self.frame_one2.grid_columnconfigure(0, weight=1)





        lenjeux_interne = Label(self.frame_one1, text="les enjeux interne",width=self.wbutton+30, relief=GROOVE, border='2px',bg='green',font=('arial',12))
        lenjeux_interne.grid(row=0, column=0,sticky=W)
        lenjeux_interne.grid_columnconfigure(0,weight=1)

        ls_enjeux_bmode.clear()

        go.lsenjeux_bmode('interne',self.pro_name)
        for i in range(len(ls_enjeux_bmode)):

            lenjeuxi = Label(self.frame_one1, text='  - '+ls_enjeux_bmode[i][0], wraplength=750,font=('arial',12), justify=LEFT)
            lenjeuxi.grid(row=i + 1, column=0,sticky='w',padx=5)


        lenjeux_interne = Label(self.frame_one2, text="les enjeux externe", width=self.wbutton + 30, relief=GROOVE,
                                border='2px', bg='green', font=('arial', 12), justify=RIGHT)
        lenjeux_interne.grid(row=0, column=1, sticky='w')
        ls_enjeux_bmode.clear()

        go.lsenjeux_bmode('externe',self.pro_name)
        for i in range(len(ls_enjeux_bmode)):
            lenjeuxi = Label(self.frame_one2, text='  - '+ls_enjeux_bmode[i][0],
                               font=('arial', 12), justify=LEFT)
            lenjeuxi.grid(row=i + 1, column=1, sticky=W,padx=5)

        #############^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ##############^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        canvas_site.create_window(0, 0, window=frame_canvas3)
        frame_canvas3.update_idletasks()
        canvas_site.config(scrollregion=canvas_site.bbox("all"))




















































    def all_items(self):
        lname_pro = Label(self.frame1, text=self.pro_name, bg="#055E33", fg="white")
        lname_pro.grid(row=0, column=0)
        ldate = Label(self.frame1, font=("arial", 15), bg="#055E33", fg="white")
        ldate.grid(row=0, column=0)
        ltime = Label(self.frame1, font=("arial", 15), bg="#055E33", fg="white")
        ltime.grid(row=0, column=1)
        ltime.grid_rowconfigure(100, weight=1)
        bretour = Button(self.frame1, text='retour')
        bretour.grid(row=0, column=2)

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
            go = part_3.part_3(self.root, self.pro_name, self.site_name, self.bsite1)
            go.all_items()
            """import mlci
            go=mlci.part_mlci(self.root,self.pro_name,self.bsite1,self.site_name)
            go.all_mlci()"""

        bretour.config(command=retour)

        # fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

        def go_contexte():
            go = organisme.organisme(self.root, self.pro_name, self.bsite1, self.site_name)
            go.all_items()
            go.b()
            """import mlci
            go=mlci.part_mlci(self.root,self.pro_name,self.bsite1,self.site_name)
            go.all_mlci()"""

        def go_leadership():
            import leadership
            go = leadership.leadership(self.root, self.pro_name, self.bsite1, self.site_name)
            go.all_items()
            go.b()

        def go_planification():
            import planification
            go = planification.planification(self.root, self.pro_name, self.bsite1, self.site_name)
            go.all_items()
            go.b()

        def go_support():
            import support
            go = support.support(self.root, self.pro_name, self.bsite1, self.site_name)
            go.all_items()
            go.b()

        def go_réalisation():
            import réalisation
            go = réalisation.réalisation(self.root, self.pro_name, self.bsite1, self.site_name)
            go.all_items()
            go.b()

        def go_évaluation():
            import évaluation
            go = évaluation.évaluation(self.root, self.pro_name, self.bsite1, self.site_name)
            go.all_items()
            go.b()

        def go_amélioration():
            import amélioration
            go = amélioration.amélioration(self.root, self.pro_name, self.bsite1, self.site_name)
            go.all_items()
            go.b()

        self.borg.config(command=go_contexte)
        self.bleader.config(command=go_leadership)
        self.bplan.config(command=go_planification)
        self.bsupp.config(command=go_support)
        self.bréal.config(command=go_réalisation)
        self.béval.config(command=go_évaluation)
        self.bamé.config(command=go_amélioration)