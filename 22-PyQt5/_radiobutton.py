<<<<<<< HEAD
import sys
from PyQt5 import QtWidgets
from _radiobuttonform import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True) # varsayılan olarak seçili geliyor.
        self.ui.radioLise.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)


        self.ui.radioIlkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen radio: " + rb.text())

    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen radio: " + rb.text())

    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText("Seçilen Ülke: " + rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText("Seçilen Eğitim: " + rb.text())



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

=======
import sys
from PyQt5 import QtWidgets
from _radiobuttonform import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True) # varsayılan olarak seçili geliyor.
        self.ui.radioLise.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)


        self.ui.radioIlkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen radio: " + rb.text())

    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen radio: " + rb.text())

    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText("Seçilen Ülke: " + rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText("Seçilen Eğitim: " + rb.text())



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

>>>>>>> 1a46586db7801035ec8faf8e3daad10a30c9983d
app()