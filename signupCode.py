from PyQt5.QtWidgets import QMainWindow,QDialog, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class Ui_Signup(QDialog):
    def __init__(self):
        super(Ui_Signup, self).__init__()

        # Load the ui file
        uic.loadUi('signup.ui',self)

        # Defining Widgets
        self.submitButton = self.findChild(QPushButton, 'signupSubmit')

        # When button pressed, Open new window
        self.submitButton.clicked.connect(self.openHomepageWindow)





    def openHomepageWindow(self):
        from homepageCode import Ui_HomePage
        self.menu_window = Ui_HomePage()
        self.close()




app = QApplication(sys.argv)
UIWindow = Ui_Signup()
UIWindow.show()
app.exec_()
