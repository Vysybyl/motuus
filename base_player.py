from movement.constants import *
from movement.utils import not_none_nor_empty
from sound.constants import *
from pygame import mixer

import os

MAX_PREVIOUS_MOVEMENTS = 100
CALIBRATION_SAMPLE_SIZE = 50


class BasePlayer(object):
    def __init__(self, count_steps=False, calibrate=False):
        # Initialization goes here
        mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

        self.previous_movements = []

        self.steps = 0
        self.__count_steps = count_steps
        if count_steps:
            self.__acceleration_trace = []

        self.__calibrate = calibrate

    def play(self, movement):
        self.previous_movements.append(movement)
        if len(self.previous_movements) > MAX_PREVIOUS_MOVEMENTS:
            self.previous_movements = self.previous_movements[1:]

        if self.__calibrate:
            if len(self.previous_movements) < CALIBRATION_SAMPLE_SIZE:
                pass
            else:
                self.__gravity = self.__estimate_gravity()
                self.__north = self.__adjust_north()
                self.__calibrate = False
                self.play_sound('66136__theta4__ding30603-spedup.wav')

        if self.__count_steps and movement.acceleration != 0:
            self.__acceleration_trace.append(movement.acceleration)

    def play_sound(self, wav_filename):
        pat = os.path.join(SOUND_FOLDER, wav_filename)
        mixer.Sound(pat).play()

    def __estimate_gravity(self):
        acc = []
        for m in self.previous_movements:
            if not_none_nor_empty(m.accelerometer):
                acc.append(np.array(m.accelerometer))
        return np.sum(acc, axis=0) / len(acc)

    def __adjust_north(self):
        mag = []
        for m in self.previous_movements:
            if not_none_nor_empty(m.magnetic_field):
                mag.append(m.magnetic_field)
        return np.sum(mag, axis=0) / len(mag)
