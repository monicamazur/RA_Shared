import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

a = [1,2,3,4,5]
print(np.average(a))

print(plt.plot(a))
plt.show()


class Generator(object):
    def __init__(self, params, shapes, n_steps):
        self.params = params
        self.shapes = shapes
        self.curve = calc_curve(n_steps)