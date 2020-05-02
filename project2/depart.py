import tkinter
from tkinter import *
import site_db
import all_db
go=all_db.all_db1

class part_1:


    def __init__(self,root):
        self.root=root

    def widget_part_1(self):
        import part_1
        go_part_1=part_1.part_1(self.root)
        go_part_1.global_()
        go_part_1.job()


if __name__ == "__main__":
    root = Tk()
    depart=part_1(root)
    depart.widget_part_1()
    root.mainloop()