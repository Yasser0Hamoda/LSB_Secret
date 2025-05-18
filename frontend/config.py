import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGIN_FORM_UI_FILE_PATH = os.path.join(BASE_DIR, 'UI', 'Login_SignUp_Form.ui')
MAIN_UI_FILE_PATH = os.path.join(BASE_DIR, 'UI', 'main.ui')
IMAGE_VIEWR_UI_FILE_PATH = os.path.join(BASE_DIR, 'UI', 'image_viewr.ui')
MESSAGE_VIEWR_UI_FILE_PATH = os.path.join(BASE_DIR, 'UI', 'message_viewer.ui')

BASE_URL = 'http://127.0.0.1:5000'
REGISTER_ENDPOINT_URL = BASE_URL+'/register'
LOGIN_ENDPOINT_URL = BASE_URL+'/login'
REFRESH_ENDPOINT_URL = BASE_URL + '/refresh'
EMBED_ENDPOINT_URL = BASE_URL + '/embed'
EXTRACT_ENDPOINT_URL = BASE_URL + '/extract'
SAVE_MESSAGE_ENDPOINT_URL = BASE_URL + '/save_message'
GET_ALL_MESSAGES_ENDPOINT_URL = BASE_URL + '/get_all_messages'