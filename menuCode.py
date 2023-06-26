from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class Ui_Menu(QMainWindow):
    def __init__(self):
        super(Ui_Menu, self).__init__()

        # Load the ui file
        uic.loadUi('menu.ui',self)

        # Defining Widgets
        self.logoutButton = self.findChild(QPushButton, 'logoutButton')
        self.exitButton = self.findChild(QPushButton, 'quitButton')

        # When button pressed, Open new window
        self.logoutButton.clicked.connect(self.openDialogBox)
        self.exitButton.clicked.connect(self.exitProg)



    def openDialogBox(self):
        # Create a message box object
        msg = QMessageBox()
        # Set the text and icon of the message box
        msg.setText("Are you sure you want to log out?")
        msg.setIcon(QMessageBox.Information)
        # Add an OK button to the message box
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Show the message box and get the user response
        response = msg.exec_()
        # If the user clicked OK, open the homepage window
        if response == QMessageBox.Yes:
            self.openLoginWindow()
        else:
            pass

    def openLoginWindow(self):
        from homepageCode import Ui_HomePage
        self.close()
        self.menu_window = Ui_HomePage()
        self.menu_window.show()

    def exitProg(self):
        QApplication.quit()







