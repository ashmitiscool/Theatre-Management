from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QPushButton, QLabel
from PyQt5 import uic
class Ui_movieDesc(QWidget):
    def __init__(self, mov):
        super(Ui_movieDesc, self).__init__()


        self.mov = mov

        # Load the ui file
        uic.loadUi('movie desc.ui',self)

        # Defining Widgets
        self.backButton = self.findChild(QPushButton, 'backButton')
        self.bookNowButton = self.findChild(QPushButton, 'bookNowButton')
        self.movieName = self.findChild(QLabel, 'movieName')
        self.movieDescLabel = self.findChild(QLabel, 'movieDescLabel')

        self.backButton.clicked.connect(self.openRecmded)
        self.bookNowButton.clicked.connect(self.openSeatsWindow)

        self.movieName.setText(mov)

        self.movieDescDict = {'The Dark Knight':"Set within a year after the events of Batman Begins (2005), Batman, Lieutenant James Gordon, and new District Attorney Harvey Dent successfully begin to round up the criminals that plague Gotham City, until a mysterious and sadistic criminal mastermind known only as \"The Joker\" appears in Gotham, creating a new wave of chaos. Batman's struggle against The Joker becomes deeply personal, forcing him to \"confront everything he believes\" and improve his technology to stop him. A love triangle develops between Bruce Wayne, Dent, and Rachel Dawes.",
                              'Titanic':'Titanica',
                              'The Godfather':'Father of all Gods'}



        if mov in self.movieDescDict:
            self.movieDescLabel.setText(self.movieDescDict[mov])


    def openRecmded(self):
        from rcmmdedMovieCode import Ui_recommended
        self.close()
        self.rcmnded_window = Ui_recommended()
        self.rcmnded_window.show()

    def openSeatsWindow(self):
        from seatsCode import Ui_seatsCode
        self.close()
        self.seats_window = Ui_seatsCode(self.mov)
        self.seats_window.show()


