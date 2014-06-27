import Pmf

def PmfMean(pmf):
    mean = 0.0
    for value, prob in pmf.Items():
        mean += (value * prob)
    return mean

def PmfVar(pmf):
    variance = 0.0
    mean = PmfMean(pmf)
    for value, prob in pmf.Items():
        variance += (prob * (value - mean) ** 2)
    return (variance ** 0.5)

pmf = Pmf.MakePmfFromList([1, 1, 2, 3])
print "mean=", PmfMean(pmf)
print "variance=", PmfVar(pmf)


