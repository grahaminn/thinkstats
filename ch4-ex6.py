import Cdf
import Pmf

import myplot
import random

values = map(lambda(x):random.weibullvariate(0.5, 1), range(1000))

cdf = Cdf.MakeCdfFromList(values)
pmf = Pmf.MakePmfFromList(values)

#myplot.Pmf(pmf)
myplot.Cdf(cdf, complement=True)
myplot.Show(title='weibull distribution log plot', yscale='log', xlabel='log value', ylabel='log complementary CDF')


