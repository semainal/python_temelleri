import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)

        # # layout = QtWidgets.QVBoxLayout() # Boxlar alt alta sıralanır. 
        # layout = QtWidgets.QHBoxLayout() # Boxlar yan yana sıralanır.

        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("blue"))
        # layout.addWidget(Color("yellow"))


# hem vertical, hem horizontal
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color("red"))
        hlayout1.addWidget(Color("blue"))
        hlayout1.addWidget(Color("green"))
        hlayout1.setContentsMargins(50,0,0,0) # soldan 50px lik boşluk bıraktık.
        hlayout1.setSpacing(50) # kutucuklar arasında 50pxlik boşluk oluşur.

        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color("purple"))
        hlayout2.addWidget(Color("yellow"))
        hlayout2.setSpacing(20)

        
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        

        # layout = QtWidgets.QGridLayout()
        # layout.addWidget(Color("red"),0,0) # ilk 0 aşağı doğru, ikinci 0 sağa doğru
        # layout.addWidget(Color("blue"),1,0)
        # layout.addWidget(Color("green"),0,2)
        # layout.addWidget(Color("yellow"),3,1)
        
        
        widget = QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()
