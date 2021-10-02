<<<<<<< HEAD
from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      

        combo = self.ui.cbSehirler

        # combo.addItem('Ankara')
        # combo.addItem('İstanbul')
        # combo.addItem('Kocaeli')
        # combo.addItems(['Adana','İzmir','Rize'])

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnClearItems.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangeIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedText)
       

    def LoadItems(self):
        sehirler = ['Adana','İzmir','Rize']
        
        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        
        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))

    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def SelectedChangeIndex(self,index):
        print(index)

    def SelectedChangedText(self,index):
        print(index)

   
app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())






=======
from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      

        combo = self.ui.cbSehirler

        # combo.addItem('Ankara')
        # combo.addItem('İstanbul')
        # combo.addItem('Kocaeli')
        # combo.addItems(['Adana','İzmir','Rize'])

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnClearItems.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangeIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedText)
       

    def LoadItems(self):
        sehirler = ['Adana','İzmir','Rize']
        
        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        
        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))

    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def SelectedChangeIndex(self,index):
        print(index)

    def SelectedChangedText(self,index):
        print(index)

   
app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())






>>>>>>> 1a46586db7801035ec8faf8e3daad10a30c9983d
