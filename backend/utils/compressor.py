import zlib
import base64

class compressor:
    @staticmethod
    def compress(message:str):
        try:
            compressed = zlib.compress(message.encode('utf-8'))
            return base64.b64encode(compressed).decode('utf-8')
        except:
            return None  
        
    @staticmethod
    def decompress(eccoded_message:str):
        try:
            compressed = base64.b64decode(eccoded_message.encode('utf-8'))
            return zlib.decompress(compressed).decode('utf-8')
        except:  
            return None

        