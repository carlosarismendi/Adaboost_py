import numpy as np

class ClassifierWeak:
    def __init__(self, pixel, edge, direction):
        self.pixel = pixel
        self.edge = edge
        self.direction = direction
        self.classification = np.empty(0, int)
        self.error = -1.0
        self.confidence = -1.0
            
    def __eq__(self, other):
        if self is None:
            if other is None:
                return True
            else:
                return False
        else:
            if other is None:
                return False

        if self.pixel == other.pixel and self.edge == other.edge and self.direction == other.direction:
            return True
        else:
            return False                            
    
    def __ne__(self, other):
        return not self == other

    
    def __str__(self):
        string = 'Pixel:' + str(self.pixel)
        string += ' | Edge:' + str(self.edge)
        string += ' | Direction:' + str(self.direction)
        return string
