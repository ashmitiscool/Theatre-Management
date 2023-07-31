from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QPushButton, QLabel
from PyQt5 import uic
class Ui_seatsCode(QWidget):
    def __init__(self, mov):
        super(Ui_seatsCode, self).__init__()


        self.mov = mov

        # Load the ui file
        uic.loadUi('seats.ui',self)

        # Defining Widgets
        self.backButton = self.findChild(QPushButton,'back')
        self.proceedButton = self.findChild(QPushButton,'proceed')
        self.movieNameLabel = self.findChild(QLabel,'movieNameLabel')

        self.movieNameLabel.setText(f'Movie Name:\n{mov}')

        self.backButton.clicked.connect(self.displayMovieDesc)

    def displayMovieDesc(self):

        from movieDesc import Ui_movieDesc
        self.close()
        self.window = Ui_movieDesc(self.mov)
        self.window.show()
