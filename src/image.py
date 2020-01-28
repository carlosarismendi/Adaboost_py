import constant
import cv2
import numpy as np

class Image:
    def __init__(self, path):
        self.image_data = cv2.imread(path, 0) # read image in grayscale mode

            
    @classmethod        
    def flatten(self, data):
        img = []
        rows, columns = data.shape       
        for r in range(rows):
            for c in range(columns):
                img.append(data[r, c])
        
        return img
