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
        self.time = self.raw_data.get(TIMESTAMP)
        self.accelerometer = self.raw_data.get(ACCELEROMETER)
        self.gyroscope = self.raw_data.get(GYROSCOPE)
        self.gravity = self.raw_data.get(GRAVITY)
        self.magnetometer = self.raw_data.get(MAGNETOMETER)
        self.orientation = self.raw_data.get(ORIENTATION)
        self.linear_acceleration = self.raw_data.get(LINEAR_ACCELERATION)

        self.pointer_vector = None
        self.rotation = None

        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.front = None
        self.back = None

        if not_none_nor_empty(self.orientation):
            # This creates a pointer vector and an orientation (or attitude) quaternion storing respectively the device
            # direction along the y axis (bottom to top) and the device orientation
            d = self.orientation
            self.pointer_vector = np.array(
                [- cos_deg(d[1]) * sin_deg(d[0]), cos_deg(d[1]) * cos_deg(d[0]), sin_deg(d[1])],
                dtype=np.double)
            self.attitude_quaternion = build_q_v(self.orientation)
            self.__build_pointers()

        self.acceleration = 0

        if not_none_nor_empty(self.accelerometer):
            # Calculates and stores the module (Euclidean norm) of the device acceleration. Please note that this
            # includes gravity.
            x = np.array(self.accelerometer)
            self.acceleration = x.dot(x)

        self.speed = None

    def __build_pointers(self):
        """Computes the closest direction of the device y axes (bottom to top)

        Possible directions are listed in DIRECTIONS
        """
        self.top = convert_vector_to_direction(self.pointer_vector)
        self.bottom = opposite(self.top)
