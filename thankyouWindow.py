from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class Ui_Thankyou(QMainWindow):
    def __init__(self):
        super(Ui_Thankyou, self).__init__()

        # Load the ui file
        uic.loadUi('thank you.ui',self)
        self.setWindowTitle('Thank You')

        # Defining Widgets
        self.menuButton = self.findChild(QPushButton,'menuButton')
        self.logoutButton = self.findChild(QPushButton,'logoutButton')


        # When button pressed, Open new window
        self.menuButton.clicked.connect(self.openMenuWindow)
        self.logoutButton.clicked.connect(self.openLoginWindow)

    def openMenuWindow(self):
        from menuCode import Ui_Menu
        self.close()
        self.menu_window = Ui_Menu()
        self.menu_window.show()

    def openLoginWindow(self):
        from homepageCode import Ui_HomePage
        self.close()
        self.homepage_wind = Ui_HomePage()
        self.homepage_wind.show()











