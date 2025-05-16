from PyQt6.QtWidgets import QMainWindow, QFileDialog, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUiType
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import MAIN_UI_FILE_PATH
import resources.resource_rc as resource_rc

MainUI, _ = loadUiType(MAIN_UI_FILE_PATH)


class application(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(application, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle("LSB")
        self.handle_buttons()
        self.openHomePage()
        self.showMaximized()


    def handle_buttons(self):  # Corrected function name
        self.pushButton_2.clicked.connect(self.openHomePage)
        self.pushButton_2.setChecked(True)
        self.pushButton.clicked.connect(self.openEmbdedPage)
        self.pushButton_3.clicked.connect(self.openExtractPage)
        self.pushButton_4.clicked.connect(self.openHistoryPage)
        self.pushButton_11.clicked.connect(lambda : self.Browseimg(self.lineEdit_7)) 
        self.pushButton_9.clicked.connect(lambda : self.Browseimg(self.lineEdit_5))
        self.showPassword.pressed.connect(lambda: self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal))
        self.showPassword.released.connect(lambda: self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password))
        self.showPassword_2.pressed.connect(lambda: self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Normal))
        self.showPassword_2.released.connect(lambda: self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Password))

    def openHomePage(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def openEmbdedPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def openExtractPage(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def openHistoryPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def Browseimg(self,value):
        fname = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        value.setText(fname[0])
