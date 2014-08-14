import Cdf
import erf
import myplot
import Pmf
import survey

table = survey.Pregnancies()
table.ReadRecords()

live_birth_terms = []

for record in table.records:
    if record.outcome != 1:
        continue
    
    live_birth_terms.append(record.prglength)

cdf = Cdf.MakeCdfFromList(live_birth_terms)
myplot.Cdf(cdf)

myplot.Show(title="distribution of live birth pregnancy lengths")

pmf = Pmf.MakePmfFromList(live_birth_terms)
mean = pmf.Mean()
stddev = (pmf.Var() ** 0.5)
print "mean = ", mean
print "std dev = ", stddev

xs = range(0, 50)

myplot.Plot(xs, map(lambda(x):erf.NormalCdf(x, mu=mean, sigma=stddev), xs)) 

myplot.Show(title="CDF From normal distribution")

