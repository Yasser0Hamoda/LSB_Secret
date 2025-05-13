import sys
from PyQt6.QtWidgets import QApplication
from Views.loginForm import loginForm
from Views.application import application

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = application()
    window.show()
    sys.exit(app.exec())