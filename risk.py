import descriptive
import Pmf

def FilteredCumulativeProbability(filter_func, pmf):
    filtered_items = filter(filter_func, pmf.Items())
    filtered_probabilities = map(lambda x:x[1], filtered_items)
    return sum(filtered_probabilities) 

def ProbEarly(pmf):
    return FilteredCumulativeProbability(lambda x: x[0] <= 37, pmf)

def ProbOnTime(pmf):
    return FilteredCumulativeProbability(lambda x: x[0] >= 38 and x[0] <= 40 , pmf)

def ProbLate(pmf):
    return FilteredCumulativeProbability(lambda x: x[0] > 40 , pmf)

def ComputeRelativeRisk(pmf_first, pmf_other):
    print 'Prob of being early for first births %f, for others %f' % (ProbEarly(pmf_first),ProbEarly(pmf_other))
    print 'Prob of being on time for first births %f, for other %f' % (ProbOnTime(pmf_first),ProbOnTime(pmf_other))
    print 'Prob of being late for first births %f, for others %f' % (ProbLate(pmf_first), ProbLate(pmf_other))

def main():
    pool, firsts, others = descriptive.MakeTables()
    ComputeRelativeRisk(firsts.pmf, others.pmf)

if __name__ == "__main__":
    main()
