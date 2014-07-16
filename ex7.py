import descriptive
import Pmf

def filtered_pmf(filter_function, pmf):
    filtered_items = filter(filter_function, pmf.Items())
    filtered_pmf = Pmf.MakePmfFromDict(dict(filtered_items))
    filtered_pmf.Normalize()
    return filtered_pmf

def prob_birth_in_next_week(week, pmf):
    new_pmf = filtered_pmf(lambda x: x[0] > week, pmf)
    return new_pmf.Prob(week + 1)

pool, firsts, others = descriptive.MakeTables()
later_first_births = prob_birth_in_next_week(38, firsts.pmf)
later_other_births = prob_birth_in_next_week(38, others.pmf)

print 'chance of first birth in week 39 %f' % later_first_births
print 'chance of other birth in week 39 %f' % later_other_births 

