#!/usr/bin/python


# p(h1) = 1/2
h1 = 0.5
# p(e|h1) = 30/40
eh1 = 0.75
# p(e|h2) = 20/40
eh2 = 0.5
# p(h2) = 1/2
h2 = 0.5

h1e = (eh1 * h1) / ((eh1 * h1) + (eh2 * h2))

print 'probability of bowl 1 given a plain cookie:', h1e 
