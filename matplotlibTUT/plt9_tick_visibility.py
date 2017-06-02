# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 9 - tick_visibility
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10, alpha=0.7) # alpha, help tick labels seen through
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# https://youtu.be/zj-tXbuFY_4?list=PLXO45tsB95cKiBRXYqNNCw8AUo6tYen3l&t=93
# label.__class__
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)  # facecolor= 'white' is better
    label.set_bbox(dict(facecolor='yellow', edgecolor='None', alpha=0.9))
plt.show()
