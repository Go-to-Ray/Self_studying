
import numpy as np
from layers import *
from gradient import numerical_gradient
from collections import OrderedDict


class EightLayerNet:
    
    def __init__(self, input_size, hidden_size, output_size,weight_multi = 0.01):
        #weight,bias
        self.params = {}
        self.params["W1"] = np.random.randn(input_size, hidden_size)/np.sqrt(input_size)*np.sqrt(2)
        self.params["W2"] = np.random.randn(hidden_size, hidden_size)/np.sqrt(hidden_size)*np.sqrt(2)
        self.params["W3"] = np.random.randn(hidden_size, hidden_size)/np.sqrt(hidden_size)*np.sqrt(2)
        self.params["W4"] = np.random.randn(hidden_size, hidden_size)/np.sqrt(hidden_size)*np.sqrt(2)
        self.params["W1"] = np.random.randn(hidden_size, hidden_size)/np.sqrt(hidden_size)*np.sqrt(2)
        self.params["W2"] = np.random.randn(hidden_size, hidden_size)/np.sqrt(hidden_size)*np.sqrt(2)
        self.params["W3"] = np.random.randn(hidden_size, hidden_size)/np.sqrt(hidden_size)*np.sqrt(2)
        self.params["W4"] = np.random.randn(hidden_size, output_size)/np.sqrt(hidden_size)*np.sqrt(2)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["b2"] = np.zeros(hidden_size)
        self.params["b3"] = np.zeros(hidden_size)
        self.params["b4"] = np.zeros(hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["b2"] = np.zeros(hidden_size)
        self.params["b3"] = np.zeros(hidden_size)
        self.params["b4"] = np.zeros(output_size)
        #make layer
        self.layers = OrderedDict()
        self.layers["Affine1"] = Affine(self.params["W1"],self.params["b1"])
        self.layers["Relu"] = Relu()
        self.layers["Affine2"] = Affine(self.params["W2"],self.params["b2"])
        self.layers["Relu"] = Relu()
        self.layers["Affine3"] = Affine(self.params["W3"],self.params["b3"])
        self.layers["Relu"] = Relu()
        self.layers["Affine4"] = Affine(self.params["W4"],self.params["b4"])
        self.layers["Relu"] = Relu()
        self.layers["Affine5"] = Affine(self.params["W5"],self.params["b5"])
        self.layers["Relu"] = Relu()
        self.layers["Affine6"] = Affine(self.params["W6"],self.params["b6"])
        self.layers["Relu"] = Relu()
        self.layers["Affine7"] = Affine(self.params["W7"],self.params["b7"])
        self.layers["Relu"] = Relu()
        self.layers["Affine8"] = Affine(self.params["W8"],self.params["b8"])
        
        
        self.lastLayer = SoftmaxWithLoss()
        
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        
        return x
    
    #x is pic_data, t is label
    def loss(self, x, t):
        y = self.predict(x)
        
        return self.lastLayer.forward(y,t)
        
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 : t = np.argmax(t,axis=1)
        
        accuracy = np.sum(y == t)/float(x.shape[0])
        return accuracy
    
    def gradient(self, x, t):
        #forward
        self.loss(x,t)
        #backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)
            
        grads = {}
        grads["W1"] = self.layers["Affine1"].dW
        grads["b1"] = self.layers["Affine1"].db
        grads["W2"] = self.layers["Affine2"].dW
        grads["b2"] = self.layers["Affine2"].db
        grads["W3"] = self.layers["Affine3"].dW
        grads["b3"] = self.layers["Affine3"].db
        grads["W4"] = self.layers["Affine4"].dW
        grads["b4"] = self.layers["Affine4"].db
        grads["W5"] = self.layers["Affine5"].dW
        grads["b5"] = self.layers["Affine5"].db
        grads["W6"] = self.layers["Affine6"].dW
        grads["b6"] = self.layers["Affine6"].db
        grads["W7"] = self.layers["Affine7"].dW
        grads["b7"] = self.layers["Affine7"].db
        grads["W8"] = self.layers["Affine8"].dW
        grads["b8"] = self.layers["Affine8"].db

        return grads