from PyQt6.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect
from PyQt6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, pyqtSignal
import os, sys
import clipboard

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controllers.popUP_controller import CustomPopup
from API_client import API_client
from Views.message_viewer_view import Ui_Form as message_viewr



class messageViewr(QDialog, message_viewr):
    message_signal = pyqtSignal(str)
    def __init__(self, message:str, parent=None):
        super().__init__(parent)
        self.message=message
        self.setupUi(self)
        self.messageInput.setText(self.message)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setModal(True)
        self.resize(0, 0)
        self.__handleButtons()
        self.__animatePopup()

    def __handleButtons(self):
        self.saveButton.clicked.connect(self.__save)
        self.copyButton.clicked.connect(self.__copy_to_clipboard)

    def __save(self):
        message = self.messageInput.toPlainText().strip()
        
        if not message:
            CustomPopup('There Is No Message To Save!', parent=self)
            return
        
        response = API_client.save_message(message)
        
        if response.get('status') == 'fail':
            CustomPopup(response.get('reason'), parent=self)
            return
        
        self.message_signal.emit(message)
        CustomPopup(response.get('reason'), icon_type='success',parent=self)

    def __copy_to_clipboard(self):
        try:
            clipboard.copy(self.message)
            CustomPopup('Message Coped Successfully', icon_type='success', parent=self)
        except:
            CustomPopup('Unable To Copy The Message!', parent=self)

    def __animatePopup(self):
        screen = QApplication.primaryScreen().availableGeometry()
        target_width, target_height = self.maximumWidth(), self.maximumHeight()
        center_x = screen.center().x() - target_width // 2
        center_y = screen.center().y() - target_height // 2
        self.final_geometry = QRect(center_x, center_y, target_width, target_height)

        if self.parent():
            self.parent_blur = QGraphicsBlurEffect()
            self.parent_blur.setBlurRadius(8)
            self.parent().setGraphicsEffect(self.parent_blur)

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(400)
        self.anim.setStartValue(QRect(screen.center().x(), screen.center().y(), 0, 0))
        self.anim.setEndValue(self.final_geometry)
        self.anim.setEasingCurve(QEasingCurve.Type.OutBack)
        self.anim.start()

    def closeEvent(self, event):
        if self.parent():
            self.parent().setGraphicsEffect(None)  # Clean blur
        self.close()
