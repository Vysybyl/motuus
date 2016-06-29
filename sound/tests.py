import unittest
import os
from constants import *
from pygame import mixer

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class MyTestCase(unittest.TestCase):
    def test_play_sound(self):
        filename = 'Bass-Drum-1.wav'
        path = os.path.join(SOUND_FOLDER, filename)
        mixer.init()
        sound = mixer.Sound(path)
        assert sound.get_length() > 0
        sound.play()

    def test_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')


if __name__ == '__main__':
    unittest.main()
