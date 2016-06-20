from movement.constants import *
from sound.constants import *
from pygame import mixer
import os

MAX_PREVIOUS_MOVEMENTS = 100


class BasePlayer(object):

    def __init__(self):
        # Initialize here variables that might be used at every new event.
        self.previous_movements = []
        mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

    def play(self, movement):
        self.previous_movements.append(movement)
        if len(self.previous_movements) > MAX_PREVIOUS_MOVEMENTS:
            self.previous_movements = self.previous_movements[1:]

    def play_sound(self, wav_filename):
        pat = os.path.join(SOUND_FOLDER, wav_filename)
        mixer.Sound(pat).play()




