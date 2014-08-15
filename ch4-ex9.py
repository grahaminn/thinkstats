import erf
import math
import numpy.random 

def Sample():
    return sorted(numpy.random.normal(0, 1, 6))
    
def Samples():
    samples = []
    for i in range(10000):
         samples.append(Sample())
    return samples

samples = Samples()
zipped = zip(*samples)

for list in zipped:
   print numpy.mean(list)

