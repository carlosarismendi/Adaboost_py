from os import listdir
from os.path import isfile, join
from image import Image
import numpy as np

class DataManager:
    def __init__(self):
        self.training_set = np.empty(10, Image)
        self.test_set = np.empty(10, Image)

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
        size_data = len(data)
        for digit in range(size_data):
            total = len(data[digit])
            n_training = total - (total - (total * percentage / 100))            
            n_training = int(n_training)
            digit_images = np.empty(n_training, Image)

            for image in range(n_training): # Images for training
                digit_images[image] = data[digit][image]

            self.training_set[digit] = digit_images
            digit_images = np.empty(total - n_training, Image)

            for image in range(n_training, total): # Images for test
                digit_images[image - n_training] = data[digit][image]
            
            self.test_set[digit] = (digit_images)


    def generate_tags_01(self, data, validDigit): #data is expected to be a 2D array
        totalData = 0
        index = 0
        size_data_valid = len(data[validDigit])

        for i in data:
            totalData += len(i)

        for i in range(validDigit):
            index += len(data[i])
        
        tags = np.empty(totalData)
        for i in range(index):
            tags[i] = -1

        for i in range(index, index+size_data_valid):
            tags[i] = 1
        
        for i in range(index+size_data_valid, totalData):
            tags[i] = -1

        return tags

    
    def generate_tags_09(self, data): #data is expected to be a 2D array
        totalData = 0
        for i in data:
            totalData += len(i)
                
        tags = np.empty(totalData)
        index = 0
        for digit in range(10):
            for image in data[digit]:
                tags[index] = digit
                index += 1

        return tags

    
    def flatten(self, array_2D):        
        size_array_2D = len(array_2D)
        total = 0
        for i in array_2D:
            total += len(i)

        array_1D = np.empty(total, Image)        
        index = 0
        for i in array_2D:
            for img in i:
                array_1D[index] = img
                index += 1

        return array_1D
