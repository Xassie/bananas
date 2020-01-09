import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from thehotel.hotel import *

HELP, QtBaseClass = uic.loadUiType('vis_interface\\help.ui')
Ui_MainWindow, QtBaseClass = uic.loadUiType('vis_interface\\l8.ui')
Ui_RegWindow, QtBaseClass = uic.loadUiType('vis_interface\\RegScreen.ui')
Ui_LogWindow, QtBaseClass = uic.loadUiType('vis_interface\\LogScreen.ui')
Ui_InfoWindow, QtBaseClass = uic.loadUiType('vis_interface\\RoomerInfo.ui')
Ui_NotRoomerWindow, QtBaseClass = uic.loadUiType('vis_interface\\notRoomer.ui')
Ui_RoomRentWindow, QtBaseClass = uic.loadUiType('vis_interface\\RoomRent.ui')


class Help(QtWidgets.QMainWindow, HELP):
    def __init__(self, parent=None):
        super(Help, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.hotel = Hotel()
        self.user = None
        self.roomed = None
        self.startMainWindow()

    def startHelp(self):
        win = Help(self)
        win.show()

    def startMainWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.register_2.clicked.connect(self.startRegWindow)
        self.ui.Login.clicked.connect(self.logInit)
        self.ui.actionHelp.triggered.connect(self.startHelp)

    def startRegWindow(self):
        self.ui = Ui_RegWindow()
        self.ui.setupUi(self)
        self.ui.Back.clicked.connect(self.startMainWindow)
        self.ui.ConfirmRegs.clicked.connect(self.regInit)
        self.ui.actionHelp.triggered.connect(self.startHelp)

    def hasNumbers(self, inputString):
        return any(char.isdigit() for char in inputString)

    def regInit(self):
        info = [
            len(self.hotel.clientbase)+1,
            self.ui.RegName.text(),
            self.ui.RegSurname.text(),
            self.ui.RegLastname.text(),
            self.ui.RegID.text(),
            self.ui.RegComment.toPlainText(),
        ]
        fine = 1
        for i in info:
            if not i:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Please")
                msg.setInformativeText('Fill everything in.')
                msg.setWindowTitle("Error")
                msg.exec_()
                fine = 0
                break

        for i in info[1:4]:
            if self.hasNumbers(i):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Do you really")
                msg.setInformativeText('Have nums in name? No.')
                msg.setWindowTitle("Error")
                msg.exec_()
                fine = 0
                break

        if fine:
            self.hotel.clientbase.append(Client(*info))
            self.hotel.clients_append(self.hotel.clientbase[-1].wfriendly())
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Done!")
            msg.setInformativeText('You\'ve been registered.')
            msg.setWindowTitle("Gratz!")
            msg.exec_()
            self.startMainWindow()

    def logInit(self):
        self.user = None
        self.roomed = None
        self.ui = Ui_LogWindow()
        self.ui.setupUi(self)
        ids = ''
        for i in self.hotel.clientbase:
            ids += str(i) + '\n'
        self.ui.users.setText(ids)
        font = QtGui.QFont('Narkisim', 10, QtGui.QFont.Bold)
        self.ui.users.setFont(font)

        self.ui.Back.clicked.connect(self.startMainWindow)
        self.ui.Login.clicked.connect(self.logging)
        self.ui.actionHelp.triggered.connect(self.startHelp)

    def logging(self):
        try:
            num = int(self.ui.lineEdit.text())
            for cl in self.hotel.clientbase:
                if int(cl.id) == num:
                    self.user = cl
                    self.check()
            if not self.user:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("No such id")
                msg.setInformativeText('Enter another one.')
                msg.setWindowTitle("Error")
                msg.exec_()

        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Please")
                msg.setInformativeText('Enter valid ID.')
                msg.setWindowTitle("Error")
                msg.exec_()

    def check(self):
        roomer = None
        self.hotel.check_roomers()
        for p in self.hotel.roomers:
            if self.user.id == p.clientInfo.id:
                roomer = True
                self.roomed = p
                self.startInfoWindow()
        if not roomer:
            self.startnotRoomerWindow()

    def startnotRoomerWindow(self):
        self.ui = Ui_NotRoomerWindow()
        self.ui.setupUi(self)
        self.ui.Back.clicked.connect(self.logInit)
        self.ui.actionHelp.triggered.connect(self.startHelp)
        self.ui.RentRoom.clicked.connect(self.startRoomRentWindow)

    def startRoomRentWindow(self):
        self.ui = Ui_RoomRentWindow()
        self.ui.setupUi(self)
        self.ui.Back.clicked.connect(self.check)
        self.ui.actionHelp.triggered.connect(self.startHelp)
        self.ui.Rent.clicked.connect(self.rooming)
        text = ''
        for i in self.hotel.rooms:
            text += str(i) + '\n'
        self.ui.Rooms.setText(text)
        font = QtGui.QFont('Narkisim', 9, QtGui.QFont.Bold)
        self.ui.Rooms.setFont(font)

    def rooming(self):
        try:
            num = int(self.ui.Number.text())
            dur = int(self.ui.duration.text())
            if dur >= 0:
                if dur <= 1000000:
                    found = False
                    for r in self.hotel.rooms:
                        if r.number == num:
                            found = True
                            if not r.busy:
                                self.hotel.movein(self.user, r, dur)
                                msg = QtWidgets.QMessageBox()
                                msg.setIcon(QtWidgets.QMessageBox.Question)
                                msg.setText("Success!")
                                msg.setInformativeText('Welcome to our hotel!')
                                msg.setWindowTitle('Done')
                                msg.exec_()
                                self.check()
                            else:
                                msg = QtWidgets.QMessageBox()
                                msg.setIcon(QtWidgets.QMessageBox.Warning)
                                msg.setText('Room is busy')
                                msg.setInformativeText('Pick another one.')
                                msg.setWindowTitle("Whoopsy..")
                                msg.exec_()
                    if not found:
                            msg = QtWidgets.QMessageBox()
                            msg.setIcon(QtWidgets.QMessageBox.Critical)
                            msg.setText("No such room")
                            msg.setInformativeText('Try harder.')
                            msg.setWindowTitle("Error")
                            msg.exec_()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("Hey!")
                    msg.setInformativeText('You are living long, bruh?\n'
                                           'Go away with that.')
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Hey!")
                msg.setInformativeText('You can\'t go back in time\nCan you?')
                msg.setWindowTitle("Error")
                msg.exec_()

        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Invalid input")
            msg.setInformativeText('Give me integers.')
            msg.setWindowTitle("Error")
            msg.exec_()

    def startInfoWindow(self):
        self.ui = Ui_InfoWindow()
        self.ui.setupUi(self)
        self.ui.Back.clicked.connect(self.logInit)
        self.ui.actionHelp.triggered.connect(self.startHelp)
        self.ui.RoomersDesk.setText(self.roomed.info())
        self.ui.Leave.clicked.connect(self.byebye)
        self.ui.Expand.clicked.connect(self.expandit)
        font = QtGui.QFont('Narkisim', 14, QtGui.QFont.Bold)
        self.ui.RoomersDesk.setFont(font)

    def expandit(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Expansion', 'So.. How many days?')
        if ok:
            try:
                text = int(text)
                if text > 0:
                    if text <= 1000000:
                        self.hotel.expansion(self.roomed, text)
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Question)
                        msg.setText('Success!')
                        msg.setInformativeText('Hope you\'ll enjoy your time.')
                        msg.setWindowTitle("All done!")
                        msg.exec_()
                        self.check()
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setText("Hey!")
                        msg.setInformativeText('You are living long, huh?\n Go away with that.')
                        msg.setWindowTitle("Error")
                        msg.exec_()

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("Hey!")
                    msg.setInformativeText('You can\'t go back in time\nCan you?')
                    msg.setWindowTitle("Error")
                    msg.exec_()

            except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('Incomplete')
                msg.setInformativeText('Enter days as an int')
                msg.setWindowTitle("Ouchie.")
                msg.exec_()

    def byebye(self):
        self.hotel.kickout(self.roomed, self.user.id)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText('Was nice knowing you.')
        msg.setInformativeText('Come back again.')
        msg.setWindowTitle("Goodbye.")
        msg.exec_()
        self.startMainWindow()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
