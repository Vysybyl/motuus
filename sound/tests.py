import unittest
import os
from constants import *
from pygame import mixer
from time import sleep
import matplotlib.pyplot as plt

from motuus.sound.sound import Sound


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

    def test_play_sound_object(self):
        filename = 'Bass-Drum-1.wav'
        s = Sound(filename)
        s.play()

    def test_play_sound_object_not_overlapping(self):
        filename = 'Bass-Drum-1.wav'
        s = Sound(filename)
        for i in range(20):
            s.play()
            sleep(0.2)

    def test_play_sound_object_overlapping(self):
        filename = 'Bass-Drum-1.wav'
        s = Sound(filename)
        for i in range(20):
            s.play(overlap=True)
            sleep(0.2)

if __name__ == '__main__':
    unittest.main()
