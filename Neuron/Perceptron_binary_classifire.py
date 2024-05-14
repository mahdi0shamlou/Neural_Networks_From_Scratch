import random
from matplotlib import pyplot as plt
import numpy as np



x_data_set = [
    [0, 1],
    [3, 2],
    [2, 1],
    [2, 2],
    [3, 3],
    [-1, 4],
    [4, 5],
    [-1, -1],
    [1, -2],
    [-2, -1],
    [-2, -2],
    [-3, -3],
    [-4, 4],
    [-4, -5]
]
y_data_set = [
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [-1],
    [-1],
    [-1],
    [-1],
    [-1],
    [-1],
    [-1]
]


def show_points(x_sets, y_sets):
    """
    This mehtode get x and y sets data and show it in 2d plot
    :param x_sets:
    :param y_sets:
    :return:
    """
    for i in range(0, len(x_sets)):
        if y_sets[i][0] == 1:
            plt.plot([x_sets[i][0]], [x_sets[i][1]], marker="o", color='red')
        else:
            plt.plot([x_sets[i][0]], [x_sets[i][1]], marker="*", color='blue')


def create_wighet(x_sets):
    """
    this methode create wighet from x_data_set
    :param x_sets:
    :return:
    """
    W = []
    for i in range(0,len(x_sets[0])):
        W.append(random.randint(-10 ,10))
    print(W)
    return W

def activation_func(net):
    """
    this methode is Hard-Limit activation function
    :param net:
    :return:
    """
    if net >= 0:
        return 1
    else:
        return -1

def optimaize_error(x,w,e):
    """
    this methode get error and x_set[i] and w in stage[i] and change w in way to optimaze
    :param x:
    :param w:
    :param e:
    :return:
    """
    for i in range(0,len(x)):
        w[i] = w[i] + (e * x[i])
    return w

def show_line_w(w):
    """
    this method get W and create line with it for plot
    :param w:
    :return:
    """

    x = np.linspace(-2, 2, 100)
    y = x * w[0] / w[1]
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

        f_resault = activation_func(net) # send it to activaition func for find a group for it
        error = y_data[random_d][0] - f_resault # find error
        if error == 0:
            continue
        else:
            x, y = show_line_w(W)
            show_points(x_data_set, y_data_set)
            plt.plot(x, y, '-r', label='W')

            W = optimaize_error(x_data[random_d], W, error)
            x, y = show_line_w(W)
            plt.plot(x, y, '-b', label='W')
            plt.show()
    return W


def test(x, y, w):
    true = 0
    false = 0
    for i in range(0, len(x)):
        net = 0
        for z in range(0, len(x[i])):
            net = net + (x[i][z] * w[z])
        res = activation_func(net)
        error = y[i][0] - res
        if  error == 0:
            true += 1
        else:
            false += 1
    return true, false



if __name__ == '__main__':

    show_points(x_data_set, y_data_set)
    plt.show
    W = create_wighet(x_data_set)
    trues, flases = test(x_data_set, y_data_set, W)
    print(f'true number is -> {trues}')
    print(f'flases number is -> {flases}')
    W = learning(x_data_set, y_data_set, 100, W)
    print('------------------------')
    x, y = show_line_w(W)
    show_points(x_data_set, y_data_set)
    plt.plot(x, y, '-r', label='LAST TRY')
    plt.show()
    print(W)
    trues, flases = test(x_data_set, y_data_set, W)
    print(f'true number is -> {trues}')
    print(f'flases number is -> {flases}')