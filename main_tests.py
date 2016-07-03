import unittest
from player import Player
from movement.dummy_data import build_random_input
from movement.movement import Movement
from time import sleep


class MyTestCase(unittest.TestCase):
    def test_player(self):
        p = Player()
        mov = Movement(build_random_input())
        p.play(mov)

    def test_player_3_times(self):
        p = Player()
        mov = Movement(build_random_input())
        p.play(mov)
        sleep(5)
        mov = Movement(build_random_input())
        p.play(mov)
        sleep(5)
        mov = Movement(build_random_input())
        p.play(mov)
        sleep(5)

    def test_player_continuous(self):
        p = Player()
        while True:
            mov = Movement(build_random_input())
            p.play(mov)
            sleep(0.5)


if __name__ == '__main__':
    unittest.main()
