#!/usr/bin/python

def probabilityOfUsageOnPositiveTest(actual_rate, sensitivity, specificity):
    return (actual_rate * sensitivity) / ((actual_rate * sensitivity) + ((1 - actual_rate) * (1 - specificity)))

print "probability of usage on positive test when real rate is 5% ", probabilityOfUsageOnPositiveTest(0.05, 0.6, 0.99)

print "probability of usage on positive test when real rate is 1% ", probabilityOfUsageOnPositiveTest(0.01, 0.6, 0.99)
