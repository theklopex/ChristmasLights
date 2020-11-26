class Pattern:
    """
    Parent class for all of the PatternKit objects.  Holds some shared members.
    Provides a pure-virtual play() method.
    """

    def __init__(self, name: str, lights: object):
        """
        A parent class for all PatternKit objects.
        :param name: The name of this PatternKit as a string.
        :param lights: A reference to the Lights object.  The lights object contains
        all of the channels that can be turned on or off.
        """
        self.name = name
        self.lights = lights

    def play(self):
        """
        A virtual method that all PatternKit objects will implement to blink the lights.
        """
        pass