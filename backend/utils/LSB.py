import cv2
import numpy as np
from config import MESSAGE_START_FLAG, MESSAGE_END_FLAG, MESSAGE_SEP

class LSB:
    #! Helper function to convert data to its binary form
    @staticmethod
    def __to_bin(data):
        if isinstance(data, str):
            return ''.join([ format(ord(i), "08b") for i in data ])
        if isinstance(data, bytes):
            return ''.join([ format(i, "08b") for i in data ])
        if isinstance(data, np.ndarray):
            return [ format(i, "08b") for i in data ]
        if isinstance(data, int) or isinstance(data, np.uint8):
            return format(data, "08b")
        return None
    
    @staticmethod
    def embeddedMessage(message:str=None, image:str=None, hashedPassword:str=None):
        if not isinstance(message, str) and isinstance(hashedPassword, str):
            message=str(message)
            hashedPassword=str(hashedPassword)
        image=cv2.imread(image)
        #! Adding the hashed password and end indecator, just to know where to end decoding
        message = MESSAGE_START_FLAG+message+MESSAGE_SEP+hashedPassword+MESSAGE_END_FLAG
        #! Number Of Maximum Bytes That The Image Can Hold
        n_bytes = image.shape[0]*image.shape[1]*3//8 
        #! Check wether the image will hold the message or not
        if len(message)>n_bytes:
            return {'error':'The message is to long to be encoded in the image'}
        #! COnverting the message to its binary form in ordr to embeded it inside the image
        message=LSB.__to_bin(message)
        msg_len=len(message)
        
        data_index=0
        for row in image:
            for bixel in row:
                r, g, b = LSB.__to_bin(bixel)
                
                if data_index<msg_len:
                    bixel[0] = int(r[:-1]+message[data_index],2)
                    data_index+=1
                if data_index<msg_len:
                    bixel[1] = int(g[:-1]+message[data_index] ,2)
                    data_index+=1
                if data_index<msg_len:
                    bixel[2] = int(b[:-1]+message[data_index],2)
                    data_index+=1
                    
                if data_index >= msg_len:
                    break
                
        return image
    
    @staticmethod
    def extractMessage(image:str):
        image=cv2.imread(image)
        binaryData=''
        for row in image:
            for bixel in row:
                bixel=LSB.__to_bin(bixel)
                r=bixel[0][-1]
                g=bixel[1][-1]
                b=bixel[2][-1]
                binaryData+=r+g+b
        messageBytes = [binaryData[i:i+8] for i in range(0, len(binaryData),8)]
        decoded_data = ""
        for byte in messageBytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-len(MESSAGE_END_FLAG):] == MESSAGE_END_FLAG:
                break
        decoded_data = decoded_data[:-len(MESSAGE_END_FLAG)]
        sep_index=decoded_data.find(MESSAGE_SEP)
        if sep_index==-1:
            return {'error':'The Image Does not contain any messages!'}
        originalmessage = decoded_data[len(MESSAGE_START_FLAG):sep_index]
        hashedPassword=decoded_data[sep_index+len(MESSAGE_SEP):]
        return {
            'message':originalmessage,
            'password':hashedPassword
                }

