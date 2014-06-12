import operator
import Pmf

def Mode(hist):
    return Allmodes(hist)[0][1]

def Allmodes(hist):
    return sorted(hist.Items(), key=operator.itemgetter(1), reverse=True)

print Mode(Pmf.MakeHistFromList([1, 2, 2, 3, 3, 3, 4, 4, 5]))

print Allmodes(Pmf.MakeHistFromList([1, 2, 2, 3, 3, 3, 4, 4, 5]))
