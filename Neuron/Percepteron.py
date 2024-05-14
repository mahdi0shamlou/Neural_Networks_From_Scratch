import numpy as np  # We need Numpy for matrix


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


def create_matrix_from_data_sets(X_data_set, Y_data_set):
    """
    we get data set and create matrix from them
    :param X_data_set:
    :param Y_data_set:
    :return:
    """
    for i in X_data_set:
        i.append(1)
    x_data_set = np.matrix(X_data_set)
    y_data_set = np.matrix(Y_data_set)
    return x_data_set, y_data_set


def activate_function(net):
    """
    this is simoid function for activation functions
    :param net:
    :return:
    """
    return 1 / (1 + np.exp(-net))



if __name__ == '__main__':

    X_data_set, Y_data_set = create_data_sets()  # you can disable this line and replace your x and y 
    X_data_set, Y_data_set = create_matrix_from_data_sets(X_data_set, Y_data_set)
    print(f"x data sets : \n {X_data_set}")
    print(f"y data sets : \n {Y_data_set}")

