import sys
from PyQt5 import uic, QtWidgets, QtBaseClass

Ui_MainWindow, QtBaseClass = uic.loadUiType('l8.ui')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.startMainWindow()
    
    def startMainWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.().clicked.connect()


def main():
    app = QtWidgets.QApplication(sys.argv)

if __name__ == '__main__':
    main()
    window - MainWindow()
    window.show()
    sys.exit(app.exec_())