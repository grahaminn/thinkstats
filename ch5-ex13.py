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

class Grid:
    def __init__(self, width, height):
        self.diagnosed = [[False for y in xrange(height)] for x in xrange(width)]

    def update(self):
        for column in range(len(self.diagnosed)):
            for row in range(len(self.diagnosed[column])):
                if numpy.random.randint(1000) == 1:
                    self.diagnosed[column][row] = True
   
    def update_over_time(self, time):
        for t in range(time):
            self.update()  
    
    def check_sub_grid_for_cluster(self, cluster_threshold, xorigin, yorigin, width, height):
        diagnosis_count = 0
        cluster = False
        for x in range (xorigin, xorigin + width):
            for y in range(yorigin, yorigin + height):
                if self.diagnosed[x][y] is True:
                    diagnosis_count += 1
                    if diagnosis_count == cluster_threshold:
                        cluster = True
                        break
            if cluster is True:
                break
        return cluster       

    def check_sub_grids_for_clusters(self, cluster_threshold, width, height):
        for x in range(len(self.diagnosed) - width):
            for y in range(len(self.diagnosed[x]) - height):
                if self.check_sub_grid_for_cluster(cluster_threshold, x, y, width, height) is True:
                    return True
        return False
                      

cluster_yield = 0.0
for experiment in range(1000):
    grid = Grid(100, 100)
    grid.update_over_time(10)
    if grid.check_sub_grids_for_clusters(4, 10, 10) is True:
        cluster_yield += 1.0

print 'clusters found at 5%:', (cluster_yield / 10.0)

cluster_yield = 0.0
for experiment in range(1000):
    grid = Grid(100, 100)
    grid.update_over_time(10)
    if grid.check_sub_grids_for_clusters(5, 10, 10) is True:
        cluster_yield += 1.0

print 'clusters found at 1%:', (cluster_yield / 10.0)

cluster_yield = 0.0
for experiment in range(1000):
    grid = Grid(100, 100)
    grid.update_over_time(30)
    if grid.check_sub_grids_for_clusters(4, 10, 10) is True:
        cluster_yield += 1.0

print 'clusters found at 5% over 30 years:', (cluster_yield / 10.0)
