
class Movement(object):

    def __init__(self, input_string = None):
        self.raw_input = input_string
        self.accelerometer = None
        self.gyroscope = None
        self.gravity = None
        self.orientation = None

        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.front = None
        self.back = None

        self.speed = None



