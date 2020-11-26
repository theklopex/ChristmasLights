import time

import Pattern

class PatternKit(Pattern.Pattern):
    """
    A PatternKit class that turns on and off channels in the collection of
    Christmas Lights!
    """
    def __init__(self, lights: object):
        """
        Initializes this instance of the PatternKit class.
        :param lights: A reference to the Lights object (whether real GPIO objects or whether
        Simulator.py objects, we don't need to know.)
        """
        super().__init__("MyPatternKit", lights)

    def play(self):
        """
        Plays a pattern of lights turning on and off.  This function must NEVER have a loop
        that loops forever.  It must return occasionally to the PatternDriver.
        :return: None
        """
        self.lights.channel(1).on()
        self.lights.channel(2).on()
        self.lights.channel(3).off()
        self.lights.channel(4).off()
        self.lights.channel(5).off()
        self.lights.channel(6).off()
        self.lights.channel(7).on()
        self.lights.channel(8).on()
        self.lights.channel(9).on()
        self.lights.channel(10).on()
        self.lights.channel(11).off()
        self.lights.channel(12).off()
        self.lights.channel(13).on()
        self.lights.channel(14).off()
        self.lights.channel(15).on()
        self.lights.channel(16).off()
        time.sleep(.5)
        self.lights.channel(1).off()
        self.lights.channel(2).off()
        self.lights.channel(3).on()
        self.lights.channel(4).on()
        self.lights.channel(5).on()
        self.lights.channel(6).on()
        self.lights.channel(7).off()
        self.lights.channel(8).off()
        self.lights.channel(9).off()
        self.lights.channel(10).off()
        self.lights.channel(11).on()
        self.lights.channel(12).on()
        self.lights.channel(13).off()
        self.lights.channel(14).on()
        self.lights.channel(15).off()
        self.lights.channel(16).on()
        time.sleep(.5)