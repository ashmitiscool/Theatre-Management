from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QPushButton
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

class Ui_Menu(QMainWindow):
    def __init__(self):
        super(Ui_Menu, self).__init__()

        # Load the ui file
        uic.loadUi('menu.ui',self)

        # Defining Widgets
        self.logoutButton = self.findChild(QPushButton, 'logoutButton')
        self.exitButton = self.findChild(QPushButton, 'quitButton')
        self.bookButton = self.findChild(QPushButton, 'bookButton')

        # When button pressed, Open new window
        self.logoutButton.clicked.connect(self.openDialogBox)
        self.exitButton.clicked.connect(self.exitProg)
        self.bookButton.clicked.connect(self.openRecmded)
        self.pushButton_2.clicked.connect(self.openProfile)
        self.about.clicked.connect(self.aboutn)

        self.setWindowTitle('Menu')

    def aboutn(self):
        from aboutCode import Ui_about
        self.close()
        self.about_win = Ui_about()
        self.about_win.show()


    def openRecmded(self):
        from rcmmdedMovieCode import Ui_recommended
        self.close()
        self.rcmnded_window = Ui_recommended()
        self.rcmnded_window.show()

    def openProfile(self):
        from profile import Ui_Profile
        self.close()
        self.profile_wind = Ui_Profile()
        self.profile_wind.show()
    #to undo point
    def openDialogBox(self):
        # Create a message box object
        msg = QMessageBox()
        # Set the text and icon of the message box
        msg.setText("Are you sure you want to log out?")
        msg.setIcon(QMessageBox.Information)
        # Add an OK button to the message box
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Show the message box and get the user response
        response = msg.exec_()
        # If the user clicked OK, open the homepage window
        if response == QMessageBox.Yes:
            self.openLoginWindow()
            self.clearInfoFile()
        else:
            pass

    def openLoginWindow(self):
        from homepageCode import Ui_HomePage
        self.close()
        self.homepage_wind = Ui_HomePage()
        self.homepage_wind.show()


    def exitProg(self):
        QApplication.quit()

    def clearInfoFile(self):
        with open('info.txt', 'w') as f:
            f.truncate(0)







