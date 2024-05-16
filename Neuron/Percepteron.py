import numpy as np  # We need Numpy for matrix
import random


def create_data_sets():
    """
     You can create your own x_data_sets and y_data_set
    :return:
    """

    x_data_set = [[-2], [2], [3], [4], [5], [6], [7], [10], [-1]]  # you can replace this with your x_data_set
    y_data_set = [
        [(i[0] * 3) + 1] for i in x_data_set
    ]  # you can replace this with your y_data_sets
    return x_data_set, y_data_set


def create_matrix_from_data_sets(x_data_set, y_data_set):
    """
    we get data set and create matrix from them
    :param x_data_set:
    :param y_data_set:
    :return:
    """
    for i in x_data_set:
        i.append(1)
    x_data_set = np.matrix(x_data_set)
    y_data_set = np.matrix(y_data_set)
    return x_data_set, y_data_set


def activate_function(net):
    """
    this is simoid function for activation functions
    :param net:
    :return:
    """
    return 1 / (1 + np.exp(-net))


def activate_function_derivative(x):
    """
    computing derivative to the Sigmoid function
    :param x:
    :return:
    """
    return x * (1 - x)


def create_w(n):
    w = []
    for i in range(0, n+1):
        w.append(random.randint(-1,1))
    w = np.matrix(w)
    #print(w)
    return w


def learning(x_data: np.matrix, y_data: np.matrix, n: int, z: int, iteration: int):
    w = create_w(n)
    print(f"this is starter Wight : {w}")
    for i in range(0, iteration):
        
        pass
    return w

if __name__ == '__main__':

    X_data_set, Y_data_set = create_data_sets()  # you can disable this line and replace your x and y
    X_data_set, Y_data_set = create_matrix_from_data_sets(X_data_set, Y_data_set)

    print(f"x data sets : {X_data_set.shape} \n {X_data_set}")
    print(f"y data sets : {Y_data_set.shape} \n {Y_data_set}")

