import os

MESSAGE_START_FLAG='<-MSG_START->'
MESSAGE_END_FLAG='<-MSG_END->'
MESSAGE_SEP='<-MSG_SEP->'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_FOLDER_PATH = os.path.join(BASE_DIR,'app', 'static', 'images')+'\\'
RESULT_IMAGE_FOLDER_PATH = os.path.join(BASE_DIR,'app', 'static', 'outputImages')+'\\'
ENV_FILE_PATH=os.path.join(BASE_DIR, '.env')
DB_FILE_PATH=os.path.join(BASE_DIR, 'stegano_app.db')
SCHEMA_FILE_PATH=os.path.join(BASE_DIR, 'app', 'db', 'schema.sql')

SUPPORTED_IMAGE_TYPES=['bmp', 'png']