import random
from matplotlib import pyplot as plt
import numpy as np
x_data_set = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [4],
    [5],
    [7],
    [8],
    [8],
    [2],
    [10],
    [11],
    [15]
]
y_data_set = [
    [3],
    [5],
    [7.1],
    [8.8],
    [11],
    [9],
    [11.2],
    [15],
    [17],
    [17.2],
    [5],
    [21],
    [22.7],
    [31]
]
def show_points(x_sets, y_sets):
    """
    This mehtode get x and y sets data and show it in 2d plot
    :param x_sets:
    :param y_sets:
    :return:
    """
    for i in range(0, len(x_sets)):
        plt.plot([x_sets[i][0]], [y_sets[i][0]], marker="o", color='black')

def create_wighet(x_sets):
    """
    this methode create wighet from x_data_set
    we create wight with len x_setes but add one wigh becuse we need bios in regression
    :param x_sets:
    :return:
    """
    W = []
    for i in range(0, len(x_sets[0])+1):
        W.append(random.randint(-10 ,10))
    print(W)
    return W


def activation_func(net):
    """
    this methode is liner activation function
    :param net:
    :return:
    """
    return net


def optimaize_error(w, e):
    """
    this methode get error and x_set[i] and w in stage[i] and change w in way to optimaze
    :param w:
    :param e:
    :return:
    """
    for i in range(0, len(w)):
        w[i] = w[i] + e
    return w

if __name__ == '__main__':
    show_points(x_data_set, y_data_set)
    plt.show()