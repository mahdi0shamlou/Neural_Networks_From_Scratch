import numpy as np


class Neuron():
    # first neuron has only one input and it is use for finding a liner regresion
    def __init__(self):
        self.w1 = np.random.random()
        print(self.w1)
    def Activate_function(self, x):
        if x > 0:
            return 1
        else:
            return 0

    def train(self, repet, input_data, output_data):
        pass


    def think(self, x):
        x = self.w1 * x
        x = self.Activate_function(x)
        return x


#-------------------------------- test
n = Neuron()
print(n.think(-1))