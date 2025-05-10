import sys
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUiType
from PyQt6.QtCore import QUrl, QRect, Qt, QSize
from PyQt6.QtGui import QDesktopServices, QIcon, QCursor
from PyQt6 import QtCore, QtGui, QtWidgets
from img import *
import resource_rc

MainUI, _ = loadUiType('project.ui')

class Ui_MainWindow(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle("LSB")
        self.handle_buttons()
        self.UI_Chanages()
        self.openHomePage()

    def UI_Chanages(self):
        self.tabWidget.tabBar().setVisible(False)


    def handle_buttons(self):  # Corrected function name
        self.pushButton_2.clicked.connect(self.openHomePage)
        self.pushButton.clicked.connect(self.openEmbdedPage)
        self.pushButton_3.clicked.connect(self.openExtractPage)
        self.pushButton_4.clicked.connect(self.openHistoryPage)
        self.pushButton_8.clicked.connect(lambda flag: self.Browseimg(self.lineEdit_3)) 
        self.pushButton_9.clicked.connect(lambda flag: self.Browseimg(self.lineEdit_5))

    def openHomePage(self):
        self.tabWidget.setCurrentIndex(0)
        
    def openEmbdedPage(self):
        self.tabWidget.setCurrentIndex(1)

    def openExtractPage(self):
        self.tabWidget.setCurrentIndex(2)
        
    def openHistoryPage(self):
        self.tabWidget.setCurrentIndex(3)

    def Browseimg(self,value):
        fname = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        value.setText(fname[0])


def main():
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
    


if __name__ == '__main__':
    main()