import Cdf
from collections import defaultdict
import myplot
import numpy
import operator
import Pmf

cohort_dict = defaultdict(int)

for year in range(10):
    for cohort in range(100):
        for person in range(100):
            if numpy.random.randint(1000) == 1:
                cohort_dict[cohort] += 1

pmf = Pmf.MakePmfFromList(cohort_dict.values())
cdf = Cdf.MakeCdfFromList(cohort_dict.values())

xs = sorted(pmf.Values())
ys = map(lambda(x):0.05, xs)
myplot.Pmf(pmf)
myplot.Plot(xs, ys)
myplot.Show(title="Distribution of diagnoses")

#graph indicates any cohort with 4 or more cases is statistically significant

#a statistically significant cluster is one with a 5% chance of occurring. in 3) we're therefore being asked 
#what are the odds that at least one of the 100 cohorts generates a 5% event? 

print 'odds of at least one cohort in 100 generating a 5% event', 1 - (0.95 ** 100)
print 'odds of at least one cohort in 100 generating a 1% event', 1 - (0.99 ** 100)

print 'There are 91x91 10x10 blocks in a 100x100 grid. the chance of at least one having a 5% event is 1 - (0.95^(91*91))=', (1 - (0.95 ** (91 ** 2)))

# Applying the same logic but with 21 times more opportunities basically guarantees there will be a cluster.


