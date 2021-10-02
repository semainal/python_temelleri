<<<<<<< HEAD
import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitapOkumak.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnHobiler1SecilenleriAl.clicked.connect(self.getAllHobiler)
        self.ui.btnHobiler2SecilenleriAl.clicked.connect(self.getAllHobiler2)

    def getAllHobiler(self):
        result = ''
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultHobiler.setText(result)

    def getAllHobiler2(self):
        result = ''
        items = self.ui.groupHobiler_2.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultHobiler2.setText(result)
               
            

    def show_state(self,value):
        cb = self.sender()

        print(value)
        print(cb.text())
        print(cb.isChecked())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

=======
import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitapOkumak.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnHobiler1SecilenleriAl.clicked.connect(self.getAllHobiler)
        self.ui.btnHobiler2SecilenleriAl.clicked.connect(self.getAllHobiler2)

    def getAllHobiler(self):
        result = ''
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultHobiler.setText(result)

    def getAllHobiler2(self):
        result = ''
        items = self.ui.groupHobiler_2.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultHobiler2.setText(result)
               
            

    def show_state(self,value):
        cb = self.sender()

        print(value)
        print(cb.text())
        print(cb.isChecked())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

>>>>>>> 1a46586db7801035ec8faf8e3daad10a30c9983d
app()