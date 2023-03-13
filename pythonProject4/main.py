from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QGridLayout




class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button = QPushButton('', self)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon('team images/spurs.png'))
        self.button.setIconSize(QtCore.QSize(200,200))
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)


    def handleButton(self):
        pass

    def grid(self):
        arsenal = QPushButton("",self)
        self.button.setIcon(QtGui.QIcon('team images/arsenal.png'))
if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
