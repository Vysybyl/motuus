import unittest
from time import sleep
from math import pi, sin, cos
from panda3d.core import Quat
from random import random as rnd

from motuus.visualize.graph2D import Graph2D
from motuus.visualize.graph3D import Graph3D
from motuus.movement.constants import *
from motuus.movement.utils import build_q, cos_deg, sin_deg
from motuus.movement.dummy_data import build_random_input
from motuus.movement.movement import Movement as move

class MyTestCase(unittest.TestCase):
    def test_graph2D(self):
        g = Graph2D(10)
        x = np.linspace(0, 1000, 1000)
        y = np.sin(x)
        a = np.array([])
        b = np.array([])
        g.add_line('testline')

        for i in range(len(x)):
            a = np.append(a, x[i])
            b = np.append(b, y[i])
            g.update_line('testline', a, b)
            g.plot()
            sleep(0.05)

    def test_graph3D(self):
        g = Graph3D()
        # g.run()
        vects = [
                 NORTH_ORIENTATION_VECTOR,
                 EAST_ORIENTATION_VECTOR,
                 SOUTH_ORIENTATION_VECTOR,
                 WEST_ORIENTATION_VECTOR,
                 UP_FRONT_ORIENTATION_VECTOR,
                 UP_LEFT_ORIENTATION_VECTOR,
                 UP_REAR_ORIENTATION_VECTOR,
                 UP_RIGHT_ORIENTATION_VECTOR ,
                 DOWN_FRONT_ORIENTATION_VECTOR,
                 DOWN_LEFT_ORIENTATION_VECTOR,
                 DOWN_REAR_ORIENTATION_VECTOR,
                 DOWN_RIGHT_ORIENTATION_VECTOR
                 ]
        while True:
            for v in vects + vects:
                # print v
                g.rotate(build_q(v[0],v[1],v[2]))
                sleep(1.0)

        return
        while True:
            tt = 180
            slp = 0.02
            rng = range(-tt, tt, 2)
            for i in rng:
                g.rotate(build_q(i, -1, 0, 0))
                sleep(slp)
            for i in rng:
                g.rotate(build_q(i, 0, 1, 0))
                sleep(slp)
            for i in rng:
                g.rotate(build_q(i, 0, 0, 1))
                sleep(slp)

    def quat_ori_test(self):
        g = Graph3D()
        while True:
            for i in range(3):
                for j in range(0, 360, 5):
                    v = np.zeros(3)
                    v[i] = 1
                    v = v * sin_deg(j/2.0)
                    q = Quat(cos_deg(j/2.0), v[0], v[1], v[2])
                    g.rotate(q)
                    sleep(0.05)

    def quat_rnd_test(self):
        g = Graph3D()
        while True:
            r = np.array([rnd(), rnd(), rnd()])
            r = r / r.dot(r)
            for j in range(0, 360, 5):
                v = r * sin_deg(j/2.0)
                q = Quat(cos_deg(j/2.0), v[0], v[1], v[2])
                g.rotate(q)
                sleep(0.10)

    def quat_composition_test(self):
        g = Graph3D()
        while True:
            # r = np.array([rnd(), rnd(), rnd()])
            # r = r / r.dot(r)
            h = None
            q0 = None
            q1 = None
            for i in range(3):
                r = np.zeros(3)
                # r[i] = 1
                r[-(i+1)] = 1
                if i == 0:
                    h = r
                    q1 = Quat(1, 0, 0, 0)
                else:
                    q1 = q0
                    # r_q = q0 * Quat(0, r[0], r[1], r[2]) + q0.conjugate()
                    r_q = q0.conjugate() * Quat(0, r[0], r[1], r[2]) * q0
                    h = np.array([r_q.getI(), r_q.getJ(), r_q.getK()])
                    h = r
                for j in range(0, 95, 5):
                    v = h * sin_deg(j/2.0)
                    q0 = Quat(cos_deg(j/2.0), v[0], v[1], v[2]) * q1
                    g.rotate(q0)
                    sleep(0.10)

    def quat_tests(self):
        x = Quat(0, 1, 0, 0)
        y = Quat(0, 0, 1, 0)
        z = Quat(0, 0, 0, 1)
        pi4_x = Quat(cos(pi/8), sin(pi/8), 0, 0)
        pi4_y = Quat(cos(pi/8), 0, sin(pi/8), 0)
        pi4_z = Quat(cos(pi/8), 0, 0, sin(pi/8))
        self.assertTrue((pi4_z * pi4_z * x * pi4_z.conjugate() * pi4_z.conjugate()).almostEqual(-y))  # ??
        self.assertTrue((pi4_y * pi4_y * x * pi4_y.conjugate() * pi4_y.conjugate()).almostEqual(z))  # ??

        self.assertTrue((pi4_x * pi4_x * z * pi4_x.conjugate() * pi4_x.conjugate()).almostEqual(y))  # ??
        self.assertTrue((pi4_y * pi4_y * z * pi4_y.conjugate() * pi4_y.conjugate()).almostEqual(-x))  # ??

        self.assertTrue((pi4_x * pi4_x * y * pi4_x.conjugate() * pi4_x.conjugate()).almostEqual(-z))
        self.assertTrue((pi4_z * pi4_z * y * pi4_z.conjugate() * pi4_z.conjugate()).almostEqual(x))

        self.assertTrue((pi4_x * x * pi4_x.conjugate()).almostEqual(x))
        self.assertTrue((pi4_y * y * pi4_y.conjugate()).almostEqual(y))
        self.assertTrue((pi4_z * z * pi4_z.conjugate()).almostEqual(z))

        self.assertTrue((pi4_z * pi4_z * x * pi4_z.conjugate() * pi4_z.conjugate()).almostEqual(-y))

    def test_quat(self):
        m = move(build_random_input())
        q1 = m.attitude_quaternion * Quat(0, 0, 1, 0) * m.attitude_quaternion.conjugate()
        q1 = np.array([q1.getI(), q1.getJ(), q1.getK()])
        q1 = q1 / np.sqrt(q1.dot(q1))
        q2 = m.attitude_quaternion.conjugate() * Quat(0, 0, 1, 0) * m.attitude_quaternion
        q2 = np.array([q2.getI(), q2.getJ(), q2.getK()])
        q2 = q2 / np.sqrt(q2.dot(q2))

        print m.top_pointer_vector
        print q2
        for i, j in zip(m.top_pointer_vector, q2):
            print i - j
            assert abs(i-j) < 0.0001


    def test_pointers(self):
        m = move(build_random_input())

        q_x = m.attitude_quaternion * Quat(0, 1, 0, 0) * m.attitude_quaternion.conjugate()
        q_x = np.array([q_x.getI(), q_x.getJ(), q_x.getK()])
        q_x = q_x / np.sqrt(q_x.dot(q_x))

        q_y = m.attitude_quaternion * Quat(0, 0, 1, 0) * m.attitude_quaternion.conjugate()
        q_y = np.array([q_y.getI(), q_y.getJ(), q_y.getK()])
        q_y = q_y / np.sqrt(q_y.dot(q_y))

        q_z = m.attitude_quaternion * Quat(0, 0, 0, 1) * m.attitude_quaternion.conjugate()
        q_z = np.array([q_z.getI(), q_z.getJ(), q_z.getK()])
        q_z = q_z / np.sqrt(q_z.dot(q_z))

        print m.top_pointer_vector
        print q_y
        for i, j in zip(m.top_pointer_vector, q_y):
            print i - j
            assert abs(i - j) < 0.0001
        print "=="
        print m.right_pointer_vector
        print q_x
        for i, j in zip(m.right_pointer_vector, q_x):
            print i - j
            assert abs(i - j) < 0.0001
        print "=="
        print m.front_pointer_vector
        print q_z
        for i, j in zip(m.front_pointer_vector, q_z):
            print i - j
            assert abs(i - j) < 0.0001
        print "=="
1

if __name__ == '__main__':
    unittest.main()
