from movement.constants import *
from sound.constants import *
from pygame import mixer
import os

last = ''


def play(mov):
    if mov.top and mov.top == UP:
        print 'UP'
        filename = 'Bass-Drum-1.wav'
        path = os.path.join(SOUND_FOLDER, filename)
        mixer.init()
        sound = mixer.Sound(path)
        assert sound.get_length() > 0
        sound.play()



