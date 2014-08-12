import Cdf
import myplot
import random

values = map(lambda(x):random.expovariate(1/32.6), range(44))
print values
cdf = Cdf.MakeCdfFromList(values)

myplot.Cdf(cdf, transform='exponential')
myplot.Show(title='exponential distribution log plot', yscale='log', xlabel='value', ylabel='complementary CDF')


