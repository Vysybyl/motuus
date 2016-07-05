# External modules import
import matplotlib.pyplot as plt
from random import choice
import numpy as np

# Project modules import
from constants import COLORS

class Graph2D(object):
    """Used to plot 2D objects (namely time series) as lines

    :param sample_size: optional argument, determines the numbers of data points considered for the plot.
    Default value is 10.
    """
    def __init__(self, sample_size=10):
        self.lines = {}
        self.sample_size = sample_size

        plt.ion()
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(111)
        self.__ax.set_xlim([-2, 2])
        self.__ax.set_ylim([-3, 3])

    def add_line(self, key):
        """Create a new line object used to plot a time series. The key must be unique.

        The line will be plotted with a random COLOR
        """
        col = self.__pick_random_color()
        self.lines[key], = self.__ax.plot(np.linspace(0,1,self.sample_size), np.linspace(0,1,self.sample_size), col)  # Returns a tuple of line objects, thus the comma

    def update_line(self, key, x, y):
        """Replot the specified line

        This method must be called after the line is created using add_line
        :param key: The line unique identifier, as specified in the add_line method
        :param x: a numpy.array of at least sample_size elements. sample_size is specified when the class is
        created. Shorter samples will be ignored (a diagonal line will be plotted instead); longer samples will be
        truncated:
            update_line("speed", range(0, 100), range(0, 15) )
        is the same as:
            update_line("speed", range(90, 100), range(5, 15) )
        :param y: a numpy.array of at least sample_size elements. Same dimension rules as per parameter x apply
        """
        times = self.__last_bit(x)
        times = times - times[-1]
        bits = self.__last_bit(y)
        self.lines[key].set_xdata(times)
        self.lines[key].set_ydata(bits)

    def plot(self):
        """(Re)Draw all lines

        Call if to repaint all lines after you have updated them with the update_line method
        """
        self.__fig.canvas.draw()

    def __pick_random_color(self):
        return choice(COLORS.values())

    def __last_bit(self, vec):
        if len(vec) < self.sample_size:  # must be at least one
            return np.linspace(0, 1, self.sample_size)
        return vec[-self.sample_size:]  # last l values
