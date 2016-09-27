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

        if mov.top == EAST:
            self.display_background('pink')
        elif mov.top == WEST:
            self.display_background('green')
        elif mov.top == DOWN:
            self.display_background('blue')
        elif mov.top == UP:
            self.display_background('yellow')
        else:
            self.display_background('red')



