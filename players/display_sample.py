from motuus.play.base_player import BasePlayer
from motuus.movement.constants import *


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
        super(Player, self).__init__(display=True)
        # Initialize here variables that might be used at every new event.


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
            # You will see a red background (the list [255, 0, 0] is just [r, g, b] notation
            self.display_background([255, 0, 0])

        # If it points down
        elif mov.top == DOWN:
            # You will see a fullscreen blue background
            self.display_background('blue', fullscreen=True)

        # If it points north
        elif mov.top == NORTH:
            # You'll see an image
            self.display_background('emule.png')

        # If it points elsewhere (east, south, west)
        # and the relative vector exists
        elif mov.top_pointer_vector is not None:
            # You'll see a the screen color continuously adjusting the green value
            # based on the vector's first component (x axis)
            # That is, rotating the device on the horizontal plane
            # will change the color from black to full green.
            x_axis = abs(mov.top_pointer_vector[0])
            self.display_background([0, int(255 * x_axis), 0])




