# External modules import
import numpy as np

TIMESTAMP = 'tim'
ACCELEROMETER = 'acc'  # Same as Acceleration including gravity
GYROSCOPE = 'gyr'  # Same as Rotation Rate
MAGNETOMETER = 'mag'
GRAVITY = 'gra'
LINEAR_ACCELERATION = 'lac'  # Same as Acceleration
ORIENTATION = 'ori'  # Same as DeviceOrientation

DATA_TAGS = [TIMESTAMP, ACCELEROMETER, GYROSCOPE, MAGNETOMETER, GRAVITY, LINEAR_ACCELERATION, ORIENTATION]

NORTH = 'n'
SOUTH = 's'
UP = 'u'
DOWN = 'd'
EAST = 'e'
WEST = 'w'

DIRECTIONS = [NORTH, SOUTH, UP, DOWN, EAST, WEST]

OPPOSITE_DIRECTIONS = [[NORTH, SOUTH],
                       [UP, DOWN],
                       [EAST, WEST]]

GRAVITY_FIELD = 9.8
MAGNETIC_FIELD = 1.0

ZERO_3D_VECTOR = np.zeros(3, np.double)

X_3D_VECTOR = np.array([1.0, 0.0, 0.0])
Y_3D_VECTOR = np.array([0.0, 1.0, 0.0])
Z_3D_VECTOR = np.array([0.0, 0.0, 1.0])

GRAVITY_3D_VECTOR = - GRAVITY_FIELD * Z_3D_VECTOR

NORTH_ORIENTATION_VECTOR = ZERO_3D_VECTOR
SOUTH_ORIENTATION_VECTOR = 180.0 * X_3D_VECTOR
EAST_ORIENTATION_VECTOR = 90.0 * X_3D_VECTOR
WEST_ORIENTATION_VECTOR = 270.0 * X_3D_VECTOR
UP_FRONT_ORIENTATION_VECTOR = 90.0 * Y_3D_VECTOR
DOWN_REAR_ORIENTATION_VECTOR = -UP_FRONT_ORIENTATION_VECTOR
UP_REAR_ORIENTATION_VECTOR = SOUTH_ORIENTATION_VECTOR + (90.0 * Y_3D_VECTOR)
DOWN_FRONT_ORIENTATION_VECTOR = -UP_REAR_ORIENTATION_VECTOR
UP_LEFT_ORIENTATION_VECTOR = EAST_ORIENTATION_VECTOR + UP_FRONT_ORIENTATION_VECTOR
UP_RIGHT_ORIENTATION_VECTOR = WEST_ORIENTATION_VECTOR + UP_FRONT_ORIENTATION_VECTOR
DOWN_LEFT_ORIENTATION_VECTOR = -UP_RIGHT_ORIENTATION_VECTOR
DOWN_RIGHT_ORIENTATION_VECTOR = -UP_LEFT_ORIENTATION_VECTOR

NORTH_3D_VECTOR = Y_3D_VECTOR
SOUTH_3D_VECTOR = -Y_3D_VECTOR
EAST_3D_VECTOR = -X_3D_VECTOR
WEST_3D_VECTOR = X_3D_VECTOR

UP_3D_VECTOR = Z_3D_VECTOR
DOWN_3D_VECTOR = -Z_3D_VECTOR

DIRECTION_VECTORS = dict()
DIRECTION_VECTORS[NORTH] = NORTH_3D_VECTOR
DIRECTION_VECTORS[SOUTH] = SOUTH_3D_VECTOR
DIRECTION_VECTORS[EAST] = EAST_3D_VECTOR
DIRECTION_VECTORS[WEST] = WEST_3D_VECTOR
DIRECTION_VECTORS[UP] = UP_3D_VECTOR
DIRECTION_VECTORS[DOWN] = DOWN_3D_VECTOR

INPUT_STILL_NORTH = dict()
INPUT_STILL_NORTH[ACCELEROMETER] = -1 * GRAVITY_3D_VECTOR
INPUT_STILL_NORTH[ORIENTATION] = NORTH_ORIENTATION_VECTOR
INPUT_STILL_NORTH[GYROSCOPE] = ZERO_3D_VECTOR
INPUT_STILL_NORTH[LINEAR_ACCELERATION] = ZERO_3D_VECTOR
INPUT_STILL_NORTH[MAGNETOMETER] = MAGNETIC_FIELD * Y_3D_VECTOR
