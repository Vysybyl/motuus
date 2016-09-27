import pygame
from pygame.locals import *

from motuus.visualize.constants import *


class Screen(object):

    def __init__(self):
        pygame.init()  # initialize pygame engine
        self.__screen = pygame.display.set_mode((640, 480))

    def display(self, background_color='black', fullscreen=False):
        if type(background_color) is str:
            c = Color(background_color)
        else:
            c = background_color
        if fullscreen:
            pygame.display.quit()
            self.__screen = pygame.display.set_mode((0, 0))
        self.__screen.fill(c)
        pygame.display.flip()




