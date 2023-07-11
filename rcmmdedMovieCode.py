from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtGui import QPixmap
import PyQt5
import sys

class Ui_recommended(QWidget):
    def __init__(self):
        super(Ui_recommended, self).__init__()

        # Load the ui file
        uic.loadUi("C:\\Users\\ashmi\\OneDrive\\Documents\\GitHub\\Theatre-Management\\recommended.ui", self)

        # Defining Widgets
        self.movieSearchBox = self.findChild(QLineEdit, 'movieSearchBox')
        self.searchButton = self.findChild(QPushButton, 'searchButton')
        self.movieLabel1 = self.findChild(QLabel, 'movieLabel1')
        self.movieName1 = self.findChild(QLabel, 'movieName1')
        #Adds search icon to button(If error, delete the two lines below this comment)
        self.pushButton.setIcon(QtGui.QIcon('Pictures\\srch.png'))
        self.pushButton.setIconSize(QtCore.QSize(16,16))



        # Connecting buttons and stuff
        self.searchButton.clicked.connect(lambda:self.displayMovies())

        # Create a QStringListModel and a QCompleter
        self.model = QStringListModel()
        # List of movies here (Should be extracted from SQL)
        self.movieList = ['Avatar', 'Titanic', 'The Godfather', 'The Dark Knight', 'Inception']
        self.model.setStringList(self.movieList)

        self.completer = QCompleter()
        self.completer.setModel(self.model)
        self.completer.setCaseSensitivity(PyQt5.QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(PyQt5.QtCore.Qt.MatchContains)  # Set filter mode to match substrings


        # Set the model and the completer for the movieSearchBox
        self.movieSearchBox.setCompleter(self.completer)

        self.imageList = {'Avatar':"C:\\Users\\ashmi\\Downloads\\projectImages\\lambos2.jpg"}

    def displayMovies(self):
        # Extracting movie from the LineEdit
        mov = self.movieSearchBox.text()
        if mov in self.movieList:
            pixmap = QPixmap(self.imageList[mov])
            self.movieLabel1.setPixmap(pixmap)
            self.movieName1.setText(mov)






