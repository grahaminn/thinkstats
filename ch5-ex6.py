import math
import myplot
import numpy
import Pmf

def mean_dev_for_sample(n):
   sample = map(lambda(x):sorted(numpy.random.normal(loc=950, scale=50, size=n)
, reverse=True)[0], range(1000))
   return numpy.mean(sample), numpy.std(sample)

       
xs = range(1, 12)
ys = map(lambda(x):mean_dev_for_sample(x), xs)

for y in ys:
    print y
 
myplot.Plot(xs, map(lambda(x):x[0],ys))
myplot.Show(title='mean vs n')  

#n=4 seems to be the threshold

pmf = Pmf.MakePmfFromList(map(lambda(x):math.floor(sorted(numpy.random.normal(loc=950, scale=50, size=4), reverse=True)[0]), range(1000)))

mean, std = mean_dev_for_sample(4)

pmf2 = Pmf.MakePmfFromList(map(lambda(x):math.floor(x), numpy.random.normal(mean, std, 1000)))

myplot.Pmf(pmf)
myplot.Pmf(pmf2)
myplot.Show(title="Test for skew on rigged sample")

#something's wrong here, can't see the difference
