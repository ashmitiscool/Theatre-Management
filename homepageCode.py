from PyQt5.QtWidgets import QLineEdit,QMainWindow, QApplication, QLabel, QPushButton, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class Ui_HomePage(QMainWindow):
    def __init__(self):
        super(Ui_HomePage, self).__init__()

        # Load the ui file
        uic.loadUi('homepage2.ui',self)

        # Defining Widgets
        self.submitButton = self.findChild(QPushButton, 'submit')
        self.signupButton = self.findChild(QPushButton, 'signup')
        self.resetButton = self.findChild(QPushButton, 'reset')

        self.nameLineEdit = self.findChild(QLineEdit, 'name')
        self.passLineEdit = self.findChild(QLineEdit, 'pwd')

        # When button pressed, Open new window
        self.submitButton.clicked.connect(self.openMenuWindow)
        self.signupButton.clicked.connect(self.openSignupWindow)
        self.resetButton.clicked.connect(self.resetTextField)

        self.show()



    def openMenuWindow(self):
        from menuCode import Ui_Menu
        self.close()
        self.menu_window = Ui_Menu()
        self.menu_window.show()

    def openSignupWindow(self):
        from signupCode import Ui_Signup
        self.close()
        self.signup_window = Ui_Signup()
        self.signup_window.show()

    def resetTextField(self):
        self.nameLineEdit.clear()
        self.passLineEdit.clear()






app = QApplication(sys.argv)
UIWindow = Ui_HomePage()
app.exec_()
