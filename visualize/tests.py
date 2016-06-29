import unittest
from graph2D import Graph2D
import numpy as np
from time import sleep
from movement.utils import ptr

class MyTestCase(unittest.TestCase):
    def test_graph2D(self):
        g = Graph2D(10)
        x = np.linspace(0, 1000, 1000)
        y = np.sin(x)
        a = np.array([])
        b = np.array([])
        g.add_line('testline')

        for i in range(len(x)):
            a = np.append(a, x[i])
            b = np.append(b, y[i])
            g.update_line('testline', a, b)
            g.plot()
            sleep(0.05)



if __name__ == '__main__':
    unittest.main()
