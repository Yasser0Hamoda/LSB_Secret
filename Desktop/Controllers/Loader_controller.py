import sys, os
from PyQt6.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, Qt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Views.Loader_view import Ui_Form as Loader_ui

class Loader(QDialog, Loader_ui):
    def __init__(self, parent=None):
        super(Loader, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) 
        self.setStyleSheet("background-color: rgb(77, 74, 69);\n"
                    "border-radius:30px;")
        self.__centerOffScreen()
      
        self.loader = QMovie(':/img/spinner.gif')
        self.label.setMovie(self.loader)

    def __centerOffScreen(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_center = screen_geometry.center()

        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screen_center)
        self.final_pos = frame_geometry.topLeft()

        # Move widget off-screen (bottom) to prepare for animation
        start_y = screen_geometry.height()
        self.move(self.final_pos.x(), start_y)
    
    def closeEvent(self, event):
        if self.parent():
            self.parent().setGraphicsEffect(None)  # Clean blur
        self.close()

    
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
        
    def start_the_loader(self):
        self.__animateEnter()
        self.loader.start()
        self.show()
    
    def destroy_the_loader(self):
        self.loader.stop()
        self.close()