import Cdf
import Pmf
import survey

def Median(sample):
    cdf = Cdf.MakeCdfFromList(sample)
    return cdf.Percentile(50)

def mk(sample, k):
    mu = Pmf.MakePmfFromList(sample).Mean()
    return sum(map(lambda (x):((x - mu) ** k), sample)) / len(sample)

def Skewness(sample):
    return mk(sample, 3) / (mk(sample, 2) ** 1.5)

def PearsonSkewness(sample):
    pmf = Pmf.MakePmfFromList(sample)
    return 3 * (pmf.Mean() - Median(sample)) / (pmf.Var() ** 0.5)

table = survey.Pregnancies()
table.ReadRecords()

def FilterNonFloat(x):
    try:
        float(x)
        return True
    except ValueError: 
        return False

birth_weights = map(lambda(x):x.birthwgt_lb, filter(lambda (x):FilterNonFloat(x.birthwgt_lb), table.records))

pregnancy_lengths = map(lambda(x):x.prglength, filter(lambda (x):FilterNonFloat(x.prglength), table.records))

print 'birth weights Skewness:',Skewness(birth_weights),' PearsonSkewnewss:',PearsonSkewness(birth_weights)

print 'pregnancy lengths Skewness:',Skewness(pregnancy_lengths),' PearsonSkewness:',PearsonSkewness(pregnancy_lengths) 
