from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox, QPushButton, QLabel
from PyQt5 import uic
import smtplib

class Ui_payment(QWidget):
    def __init__(self, mov, selected_seats_list,cost,timing):
        super(Ui_payment, self).__init__()

        self.mov = mov
        self.cost = cost
        self.timing = timing
        print('Timing in paymentCode.py is',self.timing)
        print('Type of self.timing is',type(self.timing))
        print('Cost is',self.cost)
        self.selected_seats_list = selected_seats_list
        self.seatsString = ''
        for i in self.selected_seats_list:
            self.seatsString += i + ', '
        print(self.seatsString)
        self.seatsString = self.seatsString[:-2]

        uic.loadUi('payment.ui',self)
        self.setWindowTitle('Payment')

        # Declaring UI Objects
        try:
            self.cancelButton = self.findChild(QPushButton,'cancelButton')
            self.movieName = self.findChild(QLabel,'movieName')
            self.seatsLabel = self.findChild(QLabel,'seatsLabel')
            self.costLabel = self.findChild(QLabel,'costLabel')
            self.timingLabel = self.findChild(QLabel,'timing')
            self.passLineEdit = self.findChild(QLineEdit,'passwd')
            self.proceedButton = self.findChild(QPushButton,'proceedButton')

            # Mapping Buttons
            self.cancelButton.clicked.connect(self.openSeatsWindow)
            self.proceedButton.clicked.connect(self.openThankYouWindow)
        except:
            print('Error in Findchilding or Connecting Buttons: paymentCode.py')

        try:
            self.movieName.setText('Movie: ' + self.mov)
            self.seatsLabel.setText('Seats: ' + self.seatsString)
            self.costLabel.setText('You need to pay:\n' + str(self.cost))
            self.timingLabel.setText(timing)
        except:
            print('Error in setTexting: paymentCode.py')

    def openSeatsWindow(self):
        from seatsCode import Ui_seatsCode
        self.close()
        self.seats_window = Ui_seatsCode(self.mov)
        self.seats_window.show()

    def openThankYouWindow(self):
        f = open('passwd.txt','r')
        passd = f.read()
        from thankyouWindow import Ui_Thankyou
        self.close()
        self.window = Ui_Thankyou()
        self.window.show()









