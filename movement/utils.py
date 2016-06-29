import numpy as np
from constants import *


def sin_deg(v):
    return np.sin(v * np.pi / 180.)


def cos_deg(v):
    return np.cos(v * np.pi / 180.)


def opposite(direction):
    for pair in OPPOSITE_DIRECTIONS:
        if direction == pair[0]:
            return pair[1]
        elif direction == pair[1]:
            return pair[0]
    return None


def convert_vector_to_direction(vec):
    f = lambda x: [x[0], np.dot(x[1], vec)]  # returns ['n', a . vec]
    r = map(f, DIRECTION_VECTORS.iteritems())
    r = np.array(r)
    return r[np.argmax(r[:, 1])][0]


def not_none_nor_empty(vec):
    if vec is None:
        return False
    if len(vec) == 0:
        return False
    for i in vec:
        if i is None:
            return False
    return True


class ptr:
    def __init__(self, obj):
        self.obj = obj

    def get(self):
        return self.obj

    def set(self, obj):
        self.obj = obj