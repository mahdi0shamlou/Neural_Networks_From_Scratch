# Neural_Networks
This project is about the creation and development of nerual networks from scratch

### Perceptron.py
this is a one singel perceptron and has many activation function like sigmoid or tanh or liner or hardlimits for liner_regression or classification 

> [!TIP]
> How it Works ? This perceptron use from a error function (e = (d-y)**2) and try to optimize it.

### Perceptron_binary_classifire.py
This file is a single perceptron that learns and optimizes.
This perceptron is used for classification.

> [!TIP]
> How it works ?! This perceptron has a activation function and has a optimizer function if see any difrent between output of activation function and real data send this data to optimaizer function and get new Wight from it and use from this for new calculate

### Perceptron_liner_regression.py
This file is a single perceptron that learns and optimizes.
This perceptron is used for liner regression.

> [!TIP]
> How it works?! This perceptron has an activation function (actually just returning the input and doing the note) and it has an optimizer function. If you see any difference between the output of the activation function and the actual data, send this data to the optimizer function. And get and use that new wight. From this, for the new calculation, this algorithm is slightly different from classification algorithms, and this difference is in the performance of activation and optimizer.

> [!CAUTION]
> In this file, you should know that we need BIOS in the create wight method and we create an additional w in the W vector because we need BIOS and in the show_line methode, we consider the last w for BIOS if you want Use it, just change it.

### Adaline.py
this file is a single neuron from adaline model and algorithms.

> [!TIP]
>  How it works ?! This file is an adaline neuron and it optimizes own weight with Matrix calculations. we have a difference between adaline offline learning method and perceptron learning method . and that is in one single adaline neuron we can find best wight in offline learning method only with Matrix calculations. And we dont need any online learning method like gradient descent.

> [!WARNING]
> But that is important you know that we can use gradient descent in adelaide for learning but we chose another way (offline learning method) because we already Implemented gradient descent in perceptrons file

### LSTM.py
this file is a single neuron from LSTM model and algorithms.

### CNN.py
this file is a single neuron from Convolutional neural network model and algorithms.

