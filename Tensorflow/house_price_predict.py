from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense


(train_x, train_y), (test_x, test_y) = boston_housing.load_data()

print(train_x[0])
print(train_y[0])
input()
network = Sequential()
network.add(Dense(10, activation='selu', input_shape=(13, )))
network.add(Dense(15, activation='relu'))
network.add(Dense(20, activation='relu'))
network.add(Dense(15, activation='relu'))
network.add(Dense(10, activation='relu'))
network.add(Dense(1))
network.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
network.fit(train_x, train_y, epochs=300, batch_size=10)
print(network.evaluate(test_x, test_y))