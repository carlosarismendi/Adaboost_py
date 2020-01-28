import cv2

class Image:
    def __init__(self, path):
        self.image_data = cv2.imread(path, 0) # read image in grayscale mode