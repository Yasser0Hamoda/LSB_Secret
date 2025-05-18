from PyQt6.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUiType
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import MAIN_UI_FILE_PATH
import resources.resource_rc as resource_rc
from Views.image_viewr import imageViewr
from Views.message_viewr import messageViewr
from Views.popUP import CustomPopup
from API_client import API_client

MainUI, _ = loadUiType(MAIN_UI_FILE_PATH)

class application(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(application, self).__init__(parent)
        self.setupUi(self)
        self.messages = self.__get_all_messages()
        self.stackedWidget.setCurrentIndex(0)
        if self.scrollAreaWidgetContents_3.layout() is None:
            layout = QVBoxLayout(self.scrollAreaWidgetContents_3)
            self.scrollAreaWidgetContents_3.setLayout(layout)
        self.stackedWidget.currentChanged.connect(self.__populate_messages_if_possible)
        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle("LSB")
        self.__handle_buttons()
        self.showMaximized()

    def __handle_buttons(self):
        self.pushButton_2.setChecked(True)
        self.pushButton_2.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.pushButton_3.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
        self.pushButton_4.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(3))
        self.uploadImageButton.clicked.connect(lambda : self.__Browseimg(self.extractImageInput)) 
        self.selectImageButton.clicked.connect(lambda : self.__Browseimg(self.imagePathInput))
        self.showPassword.pressed.connect(lambda: self.extractImagePasswordInput.setEchoMode(QLineEdit.EchoMode.Normal))
        self.showPassword.released.connect(lambda: self.extractImagePasswordInput.setEchoMode(QLineEdit.EchoMode.Password))
        self.showPassword_2.pressed.connect(lambda: self.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal))
        self.showPassword_2.released.connect(lambda: self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password))
        self.embedButton.clicked.connect(self.__embedImage)
        self.extractButton.clicked.connect(self.__extractMessage)

    def __embedImage(self):
        self.embedButton.setEnabled(False)
        message = self.messageInput.toPlainText().strip()
        image_path = self.imagePathInput.text().strip()
        password = self.passwordInput.text().strip()
        
        if not (message and image_path and password):
            CustomPopup('Empty Requierd Fields!', parent=self)
            self.embedButton.setEnabled(True)
            return
        
        response = API_client.embed(message, password, image_path)
        
        if response.get('status') == 'fail':
            CustomPopup(response.get('reason'), parent=self)
            self.embedButton.setEnabled(True)
            return
        
        if response.get('status') == 'success':
            imageViewr(response.get('image'), self)
        self.embedButton.setEnabled(True)

    def __extractMessage(self):
        self.extractButton.setEnabled(False)
        image_path = self.extractImageInput.text().strip()
        password = self.extractImagePasswordInput.text().strip()
        
        if not (image_path and password):
            CustomPopup('Empty Requierd Fields!', parent=self)
            self.extractButton.setEnabled(True)
            return
        
        response = API_client.extract(image_path,password)
        
        if response.get('status')=='fail':
            CustomPopup(response.get('reason'), parent=self)
            self.extractButton.setEnabled(True)
            return
        
        msgView = messageViewr(response.get('message'),parent=self)
        msgView.message_signal.connect(lambda msg: self.messages.append(msg))
        msgView.exec()
        self.extractButton.setEnabled(True)

    def __get_all_messages(self):
        response = API_client.get_all_messages()
        
        if response.get('status') == 'success':
            return response.get('messages')
        
        return []
    
    def __populate_messages_if_possible(self):
        if self.stackedWidget.currentIndex() != 3 or not self.messages:
            return
        
        if self.scrollAreaWidgetContents_3.layout() is None:
            layout = QVBoxLayout(self.scrollAreaWidgetContents_3)
            self.scrollAreaWidgetContents_3.setLayout(layout)
        elif self.scrollAreaWidgetContents_3.layout().count != 0:
            self.__delete_layout_widgets(self.scrollAreaWidgetContents_3.layout())
        
        for message in self.messages:
            self.__add_message_to_scrollArea(message)
    
    def __delete_layout_widgets(self, layout:QVBoxLayout):
        if layout is None:
            return

        while layout.count():
            item = layout.takeAt(0)

            # If it's a widget, delete it
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()
                continue

            # If it's a layout, recurse
            child_layout = item.layout()
            if child_layout is not None:
                self.__delete_layout_widgets(child_layout)
                child_layout.deleteLater()
                continue
      
    def __add_message_to_scrollArea(self, message:str):
        label = QLabel(message)
        label.setStyleSheet('''
                            width: 387;
                            height: 49;
                            top: 390px;
                            left: 333px;
                            font-family: Kdam Thmor Pro;
                            font-weight: 400;
                            font-size: 32px;
                            line-height: 100%;
                            letter-spacing: 2px;
                            text-align: center;
                            color: rgba(255, 255, 255, 0.8);

                            ''')
        self.scrollAreaWidgetContents_3.layout().addWidget(label)
    
    def __Browseimg(self,value):
        fname = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.bmp)")
        value.setText(fname[0])
