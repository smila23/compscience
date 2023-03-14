from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QGridLayout




class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button = QPushButton('', self)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon('team images/spurs.png'))
        self.button.setIconSize(QtCore.QSize(480,270))
        self.setFixedWidth(1920)
        self.setFixedHeight(1080)


    def handleButton(self):
        pass

    def grid(self):
        arsenal = QPushButton("",self)
        self.button.setIcon(QtGui.QIcon('team images/arsenal.png'))

        brighton = QPushButton("", self)
        self.button.setIcon(QtGui.QIcon('team images/brighton.png'))

        grid_layout = QGridLayout

        grid_layout.addWidget(brighton, 0, 0)
        grid_layout.addWidget(arsenal, 0, 1)

        layout_widget = QWidget()
        layout_widget.setLayout(grid_layout)
if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
