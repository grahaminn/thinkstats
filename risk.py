include Pmf

def ProbEarly(pmf):
    early_births = filter(lambda x: x[0] <= 37 , pmf.Items())
    earlyPmf = Pmf.MakePmfFromDict(dict(early_births))
    earlyPmf.Normalize()
    return earlyPmf

def ProbOnTime(pmf):
    on_time_births = filter(lambda x: x[0] >= 38 and x[0] <= 40 , pmf.Items())
    onTimePmf = Pmf.MakePmfFromDict(dict(on_time_births))
    onTimePmf.Normalize()
    return onTimePmf

def ProbLate(pmf):
    late_births = filter(lambda x: x[0] > 40 , pmf.Items())
    latePmf = Pmf.MakePmfFromDict(dict(late_births))
    latePmf.Normalize()
    return latePmf
