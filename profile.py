from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
from homepageCode import *


class Ui_Profile(QMainWindow):
    def __init__(self):
        super(Ui_Profile,self).__init__()

        uic.loadUi('profile.ui',self)

        print('This is executed at the start')
        cursor.execute("use Cinemax;")

        cmd = "select * from Users where uid = \'{}\' and passwd = \'{}\';".format(name,pwd)
        cursor.execute(cmd)
        out = cursor.fetchall()
        print(out)
        out= out[0]
        email = out[2]
        print(email)
        finame = out[3]
        lname = out[4]
        loc = out[5]
        ph = out[6]

        self.editfname = self.findChild(QPushButton,'editfname')
        self.fname = self.findChild(QLineEdit,'fname')

         #Opens File(Substitute for SQL for now)
        f = open("info.txt",'r')
        #reads file
        infoStack = f.read()
        #splits data
        info = infoStack.split(',')
        #assigns extracted data to variables
        fname = info[0]
        lname = info[1]
        email = info[2]
        ph = info[3]
        loc = info[4]

        self.fname.setText(fname) # changing finame to fname
        self.fname.setReadOnly(True)
        self.lname.setText(lname)
        self.lname.setReadOnly(True)
        self.email.setText(email)
        self.email.setReadOnly(True)
        self.ph.setText(ph)
        self.ph.setReadOnly(True)
        self.loc.setText(loc)
        self.loc.setReadOnly(True)

        self.editfname.clicked.connect(self.changeFname)
        self.editlname.clicked.connect(self.changeLname)
        self.editemail.clicked.connect(self.changeEmail)
        self.editph.clicked.connect(self.changePh)
        self.editloc.clicked.connect(self.changeLoc)
        self.done.clicked.connect(self.apply)
        #closes file
        f.close()

    def apply(self):
        fname = self.fname.text()
        lname = self.lname.text()
        email = self.email.text()
        ph = self.ph.text()
        loc = self.loc.text()
        print(fname,lname,email,ph,loc)
        fe = open('info.txt','w+')
        txt = fname+','+lname+','+email+','+ph+','+loc
        fe.write(txt)
        fe.close()
        conn1 = mys.connect(host = 'localhost', user = 'root', passwd = 'ashmitiscool')
        cursor = conn1.cursor()
        try:

            sql = "UPDATE users SET fname = %s, lname = %s, loc = %s, ph = %s where uid = %s"
            values = (fname, lname, loc, ph, email)

            cursor.execute(sql,values)
            conn1.commit()

        except:
            print('Error in exporting to sql')

        # cmd = "select * from Users where uid = \'{}\' and passwd = \'{}\';".format(name,pwd)
        # cursor.execute(cmd)
        # out = cursor.fetchall()
        # self.fname.setText(finame)
        #
        # self.lname.setText(lname)
        #
        # self.email.setText(email)
        #
        # self.ph.setText(ph)
        #
        # self.loc.setText(loc)


        from menuCode import Ui_Menu
        self.close()
        self.menu_window = Ui_Menu()
        self.menu_window.show()
    
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
