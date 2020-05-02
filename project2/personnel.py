import tkinter
from tkinter import ttk
from tkinter import *

from datetime import datetime
import time
import random


time1=""
class personnel:
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
            self.bper = Button(frame_canvas2, text="personnel", width=self.wbutton,bg='green')
            self.bper.grid(row=0, column=0)

            self.bmlci=Button(frame_canvas2,text="MLCI",width=self.wbutton,command=self.go_mlci)
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



    def b(self):
        btpr=Button(self.frame22,text='personel',command=self.jobpr)
        btpr.grid(row=0,column=0)

    def go_mlci(self):
        import mlci1
        go = mlci1.mlci1(self.root, self.pro_name, self.bsite1, self.site_name)
        go.all_items()
        go.b()
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

        bretour.config(command=retour,bg='green')
    def jobpr(self):

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

            btex = Button(frame_canvas3, text='les person', command=self.all_items)
            btex.grid(row=0, column=0)


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