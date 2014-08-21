import numpy

woman_taller_than_man = 0

for i in range(1000):
    man_height = numpy.random.normal(178, 59.4)
    woman_height = numpy.random.normal(163, 52.8) 
    if woman_height > man_height:
        woman_taller_than_man += 1

print woman_taller_than_man
