import sys
from PyQt6.QtWidgets import QApplication
from Views.loginForm import loginForm
from Views.application import application
from utils.tokenManager import TokenManager

tm = TokenManager()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    re_token = None #tm.load_Stored_Refresh_Token()
    if re_token:
        window = application()
    else:
        login = loginForm()
    sys.exit(app.exec())