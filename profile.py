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
        #closes file
        #have to create a thing where pressing the pencil icon makes line editable...
        #no time lol
        f.close()
