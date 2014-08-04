import Cdf
import myplot
import random

values = map(lambda(x):random.expovariate(1/32.6), range(44))
print values
cdf = Cdf.MakeCdfFromList(values)

myplot.Cdf(cdf, complement=True, xscale='linear', yscale='log')
myplot.Show(title='exponential distribution log plot', xlabel='value', ylabel='complementary CDF')


