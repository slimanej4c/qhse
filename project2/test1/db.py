import mysql.connector
ls_admin=[]
ls_num=[]
class db1:
    def __init__(self):

       self.mydb=mysql.connector.connect(
           host='localhost',
           user='root',
           password='slimane',

       )
       cur=self.mydb.cursor()
       cur.execute('create database if not exists test')

    def open(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='slimane',
            database='test'

        )

    def cadmin(self):
        self.open()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists admin (email varchar(100) primary key ,password varchar (25))')
        self.mydb.close()

    def iadmin(self,email,password):
        self.open()
        cur=self.mydb.cursor()
        cur.execute('insert into admin (email,password)values(%s,%s)',(email,password))
        self.mydb.commit()
        self.mydb.close()

    def lsadmin(self,vemail):
        self.open()
        cur = self.mydb.cursor()
        cur.execute('select * from admin where email=%s',(vemail,))
        list_site = cur.fetchall()
        for r in list(list_site):
            ls_admin.append(r[1])
        self.mydb.close()

    def cnum(self):
        self.open()
        cur = self.mydb.cursor()
        cur.execute('create table if not exists num (id int(11) primary key auto_increment  ,email varchar(100),num int(11),constraint fkid_email foreign key(email) references admin(email) on delete cascade on update cascade )')
        self.mydb.close()

    def inum(self,vemail,vnum):
        self.open()
        cur=self.mydb.cursor()
        cur.execute('insert into num (email,num)values(%s,%s)',(vemail,vnum))
        self.mydb.commit()
        self.mydb.close()

    def lsnum(self,vemail):
        self.open()
        cur = self.mydb.cursor()
        cur.execute('select * from num where email=%s',(vemail,))
        list_site = cur.fetchall()
        for r in list(list_site):
            ls_num.append(r[2])
        self.mydb.close()

    def cnumm(self):
        self.open()
        cur = self.mydb.cursor()
        cur.execute('create table if not exists nn(id int(11),enjeux text not null primary key ,email varchar(100),num int(11) ,unique key len_enjeux(id,enjeux(700)))')
        self.mydb.close()
go=db1()
go.cnumm()