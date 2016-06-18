from constants import *
from utils import sin_deg, cos_deg, convert_vector_to_direction, opposite


class Movement(object):
    def __init__(self, input_dict=None):
        self.raw_data = input_dict
        self.accelerometer = self.raw_data.get(ACCELEROMETER)
        self.gyroscope = self.raw_data.get(GYROSCOPE)
        self.gravity = self.raw_data.get(GRAVITY)
        self.magnetometer = self.raw_data.get(MAGNETOMETER)
        self.orientation = self.raw_data.get(ORIENTATION)
        self.linear_acceleration = self.raw_data.get(LINEAR_ACCELERATION)

        self.magnetic_field = None

        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.front = None
        self.back = None

        if self.orientation is not None:
            d = self.orientation
            self.magnetic_field = np.array(
                [- cos_deg(d[1]) * sin_deg(d[0]), cos_deg(d[1]) * cos_deg(d[0]), sin_deg(d[1])])

        self.build_pointers()

        self.speed = None

    def build_pointers(self):
        self.top = convert_vector_to_direction(self.magnetic_field)
        self.bottom = opposite(self.top)
