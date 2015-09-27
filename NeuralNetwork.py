# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Activation function for Neural Network
import numpy as np

def tan(x):
    return np.tanh(x)

def tan_deriv(x):
    return 1.0 - np.tanh(x)**2

def log(x):
    return 1/(1 + np.exp(-x))

def log_deriv(x):
    return log(x)*(1-log(x))
    
#create class Neural Network
"""
In the con­struc­tor of the class we will need to set the number of neurons in each layer,
 initialize their weights randomly between -0.25 and 0.25 
 and set the activation function to be used. Each layer, except the last one, 
 will also have a bias unit which cor­re­sponds to the threshold value for the activation.
"""
class NeuralNetwork:
    def __init__(self, layers, activation='log'):
        """
        :param layers: A list containing the number of units in each layer.
        Should be at least two values
        :param activation: The activation function to be used. Can be
        "logistic" or "tanh"
        """
        if activation == 'log':
            self.activation = log
            self.activation_deriv = log_deriv
        elif activation == 'tan':
            self.activation = tan
            self.activation_deriv = tan_deriv

        self.weights = []
        for i in range(1, len(layers) - 1):
            self.weights.append((2*np.random.random((layers[i - 1] + 1, layers[i]
                                + 1))-1)*0.25)
        self.weights.append((2*np.random.random((layers[i] + 1, layers[i +
                            1]))-1)*0.25)

    #Function to train model
    """
    Given a set of input vectors X and output values y, adjust the weights ap­propi­ate­ly. 
    The algorithm we will use is called stochastic gradient descent, 
    which chooses randomly a sample from the training data 
    and does the back­prop­a­ga­tion for that sample, 
    and this is repeated for a number of times (called epochs). 
    We also have to set the learning rate of the algorithm, 
    which determines how big a change occurs in the weights each time (pro­por­tion­al­ly to the errors).
    """
    def fit(self, X, y, learning_rate=0.1, epochs=10000):
        X = np.atleast_2d(X)
        temp = np.ones([X.shape[0], X.shape[1]+1])
        temp[:, 0:-1] = X  # adding the bias unit to the input layer
        X = temp
        y = np.array(y)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            error = y[i] - a[-1]
            deltas = [error * self.activation_deriv(a[-1])]

            for l in range(len(a) - 2, 0, -1): # we need to begin at the second to last layer
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
            deltas.reverse()
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    #Function to predict the output with using trained model
    """
    This is pretty much the same as the forward pass part of back­prop­a­ga­tion, 
    except we don't need to keep all the values of the ac­ti­va­tions for each neuron, 
    so we keep only the last one.
    """
    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0]+1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


