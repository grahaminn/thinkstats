import Cdf
from collections import defaultdict
import myplot
import numpy
import operator
import Pmf

def run_cohort(people, years):
    number_infected = 0
    for year in range(years):
        for person in range(people):
            if numpy.random.randint(1000) == 1:
                number_infected += 1
    return number_infected

def monte_carlo_cohorts(people, cohorts, years, events_required, experiments):
    experimental_successes = 0.0
    for experiment in range(experiments):
        experiment_succeeded = False
        for cohort in range(cohorts):
            if run_cohort(people, years) >= events_required:
                experimental_successes += 1.0
                break

    return experimental_successes / experiments     

cohort_dict = defaultdict(int)

for cohort in range(100000):
    cohort_dict[cohort] += run_cohort(people=100, years=10) 

pmf = Pmf.MakePmfFromList(cohort_dict.values())
cdf = Cdf.MakeCdfFromList(cohort_dict.values())

xs = sorted(pmf.Values())
ys = map(lambda(x):0.05, xs)
ys2 = map(lambda(x):0.01, xs)
myplot.Pmf(pmf)
myplot.Plot(xs, ys)
myplot.Plot(xs, ys2)
myplot.Show(title="Distribution of diagnoses")

#graph indicates any cohort with 4 or more cases is statistically significant

#a statistically significant cluster is one with a 5% chance of occurring. in 3) we're therefore being asked 
#what are the odds that at least one of the 100 cohorts generates a 5% event? 

#analytically
print 'odds of at least one cohort in 100 generating a 5% event', 1 - (0.95 ** 100)

#by simulation
print  'odds of 5% event based on 1000 experiments = ', monte_carlo_cohorts(100, 100, 10, 4, 1000)

#by analysis
print 'odds of at least one cohort in 100 generating a 1% event', 1 - (0.99 ** 100)

#by simulation
print 'odds of a 1% event based on 1000 experiments =' , monte_carlo_cohorts(100, 100, 10, 5, 1000)

print 'There are 91x91 10x10 blocks in a 100x100 grid. the chance of at least one having a 5% event is 1 - (0.95^(91*91))=', (1 - (0.95 ** (91 ** 2)))

diagnosed = [[False for y in xrange(100)] for x in xrange(100)]

def update(grid):
    for x in grid:
        for y in x:
            if numpy.random.randint(1000) == 1:
                grid[x][y] = True



# Applying the same logic but with 21 times more opportunities basically guarantees there will be a cluster.


