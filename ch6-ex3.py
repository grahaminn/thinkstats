#!/usr/bin/python

import Cdf
import irs
import Pmf

hist, pmf, cdf = irs.GetIncomeDist()

print 'mean:',cdf.Mean()
print 'median:',cdf.Percentile(50)
print 'skewness:',pmf.Skewness()
print 'pearson coefficient',3 * (pmf.Mean() - cdf.Percentile(50)) / (pmf.Var() ** 0.5)

