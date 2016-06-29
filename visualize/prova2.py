import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)

x2 = np.linspace(0, 10, 1000)
y2 = np.cos(x2)
# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x[:10], y[:10], 'r-') # Returns a tuple of line objects, thus the comma
line2, = ax.plot(x2[:10], y2[:10], 'g-') # Returns a tuple of line objects, thus the comma

for i in range(800):
    line1.set_ydata(y[i:i+10])
    line2.set_ydata(y2[i:i+10])
    fig.canvas.draw()
    plt.pause(0.25)
