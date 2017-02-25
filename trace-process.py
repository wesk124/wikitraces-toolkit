#!/usr/bin/env python

"""
data-processing.py: process wikitraces file and store them into 
single data files
"""


"""
__author__	= "Sheng Wei"
__copyright__ = "Copyright 2016"
__credits__ = "Sheng Wei"
__email__ = "shengw12@vt.edu"
"""

import sys
import datetime
import matplotlib.pyplot as plt
from math import sqrt

def get_ts(line):
	ts_str = line.split(" ")[1]
	ts_int = int(float(ts_str))
	return ts_int

def standard_deviation(lst, population=True):
	"""Calculates the standard deviation for a list of numbers."""
	num_items = len(lst)
	mean = sum(lst) / num_items
	differences = [x - mean for x in lst]
	sq_differences = [d ** 2 for d in differences]
	ssd = sum(sq_differences)
	
	if population is True:
		print('This is POPULATION standard deviation.')
		variance = ssd / num_items
	else:
		print('This is SAMPLE standard deviation.')
		variance = ssd / (num_items - 1)
	sd = sqrt(variance)
	datafile = open('data.txt', 'ab')
	datafile.write(sys.argv[2])
	datafile.write("  ")
	datafile.write(str(mean))
	datafile.write("  ")
	datafile.write(str(sd) + '\n')
	
	print('The mean of is {}.'.format(mean))
	print('The standard deviation is {}.'.format(sd))
	print('--------------------------')

if (len(sys.argv) != 7 or sys.argv[1] != "-f" or sys.argv[3] != "-m"):
	print "<Usage> trace-process.py -f datafile -m time-interval( 1-60 minute ) -p <1/0>"
	sys.exit(0)	
else:
	time_int_num = int(sys.argv[4])
	fr = open(sys.argv[2], 'r')
	prev_line = fr.readline()
	counter = 0
	counter_list = []
	prev_ts = get_ts(prev_line)	
	#print prev_ts
	while 1:
		curr_line = fr.readline() #read each line of data file
		if curr_line == "":
			break
		curr_ts = get_ts(curr_line)
		counter = counter + 1
		#print curr_ts
		if curr_ts - prev_ts >= 60 * time_int_num:
#			print counter
			counter_list.append(counter)	
			prev_line = fr.readline()
			prev_ts = get_ts(prev_line)
			counter = 0 #reset counter

standard_deviation(counter_list);

if (sys.argv[6] == "1"):
	plt.plot(counter_list)
	plt.title(sys.argv[2] + " Time vs. Number of requests " )
	plt.ylabel('Number of requests')
	plt.xlabel('Time (' + str(time_int_num) + " min)")
	plt.show()
else:
	print("Non-plot mode")

		
