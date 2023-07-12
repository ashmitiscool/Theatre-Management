from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class Ui_Profile(QMainWindow):
    def __init__(self):
        super(Ui_Profile,self).__init__()
        uic.loadUi('profile.ui',self)
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
        #sets respective variables to line edits, makes line edits uneditable
        self.fname.setText(fname)
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
        fe = open('info.txt','w+')
        txt = fname+','+lname+','+email+','+ph+','+loc
        fe.write(txt)
        fe.close()
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
