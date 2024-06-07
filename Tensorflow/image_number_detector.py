from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.utils import to_categorical

(train_x, train_y), (test_x, test_y) = mnist.load_data()
train_x = train_x.reshape((60000, 784))
test_x = test_x.reshape((10000, 784))

train_x = train_x.astype('float32')/255
test_x = test_x.astype('float32')/255

train_y = to_categorical(train_y)
test_y = to_categorical(test_y)


network = Sequential()
network.add(Dense(1024, activation='selu', input_shape=(28*28, )))
network.add(Dense(512, activation='relu'))
network.add(Dense(256, activation='relu'))
network.add(Dense(128, activation='relu'))
network.add(Dense(64, activation='relu'))
network.add(Dense(32, activation='relu'))
network.add(Dense(16, activation='relu'))
network.add(Dense(10, activation='relu'))
network.add(Dense(10, activation='softmax'))
network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
network.fit(train_x, train_y, epochs=30, batch_size=150)
print(network.evaluate(test_x, test_y))