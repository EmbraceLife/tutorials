import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# create a figure
plt.figure()

# plot 2 lines
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# doc plt.xlim; current: plt.xlim()
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set x, y axis label
plt.xlabel('I am x')
plt.ylabel('I am y')

# set x, y ticks labels
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
# doc plt.xticks
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

		   
plt.show()
