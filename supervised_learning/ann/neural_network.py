from numpy import matmul
from math import tanh, cosh
from random import random


#hyperbolic secant
def sech(x):
    return 1/cosh(x)

# hyperbolic tangent derivative
def tanh_d(x):
    return (sech(x)**2)

class Neuron:
   """
   Basic neuron with hiperbolic tangent activation function
   TODO: parameterized activation functions.
   """
   def __init__(self):
       """
       """
       pass

   def output(self, input):
       return tanh(input)


class Layer:
    """
    A single layer in a feedforward neural network gets n inputs, multiply
    it by the corresponding weights and generates the corresponding outputs.
    outs = Neurons.out(W.x)
    """
    def __init__(self, n_in, n_out):
        """
        This constructor initializes all the synaptic weights with random numbers
        in the interval [0, 0.1).
        :param n_in: number of layer inputs
        :param n_out: number of layer outputs
        """
        self.weights = [ [ 0.1*random() for j in range(n_in)] for i in range(n_out)]
        self.neurons = [ Neuron() for j in range(n_out)]
        self.n_in = n_in
        self.n_out = n_out
        self.out = []
        self.layer_input = [] # required by backpropagation
        self.neuron_in = []  # required by backpropagation

    def output(self, input):
        self.layer_input = input
        self.neuron_in = matmul(self.weights, input)
        output = []
        for i in range(self.n_out):
            output.append(self.neurons[i].output(self.neuron_in[i]))
        self.out = output
        return output

class FFNeuralNetwork:
    """
    Basic feedforward neural network.
    """
    def __init__(self, layout):
        """
        :param layout: list specifying [n_inputs, n_hidden_1, n_hidden_2, .., n_out]
        The number of layers is equal to len(layout)-1
        """
        self.layout = layout
        self.n_layers = len(layout) -1
        self.layers = []
        for i in range(self.n_layers):
            self.layers.append(Layer(layout[i],layout[i+1]))

    def output(self, input):
        """
        :param input: Neural Network input
        :return: Neural Network output
        """
        for i in range(self.n_layers):
            if i == 0:
                self.layers[i].output(input)
            else:
                self.layers[i].output(self.layers[i-1].out)
        return self.layers[self.n_layers -1].out

    def learn(self, error, eta):
        """
        This method implements the required learning algorithm.
        In this case, the backpropagation algorithm.
        :param eta the learning rate.
        :param error the output layer to be propagated
        """
        # the following loop is in reverse order because
        # output error signal is propagated from the last to
        # the first input layer
        local_gradient = []
        for k in range(self.n_layers):
            local_gradient.append([])

        for k in range(self.n_layers-1,-1,-1):  # from the last till the first layer
            if k == (self.n_layers - 1): # output layer
                for i in range(len(error)): #local gradient computation for each layer neuron
                    local_gradient[k].append(tanh_d(self.layers[k].neuron_in[i])*error[i])
                    for j in range(self.layers[k].n_in):
                        self.layers[k].weights[i][j] += eta* local_gradient[k][i] * self.layers[k].layer_input[j]
                        #print(local_gradient[k][i])
                        #print(self.layers[k].weights[i][j])
            else:
                for i in range(len( self.layers[k].out ) ):
                    bpg = 0
                    for t in range(len(self.layers[k+1].out)):
                        bpg += self.layers[k+1].weights[t][i] * local_gradient[k+1][t]
                    local_gradient[k].append(tanh_d(self.layers[k].neuron_in[i])*bpg)
                    for j in range(self.layers[k].n_in):
                        self.layers[k].weights[i][j] += eta* local_gradient[k][i] * self.layers[k].layer_input[j]








