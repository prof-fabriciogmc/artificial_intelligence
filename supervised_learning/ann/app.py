##
# Simple feedforward neural network application example.
# It solves the clasical xor non linearly separable problem.
#
# Author: Fabrício G. M. de Carvalho, Ph.D
##

from neural_network import Neuron, Layer, FFNeuralNetwork
from matplotlib import pyplot as plt


layout = [2,4,1]
training_set = [{'i':[0,1], 'o':[1]},
                {'i':[0,0], 'o':[0]},
                {'i':[1,0], 'o':[1]},
                {'i':[1,1], 'o':[0]},
                ]
neural_network = FFNeuralNetwork(layout)
w_1 = []
w_2 = []
error = []
for epoch in range(10000):
    for training_data in training_set:
        y = neural_network.output(training_data['i'])
        e = [training_data['o'][0] - y[0] ]
        neural_network.learn(e, 0.1)
    w_1.append(neural_network.layers[0].weights[0][0])
    w_2.append(neural_network.layers[0].weights[0][1])
    error.append(e[0])

plt.figure(1)
plt.plot(w_1)
plt.figure(2)
plt.plot(w_2)
plt.figure(3)
plt.plot(error)
plt.show()

print(neural_network.output([1,0]))
print(neural_network.output([0,1]))
print(neural_network.output([0,0]))
print(neural_network.output([1,1]))

