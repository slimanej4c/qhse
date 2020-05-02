import tkinter
from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
pdfmetrics.registerFont(TTFont('ar','arial.ttf'))

filename='myypdf.pdf'
documenttitle='doctitle'
title='title of slimane'
subtitle='subtitle de slimane:'
textline=['hello word','hello frineds','its me how are you do you miss me ']
image='plan1.jpg'

pdf=canvas.Canvas(filename)
pdf.setTitle(documenttitle)
pdf.setFont('ar',20)
pdf.drawString(250,750,title)

pdf.setFont('ar',12)
pdf.drawString(100,650,subtitle)
pdf.line(100,648,200,648)

text=pdf.beginText(150,630)
text.setFont('Courier',12)
text.setFillColor(colors.red)
for line in textline:
    text.textLine(line)
pdf.drawText(text)
#pdf.drawImage(image,150,500,300,150)


pdf.drawInlineImage(image,150,400,300,150)



text.setFillColor(colors.black)






def xy():
    pdf.drawString(100,800,'x100')
    pdf.drawString(200, 800, 'x200')
    pdf.drawString(300, 800, 'x300')
    pdf.drawString(400, 800, 'x400')
    pdf.drawString(500, 800, 'x500')

    pdf.drawString(10, 100, 'x100')
    pdf.drawString(10, 200, 'x200')
    pdf.drawString(10, 300, 'x300')
    pdf.drawString(10, 400, 'x400')
    pdf.drawString(10, 500, 'x500')
    pdf.drawString(10, 600, 'x600')
    pdf.drawString(10, 700, 'x700')
    pdf.drawString(10, 800, 'x800')

xy()
pdf.save()


























""""
import test1
from test1 import db
from test1.db import *
go=db.db1()
go.cadmin()
go.cnum()

root=Tk()
root.geometry('900x400')

class job:
    def __init__(self):
        self.f1=Frame(root,width=900,height=400)
        self.f1.grid(row=0,column=0)
        self.f1.grid_propagate(0)
        self.part1()

    def part1(self):
        self.bregister=Button(self.f1,text='register',command=self.register)
        self.bregister.grid(row=0,column=0)
        self.blogin=Button(self.f1,text='login',command=self.login)
        self.blogin.grid(row=1,column=1)

    def register(self):
        top=Toplevel()
        top.geometry('300x300')
        ltitle = Label(top, text='register',fg='red')
        ltitle.grid(row=0, column=0)
        vemail=StringVar()
        vpass = StringVar()
        lemail=Label(top,text='email :')
        lemail.grid(row=1,column=0)
        lpass = Label(top, text='password :')
        lpass.grid(row=2, column=0)
        eemail=Entry(top,textvariable=vemail)
        eemail.grid(row=1,column=1)
        epass = Entry(top, textvariable=vpass)
        epass.grid(row=2, column=1)
        self.breg = Button(top, text='register',command=lambda:go.iadmin(eemail.get(),epass.get()))
        self.breg.grid(row=3, column=0)

    def go(self,vemail,vpass):
        ls_admin.clear()
        go.lsadmin(vemail)
        print(ls_admin)
        if vpass not in ls_admin:
            self.f1.config(bg='red')
        else:
          ecreate = Entry(self.f1)
          ecreate.grid(row=4, column=1)

          bjob1=Button(self.f1,text='create',command=lambda:go.inum(vemail,int(ecreate.get())))
          bjob1.grid(row=4,column=0)

          def show():
              ls_num.clear()
              go.lsnum(vemail)
              for i in range(len(ls_num)):
                  lb=Label(self.f1,text=ls_num[i])
                  lb.grid(row=i+5,column=0)

          bshow = Button(self.f1, text='show numbres', command=show)
          bshow.grid(row=5, column=0)





    def login(self):
        top = Toplevel()

        top.geometry('300x300')
        ltitle = Label(top, text='login', fg='red')
        ltitle.grid(row=0, column=0)
        vemail = StringVar()
        vpass = StringVar()
        lemail = Label(top, text='email :')
        lemail.grid(row=1, column=0)
        lpass = Label(top, text='password :')
        lpass.grid(row=2, column=0)
        eemail = Entry(top, textvariable=vemail)
        eemail.grid(row=1, column=1)
        epass = Entry(top, textvariable=vpass)
        epass.grid(row=2, column=1)
        self.blog = Button(top, text='login',command=lambda:self.go(eemail.get(),epass.get()))
        self.blog.grid(row=3, column=0)



job()
root.mainloop()"""