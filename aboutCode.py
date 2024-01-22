from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic,QtGui,QtCore

class Ui_about(QWidget):
    def __init__(self):
        super(Ui_about, self).__init__()

        uic.loadUi("about.ui", self)

        self.setWindowTitle('About')

        self.back.clicked.connect(lambda:self.openHomePageWindow())

    def openHomePageWindow(self):
            from menuCode import Ui_Menu
            self.close()
            self.menu_window = Ui_Menu()
            self.menu_window.show()

