import Pmf

def RemainingLifetime(pmf, survival_age):
    remaining_ages = filter(lambda x: x[0] >= survival_age, pmf.Items())
    remainingPmf = Pmf.MakePmfFromDict(dict(remaining_ages))
    remainingPmf.Normalize()
    return remainingPmf

initialPmf = Pmf.MakePmfFromList([60, 70, 70, 80, 80, 80, 90])
print initialPmf.Items() 

remainingPmf = RemainingLifetime(initialPmf, 80)
print remainingPmf.Items()      
