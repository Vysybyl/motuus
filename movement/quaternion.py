

class Quat(object):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def almostEqual(self, other):
        return(abs(self.a - other.a < 0.00001) and
               abs(self.b - other.b < 0.00001) and
               abs(self.c - other.c < 0.00001) and
               abs(self.d - other.d < 0.00001))

    def __mul__(self, other):
        # This is a very stupid and faulty implementation but I need this as
        # hot-fix to work with faulty panda3d implementation
        # see https://www.panda3d.org/forums/viewtopic.php?t=12763
        s = other
        o = self

        x = s.a * o.a - s.b * o.b - s.c * o.c - s.d * o.d
        y = s.a * o.b + s.b * o.a + s.c * o.d - s.d * o.c
        w = s.a * o.c - s.b * o.d + s.c * o.a + s.d * o.b
        z = s.a * o.d + s.b * o.c - s.c * o.b + s.d * o.a
        
        return Quat(x, y, w, z)

    def __add__(self, other):
        return Quat(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __neg__(self):
        return Quat(-self.a, -self.b, -self.c, -self.d)

    def __str__(self):
        return "({0}, {1}i, {2}j, {3}k)".format(self.a, self.b, self.c, self.d)

    def conjugate(self):
        return Quat(self.a, -self.b, -self.c, -self.d)
