from constants import *
from random import choice
import numpy as np

FAKE_READINGS = dict()

FAKE_READINGS[ACCELEROMETER] = [np.array([2.1319, 1.1925, -0.8381]),
                                np.array([1.118, 0.1663, 1.1952]),
                                np.array([-0.3436, 0.0292, -1.218]),
                                np.array([2.4592, 1.787, -2.4731])]

FAKE_READINGS[GYROSCOPE] = [np.array([60.1376, 121.6746, -10.7275]),
                            np.array([-165.5525, 143.4781, -166.7227]),
                            np.array([-135.1816, 146.327, 9.6142]),
                            np.array([-89.0852, 19.3541, -106.8763])]

FAKE_READINGS[ORIENTATION] = [np.array([293.61, 14.38, 35.89]),
                              np.array([255.28, -93.85, -42.43]),
                              np.array([154.54, 120.8, -61.15]),
                              np.array([102.61, 155.39, 49.19])]

FAKE_READINGS[GRAVITY] = [np.array([0.6629, 0.3338, 0.0031]),
                          np.array([0.3662, -0.0456, 0.5880]),
                          np.array([0.4343, -0.0539, -0.5117]),
                          np.array([-0.3629, -0.2917, -0.3452])]


def build_random_input():
    inp = dict()
    inp[ACCELEROMETER] = choice(FAKE_READINGS[ACCELEROMETER])
    inp[GYROSCOPE] = choice(FAKE_READINGS[GYROSCOPE])
    inp[ORIENTATION] = choice(FAKE_READINGS[ORIENTATION])
    inp[GRAVITY] = choice(FAKE_READINGS[GRAVITY])
    return inp
