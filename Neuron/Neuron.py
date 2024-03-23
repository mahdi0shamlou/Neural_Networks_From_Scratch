import numpy
import pandas

class Neuron():
    # first neuron has only one input and it is use for finding a liner regresion
    def __init__(self, x1):
        self.Inputs = []
        self.Inputs.append(x1)
        pass