from PyQt6.QtWidgets import QDialog, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt, QPropertyAnimation, QTimer, QRectF
from PyQt6.QtGui import QPixmap, QPainter, QPainterPath, QBrush, QColor

class CustomPopup(QDialog):
    def __init__(self, message:str, icon_type:str = "error", parent=None):
        super().__init__(parent)

        self.setWindowTitle("Custom Popup")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        layout = QHBoxLayout()
        
        label = QLabel(message)
        label2 = QLabel()
        if icon_type == "error":
            label2.setPixmap(QPixmap("frontend/resources/icons/error-4-24.ico"))
        else: label2.setPixmap(QPixmap("frontend/resources/icons/ok-24.ico"))
        layout.addWidget(label2)
        layout.addWidget(label)
        
        self.setLayout(layout)
        self.adjustSize()
        if parent:
            parent_rect = parent.frameGeometry()
            popup_rect = self.frameGeometry()
            center_point = parent_rect.center()
            popup_rect.moveCenter(center_point)
            self.move(popup_rect.topLeft())

        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.finished.connect(self.close)
        
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.__startClosingAnimation)
        self.timer.start(1000)  # Close after 3 seconds
                
    def __startClosingAnimation(self):
        self.animation.setDirection(QPropertyAnimation.Direction.Backward)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        
        rect = QRectF(self.rect())
        path = QPainterPath()
        path.addRoundedRect(rect, 30, 30)
        
        painter.fillPath(path, QBrush(QColor("#F6F5F5")))