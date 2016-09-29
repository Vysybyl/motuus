from motuus.play.base_player import BasePlayer
from motuus.movement.constants import *
from motuus.sound.sound import Sound


class Player(BasePlayer):
    """This is the main class of motuus.

    Use it to process Movement objects as they come in and to bind them to multimedia events.
    An instance of this class is kept alive throughout every http session between the mobile device browser and the
    computer.

    If you need to store variables between inputs, you'll have to initialize them appropriately in the __init__ method.
    Some useful variables are already present in the BasePlayer and can be called directly.
    """

    def __init__(self):
        # Calling super class init (ignore the following line):
        super(Player, self).__init__()
        # Initialize here variables that might be used at every new event.
        self.ding = Sound('ding_1.wav')
        self.gun = Sound('gunshot.wav')
        self.bell = Sound('Cowbell-1.wav')

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

        # If the device top points up
        if mov.top == UP:
            # You will hear a gunshot
            self.gun.play()

        # If it points down
        elif mov.top == DOWN:
            # You will see hear a cowbell
            # a new one at every data input, even if the previous one
            # is still playing
            self.bell.play(overlap=True)



        # If it points elsewhere (notrh, east, south, west)
        # and the relative vector exists
        elif mov.top_pointer_vector is not None:
            # You'll hear a ding (overlapping, lasting 0.600 seconds)
            # which volume will be adjusted based on the north-south orientation.
            # That is, you will hear max volume when pointing to north or south
            # and zero volume when pointing to east or west

            # (the volume has values between 0.0 and 1.0)
            y_axis = abs(mov.top_pointer_vector[1])
            self.ding.set_volume(y_axis)
            self.ding.play(overlap=True, maxtime=600)




