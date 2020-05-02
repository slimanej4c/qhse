import tkinter

from tkinter import *

root=Tk()

root.geometry=('500x500')

frame=Frame(root,width=500,height=500)
frame.grid(row=0,column=0)
frame.grid_propagate(0)
frame.grid_columnconfigure(0,weight=1)
frame.grid_columnconfigure(1,weight=1)

frame1=Frame(frame,width=500,height=500)
frame1.grid(row=0,column=0)
frame1.grid_propagate(0)
frame1.grid_columnconfigure(0,weight=1)

frame2=Frame(frame,width=500,height=500)
frame2.grid(row=0,column=1)
frame2.grid_propagate(0)
frame2.grid_columnconfigure(0,weight=1)


label=Label(frame2,text='yes i am here just here')
label.grid(row=0,column=0,sticky='w')

label=Label(frame2,text='yes i am here just here here its ok')
label.grid(row=1,column=0,sticky='w')

label=Label(frame2,text='yes i am here just here here its okyes i am here just here here its okyes i am here just here here its ok')
label.grid(row=2,column=0,sticky='w')


root.mainloop()


