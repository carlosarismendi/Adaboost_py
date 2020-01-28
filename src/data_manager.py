from os import listdir
from os.path import isfile, join
from image import Image
import numpy as np

class DataManager:
    def __init__(self):
        self.training_set = []
        self.test_set = []

    def load_db_from_path(self, folder):
        mnistImages = []
        imageCount = 0

        for digit in range(10):
            print('Loading digit: ' + str(digit))
            path = folder + '/d' + str(digit) + '/'
            files = [f for f in listdir(path) if isfile(join(path, f))]            
            digit_images = []

            for image in files:
                img = Image(path+image)                
                img.image_data = Image.flatten(img.image_data)
                digit_images.append(img)
                imageCount += 1

            mnistImages.append(digit_images)
            digit_images = []
        
        print('Loaded ' + str(imageCount) + ' images.')
        return mnistImages


    def split_data(self, data, percentage):
        for digit in range(len(data)):
            total = len(data[digit])
            n_training = total - (total - (total * percentage / 100))            
            n_training = int(n_training)
            digit_images = []

            for image in range(n_training): # Images for training
                digit_images.append(data[digit][image])

            self.training_set.append(digit_images)
            digit_images = []

            for image in range(n_training, total): # Images for test
                digit_images.append(data[digit][image])
            
            self.test_set.append(digit_images)


    def generate_tags_01(self, data, validDigit): #data is expected to be a 2D array
        totalData = 0
        index = 0

        for i in range(len(data)):
            totalData += len(data[i])

        for i in range(validDigit):
            index += len(data[i])
        
        tags = np.empty(totalData)
        for i in range(index):
            tags[i] = -1

        for i in range(index, index+len(data[validDigit])):
            tags[i] = 1
        
        for i in range(index+len(data[validDigit]), totalData):
            tags[i] = -1

        return tags

    
    def generate_tags_09(self, data): #data is expected to be a 2D array
        totalData = 0

        for i in range(len(data)):
            totalData += len(data[i])
                
        tags = []
        for digit in range(10):
            for image in range(len(data[digit])):
                tags.append(digit)

        return tags

    
    def flatten(self, array_2D):        
        array_1D = []
        for i in range(len(array_2D)):
            for img in array_2D[i]:
                array_1D.append(img)

        return array_1D
