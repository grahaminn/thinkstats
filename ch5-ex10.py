import math
import thinkstats

def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binomial_distribution(n, k, p):
    return binomial_coefficient(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomial_thinkstats(n, k, p):
    return thinkstats.Binom(n, k) * (p ** k) * ((1 - p) ** (n - k))

print 'my way', binomial_distribution(100, 50, 1.0 / 6.0)
print 'thinkstats way', binomial_thinkstats(100, 50, 1.0 / 6.0)
