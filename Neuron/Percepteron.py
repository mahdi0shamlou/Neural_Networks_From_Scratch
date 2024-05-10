from matplotlib import pyplot as plt
x_data_set = [
    [1, 1],
    [1, 2],
    [2, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [4, 5],
    [-1, -1],
    [-1, -2],
    [-2, -1],
    [-2, -2],
    [-3, -3],
    [-4, -4],
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
    plt.show()

def create_wave(x_sets):
    """
    this methode create wighet from x_data_set
    :param x_sets:
    :return:
    """
    W = []
    for i in range(0,len(x_sets[0])):
        W.append(1)
    print(W)

def activation_func(net):
    """
    this methode is Hard-Limit activation function
    :param net:
    :return:
    """
    if net >= 0 :
        return 1
    else:
        return -1



if __name__ == '__main__':

    show_points(x_data_set, y_data_set)
    create_wave(x_data_set)
    print('test')