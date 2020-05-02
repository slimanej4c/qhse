import tkinter
from tkinter import *
from datetime import datetime
import time
from tkinter import ttk
from tkinter import messagebox

time1 = ""
"""import processus_db
import part1"""
import random

import all_db
from all_db import *

go=all_db.all_db1()
go.cpro()


class part_2:

    def __init__(self, root, site_name, bsite1):
        self.bsite1 = bsite1
        self.site_name = site_name
        self.root = root
        self.wroot = self.root.winfo_screenwidth() - 6
        self.hroot = self.root.winfo_screenheight() - 74

        self.root.geometry("%dx%d" % (self.wroot, self.hroot))
        vwidthtop = 100 / 1530 * 800 * self.wroot / 100
        wtop_width3_1 = round(vwidthtop, 0)
        wframe_width3_2 = str(wtop_width3_1)[:-2]
        self.wtop = int(wframe_width3_2)

        vheighttop = 100 / 790 * 500 * self.hroot / 100
        hframe1_1 = round(vheighttop, 0)
        hframe1_2 = str(hframe1_1)[:-2]
        self.htop = int(hframe1_2)

        vwidth3 = 100 / 1530 * 510 * self.wroot / 100
        wframe_width3_1 = round(vwidth3, 0)
        wframe_width3_2 = str(wframe_width3_1)[:-2]
        self.wframe3 = int(wframe_width3_2)

        vwidth5 = 100 / 1530 * 42 * self.wroot / 100
        wframe_width5_1 = round(vwidth5, 0)
        wframe_width5_2 = str(wframe_width5_1)[:-2]
        self.wframe5 = int(wframe_width5_2)

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

        self.frame3 = Frame(big_frame, width=self.wroot, height=self.hframe3, bg="#27A9E1")
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

    def sup_pro(self):
        a = messagebox.askyesno('invertissement', 'tu est sur tu veut supp' + self.vcb_pro.get())
        if a == True:
            v=self.vcb_pro.get()
            go.dpro(v)
            self.global_()
            self.job()
        else:
            None
    def ajouter_pro(self):
        day = self.eday.get()
        month = self.emonth.get()
        year = self.eyear.get()
        date_c = int(day + month + year)
        pro_name = self.vname.get()
        site_name = self.site_name
        # go1 = site_db.sitedb()
        # go = site_db.prodb()

        ls_pro.clear()
        go.lspro(self.site_name)
        # go.lpro_d(self.site_name)
        if pro_name not in ls_pro:
            go.ipro(pro_name, site_name, date_c)
            self.top.destroy()
            self.global_()
            self.job()

        else:
            print('you list pro is clear')
    def add_processus(self):
        self.top = Toplevel()
        self.top.geometry("%dx%d" % (self.wtop, self.htop))
        f2 = Frame(self.top, width=self.wtop, height=self.htop / 3)
        f2.grid(row=1, column=0)
        f2.grid_propagate(0)
        f1 = Frame(self.top, width=self.wtop, height=self.htop / 3)
        f1.grid(row=0, column=0)
        f1.grid_propagate(0)
        f3 = Frame(self.top, width=self.wtop, height=self.htop / 3)
        f3.grid(row=2, column=0)
        f3.grid_propagate(0)
        self.vday = StringVar()
        self.vmonth = StringVar()
        self.vyear = StringVar()
        self.vname = StringVar()

        lday = Label(f1, text="day", )
        lday.grid(row=0, column=1, pady=50)
        self.eday = Entry(f1, textvariable=self.vday, width=8)
        self.eday.grid(row=0, column=2, pady=50)
        lmonth = Label(f1, text="month")
        lmonth.grid(row=0, column=3, pady=50)
        self.emonth = Entry(f1, textvariable=self.vmonth, width=8)
        self.emonth.grid(row=0, column=4, pady=50)
        lyear = Label(f1, text="year:")
        lyear.grid(row=0, column=5, pady=50)
        self.eyear = Entry(f1, textvariable=self.vyear, width=8)
        self.eyear.grid(row=0, column=6, pady=50)
        lvid = Label(f1, width=13)
        lvid.grid(row=1, column=0)
        lname = Label(f1, text="le titre de pro  :")
        lname.grid(row=2, column=1)
        self.ename = Entry(f1, textvariable=self.vname)
        self.ename.grid(row=2, column=2)



        bname = Button(f2, text="valider", command=self.ajouter_pro, width=20)
        bname.grid(row=3, column=1, columnspan=3, pady=90)
    def global_(self):

        bretour = Button(self.frame11, text="retour")
        bretour.grid(row=0, column=1)

        def retour():
            import part_1
            gopart1 = part_1.part_1(self.root)
            gopart1.global_()
            gopart1.job()
            bretour.destroy()
        bretour.config(command=retour)
        self.vcb_pro = StringVar()
        self.ve_pro = StringVar()

        ladd_pro = Label(self.frame22, text="ajouter processus")
        ladd_pro.grid(row=0, column=0)

        eadd_pro = Entry(self.frame22, textvariable=self.ve_pro)
        eadd_pro.grid(row=0, column=1)

        badd_pro = Button(self.frame22, text="ajouter processus",command=self.add_processus)
        badd_pro.grid(row=0, column=2)


        lsup_pro = Label(self.frame22, text="supprimer processus")
        lsup_pro.grid(row=0, column=3)

        ls_pro.clear()
        go.lspro(self.site_name)


        cbsup_pro = ttk.Combobox(self.frame22, textvariable=self.vcb_pro)
        cbsup_pro.grid(row=0, column=4)
        cbsup_pro["values"] = ls_pro
        cbsup_pro.current()

        bsup_pro = Button(self.frame22, text="supprimer",command=self.sup_pro)
        bsup_pro.grid(row=0, column=5)
        ldate = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ldate.grid(row=0, column=0)
        ltime = Label(self.frame13, font=("arial", 15), bg="#055E33", fg="white")
        ltime.grid(row=0, column=1)
        ltime.grid_rowconfigure(100, weight=1)

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
        self.job()
    def job(self):
        frame_canvas = Frame(self.frame2, width=self.wroot - 10, height=self.hframe_canvas, bg="#2C2206")
        frame_canvas.grid(row=1, column=0)

        vsb = Scrollbar(frame_canvas, orient=VERTICAL)
        vsb.grid(row=0, column=1, rowspan=2, sticky=N + S)
        hsb = Scrollbar(frame_canvas, orient=HORIZONTAL)
        hsb.grid(row=1, column=0, columnspan=2, sticky=W + E)
        canvas_site = Canvas(frame_canvas, yscrollcommand=vsb.set, xscrollcommand=hsb.set, bg="#a2a86f",
                             width=self.wroot - 20, height=self.hframe_canvas)
        canvas_site.grid(row=0, column=0, sticky="news")
        canvas_site.grid_propagate(0)

        vsb.config(command=canvas_site.yview)
        hsb.config(command=canvas_site.xview)

        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)

        frame_canvas2 = Frame(canvas_site)
        ########################


        """go=site_db.prodb()
        ls_pro_sbd.clear()
        go.lpro_sbd(self.site_name)
        len_list_site1=len(ls_pro_sbd)"""
        go=all_db1()
        ls_pro.clear()
        go.lspro(self.site_name)



        n = 0
        if ls_pro !=[]:
            for i in range(len(ls_pro)):
                k = i / 5
                ii = str(k)
                s = len(ii)
                z = ii[s - 1]
                zz = int(ii[0])



                if i <= 4:
                    vtext = ls_pro[i]
                    bsite = Button(frame_canvas2, width=self.wframe5, height=10, text=vtext, padx=0, pady=0)
                    bsite.grid(row=1, column=i)

                if z == "0" and i > 4:
                    n = n + 1
                    f = 5 * zz

                    vtext = ls_pro[i]
                    bsite = Button(frame_canvas2, width=self.wframe5, height=10, text=vtext)
                    bsite.grid(row=1 + n, column=i - f)
                if z != "0" and i > 4:
                    f = 5 * zz

                    vtext = ls_pro[i]
                    bsite = Button(frame_canvas2, width=self.wframe5, height=10, text=vtext)
                    bsite.grid(row=1 + n, column=i - f)

                def chose(bsite1):
                    import part_3
                    pro_name = bsite1["text"]

                    go_part_4 = part_3.part_3(self.root, pro_name, self.site_name, self.bsite1)
                    go_part_4.all_items()

                bsite["command"] = lambda bsite1=bsite: bsite.configure(command=chose(bsite1))

        ######################

        canvas_site.create_window(0, 0, window=frame_canvas2)
        frame_canvas2.update_idletasks()

        canvas_site.config(scrollregion=canvas_site.bbox("all"))


