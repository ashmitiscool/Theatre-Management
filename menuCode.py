from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class Ui_Menu(QMainWindow):
    def __init__(self):
        super(Ui_Menu, self).__init__()

        # Load the ui file
        uic.loadUi('menu.ui',self)

        # Defining Widgets
        #self.submitButton = self.findChild(QPushButton, 'submit')

        # When button pressed, Open new window
        #self.submitButton.clicked.connect(self.openMenuWindow)





    # def openMenuWindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_Menu()
    #     self.ui.setupUi(self.window)
    #     self.window.show()




app = QApplication(sys.argv)
UIWindow = Ui_Menu()
UIWindow.show()
app.exec_()
