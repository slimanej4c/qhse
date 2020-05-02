
import mysql.connector
ls_date=[]
ls_site=[]
ls_pro=[]

ls_site_d=[]

ls_pro_sbd=[]
ls_pro_d=[]
import re

class all_db1:

    def __init__(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane'
        )
        cur=self.mydb.cursor()
        cur.execute('create database if not exists qhsecontrol')


    def open_data(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhsecontrol')
    def csite(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists site (site_name varchar(11) primary key,date_c VARCHAR (10))')
        self.mydb.close
        print("ok")
    def isite(self,vsite_name,vdate_c):

        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into site (site_name,date_c)values(%s,%s)',(vsite_name, vdate_c))
        self.mydb.commit()
        self.mydb.close()
    def dsite(self,vsite_name):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('delete from site where site_name=%s ',(vsite_name,))
        self.mydb.commit()
        self.mydb.close()
    def lssite(self):

        self.open_data()
        cur = self.mydb.cursor()
        cur.execute("select * from site")
        list_site = cur.fetchall()
        for r in list(list_site):
            ls_site.append(r[0])
        self.mydb.close()


    def cpro(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists pro (pro_name VARCHAR (10) primary key ,site_name varchar(25),date_c varchar (20),constraint fkid_site foreign key(site_name) references site(site_name) on delete cascade on update cascade )')
        self.mydb.close
        print("ok")
    def ipro(self,vpro_name,vsite_name,vdate_c):
        v=vpro_name+'_'+vsite_name

        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into pro (pro_name,site_name,date_c)values(%s,%s,%s)',(v,vsite_name, vdate_c,))
        self.mydb.commit()
        self.mydb.close()
    def dpro(self,vpro_name):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('delete from pro where pro_name=%s ',(vpro_name,))
        self.mydb.commit()
        self.mydb.close()
    def lspro(self,vsite_name):

        self.open_data()
        cur = self.mydb.cursor()
        cur.execute("select * from pro where site_name=%s",(vsite_name,))
        list_pro = cur.fetchall()
        for r in list(list_pro):
            ls_pro.append(r[0])
        self.mydb.close()

go=all_db1()
go.csite()
go.cpro()