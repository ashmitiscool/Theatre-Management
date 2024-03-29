from PyQt5.QtWidgets import QLineEdit, QWidget, QMessageBox,QDateEdit, QComboBox, QPushButton, QLabel, QCheckBox
from PyQt5 import uic
from homepageCode import *

cmd = "create table if not exists booked(User varchar(500) unique, seats varchar(1000), movie varchar(500), snacks varchar(500), price int);"
cursor.execute(cmd)
conn.commit()

class Ui_seatsCode(QWidget):
    def __init__(self, mov):
        super(Ui_seatsCode, self).__init__()


        self.mov = mov

        # Load the ui file
        uic.loadUi('seats.ui',self)
        self.setWindowTitle('Booking')

        # Defining Widgets
        self.selected_seats_list = []
        self.selected_food_list = []

        self.seat_checkboxes = []
        for row in range(8):
            for col in range(10):
                seat_label = chr(ord('A') + row) + str(col + 1)
                checkbox = self.findChild(QCheckBox, seat_label)
                self.seat_checkboxes.append(checkbox)
        
        #check if occupied:
        self.checkOcc()
        
        # FindChilding
        self.backButton = self.findChild(QPushButton,'back')
        self.proceedButton = self.findChild(QPushButton,'proceed')
        self.movieNameLabel = self.findChild(QLabel,'movieNameLabel')
        self.popcorn_checkbox = self.findChild(QCheckBox,'popcorn')
        self.pretzels_checkbox = self.findChild(QCheckBox,'pretzel')
        self.nachos_checkbox = self.findChild(QCheckBox,'nachos')
        self.chocolate_checkbox = self.findChild(QCheckBox,'choco')
        self.timing = self.findChild(QComboBox,'timing')
        self.date = self.findChild(QDateEdit,'date')

        self.movieNameLabel.setText('Movie Name:\n{}'.format(mov))

        # Connecting Buttons
        self.backButton.clicked.connect(self.displayMovieDesc)
        self.proceedButton.clicked.connect(self.proceed_button_clicked)

    def checkOcc(self):
        pass
##        cmd = 'select * from booked;'
##        cursor.execute(cmd)
##        x = cursor.fetchall()
##        seatChecked = []
##        for entry in x:
##            if entry[2] == self.mov:
##                data = entry[1]
##                data = data.split('.')
##                seatChecked.extend(data)
##        for checkbox in seatChecked:
##            checkbox.setDisabled(True)

        
    def proceed_button_clicked(self):
        self.selected_seats_list = []

        for checkbox in self.seat_checkboxes:
            if checkbox.isChecked():
                seat_label = checkbox.objectName()
                self.selected_seats_list.append(seat_label)

        # Print the selected seats (you can modify this part to store the list in a file or database)
        print("Selected seats:", self.selected_seats_list)
        seat_costs = {'A1': 250, 'A2': 250, 'A3': 250, 'A4': 250, 'A5': 250,
    'A6': 250, 'A7': 250, 'A8': 250, 'A9': 250, 'A10': 250,
    'B1': 200, 'B2': 200, 'B3': 200, 'B4': 200, 'B5': 200,
    'B6': 200, 'B7': 200, 'B8': 200, 'B9': 200, 'B10': 200,
    'C1': 150, 'C2': 150, 'C3': 150, 'C4': 150, 'C5': 150,
    'C6': 150, 'C7': 150, 'C8': 150, 'C9': 150, 'C10': 150,
    'D1': 150, 'D2': 150, 'D3': 150, 'D4': 150, 'D5': 150,
    'D6': 150, 'D7': 150, 'D8': 150, 'D9': 150, 'D10': 150,
    'E1': 150, 'E2': 150, 'E3': 150, 'E4': 150, 'E5': 150,
    'E6': 150, 'E7': 150, 'E8': 150, 'E9': 150, 'E10': 150,
    'F1': 100, 'F2': 100, 'F3': 100, 'F4': 100, 'F5': 100,
    'F6': 100, 'F7': 100, 'F8': 100, 'F9': 100, 'F10': 100,
    'G1': 100, 'G2': 100, 'G3': 100, 'G4': 100, 'G5': 100,
    'G6': 100, 'G7': 100, 'G8': 100, 'G9': 100, 'G10': 100,
    'H1': 100, 'H2': 100, 'H3': 100, 'H4': 100, 'H5': 100,
    'H6': 100, 'H7': 100, 'H8': 100, 'H9': 100, 'H10': 100}



        self.total_cost = 0
        for seat in self.selected_seats_list:
            self.total_cost += seat_costs[seat]

        if self.popcorn_checkbox.isChecked():
            self.selected_food_list.append("Popcorn")
            self.total_cost += 100

        if self.pretzels_checkbox.isChecked():
            self.selected_food_list.append("Pretzels")
            self.total_cost += 130

        if self.nachos_checkbox.isChecked():
            self.selected_food_list.append("Nachos")
            self.total_cost += 100

        if self.chocolate_checkbox.isChecked():
            self.selected_food_list.append("Chocolate")
            self.total_cost += 75

        if self.total_cost==0 or self.selected_seats_list==[]:
            self.error.setText('Select a seat!')
            self.error.setVisible(True)
        else:
            current_user = ''
            with open('info.txt','r') as x:
                data = x.read()
                data = data.split('!!!!!')
                current_user = data[0]
            seats = ''
            snacks = ''
            for item in self.selected_seats_list:
                seats+=item
                seats+='.'
            for item in self.selected_food_list:
                snacks+=item
                snacks+='.'
            seats = seats[:-1]
            print(seats)
            print(current_user)
            try:
                cmd = "insert into booked values('{}','{}','{}','{}','{}');".format(current_user,seats,self.mov,snacks,self.total_cost)
                print(cmd)
                cursor.execute(cmd)
                conn.commit()
                from paymentCode import Ui_payment
                self.close()
                self.timendate = self.timing.currentText()+' '+self.date.date().toString("dd-MM-yyyy")
                print(self.timendate)
                self.window = Ui_payment(self.mov, self.selected_seats_list, self.total_cost,self.timendate)
                self.window.show()
            except:
                self.error.setText('You already booked once, try cancelling your booking..')
            

    def displayMovieDesc(self):

        from movieDesc import Ui_movieDesc
        self.close()
        self.window = Ui_movieDesc(self.mov)
        self.window.show()
