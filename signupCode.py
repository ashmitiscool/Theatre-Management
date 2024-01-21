from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
from homepageCode import cursor,conn

##cursor.execute('drop database if exists Cinemax;')
cursor.execute('create database if not exists Cinemax;')
cursor.execute('use Cinemax;')
cursor.execute('create table if not exists Users(ID int primary key not null auto_increment, passwd varchar(20) not null, uid varchar(30) not null unique, fname varchar(20), lname varchar(20), loc varchar(20), ph varchar(10));')

class Ui_Signup(QDialog):
    def __init__(self):
        super(Ui_Signup, self).__init__()

        # Load the ui file
        uic.loadUi('signup.ui',self)

        # Defining Widgets
        self.submitButton = self.findChild(QPushButton, 'signupSubmit')
        self.backButton = self.findChild(QPushButton, 'backButton')

        #Sets Error to Invisible
        self.error.setVisible(False)

        # When button pressed, Open new window and add info to database
        self.submitButton.clicked.connect(self.openDialogBox)
        self.backButton.clicked.connect(self.openHomepageWindow)


    def openDialogBox(self):
        name = self.name.text()
        pwd = self.pwd.text()
        confpwd = self.confpwd.text()
        if confpwd==pwd:
            pwd = confpwd
            self.error.setVisible(False)
        else:
            self.error.setVisible(True)
            return 0
                
        cmd="insert into Users (passwd,uid,fname,lname,loc,ph) values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format(pwd,name,'','','','')
        cursor.execute(cmd)
        conn.commit()
        #(ID,passwd,uid,fname,lname,loc,ph)
            
        # Create a message box object
        msg = QMessageBox()
        # Set the text and icon of the message box
        msg.setText("Account Created, Please Log In")
        msg.setIcon(QMessageBox.Information)
        # Add an OK button to the message box
        msg.setStandardButtons(QMessageBox.Ok)
        # Show the message box and get the user response
        response = msg.exec_()
        # If the user clicked OK, open the homepage window
        if response == QMessageBox.Ok:
            self.openHomepageWindow()

    def openHomepageWindow(self):
        from homepageCode import Ui_HomePage
        self.close()
        self.menu_window = Ui_HomePage()
        self.menu_window.show()








