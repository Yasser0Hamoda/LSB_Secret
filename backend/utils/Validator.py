import numpy as np
from config import MESSAGE_START_FLAG

class validator:
    
    @staticmethod
    def isImage(image):
        return isinstance(image, np.ndarray)
    
    
        