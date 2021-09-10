import numpy as np
import matplotlib.pyplot as plt

#Data for plotting
x = np.arange(0, 2*np.pi, .1)
y1 = np.sin(x)
y2 = np.cos(x)

#Plot
plt.plot(x,y1,x,y2)
plt.show()