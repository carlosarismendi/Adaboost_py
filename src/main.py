from adaboost import Adaboost
from data_manager import DataManager
from classifier_weak import ClassifierWeak
import numpy as np

adb = Adaboost(10, 10)
dm = DataManager()
percentage = 60

def count_correct_predictions(predictions, tags):
    hits = 0
    size_tags = len(tags)    
    for i in range(size_tags):
        hits += 1 if predictions[i] == tags[i] else 0
    
    return hits


def print_results(prediction_training, prediction_test, training_tags, test_tags):
    size_training = len(training_tags)
    size_test = len(test_tags)
    training_hits = count_correct_predictions(prediction_training, training_tags)
    test_hits = count_correct_predictions(prediction_test, test_tags)

    training_hits_percentage = training_hits * 100 / size_training
    test_hits_percentage = test_hits * 100 / size_test

    print('\nNumber of weak classifiers per strong: ' + str(adb.T_CLASSIFIERS))
    print('Number of attempts to obtain a good weak classifier: ' + str(adb.A_ATTEMPTS))
    print('Total images: ' + str((len(prediction_training) + len(prediction_test))))
    print('Training images: ' + str(len(prediction_training)))
    print('Test images: ' + str(len(prediction_test)))
    print('Hits for training images: ' + str(training_hits) + " of " + str(size_training) + " | Percentage hits: " + str(training_hits_percentage))
    print('Hits for test images: ' + str(test_hits) + " of " + str(size_test) + " | Percentage hits: " + str(test_hits_percentage))
    print('\n')


def generate_classifiers(data): #data is expected to be 1D array
    classifiers = []
    print('')
    for digit in range(10):
        print('Classifier for digit: ' + str(digit))
        training_tags = dm.generate_tags_01(dm.training_set, digit)
        classifier = adb.adaboost(data, training_tags)
        classifiers.append(classifier)

    return classifiers


def manyImages(folder):
    data = dm.load_db_from_path(folder)
    dm.split_data(data, percentage)

    training_img = dm.flatten(dm.training_set)
    test_img = dm.flatten(dm.test_set)
    training_tags = dm.generate_tags_09(dm.training_set)
    test_tags = dm.generate_tags_09(dm.test_set)

    classifiers = generate_classifiers(training_img)
    prediction_training = adb.apply_strong_classifiers(training_img, classifiers)
    prediction_test = adb.apply_strong_classifiers(test_img, classifiers)

    print_results(prediction_training, prediction_test, training_tags, test_tags)

if __name__ == "__main__":
    manyImages("mnist_1000")