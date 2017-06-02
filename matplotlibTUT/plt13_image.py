# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 13 - image
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
"""

import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""
fig = plt.figure(1, figsize=(6, 4))
plt.suptitle("effect of interpolation and cmap")


## interpolation: None or nearest have same effect to me
fig.add_subplot(2,5,1)
plt.imshow(a, interpolation=None, cmap='bone', origin='lower')
plt.title("None")
fig.add_subplot(2,5,2)
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
plt.title("nearest")
fig.add_subplot(2,5,3)
plt.imshow(a, interpolation='bilinear', cmap='bone', origin='lower')
plt.title("bilinear")
fig.add_subplot(2,5,4)
plt.imshow(a, interpolation='bicubic', cmap='bone', origin='lower')
plt.title("bicubic")
fig.add_subplot(2,5,5)
plt.imshow(a, interpolation='spline16', cmap='bone', origin='lower')
plt.title("spline16")

# options of cmap params
# https://matplotlib.org/examples/color/colormaps_reference.html
# https://matplotlib.org/users/colormaps.html
# origin: lower = set (0,0) to lower left, upper = set (0,0) to upper left
fig.add_subplot(2,5,6)
plt.imshow(a, interpolation=None, cmap='rainbow', origin='lower')
plt.title("rainbow")
fig.add_subplot(2,5,7)
plt.imshow(a, interpolation='nearest', cmap='binary', origin='lower')
plt.title("binary")
fig.add_subplot(2,5,8)
plt.imshow(a, interpolation='bilinear', cmap='cool', origin='lower')
plt.title("cool")
fig.add_subplot(2,5,9)
plt.imshow(a, interpolation='bicubic', cmap='GnBu', origin='lower')
plt.title("GnBu")
fig.add_subplot(2,5,10)
plt.imshow(a, interpolation='spline16', cmap='plasma', origin='lower')
plt.title("plasma")

# only apply to the last image, shrink the size of color bar
plt.colorbar(shrink=.52)

plt.xticks(())
plt.yticks(())
plt.show()
