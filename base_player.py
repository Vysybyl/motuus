from movement.constants import *
from movement.utils import not_none_nor_empty
from sound.constants import *
from pygame import mixer
from visualize.graph2D import Graph2D

import os

MAX_PREVIOUS_MOVEMENTS = 100

CALIBRATION_SAMPLE_SIZE = 50

# Step counter settings
ACC_TRACE_SAMPLE_SIZE = 200
ACC_AVERAGE_SMOOTHING_FACTOR = 0.7  # Between 0 and 1
REAL_ACC_THRESHOLD = GRAVITY_FIELD * 10.0 * 0.15  # 0.15 seems ok for walking
STEP_COUNTER_SAMPLE_TIME_WINDOW = 1.0  # in seconds
MINIMUM_TIME_BETWEEN_STEPS = 0.3  # in seconds


class BasePlayer(object):
    def __init__(self, count_steps=False, calibrate=False):
        # Initialization goes here
        mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

        self.__g2D = Graph2D()
        self.__g2D.add_line('acceleration')
        self.__g2D.add_line('acc_avg')
        self.__g2D.add_line('acc_tresh')

        self.previous_movements = []

        self.steps = 0
        self.__count_steps = count_steps
        self.__acceleration_trace = None
        self.__last_step_time = 0

        self.__calibrate = calibrate
        self.__gravity = None

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
            if self.__acceleration_trace is None:
                # The first time we enter here
                # The array will have a row structure of [time, acceleration, acc moving average, threshold]
                first_vec = np.array([movement.time, movement.acceleration, movement.acceleration, movement.acceleration], dtype=np.double)
                self.__acceleration_trace = np.vstack((first_vec, first_vec, first_vec))
                # print "Acc trace " + str( self.__acceleration_trace)
            else:
                t = movement.time - 1000.0 * STEP_COUNTER_SAMPLE_TIME_WINDOW  #  beginning of the time window, milliseconds
                # print "Time diff " + str(t)
                times = self.__acceleration_trace[:, 0]
                # print "Times " + str(times)
                # print "Times > t" + str(times > t)
                sample = self.__acceleration_trace[(times > t)]  # all lines where time is bigger than t
                # print "Sample len " + str(len(sample))
                ln = len(sample)
                if ln == 0:
                    print "ERROR: empty sample for step counter calculations. Try using a wider STEP_COUNTER_SAMPLE_TIME_WINDOW"
                else:
                    # avg = np.average(sample[:, 1])  # maybe we should use an exponential moving average?
                    avg = sample[-1, 2] * (1.0 - ACC_AVERAGE_SMOOTHING_FACTOR) + movement.acceleration * ACC_AVERAGE_SMOOTHING_FACTOR
                    # print avg
                    threshold = (np.max(sample[:, 1]) + np.min(sample[:, 1])) / 2

                    vun = sample[-1, 2] > sample[-1, 3]
                    du = avg < threshold
                    tri = movement.time - self.__last_step_time > MINIMUM_TIME_BETWEEN_STEPS * 1000.0
                    # if vun: print "Un"
                    # if du: print "Du"
                    # if tri: print "Tri"
                    if (
                        sample[-1, 2] > sample[-1, 3] and
                        avg < threshold and
                        np.max(sample[:, 1]) - threshold > REAL_ACC_THRESHOLD and
                        movement.time - self.__last_step_time > MINIMUM_TIME_BETWEEN_STEPS * 1000.0
                    ):
                        self.steps += 1
                        self.__last_step_time = movement.time

                    self.__acceleration_trace = np.vstack((
                        self.__acceleration_trace, np.array([movement.time, movement.acceleration, avg, threshold],
                                                            dtype=np.double)
                    ))
                    # print "Acc trace " + str(self.__acceleration_trace)
                    lin_x = self.__acceleration_trace[:, 0] / 1000  # milliseconds
                    lin_y = self.__acceleration_trace[:, 1] / 100
                    lin_avg = self.__acceleration_trace[:, 2] / 100
                    lin_tresh = self.__acceleration_trace[:, 3] / 100
                    # print "lin x " + str(lin_x)
                    # print "lin y " + str(lin_y)
                    self.__g2D.update_line('acceleration',
                                           lin_x,
                                           lin_y)
                    self.__g2D.update_line('acc_avg',
                                           lin_x,
                                           lin_avg)
                    self.__g2D.update_line('acc_tresh',
                                           lin_x,
                                           lin_tresh)
                    self.__g2D.plot()
                    if len(self.__acceleration_trace) > ACC_TRACE_SAMPLE_SIZE:
                        self.__acceleration_trace = self.__acceleration_trace[-ACC_TRACE_SAMPLE_SIZE:]

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
