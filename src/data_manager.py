from os import listdir
from os.path import isfile, join
from img import Image
import numpy as np

class DataManager:
    def __init__(self):
        self.training_set = []
        self.test_set = []

    def __loadDBFromPath(self, folder):
        mnistImages = []
        imageCount = 0

        for digit in range(10):
            print('Loading digit: ' + digit)
            path = folder + '/d' + digit
            files = [f for f in listdir(path) if isfile(join(path, f))]
            digit_images = []

            for image in files:
                img = Image(image)
                digit_images.append(img)
                imageCount += 1

            mnistImages.append(digit_images)
            digit_images = []
        
        print('Loaded ' + imageCount + ' images.')
        return mnistImages


    def loadImages(self, folder, percentage):
        mnistImages = __loadDBFromPath(folder)

        for digit in range(len(mnistImages)):
            total = len(mnistImages[digit])
            n_training = total - (total - (total * percentage / 100))            
            digit_images = []

            for image in range(n_training): # Images for training
                digit_images.append(mnistImages[digit][image])

            self.training_set.append(digit_images)                
            digit_images = []

            for image in range(n_training, total): # Images for test
                digit_images.append(mnistImages[digit][image])
            
            self.test_set.append(digit_images)
            digit_images[]            


    def generateTags01(self, data, validDigit): #data is expected to be a 2D array
        totalData = 0
        index = 0

        for i in range(len(data)):
            totalData += len(data[i])

        for i in range(validDigit):
            index += len(data[i])
        
        tags = np.full(totalData, -1)
        for i in range(index, index+len(data[validDigit])):
            tags[i] = 1
        
        return tags

    
    def generateTags09(self, data): #data is expected to be a 2D array
        totalData = 0

        for i in range(len(data)):
            totalData += len(data[i])
                
        tags = []
        for digit in range(10):
            for image in len(data[digit]):
                tags.append(digit)

        return tags