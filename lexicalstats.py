#!/usr/bin/python

from collections import defaultdict
import getopt
import sys

worddict = defaultdict(int)

def scan_line(line):
    line = line.strip(string.punctuation)
    line = line.lower()
    for word in line.split():
         worddict[word] += 1


  
