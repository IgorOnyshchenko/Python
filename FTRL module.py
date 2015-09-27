# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 23:31:18 2015

@author: Igor
"""
import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

# Function of loss 
def log_loss(y, p):
    """
    :param y: True target value
    :param p: Predicted probability
    :return: Log loss.
    """
    p = max(min(p, 1. - 10e-15), 10e-15)
    return -np.log(p) if y == 1 else -np.log(1. - p)    


class FTRLProximal:
    
    def __init__(self, n_inputs):
        self.z = np.zeros(n_inputs)
        self.n = np.zeros(n_inputs)  
        

    def fit_iteration(self, x, y, alpha, beta, lambda_1, lambda_2):

        alpha_inv = 1 / alpha
        
        w = self.weight_update(x, alpha_inv, beta, lambda_1, lambda_2)
        p = self.sigmoid(w.sum())
        g = (p - y)
        dn = self.n[x] + g**2        
        sigma = alpha_inv * (np.sqrt(dn) - np.sqrt(self.n[x]))
        self.z[x] = self.z[x] + g - sigma * w
        self.n[x] = dn
       
        return p, x, g, w


    def weight_update(self, x, alpha_inv, beta, lambda_1, lambda_2):
        dw = np.zeros(x.size)
        mask = np.abs(self.z[x]) > lambda_1
        
        z_i = self.z[x][mask]
        n_i = self.n[x][mask]
        
        dw[mask] = (np.sign(z_i) * lambda_1 - z_i) / ((beta + np.sqrt(n_i)) * alpha_inv + lambda_2)
        
        return dw


    def predict(self, x, alpha_inv, beta, lambda_1, lambda_2):
        w = self.weight_update(x, alpha_inv, beta, lambda_1, lambda_2)
        
        return self.sigmoid(w.sum())


    #Sum errors and number of cases with x=1 in row    
    def count_x_error(self, x):
        g_x=[0]*len(x)
        g_n=[0]*len(x)
        
        for i in range(len(x)):
            if float(x[i])==1: 
                g_x[i]+=self.g
                g_n[i]+=1
            else:
                continue
            
        return g_x, g_n


    
    