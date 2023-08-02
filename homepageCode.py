from PyQt5.QtWidgets import QLineEdit,QMainWindow, QApplication, QLabel, QPushButton, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
import mysql.connector as mys

f = open('sql.txt','r')
sql = f.read()
sqlx = sql.split(',')
hostx = sqlx[0]
userx = sqlx[1]
passwdx = sqlx[2]
global conn
conn = mys.connect(host = 'localhost', user = 'root', passwd = 'ashmitiscool')
f.close()
global cursor
cursor = conn.cursor()
f = open('info.txt','a+')

#MySQL Connection: Enter your SQL parameters in sql.txt
#in the txt file...1st param: host, 2nd: root, 3rd:password...do not delete the commas



# Actually login page
# Page to start the program
class Ui_HomePage(QMainWindow):
    def __init__(self):
        super(Ui_HomePage, self).__init__()



        # Load the ui file
        uic.loadUi('homepage2.ui',self)

        # Defining Widgets
        self.submitButton = self.findChild(QPushButton, 'submit')
        self.signupButton = self.findChild(QPushButton, 'signup')
        self.resetButton = self.findChild(QPushButton, 'reset')
        self.error.setVisible(False)
        self.nameLineEdit = self.findChild(QLineEdit, 'name')
        self.passLineEdit = self.findChild(QLineEdit, 'pwd')

        # When button pressed, Open new window
        self.submitButton.clicked.connect(self.openMenuWindow)
        self.signupButton.clicked.connect(self.openSignupWindow)
        self.resetButton.clicked.connect(self.resetTextField)

        self.show()

#Undo area

    def openMenuWindow(self):
        name = self.name.text()
        pwd = self.pwd.text()
        if name!='admin' and pwd!='admin':
            cursor.execute("use Cinemax;")
            try:
                try:
                    strg = name+'*_*'+pwd
                    f.write(strg)
                    f.close()
                except:
                    print('file error')
                cmd = "select * from Users where uid = \'{}\' and passwd = \'{}\';".format(name,pwd)
                cursor.execute(cmd)
                out = cursor.fetchall()
                if len(out) == 0:
                    self.error.setVisible(True)
                    return 0
                out = out[0]
                print(out)
                self.error.setVisible(False)
            except:
                self.error.setVisible(True)
                print('Except error')
                return 0

            from menuCode import Ui_Menu
            self.close()
            self.menu_window = Ui_Menu()
            self.menu_window.show()
        else:
            self.close()
            with open("adminCLI.py") as f:
                exec(f.read())


    def openSignupWindow(self):
        from signupCode import Ui_Signup
        self.close()
        self.signup_window = Ui_Signup()
        self.signup_window.show()

    def resetTextField(self):
        self.nameLineEdit.clear()
        self.passLineEdit.clear()







