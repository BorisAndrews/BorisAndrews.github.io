'''
Imports
'''
import numpy as np
import matplotlib.pyplot as plt



'''
Parameters
'''
refractive_indices = [1, 2, 3]
init_angle = np.pi/4



'''
Compute angles
'''
angles = [init_angle]
for index, refractive_index in enumerate(refractive_indices[1:]):
    angles += [np.arcsin(refractive_indices[index]/refractive_index * np.sin(angles[-1]))]



'''
Compute positions
'''
ys = [0]
for angle in angles:
    ys += [ys[-1] + np.tan(angle)]



'''
Plot
'''
plt.plot(np.arange(len(refractive_indices)+1), ys)
plt.show()
