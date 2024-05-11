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
        w[i] = w[i] + (0.1*e)
    return w
def show_line_w(w):
    """
    this method get W and create line with it for plot
    :param w:
    :return:
    """

    x = np.linspace(-10, 10, 100)
    y = (x * w[0]) + w[1]
    return x, y
def learning(x_data, y_data, number_iterition, W):
    """
    this methode get y and x data and learn from these and ...
    :param x_data:
    :param y_data:
    :param number_iterition:
    :param W:
    :return:
    """
    for i in range(0, number_iterition):
        random_d = random.randint(0, len(x_data)-1) # choses a random sampel for optimaization
        net = 0 # create net for tershold

        for z in range(0, len(x_data[random_d])):
            net = net + (x_data[random_d][z]*W[z]) # sumtion of wixi
        net += W[len(W)-1] # this is bios
        f_resault = activation_func(net) # send it to activaition func for find a group for it
        error = y_data[random_d][0] - f_resault # find error
        print(error)
        if error == 0:
            continue
        else:
            x, y = show_line_w(W)
            show_points(x_data_set, y_data_set)
            plt.plot(x, y, '-r', label='W')

            W = optimaize_error(W, error)
            x, y = show_line_w(W)
            plt.plot(x, y, '-b', label='W')

    return W


if __name__ == '__main__':
    show_points(x_data_set, y_data_set)
    plt.show
    W = create_wighet(x_data_set)

    W = learning(x_data_set, y_data_set, 100, W)
    print('------------------------')
    x, y = show_line_w(W)
    show_points(x_data_set, y_data_set)
    plt.plot(x, y, '-r', label='LAST TRY')
    plt.show()
    print(W)
