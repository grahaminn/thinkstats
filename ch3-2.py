import Pmf

def BiasPmf(pmf, observer_speed):
    new_pmf = pmf.Copy()
    map(lambda(x):new_pmf.Mult(x, abs(observer_speed-x)), new_pmf.Values())
    new_pmf.Normalize()
    return new_pmf


    
