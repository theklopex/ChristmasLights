import graphics

import GraphicsJson

class WindowSingleton:
    """
    A singleton that is responsible for the graphics.GraphWin window.
    """
    class __WindowSingleton:
        """
        The actual object that the WindowSingleton class maintains one instance of.
        """
        def __init__(self):
            """
            Initializes the Graphics environment to visualize the channels.
            Loads the MapData.json file and sets up the visualization.
            """
            self._channels = GraphicsJson.ChannelCollection()
            self._graphics = GraphicsJson.GraphicsJson('MapData.json', self._channels)

        def close(self):
            """
            Closes the graphics environment.
            :return: None
            """
            self._graphics.close()

        def on(self, num: int):
            """
            Turns on all objects for the requested channel number.
            :param num: The channel number to turn on.
            :return: None
            """
            self._channels.on(num)

        def off(self, num):
            """
            Turns off all objects for the requested channel number.
            :param num: The channel number to turn off.
            :return: None
            """
            self._channels.off(num)

    # A static variable for this class to hold the one instance of the Singleton.
    _instance = None

    def __init__(self):
        """
        The Singleton part of this object.  Creates a __WindowSingleton object if
        one does not already exist.
        """
        if not WindowSingleton._instance:
            WindowSingleton._instance = WindowSingleton.__WindowSingleton()
        # If one is already defined, then we will not resize it.

    def __getattr__(self, name: str):
        """
        Gets the requested attribute from the instance of the __WindowSingleton.
        :param name: Name of the attribute to return.
        :return: The value of the requested attribute.
        """
        return getattr(self._instance, name)

    def close(self):
        """
        Closes the __WindowSingleton object for everyone.
        :return:
        """
        WindowSingleton._instance.close()

    def on(self, num: int):
        """
        Turns on the requested channel.
        :param num: The channel number to turn on.
        :return: None
        """
        WindowSingleton._instance.on(num)

    def off(self, num: int):
        """
        Turns off the requested channel.
        :param num: The channel number to turn off.
        :return: None
        """
        WindowSingleton._instance.off(num)


class LED:
    """
    A bogus LED class.  This class has the same name and interface as the LED class
    from the gpiozero module.  This bogus LED class turns on and off graphical
    visualizations channels (from the MapData.json file) in the GUI.
    """
    def __init__(self, num: int):
        """
        Initializes this instance of the LED class.
        :param num: The channel number that this LED object will control.
        """
        self._num = num
        self._window_singleton = WindowSingleton()

    def on(self):
        """
        Turns on the channel associated with this LED object.
        :return: None
        """
        print('led %d is on'%(self._num))
        self._window_singleton.on(self._num)

    def off(self):
        """
        Turns off the channel associated with this LED object.
        :return: None
        """
        print('led %d is off'%(self._num))
        self._window_singleton.off(self._num)
