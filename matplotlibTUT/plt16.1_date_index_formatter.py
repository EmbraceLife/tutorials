"""
When plotting daily data, a frequent request is to plot the data
ignoring skips, e.g., no extra spaces for weekends.  This is particularly
common in financial time series, when you may have data for M-F and
not Sat, Sun and you don't want gaps in the x axis.  The approach is
to simply use the integer index for the xdata and a custom tick
Formatter to get the appropriate date string for a given index.
"""

from __future__ import print_function
import numpy as np
from matplotlib.mlab import csv2rec
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.ticker import Formatter

# get data path for a csv data file
datafile = cbook.get_sample_data('msft.csv', asfileobj=False)
print('loading %s' % datafile)
# load csv into rec object
r = csv2rec(datafile)[-40:]


class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(np.round(x))
        if ind >= len(self.dates) or ind < 0:
            return ''

        return self.dates[ind].strftime(self.fmt)

# reverse the order of numpy array of date objects
formatter = MyFormatter(r.date[::-1])

fig, ax = plt.subplots()
# plot x-axis with date
ax.xaxis.set_major_formatter(formatter)
# r.close is np.array
ax.plot(np.arange(len(r)), r.close, 'o-')
# make sure date don't overlap for viewing
fig.autofmt_xdate()
plt.show()
