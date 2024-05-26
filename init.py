"""This is a test on jupyter notebook sending cluster plots to qtconsole."""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
sin_x = np.sin(x)
cos_x = np.cos(x)

plt.scatter(x, sin_x)
plt.scatter(x, cos_x)
plt.show()

