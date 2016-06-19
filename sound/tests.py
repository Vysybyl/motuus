import unittest
import os
from constants import *
from pygame import mixer


class MyTestCase(unittest.TestCase):
    def test_play_sound(self):
        filename = 'Bass-Drum-1.wav'
        filename2 = 'Electronic-Kick-2.wav'
        path = os.path.join(SOUND_FOLDER, filename)
        mixer.init()
        sound = mixer.Sound(path)
        assert sound.get_length() > 0
        sound.play()


if __name__ == '__main__':
    unittest.main()
