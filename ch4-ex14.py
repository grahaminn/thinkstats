import numpy

def weibullvariate(lam, k):
  return lam * numpy.random.weibull(k, 1)


