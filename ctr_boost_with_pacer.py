# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:07:41 2015

@author: User
"""
import numpy as np
from collections import deque


class ctr_boost_pace:
    
    def __init__(self, bid, budget, learning_rate = 0.01, cache_size = 10):
        self.rate = learning_rate
        self.cache_size = cache_size
        self.ctr_cache = deque(maxlen = cache_size)
        self.threshold = 0
        self.sb = 0
        self.bid = bid
        self.budget = budget
        self.B = 0
        
        
    def update_sb(self, win):
        if win > 0:
            self.sb += self.Bid    
        
    
    def update(self, ctr_estimate, time, budget_limit):
        self.B = self.budget*budget_limit
        self.ctr_cache.append(ctr_estimate)
        self.threshold = np.median(self.ctr_cache)+self.rate*(self.sb/self.B - time/24/6)
        
        
    def get_bid(self, ctr_estimate):
        if ctr_estimate > self.threshold and self.sb+self.Bid <= self.B:
            bid = 1.0
        else:
            bid = 0.0
            
        return bid
        
        