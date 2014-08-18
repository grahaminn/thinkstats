import Cdf
import populations
import math
import myplot
import numpy
import Pmf

pops = populations.ReadData()
bucketed_pops = map(lambda(x):50*math.floor(x/50.0),pops)

pmf = Pmf.MakePmfFromList(bucketed_pops)
cdf = Cdf.MakeCdfFromPmf(pmf)

myplot.Pmf(pmf)
myplot.Show(title="Pmf of populations", xscale='log')

myplot.Cdf(cdf)
myplot.Show(title="Cdf of populations", inverse=True, xscale='log')

xs = sorted(numpy.random.normal(0, 1, len(pops)))
ys = sorted(bucketed_pops)

myplot.Plot(xs, ys)
myplot.Show(title="Normal plot for populations")

ys2 = sorted(map(lambda(y):math.log10(y+1),bucketed_pops))

myplot.Plot(xs, ys2)
myplot.Show(title="LogNormal plot for populations") 

#it looks more like a lognormal, but with a hard lower bound (as expected)
