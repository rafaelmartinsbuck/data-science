#!/usr/bin/python

import sys

header = False
for line in sys.stdin:
# your code here
	if not header:
		header = True
		continue
	data = line.split(',')
	if len(data) == 22:
		unit = data[1]
		entries_hourly = data[6]
		print '{0}\t{1}'.format(unit, entries_hourly)


