#!/usr/bin/python

import sys

entriesTotal = 0
oldUnit = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
    	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue
	
	thisUnit, thisEntries = data_mapped
	
	if oldUnit and (oldUnit != thisUnit):
		print oldUnit, "\t", entriesTotal
		oldUnit = thisUnit
		entriesTotal = 0
    	
	oldUnit = thisUnit
    	entriesTotal += float(thisEntries)

if oldUnit != None: