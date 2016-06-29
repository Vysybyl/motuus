import matplotlib.pyplot as plt
from constants import COLORS
from random import choice
import numpy as np


class Graph2D(object):
    def __init__(self, sample_size=5):
        self.lines = {}
        self.sample_size = sample_size

        plt.ion()
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(111)
        self.__ax.set_xlim([-10, 10])
        self.__ax.set_ylim([-10, 10])

    def add_line(self, key):
        col = self.__pick_random_color()
        self.lines[key], = self.__ax.plot(np.linspace(0,1,self.sample_size), np.linspace(0,1,self.sample_size), col)  # Returns a tuple of line objects, thus the comma

    def update_line(self, key, x, y):
            times = self.__last_bit(x)
            times = times - times[-1]
            self.lines[key].set_xdata(times)
            self.lines[key].set_ydata(self.__last_bit(y))

    def plot(self):
        self.__fig.canvas.draw()

    def __pick_random_color(self):
        return choice(COLORS.values())

    def __last_bit(self, vec):
        if len(vec) < self.sample_size:  # must be at least one
            return np.linspace(0, 1, self.sample_size)
        return vec[-self.sample_size:]  # last l values
