from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter
import PyQt5
import sys

class Ui_recommended(QWidget):
    def __init__(self):
        super(Ui_recommended, self).__init__()

        # Load the ui file
        uic.loadUi("C:\\Users\\ashmi\\OneDrive\\Documents\\GitHub\\Theatre-Management\\recommended.ui", self)

        # Defining Widgets
        self.movieSearchBox = self.findChild(QLineEdit, 'movieSearchBox')

        # Create a QStringListModel and a QCompleter
        self.model = QStringListModel()
        self.model.setStringList(['Avatar', 'Titanic', 'The Godfather', 'The Dark Knight', 'Inception'])

        self.completer = QCompleter()
        self.completer.setModel(self.model)
        self.completer.setCaseSensitivity(PyQt5.QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(PyQt5.QtCore.Qt.MatchContains)  # Set filter mode to match substrings


        # Set the model and the completer for the movieSearchBox
        # Error may be here
        self.movieSearchBox.setCompleter(self.completer)

        # Add some data to the model, either from a list or from a database query
        # For example, using a list of movie names


        # When button pressed, Open new window
        # self.logoutButton.clicked.connect(self.openDialogBox)


