from movement.constants import *
from base_player import BasePlayer


class Player(BasePlayer):

    def __init__(self):
        # Calling super class init:
        super(Player, self).__init__()
        # Initialize here variables that might be used at every new event.
        self.count = 0

    def play(self, mov):
        # Calling super class play:
        super(Player, self).play(mov)

        self.count += 1
        print str(self.count)
        if mov.top and mov.top == UP:
            print 'UP'
            self.play_sound('Bass-Drum-1.wav')
        if mov.top and mov.top == DOWN:
            print 'DOWN'
            self.play_sound('Cowbell-2.wav')


