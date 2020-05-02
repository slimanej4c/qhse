
import mysql.connector
ls_date_enjeux=[]
ls_site_enjeux=[]
ls_pro_enjeux=[]




ls_enjeux=[]
ls_analyse=[]
ls_enjeux_bytype=[]
ls_enjeux_bmode=[]
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
    def cenjeux(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists enjeux (id int(11) primary key auto_increment ,mode_enjeux varchar(50) ,type_enjeux varchar(300),enjeux text ,'
                    'date_c VARCHAR (10),pro_enjeux varchar(50),constraint fk_pro foreign key (pro_enjeux) references pro(pro_name) on delete cascade on update cascade)')
        self.mydb.close

    def ienjeux(self,vmode,vtype,venjeux,vdate,vpro,vsite):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into enjeux(mode_enjeux,type_enjeux,enjeux,date_c,pro_enjeux)values(%s,%s,%s,%s,%s)',(vmode,vtype,venjeux, vdate,vpro))
        self.mydb.commit()
        self.mydb.close()
    def lsenjeux(self):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute("select enjeux  from enjeux")
        list_site = cur.fetchall()
        for r in list(list_site):
            ls_enjeux.append(r)
        self.mydb.close()
    def lsenjeux_bt(self,vtype):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute("select enjeux from enjeux where type_enjeux=%s",(vtype,))
        list_type = cur.fetchall()
        for r in list(list_type):
            ls_enjeux_bytype.append(r)
        self.mydb.close()

    def lsenjeux_bmode(self,vmode,vpro_name):

        self.open_data()
        cur = self.mydb.cursor()
        cur.execute("select enjeux from enjeux where mode_enjeux=%s and pro_enjeux=%s",(vmode,vpro_name))
        list_mode = cur.fetchall()
        for r in list(list_mode):
            ls_enjeux_bmode.append(r)
        self.mydb.close()
    def canalyse(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists swot (id int(11) primary key auto_increment ,mode_enjeux varchar(50) ,type_enjeux varchar(300),enjeux text ,analyse text,valeur varchar(15),lie varchar(25),'
                    'date_c VARCHAR (10),pro_enjeux varchar(50),constraint fk_pro_analyse foreign key (pro_enjeux) references pro(pro_name) on delete cascade on update cascade)')
        self.mydb.close
    def ianalyse(self,vmode,vtype,venjeux,vanalyse,vvaleur,vlie,vdate,vpro):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into swot(mode_enjeux,type_enjeux,enjeux,analyse,valeur,lie,date_c,pro_enjeux)values(%s,%s,%s,%s,%s,%s,%s,%s)',(vmode,vtype,venjeux,vanalyse,vvaleur,vlie, vdate,vpro))
        self.mydb.commit()
        self.mydb.close()
    def lsanalyse(self):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute("select analyse from enjeux")
        list_site = cur.fetchall()
        for r in list(list_site):
            ls_analyse.append(r)
        self.mydb.close()

go=all_db1()
go.cenjeux()

go.canalyse()

print(ls_enjeux)

