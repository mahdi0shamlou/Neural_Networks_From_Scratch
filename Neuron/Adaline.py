import random
from matplotlib import pyplot as plt
import numpy as np

x_data_set = np.matrix([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10],
    [11],
    [12],
    [13],
    [14]
])
y_data_set = np.matrix([
    [2],
    [4],
    [6.1],
    [8],
    [10],
    [12],
    [14],
    [16],
    [18],
    [20.1],
    [21.9],
    [24],
    [26],
    [28]
])

def Optimaize(x: np.matrix, y: np.matrix):
    """
    this methode get x and y and find best wight for x * w = y
    we calculate wight with matrix
    :param x:
    :param y:
    :return:
    """
    W = x.T.dot(y) / (x.T.dot(x))
    return W

if __name__ == '__main__':
    print(x_data_set.shape)
    print(x_data_set.T.shape)

    pass