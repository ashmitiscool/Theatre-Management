from PyQt5.QtWidgets import QLineEdit,QMainWindow, QApplication, QLabel, QPushButton, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
class Ui_starting():
    def __init__(self):
        super(Ui_starting, self).__init__()




        from homepageCode import Ui_HomePage

        self.menu_window = Ui_HomePage()
        self.menu_window.show()



app = QApplication(sys.argv)
UIWindow = Ui_starting()
app.exec_()
