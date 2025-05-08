import os
import cv2
import numpy as np
from werkzeug.datastructures import FileStorage
from utils.LSB import LSB
from config import IMAGE_FOLDER_PATH, RESULT_IMAGE_FOLDER_PATH, SUPPORTED_IMAGE_TYPES, MESSAGE_START_FLAG

class validator:
    @staticmethod
    def supported_Type(image:FileStorage):
        return True if image.filename.split('.')[-1] in SUPPORTED_IMAGE_TYPES else False
    
    @staticmethod
    def supported_Number_Of_Channels(image:np.ndarray):
        return image.shape[2]==3
    
    @staticmethod
    def containting_message(image:np.ndarray)->bool:
        number_of_iter=len(MESSAGE_START_FLAG)*8//3+1
        extracted_binaries=''
        counter=0
        for row in image:
            for bixel in row:
                extracted_binaries+=LSB.to_bin(bixel[0])[-1]+LSB.to_bin(bixel[1])[-1]+LSB.to_bin(bixel[2])[-1]
                counter+=1
                if counter>number_of_iter:
                    break
            if counter>number_of_iter:
                break
            
        extracted_bytes=[extracted_binaries[x:x+8] for x in range(0, len(extracted_binaries),8)]
        extracted_string=''.join([chr(int(x,2)) for x in extracted_bytes])
        
        return extracted_string[:len(MESSAGE_START_FLAG)]==MESSAGE_START_FLAG
        
    
class gen_functionality:
    @staticmethod
    def remove_image(image_path:str):
        if os.path.exists(image_path):
            os.remove(image_path)
            
    @staticmethod
    def save_image(image:FileStorage):
        image_path=IMAGE_FOLDER_PATH+image.filename
        image.save(image_path)
        
    @staticmethod
    def saveMat(image:np.ndarray, filename:str):
        saved_path=RESULT_IMAGE_FOLDER_PATH+filename
        cv2.imwrite(RESULT_IMAGE_FOLDER_PATH+filename,image)
        return saved_path

    @staticmethod
    def image_to_Mat(image:FileStorage):
        gen_functionality.save_image(image)
        converted_image=cv2.imread(IMAGE_FOLDER_PATH+image.filename)
        gen_functionality.remove_image(IMAGE_FOLDER_PATH+image.filename)
        return converted_image