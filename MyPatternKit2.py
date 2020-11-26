import time

import Pattern

class PatternKit(Pattern.Pattern):
    """
    A PatternKit class that turns on and off channels in the collection of
    Christmas Lights!
    """
    def __init__(self, lights):
        """
        Initializes this instance of the PatternKit class.
        :param lights: A reference to the Lights object (whether real GPIO objects or whether
        Simulator.py objects, we don't need to know.)
        """
        super().__init__("MyPatternKit2", lights)

    def play(self):
        """
        Plays a pattern of lights turning on and off.  This function must NEVER have a loop
        that loops forever.  It must return occasionally to the PatternDriver.
        :return: None
        """
        for i in range(1, 17):
            self.lights.channel(i).on()
            time.sleep(.3)
            self.lights.channel(i).off()
