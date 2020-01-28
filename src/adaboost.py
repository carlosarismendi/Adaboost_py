import constant
import classifier_weak
import random

class Adaboost:
    def __init__(self, t_classifiers, a_attempts):
        self.T_CLASSIFIERS = t_classifiers
        self.A_ATTEMPTS = a_attempts


    def generate_random_classif(self, dimension):
        pixel = random.randrange(0, constant.PIXEL, 1)
        edge = random.randrange(0, constant.EDGE+1, 1)
        direction = constant.LEFT if random.randrange(0,2,1) == 0 else constant.RIGHT
        classifier = ClassifierWeak(pixel, edge, direction, dimension)

        return classifier

    
    def applyClassifier(self, classifier, data): #data is expected to be a 1D array
        if classifier.direction == constant.LEFT:
            for image in range(len(data)):
                color = data[image].image_data[classifier.pixel]
                classifier.classificaton[image] = 1 if color <= classificaton.edge else -1
        
        else:
            for image in range(len(data)):
                color = data[image].image_data[classifier.pixel]
                classifier.classificaton[image] = 1 if color > classificaton.edge else -1

        return classifier.classificaton
