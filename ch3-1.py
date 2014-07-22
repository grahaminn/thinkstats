import Pmf

pmf = Pmf.MakePmfFromDict({7:8,12:8,17:14,22:4,27:6,32:12,37:8,42:3,47:2})
print "Dean's pmf mean:%f" % pmf.Mean()

print "average class size per student: %f" % (((7 * 8) + (8 * 12) + (14 * 17) + (22 * 4) + (6 * 27) + (12 * 32) + (8 * 37) + (3 * 42) + (2 * 47)) / 65)
