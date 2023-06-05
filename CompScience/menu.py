
from PyQt5 import QtCore, QtGui, QtWidgets
import teamimages
import json
class Ui_selection_menu(object):
    def setupUi(self, selection_menu):
        selection_menu.setObjectName("selection_menu")
        selection_menu.resize(800, 599)
        self.centralwidget = QtWidgets.QWidget(selection_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, 40, 321, 531))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 380, 221, 131))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 250, 221, 131))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 120, 221, 131))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.pushButton.setObjectName("pushButton")
        selection_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(selection_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        selection_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(selection_menu)
        self.statusbar.setObjectName("statusbar")
        selection_menu.setStatusBar(self.statusbar)

        self.retranslateUi(selection_menu)
        QtCore.QMetaObject.connectSlotsByName(selection_menu)

    def retranslateUi(self, selection_menu):
        _translate = QtCore.QCoreApplication.translate
        selection_menu.setWindowTitle(_translate("selection_menu", "MainWindow"))
        self.pushButton_2.setText(_translate("selection_menu", "NextMatch"))
        self.pushButton_3.setText(_translate("selection_menu", "PassMap"))
        self.pushButton_4.setText(_translate("selection_menu", "ShotMap"))
        self.pushButton.setText(_translate("selection_menu", "<---------"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selection_menu = QtWidgets.QMainWindow()
    ui = Ui_selection_menu()
    ui.setupUi(selection_menu)
    selection_menu.show()
    sys.exit(app.exec_())
