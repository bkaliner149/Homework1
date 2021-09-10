import numpy as np
import matplotlib as plt

#Data for plotting
x = (0, 2*np.pi, .01)
y1 = np.sin
y2 = np.cos

#Plot
plt.plot(x, y1, y2)