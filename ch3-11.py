import Cdf

def Median(cdf):
   return cdf.Value(0.5)

def Interquartile(cdf):
   return cdf.Value(0.75) - cdf.Value(0.25)

cdf = Cdf.MakeCdfFromList([1, 2, 3, 4, 5, 6])

print 'median %f:' % Median(cdf)
print 'interquartile %f:' % Interquartile(cdf)
