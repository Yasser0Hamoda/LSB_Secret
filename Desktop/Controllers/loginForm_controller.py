from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controllers.popUP_controller import CustomPopup
from Controllers.application_controller import application
import resources.resources_rc as resource_rc
from API_client import API_client
from Views.Login_SignUp_Form_view import Ui_Form as loginform


class loginForm(QWidget, loginform):
    def __init__(self, parent=None):
        super(loginForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.__centerOnScreen()
        self.__handelButtons()
        self.__handelLineEdits()

    
    def __login(self):
        user_name = self.userNameLoginInput.text().strip()
        password = self.passwordLoginInput.text().strip()
        
        if not(user_name and password):
            CustomPopup('Empty Required Feilds!', parent=self)
            return
        
        res = API_client.login(user_name, password, self.rememberMe.isChecked())
        
        if res.get('status') == 'fail':
            CustomPopup(str(res.get('reason')), parent=self)
            return
        app = application(self)
        self.close()
            
    def __signUp(self):
        user_name = self.userNameSignUpInput.text().strip()
        password = self.passwordSignUpInput.text().strip()
        pass_confirm = self.confirmPasswordSignUpInput.text().strip()
        
        if not (user_name and password and pass_confirm):
            CustomPopup('Empty Required Feilds!', parent=self)
            return 
        
        if password != pass_confirm:
            CustomPopup('password and password Confirmation do not match!', parent=self)
            return 
               
        res = API_client.signUp(user_name, password, pass_confirm)
        
        if res.get('status') == 'success':
            CustomPopup(res.get('message'), parent=self, icon_type='success')
        else:
            CustomPopup(res.get('reason'), parent=self)
            
    def __centerOnScreen(self):
        secreanGeomery = QApplication.primaryScreen().availableGeometry()
        screenCenter = secreanGeomery.center()
        
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screenCenter)
        self.move(frame_geometry.topLeft())
    
    def __handelLineEdits(self):
        regex = QRegularExpression(r"^[a-zA-Z0-9!@#$%^&*()_\-+=\[{\]};:'\",.<>?/\\|~`]*$")
        validator = QRegularExpressionValidator(regex)
        self.userNameLoginInput.setValidator(validator)
        self.passwordLoginInput.setValidator(validator)
        self.userNameSignUpInput.setValidator(validator)
        self.passwordSignUpInput.setValidator(validator)
        self.confirmPasswordSignUpInput.setValidator(validator)

    def __handelButtons(self):
        self.loginSwitchButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.signupSwitchButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.signUpButton.clicked.connect(self.__signUp)
        self.loginButton.clicked.connect(self.__login)
        self.showPassword.pressed.connect(lambda: self.passwordLoginInput.setEchoMode(QLineEdit.EchoMode.Normal))
        self.showPassword.released.connect(lambda: self.passwordLoginInput.setEchoMode(QLineEdit.EchoMode.Password))
        self.showPassword_2.pressed.connect(lambda: self.passwordSignUpInput.setEchoMode(QLineEdit.EchoMode.Normal))
        self.showPassword_2.released.connect(lambda: self.passwordSignUpInput.setEchoMode(QLineEdit.EchoMode.Password))
        self.showPassword_3.pressed.connect(lambda: self.confirmPasswordSignUpInput.setEchoMode(QLineEdit.EchoMode.Normal))
        self.showPassword_3.released.connect(lambda: self.confirmPasswordSignUpInput.setEchoMode(QLineEdit.EchoMode.Password))
