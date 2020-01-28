import numpy as np

class ClassifierWeak:
        def __init__(self):
            self.pixel = -1
            self.edge = -1
            self.direction = ''
            self.classification = np.numpy(0)
            self.error = -1.0
            self.confidence = -1.0
                
        def with_values(self, pixel, edge, direction, size):
            self.pixel = -1
            self.edge = -1
            self.direction = ''
            self.classification = np.empty(size)
            self.error = -1.0
            self.confidence = -1.0

        def __eq__(self, other):
            return self.pixel == other.pixel and self.edge == other.edge and self.direction == other.direction
        
        def __ne__(self, other):
            return not self == another