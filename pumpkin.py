import csv
import math
import thinkstats

pumpkins = []
with open('pumpkins.csv', 'rU') as csvfile:
    pumpkinreader = csv.reader(csvfile, dialect='excel')
    for pumpkin_row in pumpkinreader:
        pumpkin = pumpkin_row[0]
        if pumpkin.isdigit():
            pumpkins.append(float(pumpkin))
    print pumpkins
    mean, variance = thinkstats.MeanVar(pumpkins)
    print 'mean=%s, variance=%s' % (mean, variance)
    print 'std deviation=', math.sqrt(variance)
    
