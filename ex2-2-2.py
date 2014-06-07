import csv
import math
import survey
import thinkstats

table = survey.Pregnancies()
table.ReadRecords()

first_births = []
other_births = []

for record in table.records:
    if record.outcome != 1:
        continue
   
    if record.birthord == 1:
        first_births.append(record.prglength)
    else:
        other_births.append(record.prglength)

first_births_mean, first_births_variance = thinkstats.MeanVar(first_births)
other_births_mean, other_births_variance = thinkstats.MeanVar(other_births)

print 'mean of first birth gestation=', first_births_mean
print 'std deviation of first birth gestation=', math.sqrt(first_births_variance)
print 'mean of other birth gestation=', other_births_mean
print 'std deviation of other birth gestation=', math.sqrt(other_births_variance)

    
