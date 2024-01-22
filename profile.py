from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel,QDialog,QPushButton,QFileDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
from homepageCode import *

cursor.execute("use Cinemax;")
f = open('info.txt','r+')
info = f.read()
f.close()
infos = info.split('!!!!!')
name = infos[0]
pwd = infos[1]

cmd = 'create table if not exists pfps(uid varchar(30) not null primary key, picloc varchar(700) not null);'
cursor.execute(cmd)

# Found the issue, its in the below line, you have taken the info from the name and pwd before it was updated, you have to import from Sql again every time ran this window
cmd = "select * from Users where uid = \'{}\' and passwd = \'{}\';".format(name,pwd)
cursor.execute(cmd)
out = cursor.fetchall()
print(out)
out = out[0]
email = out[2]
print(email)
finame = out[3]
lname = out[4]
loc = out[5]
ph = out[6]

cmd = 'select picloc from pfps where uid = \'{}\''.format(name)
cursor.execute(cmd)
out = cursor.fetchall()
print(out)
pfpath = ''
if len(out)==0:
    pfpath = 'null'
else:
    pfpath = out

class Ui_Profile(QMainWindow):
    def __init__(self):
        super(Ui_Profile,self).__init__()

        uic.loadUi('profile.ui',self)
        self.setWindowTitle('Profile')

        self.editfname = self.findChild(QPushButton,'editfname')
        self.fname = self.findChild(QLineEdit,'fname')

        self.fname.setText(finame)
        self.fname.setReadOnly(True)
        self.lname.setText(lname)
        self.lname.setReadOnly(True)
        self.email.setText(email)
        self.email.setReadOnly(True)
        self.ph.setText(ph)
        self.ph.setReadOnly(True)
        self.loc.setText(loc)
        self.loc.setReadOnly(True)

        if pfpath!='null':
            pixmap = QPixmap(pfpath[0][0]).scaled(220, 270)
            self.pic.setPixmap(pixmap)

        
        self.editfname.clicked.connect(self.changeFname)
        self.editlname.clicked.connect(self.changeLname)
        self.editemail.clicked.connect(self.changeEmail)
        self.editph.clicked.connect(self.changePh)
        self.editloc.clicked.connect(self.changeLoc)
        self.done.clicked.connect(self.apply)
        self.browse.clicked.connect(self.changePic)
        self.reload.clicked.connect(self.Bookings)
        self.cancel.clicked.connect(self.cancelb)
        #closes file
        f.close()

    def apply(self):
        fname = self.fname.text()
        lname = self.lname.text()
        email = self.email.text()
        ph = self.ph.text()
        loc = self.loc.text()
        print(fname,lname,email,ph,loc)
        # fe = open('info.txt','w+')
        # txt = fname+','+lname+','+email+','+ph+','+loc
        # fe.write(txt)
        # fe.close()
        try:
            cmd = "update users set fname=\"{}\",lname=\"{}\",loc=\"{}\",ph=\"{}\" where uid=\"{}\"".format(fname,lname,loc,ph,email)
            cursor.execute(cmd)
            conn.commit()

        except:
            print('Error in exporting to sql')
        conn.commit()
        from menuCode import Ui_Menu
        self.close()
        self.menu_window = Ui_Menu()
        self.menu_window.show()

    def changePic(self):
        fname = QFileDialog.getOpenFileName(self,"Open File",'Pictures','Images (*.png *.jpg)')
        pixmap = QPixmap(fname[0]).scaled(220, 270)
        self.pic.setPixmap(pixmap)
        print(fname[0])
        cmd = ''
        print(pfpath)
        if pfpath=='null':
            cmd = "insert into pfps values('{}','{}');".format(name,fname[0])
        else:
            cmd = "update pfps set picloc = '{}' where uid = '{}';".format(fname[0],name)
        print(cmd)
        cursor.execute(cmd)
        conn.commit()            
            
    def changeFname(self):
        self.fname.setReadOnly(False)

    def changeLname(self):
        self.lname.setReadOnly(False)

    def changeEmail(self):
        self.email.setReadOnly(False)

    def changePh(self):
        self.ph.setReadOnly(False)

    def changeLoc(self):
        self.loc.setReadOnly(False)

    def cancelb(self):
        cmd = "delete from booked where user = '{}';".format(name)
        cursor.execute(cmd)
        conn.commit()

    def Bookings(self):
    
        cmd = 'select * from booked;'
        cursor.execute(cmd)
        x = cursor.fetchall()
        mov = ''
        seats = ''
        snacks = ''
        price = 0
        for datas in x:
            if datas[0]==name:
                mov = datas[2]
                seats = datas[1]
                snacks = datas[3]
                price = datas[4]
                print(datas)
                break
        mnsamp = mov
        self.name.setText(mnsamp)
        sbsamp = seats
        self.booked.setText(sbsamp)
        snsamp = snacks
        self.snacks.setText(snsamp)
        prsamp = str(price)
        self.price.setText(prsamp)
        print(mnsamp,sbsamp,snsamp,prsamp,sep='$')
        
