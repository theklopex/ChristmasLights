try:
    # If we run this on the Raspberry Pi, then we will use the GPIO module.
    from gpiozero import LED
    use_simulator = False
except:
    # Otherwise, we will use the Simulator that uses a little GUI.
    from Simulator import LED
    use_simulator = True

# The mapping of the numbered power outlet (in brackets []) to the GPIO
# pin number (on the right).
gpio_mapping = {}
gpio_mapping[1] = 4
gpio_mapping[2] = 17
gpio_mapping[3] = 27
gpio_mapping[4] = 22
gpio_mapping[5] = 23
gpio_mapping[6] = 24
gpio_mapping[7] = 25
gpio_mapping[8] = 12
gpio_mapping[9] = 5
gpio_mapping[10] = 6
gpio_mapping[11] = 13
gpio_mapping[12] = 19
gpio_mapping[13] = 26
gpio_mapping[14] = 16
gpio_mapping[15] = 20
gpio_mapping[16] = 21

def map_to_gpio(number):
    """
    So, we had a problem...  I did not want the simulator displaying the
        GPIO pin values.  I wanted it to display the channel values.  This
        function maps the channel value to the GPIO pin value if we are
        talking to the GPIO interface.  Otherwise, it returns the input
        channel number for the simulator purpose.
        :param number: The channel number
    :param number: Number of the channel to map to the GPIO pin number
    :return: Either the GPIO pin number, or the number passed in if we are using the simulator.
    """
    if use_simulator == True:
        return number

    return gpio_mapping(number)


class Lights:
    """
    A class that contains the list of 16 channels that can be turned on or off.
    """
    def __init__(self):
        """
        Initializes the Lights object's collection of channels.
        """
        self._channel = {}
        for i in range(1, 17):
            self._channel[i] = LED(map_to_gpio(i))
        self.reset()

    def channel(self, num: int):
        """
        Returns a reference to the requested channel.
        :param num: The number of the channel to return.
        :return: A reference to the requested channel object.  What this actually
        is changes between an LED object (when on a Raspberry Pi) to a fake LED
        object from Simulator.py (when on a PC).
        """
        return self._channel[num]

    def reset(self):
        """
        Turns off all of the channels.
        :return: None
        """
        for item in self._channel.values():
            item.off()
