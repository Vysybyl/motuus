from motuus.movement.constants import *
from motuus.sound.sound import Sound
from random import choice

from motuus.play.base_player import BasePlayer


class Player(BasePlayer):
    """This is the main class of motuus.

    Use it to process Movement objects as they come in and to bind them to multimedia events.
    An instance of this class is kept alive throughout every http session between the mobile device browser and the
    computer.

    If you need to store variables between inputs, you'll have to initialize them appropriately in the __init__ method.
    Some useful variables are already present in the BasePlayer and can be called directly.
    """

    def __init__(self, ):
        # Calling super class init (ignore the following line):
        super(Player, self).__init__(count_steps=True)
        # Initialize here variables that might be used at every new event.
        self.count = 0
        s1 = Sound('dino-stomp-1.wav')
        s2 = Sound('dino-stomp-2.wav')
        s3 = Sound('dino-stomp-3.wav')
        s4 = Sound('dino-stomp-4.wav')
        self.stomps = [s1, s2, s3, s4]
        self.roar = Sound('trex-roar.wav')
        self.roar.set_volume(0.2)
        self.stays_up = 0

    def play(self, mov):
        """This method is called anytime a new Movement input comes in from the device.

        Use it to process every new mov and bind it to multimedia event, etc.
        PLEASE NOTE that you should avoid long processing tasks within this method. If the device transmission
        frequency is set to 5Hz (5 new inputs per second) the server will only have 0.2 seconds to receive and
        process every input.
        Do not overload it!
        """
        # Calling super class play (ignore the following line):
        super(Player, self).play(mov)

        if self.count != self.steps:
            choice(self.stomps).play(overlap=True)
            print 'Getting closer...' + str(self.steps)
            self.count = self.steps

        # print mov.top


        if mov.top == UP:
            self.stays_up += 1
            if self.stays_up > 3:
                self.roar.play()
                print "Roaaarrr!!!" + str(self.roar.get_volume())
        else:
            self.stays_up = 0
