import pygame
from pygame.locals import *
from os import path
import constants



class Screen(object):

    def __init__(self):
        pygame.init()  # initialize pygame engine
        self.__screen = pygame.display.set_mode((640, 480))
        self.__fullscreen = False

    def display(self, background='black', fullscreen=False):

        if fullscreen and not self.__fullscreen:
            pygame.display.quit()
            self.__screen = pygame.display.set_mode((0, 0))
            self.__fullscreen = True
        if not fullscreen and self.__fullscreen:
            pygame.display.quit()
            self.__screen = pygame.display.set_mode((640, 480))
            self.__fullscreen = False

        t = type(background)
        if t is str:
            if "." in background:
                pat = path.join(constants.IMAGE_FOLDER, background)
                img = pygame.image.load(pat)
                self.__screen.blit(img, (0, 0))
                pygame.display.flip()
                return
            else:
                c = Color(background)
        else:
            c = background

        self.__screen.fill(c)
        pygame.display.flip()




