from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtGui import QPixmap
import PyQt5
import random
import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',passwd='ashmitiscool',auth_plugin='mysql_native_password',database='cinemax')
mycursor = mycon.cursor()

import sys
class Ui_recommended(QWidget):
    def __init__(self):
        super(Ui_recommended, self).__init__()

        # Load the ui file
        uic.loadUi("recommended.ui", self)

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

        # Movie Buttons
        self.movieButton1 = self.findChild(QPushButton, 'movieButton1')
        self.movieButton2 = self.findChild(QPushButton, 'movieButton2')
        self.movieButton3 = self.findChild(QPushButton, 'movieButton3')
        self.movieButton4 = self.findChild(QPushButton, 'movieButton4')
        self.movieButton5 = self.findChild(QPushButton, 'movieButton5')
        self.movieButton6 = self.findChild(QPushButton, 'movieButton6')

        self.backButton = self.findChild(QPushButton, 'backButton')
        #Adds search icon to button(If error, delete the two lines below this comment)
        self.searchButton.setIcon(QtGui.QIcon('Pictures\\srch.png'))
        self.searchButton.setIconSize(QtCore.QSize(16,16))



        # Connecting buttons and stuff
        self.movieButton1.clicked.connect(lambda:self.displayMovieDesc())
        self.movieButton2.clicked.connect(lambda:self.displayMovieDesc())
        self.movieButton3.clicked.connect(lambda:self.displayMovieDesc())
        self.movieButton4.clicked.connect(lambda:self.displayMovieDesc())
        self.movieButton5.clicked.connect(lambda:self.displayMovieDesc())
        self.movieButton6.clicked.connect(lambda:self.displayMovieDesc())
        self.searchButton.clicked.connect(lambda:self.displayMovies())
        self.backButton.clicked.connect(lambda:self.openHomePageWindow())

        # Create a QStringListModel and a QCompleter
        self.model = QStringListModel()
        # List of movie names here (Should be extracted from SQL)
        # Undo point
        query = "SELECT MovieName FROM movies"
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.movieList = [row[0] for row in result]
        #self.movieList = ['Avatar', 'Titanic', 'The Godfather', 'The Dark Knight', 'Inception', 'Shrek', 'Spiderman']
        self.model.setStringList(self.movieList)

        # Completer stuff
        self.completer = QCompleter()
        self.completer.setModel(self.model)
        self.completer.setCaseSensitivity(PyQt5.QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(PyQt5.QtCore.Qt.MatchContains)  # Set filter mode to match substrings

        # Set the model and the completer for the movieSearchBox
        self.movieSearchBox.setCompleter(self.completer)
        # List of movies banners here (Should be extracted from SQL)
        # Undo point

        query = "SELECT MovieName, MovieImage FROM movies"
        mycursor.execute(query)
        result = mycursor.fetchall()

        self.imageList = {row[0]: row[1] for row in result}
        # self.imageList = {'Avatar':'Pictures\\avatar.jpg',
        #                   'Titanic':'Pictures\\titanic.jpg',
        #                   'The Godfather':'Pictures\\samp.jpg',
        #                   'The Dark Knight':'Pictures\\dark_knight.jpg',
        #                   'Inception':'Pictures\\inception.jpg',
        #                   'Shrek':'Pictures\\shrek.jpg',
        #                   'Spiderman':'Pictures\\samp.jpg'}

    # This is the point which marks the place to undo code XD
    def displayMovies(self):
        # Extracting movie from the LineEdit
        search_text = self.movieSearchBox.text()
        matching_movies = [movie for movie in self.movieList if search_text.upper() in movie.upper()]
        displayed_movies = []
        for i in range(1, 7):  # Assuming you have 6 labels and buttons
            movieLabel = "movieLabel"+str(i)#Set compatibility
            movieName = "movieName"+str(i)#Set compatibility
            if i <= len(matching_movies):
                try:
                    pixmap = QPixmap(self.imageList[matching_movies[i-1]])
                    label = getattr(self, movieLabel)
                    name = getattr(self, movieName)
                    label.setPixmap(pixmap)
                    name.setText(matching_movies[i-1])
                    displayed_movies.append(matching_movies[i-1])
                    print(displayed_movies)
                except IndexError:
                    # Handle the case where there are less than 6 matching movies
                    print('Error1')
                    break
            else:
                try:
                    # Display random movies if no matching movies found
                    possible_movies = [movie for movie in self.movieList if movie not in displayed_movies]
                    random_movie = random.choice(possible_movies)
                    displayed_movies.append(random_movie)
                    #random_movie = random.choice(self.movieList)
                    # Error can be in the following line
                    pixmap = QPixmap(self.imageList[random_movie])
                    label = getattr(self, movieLabel)
                    name = getattr(self, movieName)
                    label.setPixmap(pixmap)
                    name.setText(random_movie)
                except:
                    print('Error2')


    def displayMovieDesc(self):
        mov = self.movieName1.text()
        print(mov)
        if mov != '':
            from movieDesc import Ui_movieDesc
            self.close()
            self.window = Ui_movieDesc(mov)
            self.window.show()

    def openHomePageWindow(self):
        from menuCode import Ui_Menu
        self.close()
        self.menu_window = Ui_Menu()
        self.menu_window.show()






