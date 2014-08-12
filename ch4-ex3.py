import Cdf
import Pmf

import myplot
import random

def paretovariate(a, xm):
  return xm * random.paretovariate(a)

values = map(lambda(x):paretovariate(1,1), range(44))

cdf = Cdf.MakeCdfFromList(values)
pmf = Pmf.MakePmfFromList(values)

#myplot.Pmf(pmf)
myplot.Cdf(cdf, complement=True)
myplot.Show(title='pareto distribution log plot', xscale='log', yscale='log', xlabel='log value', ylabel='log complementary CDF')


