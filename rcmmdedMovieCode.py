from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtGui import QPixmap
import PyQt5
import random
import sys

class Ui_recommended(QWidget):
    def __init__(self):
        super(Ui_recommended, self).__init__()

        # Load the ui file
        uic.loadUi("C:\\Users\\ashmi\\OneDrive\\Documents\\GitHub\\Theatre-Management\\recommended.ui", self)

        # Defining Widgets
        self.movieSearchBox = self.findChild(QLineEdit, 'movieSearchBox')
        self.searchButton = self.findChild(QPushButton, 'searchButton')

        # Movie Labels
        self.movieLabel1 = self.findChild(QLabel, 'movieLabel1')
        self.movieLabel2 = self.findChild(QLabel, 'movieLabel2')
        self.movieLabel3 = self.findChild(QLabel, 'movieLabel3')
        self.movieLabel4 = self.findChild(QLabel, 'movieLabel4')
        self.movieLabel5 = self.findChild(QLabel, 'movieLabel5')
        self.movieLabel6 = self.findChild(QLabel, 'movieLabel6')

        # Movie Names
        self.movieName1 = self.findChild(QLabel, 'movieName1')
        self.movieName2 = self.findChild(QLabel, 'movieName2')
        self.movieName3 = self.findChild(QLabel, 'movieName3')
        self.movieName4 = self.findChild(QLabel, 'movieName4')
        self.movieName5 = self.findChild(QLabel, 'movieName5')
        self.movieName6 = self.findChild(QLabel, 'movieName6')

        self.backButton = self.findChild(QPushButton, 'backButton')
        #Adds search icon to button(If error, delete the two lines below this comment)
        self.searchButton.setIcon(QtGui.QIcon('Pictures\\srch.png'))
        self.searchButton.setIconSize(QtCore.QSize(16,16))



        # Connecting buttons and stuff
        self.searchButton.clicked.connect(lambda:self.displayMovies())
        self.backButton.clicked.connect(lambda:self.openHomePageWindow())

        # Create a QStringListModel and a QCompleter
        self.model = QStringListModel()
        # List of movie names here (Should be extracted from SQL)
        self.movieList = ['Avatar', 'Titanic', 'The Godfather', 'The Dark Knight', 'Inception']
        self.model.setStringList(self.movieList)

        # Completer stuff
        self.completer = QCompleter()
        self.completer.setModel(self.model)
        self.completer.setCaseSensitivity(PyQt5.QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(PyQt5.QtCore.Qt.MatchContains)  # Set filter mode to match substrings

        # Set the model and the completer for the movieSearchBox
        self.movieSearchBox.setCompleter(self.completer)
        # List of movies banners here (Should be extracted from SQL)
        self.imageList = {'Avatar':"C:\\Users\\ashmi\\Downloads\\projectImages\\lambos2.jpg",
                          'Titanic':'C:\\Users\\ashmi\\Downloads\\projectImages\\lambos2.jpg',
                          'The Godfather':'C:\\Users\\ashmi\\Downloads\\projectImages\\lambos2.jpg',
                          'The Dark Knight':'C:\\Users\\ashmi\\Downloads\\projectImages\\lambos2.jpg',
                          'Inception':'C:\\Users\\ashmi\\Downloads\\projectImages\\lambos2.jpg'}

    # This is the point which marks the place to undo code XD
    def displayMovies(self):
        # Extracting movie from the LineEdit
        search_text = self.movieSearchBox.text()
        matching_movies = [movie for movie in self.movieList if search_text.upper() in movie.upper()]

        for i in range(1, 7):  # Assuming you have 6 labels and buttons
            if i <= len(matching_movies):
                try:
                    pixmap = QPixmap(self.imageList[matching_movies[i-1]])
                    label = getattr(self, f"movieLabel{i}")
                    name = getattr(self, f"movieName{i}")
                    label.setPixmap(pixmap)
                    name.setText(matching_movies[i-1])
                except IndexError:
                    # Handle the case where there are less than 6 matching movies
                    print('Error1')
                    break
            else:
                try:
                    # Display random movies if no matching movies found
                    random_movie = random.choice(self.movieList)
                    print(random_movie)
                    # Error in the following line
                    pixmap = QPixmap(self.imageList[random_movie])

                    label = getattr(self, f"movieLabel{i}")
                    name = getattr(self, f"movieName{i}")
                    print(label,name)
                    label.setPixmap(pixmap)
                    name.setText(random_movie)
                except:
                    print('Error2')


    def openHomePageWindow(self):
        from menuCode import Ui_Menu
        self.close()
        self.menu_window = Ui_Menu()
        self.menu_window.show()






