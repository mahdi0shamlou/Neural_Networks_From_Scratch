import numpy as np  # We need Numpy for matrix
import random

from numpy.distutils.system_info import x11_info
from sklearn.preprocessing import normalize

def create_data_sets():
    """
     You can create your own x_data_sets and y_data_set
    :return:
    """

    x_data_set = [[-12], [12], [8], [9], [10], [17], [11], [15], [-10], [-14]]  # you can replace this with your x_data_set
    y_data_set = []
    for i in x_data_set:
        if i[0] > 3:
            y_data_set.append([1])
        else:
            y_data_set.append([-1])

    #y_data_set = normalize(y_data_set, axis=0, norm='max')
    #x_data_set = normalize(x_data_set, axis=0, norm='max')
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


def activate_function_derivative(net):
    """
    computing derivative to the Sigmoid function
    :param net:
    :return:
    """
    return np.exp(-net) / ((1 + np.exp(-net)) * (1 + np.exp(-net)))


def create_w(n):
    """
    this methode get number of input layer and create random wight with it
    :param n:
    :return:
    """
    w = []
    for i in range(0, n+1):
        w.append(random.uniform(-1,1))
    w = np.matrix(w)
    return w


def learning(x_data: np.matrix, y_data: np.matrix, n: int, z: int, iteration: int):
    w = create_w(n)
    print(f"this is starter Wight : {w}")
    '''
    
    
    print(f"this is X-data : {x_data[0]}")
    print(f"this is Y-data : {y_data[0]}")
    net = w.dot(x_data[0].T)
    print(f"this is net of simpel one : {net}")
    resalut = activate_function(net)
    print(f"this is resualt of activation methode : {resalut}")
    error = (y_data.item(0) - resalut)
    print(f"this is error : {error}")

    net_new = w.item(0) * x_data.item(0)
    print(f"this is new net {net_new}")
    new_dif = activate_function_derivative(net_new)
    print(f"this is diff of activaet {new_dif}")

    print("----------------------------")
    print(f"this is way we should go {new_dif*error*x_data.item(0)*-1}")
    
    ##################################
    print("\n-----------------------")
    net = w.dot(x_data.T)
    print(f"this is all of net : \n{net}\n-----------------------")
    resalut = activate_function(net)
    print(f"this is all of resalut : \n{resalut}\n-----------------------")
    error = y_data.T-resalut
    print(f"this is error {error}")
    print(x_data.shape)
    print(error.shape)
    print(error.dot(x_data))
    print(net.T.shape)
    difs = map(activate_function_derivative, net.T)
    print(list(difs))
    difs = activate_function_derivative(net.T)
    print(difs)
    print(difs.shape)
    '''
    for i in range(0, iteration):
        rand_num = random.randint(0, 9)
        #rand_num = 0
        net = w.dot(x_data[rand_num].T)
        resault = activate_function(net)
        error = y_data[rand_num] - resault
        w_new_adj = []
        for z in range(0, n+1):
            new_nets = w.item(z) * x_data[rand_num].item(z)
            difs = activate_function_derivative(new_nets)
            adjs_add = error*difs*x_data[rand_num].item(0) # find how much should change for wight
            w_new_adj.append(adjs_add.item(0))

        w_new_adj = np.matrix(w_new_adj)
        w = w + w_new_adj # optimize wight
        print(w)
        print(w_new_adj)
        print(w)
        print('---------------')


        pass

    return w


if __name__ == '__main__':

    X_data_set, Y_data_set = create_data_sets()  # you can disable this line and replace your x and y
    X_data_set, Y_data_set = create_matrix_from_data_sets(X_data_set, Y_data_set)
    #print(f"x data sets : {X_data_set.shape} \n {X_data_set}")
    #print(f"y data sets : {Y_data_set.shape} \n {Y_data_set}")
    w = learning(x_data=X_data_set, y_data=Y_data_set, n=1, z=1, iteration=100000)

    net = w.dot(X_data_set.T)
    print(net)
    resault = activate_function(net)
    print(resault)
    print(resault.shape)
    print(Y_data_set.shape)
    error = Y_data_set.T - resault

    for i in range(0, 9):
        a = error.item(i)
        print("%.16f" % a)

    #print(error)


