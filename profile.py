from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
from homepageCode import *

cursor.execute("use Cinemax;")
# Found the issue, its in the below line, you have taken the info from the name and pwd before it was updated, you have to import from Sql again every time ran this window
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

class Ui_Profile(QMainWindow):
    def __init__(self):
        super(Ui_Profile,self).__init__()

        uic.loadUi('profile.ui',self)

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
        # fe = open('info.txt','w+')
        # txt = fname+','+lname+','+email+','+ph+','+loc
        # fe.write(txt)
        # fe.close()
        try:
            cursor.execute(f'update users set fname="{fname}",lname="{lname}",loc="{loc}",ph="{ph}" where uid="{email}";')
            conn.commit()

        except:
            print('Error in exporting to sql')
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
