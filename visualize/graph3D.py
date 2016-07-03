from motuus.visualize.constants import MODELS_FOLDER
from motuus.movement.utils import sin_deg, cos_deg
from motuus.movement.constants import NORTH_3D_VECTOR
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from random import random as r
from os import path
from panda3d.core import Quat
from threading import Thread
from time import sleep, ctime, time

filename = 'smartphone'
exitFlag = False


class Graph3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        # self.scene = self.loader.loadModel("models/environment")
        # # Reparent the model to render.
        # self.scene.reparentTo(self.render)
        # # Apply scale and position transforms on the model.
        # self.scene.setScale(0.25, 0.25, 0.25)
        # self.scene.setPos(-8, 42, 0)
        pat = path.join(MODELS_FOLDER, filename)
        # pat = Filename(pat)
        self.__p = self.loader.loadModel(pat)
        # self.__p = self.loader.loadModel('models/misc/rgbCube')
        self.__p.reparentTo(self.render)
        self.__p.setScale(1.0, 1.0, 1.0)
        self.__p.setPos(0, 25, 0)
        self.__p.setColorScale(r(), r(), r(), r())

    def rotate(self, quat):
        # nu = Quat(quat.q[0], quat.q[1], quat.q[2], quat.q[3])
        self.__p.setQuat(quat)
        self.taskMgr.step()

    def spinCameraTask(self, task):
        self.__p.setQuat(self.rotation_quat)
        return Task.cont


if __name__ == '__main__':
    app = Graph3D()
    app.run()




# class Graph3D(object):
#     def __init__(self):