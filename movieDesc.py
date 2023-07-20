from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox
from PyQt5 import uic
class Ui_movieDesc(QWidget):
    def __init__(self, mov):
        super(Ui_movieDesc, self).__init__()




        # Load the ui file
        uic.loadUi('movie desc.ui',self)

        # Defining Widgets
        #self.submitButton = self.findChild(QPushButton, 'signupSubmit')



    def openRecmded(self):
        from rcmmdedMovieCode import Ui_recommended
        self.close()
        self.rcmnded_window = Ui_recommended()
        self.rcmnded_window.show()


