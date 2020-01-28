import numpy as np

class ClassifierWeak:
        # def __init__(self):
        #     self.pixel = -1
        #     self.edge = -1
        #     self.direction = ''
        #     self.classification = np.empty(0, int)
        #     self.error = -1.0
        #     self.confidence = -1.0
                        
        #@classmethod                
        def __init__(self, pixel, edge, direction):
            self.pixel = -1
            self.edge = -1
            self.direction = ''
            self.classification = np.empty(0, int)
            self.error = -1.0
            self.confidence = -1.0
        
        def __eq__(self, other):
            return self.pixel == other.pixel and self.edge == other.edge and self.direction == other.direction
        
        def __ne__(self, other):
            return not self == another