from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QLabel, QPushButton
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
        self.submitButton.clicked.connect(self.openDialogBox)





    def openDialogBox(self):
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





