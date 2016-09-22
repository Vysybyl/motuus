# External modules import
import numpy as np


# Project modules import
from motuus.movement.constants import *
from motuus.movement.quaternion import Quat

"""Includes utility functions used to process sensor data

"""

def sin_deg(v):
    """Computes the sine of v

    :param v: angle in degrees
    :return: sin(v)
    """
    return np.sin(v * np.pi / 180.)


def cos_deg(v):
    """Computes the cosine of v

    :param v: angle in degrees
    :return: cos(v)
    """
    return np.cos(v * np.pi / 180.)


def opposite(direction):
    """Return the opposite direction

    Ex. opposite(LEFT) => RIGHT
    :param direction: one of the accepted DIRECTIONS
    :return: a DIRECTION (str)
    """
    for pair in OPPOSITE_DIRECTIONS:
        if direction == pair[0]:
            return pair[1]
        elif direction == pair[1]:
            return pair[0]
    return None


def convert_vector_to_direction(vec):
    """Converts a vector to the closest DIRECTION

    Ex. convert_vector_to_direction(numpy.array([0, 1, 0])) => NORTH
    :param vec: a 1 x 3 numpy array
    :return: a DIRECTION (str)
    """
    f = lambda x: [x[0], np.dot(x[1], vec)]  # returns ['n', a . vec]
    r = map(f, DIRECTION_VECTORS.iteritems())
    r = np.array(r)
    return r[np.argmax(r[:, 1])][0]


def not_none_nor_empty(vec):
    """Verifies if the argument is None or empty. To be used on lists or numpy arrays

    If vec contains a None entry, the function returns False
    Ex. not_none_nor_empty([1, 'abc', None, 23.4]) => False
    :param vec:
    :return: bool
    """
    if vec is None:
        return False
    if len(vec) == 0:
        return False
    for i in vec:
        if i is None:
            return False
    return True


def build_attitude_q(alpha, beta, gamma):
    """Builds a panda3d.core.Quat attitude quaternion based on the device orientation described by the parameters

    Parameters are based on the javascript library parameters with the same names. Parameters measure angle in degrees
    :param alpha: Rotation of the device around the z axis (pointing outside of the screen).
    :param beta: Rotation of the device around the x axis (pointing left to right).
    :param gamma: Rotation of the device around the y axis (pointing bottom to top).
    :return: a panda3d.core.Quat quaternion. It can be used directly to orientate 3D objects or define transformation
    with the setQuat method
    """
    a = Quat(cos_deg(alpha / 2.0), 0, 0, sin_deg(alpha / 2.0))
    b = Quat(cos_deg(beta / 2.0), sin_deg(beta / 2.0), 0, 0) * a
    c = Quat(cos_deg(gamma/2.0), 0, sin_deg(gamma/2.0), 0) * b
    return c

def build_attitude_q_v(vec):
    """Builds a panda3d.core.Quat attitude quaternion based on the device orientation described by the argument vec

    :param vec: a 1 x 3 numpy array or a list (Any indexed object with length > 2 will work) containing orientation
     angles in degrees.
    :return: a panda3d.core.Quat quaternion. It can be used directly to orientate 3D objects or define transformation
    with the setQuat method
    """
    return build_attitude_q(vec[0], vec[1], vec[2])


def build_q_v(vec):
    """Builds a panda3d.core.Quat quaternion representation of a unit vector (versor), to be rotated using quaternion
    multiplication

    :param vec: a unit vector as a 1 x 3 numpy array or a list (Any indexed object with length > 2 will work)
    :return: a panda3d.core.Quat quaternion.
    """
    return build_q(vec[0], vec[1], vec[2])


def build_q(x, y, z):
    """Builds a panda3d.core.Quat quaternion representation of a unit vector (versor), to be rotated using quaternion
    multiplication

    :param x: x-component
    :param y: y-component
    :param z: z-component
    :return: a panda3d.core.Quat quaternion.
    """
    return Quat(0, x, y, z)


def build_v(q):
    x = np.array([q.b, q.c, q.d])  # i, j, k
    x = x / np.sqrt(x.dot(x))
    return x