from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import mysql.connector as mys
conn = mys.connect(host = 'localhost', user = 'root', passwd = 'ashmitiscool', database='cinemax')
cursor = conn.cursor()
class Ui_movieDesc(QWidget):
    def __init__(self, mov):
        super(Ui_movieDesc, self).__init__()


        self.mov = mov
        print('movie name is ',mov)

        # Load the ui file
        uic.loadUi('movie desc.ui',self)
        try:
            cursor.execute('select * from movies where MovieName="{}"'.format(mov)) # Order of data: (0)MovieName, (1)Image Path, (2)MovieDesc,
                                                                                    # (3)MovieDate
        except:
            print('Error in Getting Movie Details')
        self.movieData = cursor.fetchone()
        print('Movie Data is ',self.movieData)

        # Defining Widgets
        self.backButton = self.findChild(QPushButton, 'backButton')
        self.bookNowButton = self.findChild(QPushButton, 'bookNowButton')
        self.movieName = self.findChild(QLabel, 'movieName')
        self.movieDescLabel = self.findChild(QLabel, 'movieDescLabel')
        self.DateLabel = self.findChild(QLabel, 'DateLabel')
        self.movieBannerImage = self.findChild(QLabel, 'movieBannerImage')


        self.backButton.clicked.connect(self.openRecmded)
        self.bookNowButton.clicked.connect(self.openSeatsWindow)

        try:
            self.movieName.setText(self.movieData[0])

            image_path = self.movieData[1]
            pixmap = QPixmap(image_path)
            self.movieBannerImage.setPixmap(pixmap)
            # Date Label
            try:
                self.DateLabel.setText("{}".format(self.movieData[3]))
            except:
                print('Error in setting Date Label')

            self.movieDescLabel.setText(self.movieData[2])
        except:
            print('Error in putting the data in the labels')


        # self.movieDescDict = {'The Dark Knight':"Set within a year after the events of Batman Begins (2005), Batman, Lieutenant James Gordon, and new District Attorney Harvey Dent successfully begin to round up the criminals that plague Gotham City, until a mysterious and sadistic criminal mastermind known only as \"The Joker\" appears in Gotham, creating a new wave of chaos. Batman's struggle against The Joker becomes deeply personal, forcing him to \"confront everything he believes\" and improve his technology to stop him. A love triangle develops between Bruce Wayne, Dent, and Rachel Dawes.",
        #                       'Titanic':'Titanica',
        #                       'The Godfather':'Father of all Gods'}
        #
        #
        #
        # if mov in self.movieDescDict:
        #     self.movieDescLabel.setText(self.movieDescDict[mov])


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


