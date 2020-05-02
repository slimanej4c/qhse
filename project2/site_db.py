

import mysql.connector
ls_date=[]
ls_site_db=[]
ls_site_sbd=[]

ls_site_d=[]

ls_pro_sbd=[]
ls_pro_d=[]
import re

class sitedb:

    def __init__(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane'
        )
        cur=self.mydb.cursor()
        cur.execute('create database if not exists qhse')


    def open_data(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse')
    def cdate(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists date(id_date int(11) primary key)')
        self.mydb.close
        print("ok")
    def idate(self,date_now):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into date (id_date)values(%s)',(date_now,))
        self.mydb.commit()
        self.mydb.close()
        print('iddd')
    def lsdate(self):

        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('select * from date ')
        sdate=cur.fetchall()
        for x in list(sdate):
            ls_date.append(x[0])
        self.mydb.close()
    ###################################################################################################################
    def site(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists site (id int(11) primary key auto_increment,id_date int(11),site_name varchar (25) ,constraint fkid_site foreign key(id_date) references date(id_date) on delete cascade on update cascade )')
        self.mydb.close()

    def isite(self,id_date,site_name):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into site (id_date,site_name)values(%s,%s)',(id_date,site_name,))
        self.mydb.commit()
        self.mydb.close()
    def lssite(self):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('select site_name  from site ')
        sdate = cur.fetchall()
        for x in list(sdate):
            ls_site.append(x[0])
        self.mydb.close()
    def dsite(self,id_date):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('delete from site where id_date=%s ',(id_date,))
        self.mydb.commit()
        self.mydb.close()
    def dsiteanddate(self,id_date,sitename):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('delete from site where id_date=%s and site_name=%s ',(id_date,sitename))
        self.mydb.commit()
        self.mydb.close()
    def lssite_sbd(self):
        ls_site_d.clear()
        go.lssite_d()
        if ls_site_d !=[]:
            self.open_data()
            cur = self.mydb.cursor()
            cur.execute('select site_name  from site where id_date=%s',(ls_site_d[-1],))
            sdate = cur.fetchall()
            for x in list(sdate):
                ls_site_sbd.append(x[0])
            self.mydb.close()


    def lssite_d(self):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('select id_date  from site')
        sdate = cur.fetchall()
        for x in list(sdate):
            ls_site_d.append(x[0])
        self.mydb.close()
######################################################################################################################################
class prodb :
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse',
        )
        self.mydb.close()



    def open_data(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse')

    def ctsite(self,sitename):
        sitename = sitename.replace(" ", "_")

        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists  '+sitename+' (id int(11)  primary key auto_increment, id_date int(8) ,proname varchar(50), foreign key(id_date) references date(id_date) on delete cascade on update cascade )')
        self.mydb.close()
    def ipro(self,sitename,id_date,proname):
        #sitename = sitename.replace(" ", "_")
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('insert into '+sitename+'(id_date,proname)values(%s,%s)',(id_date,proname))
        self.mydb.commit()
        self.mydb.close()
    def lpro_sbd(self,sitename):
        self.open_data()
        ls_pro_d.clear()

        self.lpro_d(sitename)
        if ls_pro_d !=[]:
            self.open_data()
            cur=self.mydb.cursor()
            cur.execute('select proname from '+sitename+' where id_date=%s',(ls_pro_d[-1],))
            spro=cur.fetchall()
            for x in list(spro):
                ls_pro_sbd.append(x[0])
            self.mydb.close()
    def lpro_d(self,sitename):
        self.open_data()

        cur=self.mydb.cursor()
        cur.execute('select id_date from '+sitename)
        sid_date=cur.fetchall()
        for x in list(sid_date):
            ls_pro_d.append(x[0])
        self.mydb.close()
    def dpro(self,sitename,proname,id_date):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('delete from '+sitename+' where id_date=%s and proname=%s',(id_date,proname))
        self.mydb.commit()
        self.mydb.close()
go=sitedb()
go.cdate()
go.site()

#####################################################################################################################################################
ls_numéro=[]
ls_type=[]
ls_poid=[]
ls_lieu=[]
ls_v=[]
ls_r=[]
class mlci:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse',
        )
        self.mydb.close()
    def open(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse')
    def ctex(self,name_pro):
        vpro=name_pro.replace(" ","_")
        name_ex=vpro+"mlci"
        self.open()
        cur=self.mydb.cursor()
        cur.execute("create table if not exists "+name_ex+" (id int(11)  not null primary key auto_increment, numéro int(11),type varchar(25),poid varchar(10),lieu varchar(200),verification varchar(10),recharge varchar(10))")
        self.mydb.close()

    def iex(self,vnum,vtype,vpoid,vlieu,vv,vr,name_pro):
        vpro = name_pro.replace(" ", "_")
        pro_name = vpro + "mlci"
        self.open()
        cur = self.mydb.cursor()
        cur.execute('insert into '+ pro_name+' (numéro,type,poid,lieu,verification,recharge)values(%s,%s,%s,%s,%s,%s)',(vnum,vtype,vpoid,vlieu,vv,vr))
        self.mydb.commit()
        self.mydb.close()

    def uex(self,vnum,vtype,vpoid,vlieu,vv,vr,vnum1,name_pro):
        vpro = name_pro.replace(" ", "_")
        pro_name = vpro + "mlci"
        print('dbdbdb'+vv)
        self.open()
        cur = self.mydb.cursor()
        cur.execute("update " +pro_name+ " set numéro=%s,type=%s,poid=%s,lieu=%s,verification=%s,recharge=%s where numéro=%s",(vnum,vtype,vpoid,vlieu,vv,vr,vnum1))
        self.mydb.commit()
        self.mydb.close()
    def lsex(self,name_pro):
        vpro = name_pro.replace(" ", "_")
        name_ex = vpro + "mlci"
        self.open()
        cur = self.mydb.cursor()
        cur.execute("select * from "+name_ex+ "")
        list_ex = cur.fetchall()
        for r in list(list_ex):
            ls_numéro.append(r[1])
        for r in list(list_ex):
            ls_type.append(r[2])
        for r in list(list_ex):
            ls_poid.append(r[3])
        for r in list(list_ex):
            ls_lieu.append(r[4])
        for r in list(list_ex):
            ls_v.append(r[5])
        for r in list(list_ex):
            ls_r.append(r[6])
        self.mydb.close()
    def dex(self,lnum,name_pro):
        vpro = name_pro.replace(" ", "_")
        pro_name = vpro + "mlci"
        self.open()
        cur=self.mydb.cursor()
        cur.execute("delete from "+pro_name+" where numéro=%s ",(lnum,))
        self.mydb.commit()
        self.mydb.close()
    def ctimg(self,pro_name):
        self.open()
        img="img"+ pro_name
        print(img)
        cur=self.mydb.cursor()
        cur.execute('create table if not exists ' + img +' (id int(3) not null auto_increment primary key, img blob)')
        self.mydb.close()

    def table_img1(self,pro_name,source):
        self.open()
        img="img"+ pro_name
        print(img)
        cur=self.mydb.cursor()
        cur.execute('insert into '+ img +' (img )values(%s)',(source,))
        self.mydb.commit()
        self.mydb.close()

    list_img=[]
    def lsimg(self,pro_name):
        img = "img" + pro_name

        self.open()
        cur = self.mydb.cursor()
        cur.execute("select * from "+img+ "")
        select_ex = cur.fetchall()
        lselect_ex = list(select_ex)
        global list_img

        for r in range(len(lselect_ex)):
            pro_ex= lselect_ex[r][1]
            list_img.append(pro_ex)
        self.mydb.close()
ls_tablesmlci=[]
class globalmlci:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse',
        )
        self.mydb.close()

    def open(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='qhse')

    def salltables(self):
           self.open()
           cur=self.mydb.cursor()
           cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'qhse' ")
           listtable=cur.fetchall()

           for i in list(listtable):

               pattern = re.compile("^([a-z]+mlci)+$")
               if pattern.match(i[0]):
                   ls_tablesmlci.append(i[0])

                   print(ls_tablesmlci)
           self.mydb.close()
    def uniontables(self):
           self.open()
           cur=self.mydb.cursor()
           cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'qhse' ")
           list=cur.fetchall()
           print(list)

           self.mydb.close()

k=globalmlci()
k.uniontables()









"""
a=10
b='erfverv'
c='dfvfv'
d='erfverv'
e='dfvfv'
f='erfverv'
g='ddp'
k=5
go=mlci()
go.uex(a,b,c,d,e,f,k,g)"""
"""
d='mlci'
import re
string='dsdmlci'
pattern = re.compile("^([a-z]+mlci)+$")

if pattern.match(string):
    print("yess")"""




