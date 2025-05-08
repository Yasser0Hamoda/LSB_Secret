import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
from utils.LSB import LSB
from config import IMAGE_FOLDER_PATH, RESULT_IMAGE_FOLDER_PATH
    
if __name__=='__main__':
    image=IMAGE_FOLDER_PATH+'sample-bmp-files-sample_1280x853.bmp'
    emb_image = LSB.embeddedMessage(message='Mession Done!!', image=image, hashedPassword='This is the password')
    cv2.imwrite(RESULT_IMAGE_FOLDER_PATH+'result_image_2.bmp', emb_image)
    print(LSB.extractMessage(image=RESULT_IMAGE_FOLDER_PATH+'result_image_2.bmp'))
