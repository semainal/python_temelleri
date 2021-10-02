<<<<<<< HEAD
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()


    win.setWindowTitle("First Application")
    win.setGeometry(200,200,500,500) # 200 ekranın konumu, 500 pencere büyüklüğü
    win.setWindowIcon(QIcon("ucak-icon2.png"))
    win.setToolTip("My ToolTip")


    win.show()
    sys.exit(app.exec_())


=======
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()


    win.setWindowTitle("First Application")
    win.setGeometry(200,200,500,500) # 200 ekranın konumu, 500 pencere büyüklüğü
    win.setWindowIcon(QIcon("ucak-icon2.png"))
    win.setToolTip("My ToolTip")


    win.show()
    sys.exit(app.exec_())


>>>>>>> 1a46586db7801035ec8faf8e3daad10a30c9983d
window()