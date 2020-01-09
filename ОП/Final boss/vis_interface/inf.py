import sys
from PyQt5 import uic, QtWidgets
from thehotel.hotel import *

Ui_MainWindow, QtBaseClass = uic.loadUiType('l8.ui')
Ui_RegWindow, QtBaseClass = uic.loadUiType('RegScreen.ui')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.startMainWindow()
    
    def startMainWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.register_2.clicked.connect(self.startRegWindow)

    def startRegWindow(self):
        self.ui = Ui_RegWindow()
        self.ui.setupUi(self)
        self.ui.Back.clicked.connect(self.startMainWindow)
        self.ui.ConfirmRegs.clicked.connect(self.regInit)

    def regInit(self):
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()