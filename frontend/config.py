import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGIN_FORM_UI_FILE_PATH = os.path.join(BASE_DIR, 'UI', 'Login_SignUp_Form.ui')
MAIN_UI_FILE_PATH = os.path.join(BASE_DIR, 'UI', 'main.ui')

BASE_URL = 'http://127.0.0.1:5000'
REGISTER_ENDPOINT_URL = BASE_URL+'/register'
LOGIN_ENDPOINT_URL = BASE_URL+'/login'