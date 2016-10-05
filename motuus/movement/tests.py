import unittest
from constants import *
from dummy_data import build_random_input
from utils import opposite
from movement import Movement as move


class MyTestCase(unittest.TestCase):

    def test_still_north(self):
        m = move(INPUT_STILL_NORTH)
        assert m.top == NORTH
        assert m.bottom == SOUTH

    def test_fake_input(self):
        m = move(build_random_input())
        assert m.top == opposite(m.bottom)

    def test_gravity(self):
        m = move(build_random_input())
        assert m.linear_acceleration



if __name__ == '__main__':
    unittest.main()
