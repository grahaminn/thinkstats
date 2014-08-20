import Cdf
import math
import myplot
import numpy
import brfss

resp = brfss.Respondents()
resp.ReadRecords('.')
filtered_records = filter(lambda(x):x.wtkg2 != 'NA', resp.records)

xs = sorted(numpy.random.normal(0, 1, len(filtered_records)))
ys = sorted(map(lambda(y):y.wtkg2, filtered_records))
logys = sorted(map(lambda(y):math.log10(y.wtkg2), filtered_records)) 

myplot.Plot(xs, ys)
myplot.Show(title="Normal plot for weight")

myplot.Plot(xs,logys)
myplot.Show(title="Normal plot for log(weight)")

