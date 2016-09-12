import pygame
from pygame.locals import *

from motuus.visualize.constants import *


class Screen(object):

    def __init__(self):
        pygame.init()  # initialize pygame engine
        self.__screen = pygame.display.set_mode((640, 480))

    def display(self, background_color='black'):
        self.__screen.fill(Color(background_color))
        pygame.display.flip()




