#!/usr/bin/python

import math
import random

class RandomVariable(object):
    """Parent class for all random variables."""

class Exponential(RandomVariable):
    def __init__(self, lam):
        self.lam = lam

    def generate(self):
        return random.expovariate(self.lam)

class Erlang(RandomVariable):
    def __init__(self, lam, k):
        self.lam = lam
        self.k = k
        self.expo = Exponential(lam)

    def generate(self):
        total = 0
        for i in range(self.k):
            total += self.expo.generate()
        return total

class Uniform(RandomVariable):
    def __init__(self, min, max):
        self.min = min
        self.max = max
     
    def generate(self):
        return random.uniform(self.min, self.max)

class Gumbel(RandomVariable):
    def __init__(self, mu, b):
        self.mu = mu
        self.b = b
        self.uniform = Uniform(0, 1)
 
    def generate(self):
        return self.mu - (self.b * math.log(0-math.log(self.uniform.generate())))
 
