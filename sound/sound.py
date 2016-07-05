# External modules import
from pygame import mixer
from os import path
from time import time

# Project modules import
from motuus.sound.constants import SOUND_FOLDER, FREQUENCY, SIZE, CHANNELS, BUFFER

mixer.init(frequency=FREQUENCY, size=SIZE, channels=CHANNELS, buffer=BUFFER)


class Sound(object):
    def __init__(self, filename):
        """Creates a new Sound object.

        sound.Sound objects can be played using the player.play_sound method.
        For performance optimization all Sound objects must be created before any data is streamed from the device
        len(Sound) returns the lenght of the sound in seconds.
        :param filename: The filename of a .WAV file that must be saved in the project /data/sound folder. The name must
        include the extension.
        """
        if filename is None or type(filename) is not str or len(filename) < 5:
            raise ValueError("The filename " + filename + " is not a valid .WAV filename.")
        pat = path.join(SOUND_FOLDER, filename)
        self.__s = mixer.Sound(pat)
        self.__l = self.__s.get_length()
        self.__end = 0.0

    def __len__(self):
        """Return the length of the sound

        :return: the length of the sound in seconds
        """
        return self.__l

    def play(self, overlap=False, loops=0, maxtime=0, fade_ms=0):
        """Plays the sound

        :param overlap: When set to False, if play() is called while the sound is already playing, it will not be played
        :param loops: Number of times the sound will be repeated
        :param maxtime: cut the sound after the given number of milliseconds
        :param fade_ms: fade in during the given number of milliseconds
        """
        if overlap:
            self.__end = time() + self.__l
            self.__s.play(loops, maxtime, fade_ms)
        else:
            if time() > self.__end:
                self.__end = time() + self.__l
                self.__s.play(loops, maxtime, fade_ms)

    def get_volume(self):
        """Gets the Sound volume

        :return: a value from 0.0 to 1.0 representing the volume for this Sound.
        """
        return self.__s.get_volume()

    def set_volume(self, val):
        """Sets the Sound volume

        :param val: a value from 0.0 to 1.0 representing the volume for this Sound.
        """
        return self.__s.set_volume(val)
