# External modules import
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Quat
from random import random as r
from os import path

# Project modules import
from motuus.visualize.constants import MODELS_FOLDER, MODEL_NAME


class Graph3D(ShowBase):
    """Used to plot 3D objects (namely a panda3d .egg model file to represent the device)

    """
    def __init__(self):
        ShowBase.__init__(self)
        pat = path.join(MODELS_FOLDER, MODEL_NAME)
        self.__p = self.loader.loadModel(pat)

        self.__p.reparentTo(self.render)
        self.__p.setScale(1.0, 1.0, 1.0)
        self.__p.setPos(0, 25, 0)
        self.__p.setColorScale(r(), r(), r(), r())

    def rotate(self, quat):
        """Updates the device model orientation based on the given quaternion

        :param quat: the panda3d.core.Quat attitude quaternion that represents the current device orientation.
        Quat(cos(angl/2), sin(angl/2)*x, sin(angl/2)*y, sin(angl/2)*z) means that the main axes of the model is
        aligned to vector (x, y, z) and then the model is rotated of angle angl around this same axes.
        """
        q = Quat(quat.a, quat.b, quat.c, quat.d)
        self.__p.setQuat(q)
        self.taskMgr.step()

