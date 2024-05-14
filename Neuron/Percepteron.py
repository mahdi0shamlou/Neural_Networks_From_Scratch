import numpy as np  # We need Numpy for matrix


def create_data_sets():
    """
     You can create your own x_data_sets and y_data_set
    :return:
    """
    X_data_set = [[-2, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [10, 1], [-1, 1]]
    Y_data_set = [
        [(i[0] * 3) + 1] for i in X_data_set
    ]
    return X_data_set, Y_data_set


def create_matrix_from_data_sets(X_data_set, Y_data_set):
    """
    we get data set and create matrix from them
    :param X_data_set:
    :param Y_data_set:
    :return:
    """
    X_data_set = np.matrix(X_data_set)
    Y_data_set = np.matrix(Y_data_set)
    return X_data_set, Y_data_set


if __name__ == '__main__':
    X_data_set, Y_data_set = create_data_sets()
    X_data_set, Y_data_set = create_matrix_from_data_sets(X_data_set, Y_data_set)
    print(f"x data sets : \n {X_data_set}")
    print(f"y data sets : \n {Y_data_set}")

