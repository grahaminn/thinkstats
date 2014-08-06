import Cdf
import Pmf

import myplot
import random

def paretovariate(a, xm):
  return xm * random.paretovariate(a)

values = map(lambda(x):random.expovariate(1.0/5.0), range(44))

cdf = Cdf.MakeCdfFromList(values)
pmf = Pmf.MakePmfFromList(values)

myplot.Pmf(pmf)
# myplot.Cdf(cdf, complement=True, xscale='log', yscale='log')
myplot.Show(title='pareto distribution log plot', xlabel='log value', ylabel='log complementary CDF')


