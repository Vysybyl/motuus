import numpy as np
import matplotlib.pyplot as plt

# plt.axis([0, 10, 0, 1])
# plt.ion()
#
#
# def redraw():
#     y = np.random.random((6,1))
#     x = range(6)
#     plt.plot(x, y)
#     plt.draw()
#
# # for i in range(10):
# #     y = np.random.random()
# #     plt.scatter(i, y)
# #     plt.pause(0.05)
# #
# while True:
#     plt.pause(3.0)
#     redraw()


class C:
    def __init__(self, val):
        self.val = [1]
        self.val[0] = val[0]

a = [np.array([])]
b = [np.array([])]

print a
print b
ca = C(a)
cb = C(b)
print ca.val
print cb.val

a[0] = np.append(a[0],1)
b[0] = np.append(b[0],2)

print a
print b
print ca.val
print cb.val
