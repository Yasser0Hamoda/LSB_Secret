from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUiType
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import LOGIN_FORM_UI_FILE_PATH
from Views.popUP import CustomPopup
import resources.resource_rc as resource_rc


loginform,_ = loadUiType(LOGIN_FORM_UI_FILE_PATH)

class loginForm(QWidget, loginform):
    def __init__(self, parent=None):
        super(loginForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.__centerOnScreen()
        self.pushButton_15.clicked.connect(self.__pop)
        
    def __pop(self):
        cus = CustomPopup('hell Yeh!!', parent=self, icon_type='success')
        cus.exec()
        
    def __centerOnScreen(self):
        secreanGeomery = QApplication.primaryScreen().availableGeometry()
        screenCenter = secreanGeomery.center()
        
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screenCenter)
        self.move(frame_geometry.topLeft())
