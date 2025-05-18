import sys
from PyQt6.QtWidgets import QApplication
from Views.loginForm import loginForm
from Views.application import application
from utils.tokenManager import TokenManager
from utils.helper import helper
from API_client import API_client

tm = TokenManager()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    re_token = tm.load_Stored_Refresh_Token()
    
    if re_token and helper.there_is_internet_connection() and API_client.refresh():
        window = application()
    else:
        login = loginForm()
    sys.exit(app.exec())

