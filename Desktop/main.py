import sys
from PyQt6.QtWidgets import QApplication
from Controllers.loginForm_controller import loginForm
from Controllers.application_controller import application
from utils.tokenManager import TokenManager
from utils.helper import helper
from API_client import API_client

tm = TokenManager()
  
def main():
    app = QApplication(sys.argv)
    re_token = tm.load_Stored_Refresh_Token()
    
    login = loginForm()
    
    if re_token and helper.there_is_internet_connection() and API_client.refresh():
        window = application(login)
    else:
        login.show()
    sys.exit(app.exec())