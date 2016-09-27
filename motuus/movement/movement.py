# External modules import
import numpy as np
import json

# Project modules import
from motuus.movement.utils import *
from motuus.movement.constants import *


class Movement(object):
    def __init__(self, input_dict=None):
        """Wrapper around each sensor data input.

        :param input_dict: dict or string containing a json object.
        The keys are defined by one of the DATA_TAGS.
        """
        if type(input_dict) is not dict:
            try:
                input_dict = json.loads(input_dict)
            except:
                input_dict = {}
        self.raw_data = input_dict
        """dict storing the original sensor data"""
        self.time = self.raw_data.get(TIMESTAMP)
        """Timestamp"""
        self.accelerometer = self.raw_data.get(ACCELEROMETER)
        """list storing acceleromenter data (from javascript 'accelerationIncludingGravity')"""
        self.gyroscope = self.raw_data.get(GYROSCOPE)
        """list storing gyroscope data (from javascript 'rotationRate')"""
        self.gravity = self.raw_data.get(GRAVITY)
        """list storing gravity data (if present, obtained by the accelerometer data)"""
        self.magnetometer = self.raw_data.get(MAGNETOMETER)
        """list storing magnetometer data"""
        self.orientation = self.raw_data.get(ORIENTATION)
        """list storing orientation data (from javascript 'deviceorientation')"""
        self.linear_acceleration = self.raw_data.get(LINEAR_ACCELERATION)
        """list storing orientation data (from javascript 'acceleration')"""

        self.right_pointer_vector = None
        """A numpy.array unit vector storing the device x axis (left to right) orientation"""
        self.top_pointer_vector = None
        """A numpy.array unit vector storing the device y axis (bottom to top) orientation"""
        self.front_pointer_vector = None
        """A numpy.array unit vector storing the device z axis (back to front) orientation"""

        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.front = None
        self.back = None

        if not_none_nor_empty(self.orientation):
            # This creates a pointer vector and an orientation (or attitude) quaternion storing respectively the device
            # direction along the y axis (bottom to top) and the device orientation
            q = build_attitude_q_v(self.orientation)
            self.attitude_quaternion = q
            q_con = q.conjugate()
            self.top_pointer_vector = build_v(q_con * build_q_v(Y_3D_VECTOR) * q)
            self.right_pointer_vector = build_v(q_con * build_q_v(X_3D_VECTOR) * q)
            self.front_pointer_vector = np.cross(self.right_pointer_vector, self.top_pointer_vector)
            self.__build_pointers()

        self.acceleration = None
        """If present, stores the module of the acceleration (of the Movement.accelerometer)"""

        if not_none_nor_empty(self.accelerometer):
            # Calculates and stores the module (Euclidean norm) of the device acceleration. Please note that this
            # includes gravity.
            x = np.array(self.accelerometer)
            self.acceleration = np.sqrt(x.dot(x))

        self.speed = None
        """If present, stores the module of the current speed"""

    def __build_pointers(self):
        """Computes the closest direction of the device y axes (bottom to top)

        Possible directions are listed in DIRECTIONS
        """
        self.top = convert_vector_to_direction(self.top_pointer_vector)
        self.bottom = opposite(self.top)
        self.right = convert_vector_to_direction(self.right_pointer_vector)
        self.left = opposite(self.right)
        self.front = convert_vector_to_direction(self.front_pointer_vector)
        self.back = opposite(self.front)
