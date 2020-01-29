# Adaboost for digit recognizing
This is a basic implementation of the well-known Adaboost algorithm in Python. 
For this solution, 1000 images with 28x28 pixels have been used (MNIST data subset).
Each weak classifier only check 1 pixel/image and determines if the light intensity of that
pixel is "less or equal" or greater than a given edge and then classifies the input image as
1 o -1, being 1 the digit that the classifier must recognize as "ok" and -1 the others. This way,
a strong classifier is composed by T weak classifiers and recognize a unique digit (e.g. 7).
Therefore, in case it is necessary to recognize all digits from 0 to 9, ten strong classifiers must
be generated.

- adaboost.py: implements the class Adaboost, which generates, trains and applys both weak and strong classifiers
given T(number of weak classifiers in a strong one) and A(number of attempts to get a "good" weak classifier).
- classifier_weak: implements the class ClassifierWeak, previously explained its working.
- constant.py: contains global constants that the different classes use.
- data_manager: this class has methods to generate tags both for training(-1, 1) and testing(0, 9). It also implements
method for reading images from a given folder and split data in two groups given a percentage, so that percentage represents
the amount of images used for training and the rest for testing purposes.
- image.py: reads a image in grayscale given a path using OpenCV.
- main.py: code to generate ten strong classifiers (one per digit), apply those classifiers to obtain the results and print
them later.

To run the program, run in the command prompt the following command inside the src folder:
  \npython main.py
  
In case of using Python 3: 
  \npython3 main.py
  
Note that OpenCV must be installed. To install OpenCV:
  \npip install opencv-python
