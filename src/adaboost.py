import constant
import random
import numpy as np
from image import Image
from classifier_weak import ClassifierWeak
from math import log2, exp

class Adaboost:
    def __init__(self, t_classifiers, a_attempts):
        self.T_CLASSIFIERS = t_classifiers
        self.A_ATTEMPTS = a_attempts


    def generate_random_classif(self, dimension):
        pixel = random.randrange(0, constant.PIXELS, 1)
        edge = random.randrange(0, constant.MAX_EDGE + 1, 1)
        direction = constant.LEFT if random.randrange(0,2,1) == 0 else constant.RIGHT
        classifier = ClassifierWeak(pixel, edge, direction)

        return classifier

    
    def apply_classifier(self, classifier, data): #data is expected to be a 1D array
        classifier.classification = np.empty(len(data))

        if classifier.direction == constant.LEFT:
            for image in range(len(data)):
                color = data[image].image_data[classifier.pixel]
                classifier.classificaton[image] = 1 if color <= classificaton.edge else -1
        
        else:
            for image in range(len(data)):
                color = data[image].image_data[classifier.pixel]
                classifier.classificaton[image] = 1 if color > classificaton.edge else -1

        return classifier.classificaton


    def calculate_error(self, classifier, tags, D):

        error = 0.0
        for i in range(len(tags)):
            e = 0 if classifier.classificaton[i] == tags[i] else 1
            error += D[i] * e

        return error

    
    def calculate_confidence(self, error):
        confidence = math.log2((1.0 - error) / error) / 2
        return confidence

    
    def update_D(self, classifier, tags, D):
        Z = 0.0
        for i in range(len(tags)):
            D[i] = D[i] * math.exp(-classifier.confidence * tags[i] * classifier.classificaton[i])
            Z += D[i]
        
        for i in range(len(tags)):
            D[i] = D[i] / Z

        return D


    def adaboost(self, data, tags):
        N = len(data)
        D = np.full(N, 1/N)

        classifiers = np.empty(self.T_CLASSIFIERS, ClassifierWeak)

        for t in range(self.T_CLASSIFIERS):
            classifier_1 = self.generate_random_classif(N)
            print(type(classifier_1))
            classifier_1.classificaton = self.apply_classifier(classifier_1, data)
            classifier_1.error = self.calculate_error(classifier_1, tags, D)

            for a in range(self.A_ATTEMPTS):
                classifier_2 = self.generate_random_classif(N)
                if classifier_2 in classifiers:
                    a -= 1
                    continue

                classifier_2.classificaton = self.apply_classifier(classifier_2, data)
                classifier_2.error = self.calculate_error(classifier_2, tags, D)

                if(classifier_2.error < classifier_1.error):
                    classifier_1 = classifier_2

            classifier_1.confidence = self.calculate_confidence(classifier_1.error)            
            self.update_D(classifier_1, tags, D)
            classifiers[t] = classifier_1
        
        return classifiers


    def _apply_strong_classif(self, image_, classifier):
        data = [image]
        for c in classifier:
            c.classificaton = self.apply_classifier(c, data)

        prediction = 0.0
        for c in classifier:
            prediction += c.confidence * c.classificaton[0]

        return prediction

    
    def apply_strong_classifiers(self, data, classifiers):
        results = np.empty(len(data))
        for image in len(data):
            digit = 0
            maxPrediction = -999999.0

            for c in len(classifiers):
                prediction = self._apply_strong_classif(data[image], classifiers[c])
                if prediction > maxPrediction:
                    maxPrediction = prediction
                    digit = c

            results[image] = digit