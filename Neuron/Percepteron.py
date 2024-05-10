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
def Show_points(x_sets, y_sets):
    for i in range(0, len(x_sets)):
        if y_sets[i][0] == 1:
            plt.plot([x_sets[i][0]], [x_sets[i][1]], marker="o", color='red')
        else:
            plt.plot([x_sets[i][0]], [x_sets[i][1]], marker="*", color='blue')
    plt.show()





if __name__ == '__main__':
    Show_points(x_data_set, y_data_set)
    print('test')

