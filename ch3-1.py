import Pmf

class_dict = {7: 8, 12: 8, 17: 14, 22: 4, 27: 6, 32: 12, 37: 8, 42: 3, 47: 2}


pmf = Pmf.MakePmfFromDict(class_dict)
print "Dean's pmf mean:%f" % pmf.Mean()

total_students = 0
total_classes = 0
map(lambda (size):pmf.Mult(size, size), pmf.Values()) 
pmf.Normalize()

print "average perceived class size per student: %f" % pmf.Mean()

# the sample can be unbiased by mapping lambda(size):pmf.Mult(size,1/size) over it
