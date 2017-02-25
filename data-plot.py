#!/usr/bin/env python

"""
data-plot.py: plot the average of every trace file
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


datasfile = open('data.txt', 'r')
avglist = [];
for line in datasfile.readlines():
	avg = line.split("  ")[1]
	avglist.append(int(avg))	


plt.plot(avglist, 'ro-')
plt.title(" Average number of requests distribution " )
plt.ylabel('Number of requests')
plt.ylim([0,500000])
plt.xlabel('Time (hr)')
plt.show()
