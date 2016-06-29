from movement.constants import *
from base_player import BasePlayer


class Player(BasePlayer):

    def __init__(self, ):
        # Calling super class init:
        super(Player, self).__init__(count_steps=True)
        # Initialize here variables that might be used at every new event.
        self.count = 0

    def play(self, mov):
        # print mov.time
        # Calling super class play:
        super(Player, self).play(mov)
        #print 'Acceleration norm: ' + str(mov.acceleration)
        # print 'Graph: ' + '-' * int(mov.acceleration/10)
        # print 'Acc ' + str(mov.acceleration)
        # print 'Gravity field ' + str(GRAVITY_FIELD)

        if self.count != self.steps:
            print 'Steps: ' + str(self.steps)
            self.count = self.steps
            # self.play_sound('gunshot.wav')
        # self.count += 1
        # print str(self.count)
        #if mov.top and mov.top == UP:
        #     print 'UP'
        #    self.play_sound('Bass-Drum-1.wav')
        #if mov.top and mov.top == DOWN:
        #     print 'DOWN'
        #    self.play_sound('Cowbell-2.wav')


