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

        lines = []

        # Raw data
        lines.append(" === RAW DATA === ")
        lines.append("TIMESTAMP:\t\t\t" + str(mov.time))
        lines.append("ACCELEROMETER:\t\t\t" + str(mov.accelerometer))
        lines.append("GYROSCOPE:\t\t\t" + str(mov.gyroscope))
        lines.append("GRAVITY:\t\t\t" + str(mov.gravity))
        lines.append("MAGNETOMETER:\t\t\t" + str(mov.magnetometer))
        lines.append("ORIENTATION:\t\t\t" + str(mov.orientation))
        lines.append("LINEAR_ACCELERATION:\t\t\t" + str(mov.linear_acceleration))

        # Directions
        lines.append(" === DIRECTIONS === ")
        lines.append("TOP:\t\t\t" + str(mov.top) + " "*6)
        lines.append("BOTTOM:\t\t\t" + str(mov.bottom) + " "*6)
        lines.append("FRONT:\t\t\t" + str(mov.front) + " "*6)
        lines.append("BACK:\t\t\t" + str(mov.back) + " "*6)
        lines.append("LEFT:\t\t\t" + str(mov.left) + " "*6)
        lines.append("RIGHT:\t\t\t" + str(mov.right) + " "*6)

        # Direction vectors
        lines.append(" === POINTER VECTORS ===")
        lines.append("TOP POINTER VECTOR:\t\t\t" + str(mov.top_pointer_vector))
        lines.append("FRONT POINTER VECTOR:\t\t\t" + str(mov.front_pointer_vector))
        lines.append("RIGHT POINTER VECTOR:\t\t\t" + str(mov.right_pointer_vector))
        lines.append("GRAVITY POINTER VECTOR:\t\t\t" + str(mov.gravity_pointer_vector))

        # Acceleration
        lines.append(" === DERIVED DATA ===")
        lines.append("ACCELERATION:\t\t\t" + str(mov.acceleration))
        lines.append("ACCELERATION WITHOUT GRAVITY VECTOR:\t\t\t" + str(mov.accel_without_gravity_vector))
        lines.append("ACCELERATION WITHOUT GRAVITY:\t\t\t" + str(mov.acceleration_without_gravity))


        # BasePlayer properties
        lines.append(" === PROCESSED INFORMATION ===")
        lines.append("STEPS:\t\t\t" + str(self.steps))

        print "\n".join(lines)




