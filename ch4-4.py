import Cdf
import myplot
import Pmf
import random

values = map (lambda(x):100*random.paretovariate(1/1.7), range(600))


pmf = Pmf.MakePmfFromList(values)
cdf = Cdf.MakeCdfFromList(values)

myplot.Cdf(cdf)

myplot.Show()
