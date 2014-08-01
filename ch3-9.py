import Cdf
import myplot
import random
import survey

def SampleCdf(cdf, n):
    sample = []
    for i in range(n):
         value = cdf.Value(random.random())
         sample.append(value)
    return Cdf.MakeCdfFromList(sample)

table = survey.Pregnancies()
table.ReadRecords()

def ExtractBirthWeights(recs):
    wgts = []
    for rec in recs:
        try:
           wgts.append(float(rec.birthwgt_lb))
        except ValueError:
           pass
    return wgts

birthCdf = Cdf.MakeCdfFromList(ExtractBirthWeights(table.records))

# myplot.Cdf(birthCdf)
myplot.Cdf(SampleCdf(birthCdf, 3))
myplot.Show(title='Sample vs Orig CDF', xlabel='Birth Weight (lbs)', ylabel='probability')
