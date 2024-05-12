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
    [3.9],
    [6.2],
    [8.3],
    [9.2],
    [11.7],
    [14.4],
    [16.2],
    [18],
    [20.4],
    [21.6],
    [24.2],
    [26.4],
    [27.3]
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


def show(x , y, w):
    for i in range(0, len(x)):
        plt.plot([x.item(i)], [y.item(i)], marker="o", color='black')

    x_line = np.linspace(0, 14, 100)
    y_line = (x_line * w.item(0))
    plt.plot(x_line, y_line, '-r', label='line')
    plt.show()


    return x, y
if __name__ == '__main__':
    W = Optimaize(x_data_set, y_data_set)
    print(f'Wight is -> {W}')
    show(x_data_set, y_data_set, W)

