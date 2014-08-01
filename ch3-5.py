import relay
import Cdf
import Pmf
import myplot

speeds = relay.GetSpeeds(relay.ReadResults())

pmf = Pmf.MakePmfFromList(speeds)
cdf = Cdf.MakeCdfFromList(speeds)

myplot.Pmf(pmf)
myplot.Cdf(cdf)

myplot.Show(title='PMF vs CDF of running speeds', xlabel='speed (mph)', ylabel='probability')
