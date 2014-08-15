import math
import myplot
import numpy
import relay

results = relay.ReadResults()
speeds = relay.GetSpeeds(results)
xs = sorted(numpy.random.normal(0, 1, len(speeds)))
ys = sorted(speeds)
myplot.Plot(xs, ys)
myplot.Show(title="Normal Plot for Running Speeds")


