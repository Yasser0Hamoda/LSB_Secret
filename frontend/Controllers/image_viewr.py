from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog, QGraphicsBlurEffect
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QByteArray
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Views.image_viewr_view import Ui_Form as image_viewr
import resources.resource_rc as resource_rc
from Controllers.popUP import CustomPopup


class imageViewr(QDialog, image_viewr):
    def __init__(self, image_file, parent=None):
        super(imageViewr, self).__init__(parent)
        self.image_file = image_file
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setModal(True)
        self.saveButton.clicked.connect(self.__save)
        self.__centerOffScreen()
        self.__animateEnter()
        self.__setImageOnLabel()
        self.exec()
        
    def __setImageOnLabel(self):
        try:
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(self.image_file.content))
            self.imageLabel.setPixmap(pixmap)
        except:
            self.imageLabel.setText('Faild To Load The Image')

    def __centerOffScreen(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_center = screen_geometry.center()

        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screen_center)
        self.final_pos = frame_geometry.topLeft()

        # Move widget off-screen (bottom) to prepare for animation
        start_y = screen_geometry.height()
        self.move(self.final_pos.x(), start_y)

    def __animateEnter(self):
        if self.parent():
            self.parent_blur = QGraphicsBlurEffect()
            self.parent_blur.setBlurRadius(8)
            self.parent().setGraphicsEffect(self.parent_blur)
            
        self.enter_animation = QPropertyAnimation(self, b"pos", self)
        self.enter_animation.setDuration(500)
        self.enter_animation.setStartValue(QPoint(self.final_pos.x(), QApplication.primaryScreen().availableGeometry().height()))
        self.enter_animation.setEndValue(self.final_pos)
        self.enter_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.enter_animation.start()

    def closeEvent(self, event):
        if self.parent():
            self.parent().setGraphicsEffect(None)  # Clean blur
        self.close()

    def __save(self):
        try:
            saveLocation = QFileDialog.getExistingDirectory(parent=self, caption='Select place to save the image')
            content_disposition = self.image_file.headers.get('Content-Disposition', '')
            filename = None

            if 'filename=' in content_disposition:
                filename = content_disposition.split('filename=')[1].strip('";')
                
            with open(os.path.join(saveLocation,filename if filename else 'embed.bmp'),'wb') as f:
                f.write(self.image_file.content)
            CustomPopup('Image Saved Successfully', icon_type='success', parent=self,)
            return
        except:
            CustomPopup('Unable To Save The Image!', parent=self)
