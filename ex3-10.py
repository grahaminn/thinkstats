import Cdf
import myplot
import Pmf
import random


random_numbers = []
for i in range(1000):
    random_numbers.append(random.random())

pmf = Pmf.MakePmfFromList(random_numbers)
cdf = Cdf.MakeCdfFromList(random_numbers)

myplot.Pmf(pmf)
myplot.show(title='PMF of random numbers 0-1',xlabel='value',ylabel='probability')

myplot.Cdf(cdf)
myplot.show(title='CDF of random numbers 0-1',xlabel='value', ylabel='probability')
