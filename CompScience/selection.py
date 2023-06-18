from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_selection_menu


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_selection_menu()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 911)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -10, 781, 780))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(0, 140))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.leeds = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.leeds.setMinimumSize(QtCore.QSize(0, 150))
        self.leeds.setStyleSheet("border-image: url(:/team images/leeds.png);")
        self.leeds.setText("")
        self.leeds.setObjectName("leeds")
        self.leeds.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.leeds, 1, 5, 1, 1)
        self.brighton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.brighton.setMinimumSize(QtCore.QSize(0, 150))
        self.brighton.setStyleSheet("border-image: url(:/team images/brighton.png);")
        self.brighton.clicked.connect(self.openWindow)
        self.brighton.setText("")
        self.brighton.setObjectName("brighton")
        self.gridLayout.addWidget(self.brighton, 0, 5, 1, 1)
        self.brentford = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.brentford.setMinimumSize(QtCore.QSize(0, 150))
        self.brentford.setStyleSheet("border-image: url(:/team images/brentford.png);")
        self.brentford.setText("")
        self.brentford.setObjectName("brentford")
        self.brentford.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.brentford, 0, 4, 1, 1)
        self.arsenal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arsenal.setMinimumSize(QtCore.QSize(0, 150))
        self.arsenal.setAutoFillBackground(False)
        self.arsenal.setStyleSheet("\n""border-image: url(:/team images/arsenal.png);\n""")
        self.arsenal.setText("")
        self.arsenal.setObjectName("arsenal")
        self.arsenal.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.arsenal, 0, 0, 1, 1)
        self.crystal_palace = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.crystal_palace.setMinimumSize(QtCore.QSize(0, 150))
        self.crystal_palace.setStyleSheet("border-image: url(:/team images/crystal palace.png);")
        self.crystal_palace.setText("")
        self.crystal_palace.setObjectName("crystal_palace")
        self.crystal_palace.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.crystal_palace, 1, 1, 1, 1)
        self.leicester = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.leicester.setMinimumSize(QtCore.QSize(0, 150))
        self.leicester.setStyleSheet("border-image: url(:/team images/leicester.png);")
        self.leicester.setText("")
        self.leicester.setObjectName("leicester")
        self.leicester.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.leicester, 2, 0, 1, 1)
        self.man_united = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.man_united.setMinimumSize(QtCore.QSize(0, 150))
        self.man_united.setStyleSheet("border-image: url(:/team images/man united.png);")
        self.man_united.setText("")
        self.man_united.setObjectName("man_united")
        self.man_united.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.man_united, 2, 4, 1, 1)
        self.everton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.everton.setMinimumSize(QtCore.QSize(0, 150))
        self.everton.setStyleSheet("border-image: url(:/team images/everton.png);")
        self.everton.setText("")
        self.everton.setObjectName("everton")
        self.everton.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.everton, 1, 2, 1, 1)
        self.man_city = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.man_city.setMinimumSize(QtCore.QSize(0, 150))
        self.man_city.setStyleSheet("border-image: url(:/team images/man city.png);")
        self.man_city.setText("")
        self.man_city.setObjectName("man_city")
        self.man_city.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.man_city, 2, 2, 1, 1)
        self.liverpool = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.liverpool.setMinimumSize(QtCore.QSize(0, 150))
        self.liverpool.setStyleSheet("border-image: url(:/team images/liverpool.png);")
        self.liverpool.setText("")
        self.liverpool.setObjectName("liverpool")
        self.liverpool.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.liverpool, 2, 1, 1, 1)
        self.fulham = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fulham.setMinimumSize(QtCore.QSize(0, 150))
        self.fulham.setStyleSheet("border-image: url(:/team images/fulham.png);")
        self.fulham.setText("")
        self.fulham.setObjectName("fulham")
        self.fulham.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.fulham, 1, 4, 1, 1)
        self.bournemouth = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bournemouth.setMinimumSize(QtCore.QSize(0, 150))
        self.bournemouth.setStyleSheet("border-image: url(:/team images/bournemouth.png);")
        self.bournemouth.setText("")
        self.bournemouth.setObjectName("bournemouth")
        self.bournemouth.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.bournemouth, 0, 2, 1, 1)
        self.aston_villa = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.aston_villa.setMinimumSize(QtCore.QSize(0, 150))
        self.aston_villa.setStyleSheet("border-image: url(:/team images/aston villa.png);")
        self.aston_villa.setText("")
        self.aston_villa.setObjectName("aston_villa")
        self.aston_villa.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.aston_villa, 0, 1, 1, 1)
        self.chelsea = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chelsea.setMinimumSize(QtCore.QSize(0, 150))
        self.chelsea.setStyleSheet("border-image: url(:/team images/chelsea.png);")
        self.chelsea.setText("")
        self.chelsea.setObjectName("chelsea")
        self.chelsea.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.chelsea, 1, 0, 1, 1)
        self.nottingham = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nottingham.setMinimumSize(QtCore.QSize(0, 150))
        self.nottingham.setStyleSheet("border-image: url(:/team images/nottingham.png);")
        self.nottingham.setText("")
        self.nottingham.setObjectName("nottingham")
        self.nottingham.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.nottingham, 4, 0, 1, 1)
        self.wolves = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.wolves.setMinimumSize(QtCore.QSize(0, 150))
        self.wolves.setStyleSheet("border-image: url(:/team images/wolves.png);")
        self.wolves.setText("")
        self.wolves.setObjectName("wolves")
        self.wolves.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.wolves, 4, 5, 1, 1)
        self.southampton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.southampton.setMinimumSize(QtCore.QSize(0, 150))
        self.southampton.setStyleSheet("border-image: url(:/team images/southampton.png);")
        self.southampton.setText("")
        self.southampton.setObjectName("southampton")
        self.southampton.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.southampton, 4, 1, 1, 1)
        self.newcastle = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.newcastle.setMinimumSize(QtCore.QSize(0, 150))
        self.newcastle.setStyleSheet("border-image: url(:/team images/newcastle.png);")
        self.newcastle.setText("")
        self.newcastle.setObjectName("newcastle")
        self.newcastle.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.newcastle, 2, 5, 1, 1)
        self.spurs = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.spurs.setMinimumSize(QtCore.QSize(0, 150))
        self.spurs.setStyleSheet("border-image: url(:/team images/spurs.png);")
        self.spurs.setText("")
        self.spurs.setObjectName("spurs")
        self.spurs.clicked.connect(self.openWindow)
        self.gridLayout.addWidget(self.spurs, 4, 2, 1, 1)
        self.west_ham = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.west_ham.setMinimumSize(QtCore.QSize(0, 150))
        self.west_ham.setStyleSheet("border-image: url(:/team images/west ham.png);")
        self.west_ham.setText("")
        self.west_ham.setObjectName("west_ham")
        self.gridLayout.addWidget(self.west_ham, 4, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
