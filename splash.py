import sys
from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen
#IMport undo place here
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
import time

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen,self).__init__()
        uic.loadUi('splash.ui',self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())   
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        
    def forward(self):
        for i in range(0,100):
                time.sleep(0.1)
                self.progressBar.setValue(i)
                
class Ui_starting():
    def __init__(self):
        super(Ui_starting, self).__init__()

        from homepageCode import Ui_HomePage

        self.menu_window = Ui_HomePage()
        self.menu_window.show()
               
if __name__ == '__main__':
    app = QApplication(sys.argv)
     
    splash = SplashScreen()
    splash.show()
    splash.forward()
    UIWindow = Ui_starting()
    splash.hide()
    splash.finish(self,UIWindow)
    app.exec_()
