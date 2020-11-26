import json
import time

import graphics

DEBUG = True


class GShape:
    """
    A parent class that represents a shape.  It is named GShape for "Graphical shape"
    since "shape" is such a generic word.
    """
    def __init__(self, win: object, name: str, channel: int, x: int, y: int, color: str):
        """
        A generic shape object.
        :param win: The graphics window.
        :param name: A string name of the thing this shape represents.
        :param channel: What channel on the Christmas lights controller this is associated with.
        :param x: The x coordinate of the top left of box containing the shape.
        :param y: The y coordinate of the top left of box containing the shape.
        :param color: The X11 name of the color as a string of the shape when it is on.
        """
        self._win = win
        self._name = name
        self._channel = channel
        self._x = x
        self._y = y
        self._color = color
        self._graphics_object = None
        self._current_color = ChannelCollection.GRAY

    def draw(self):
        """
        Draws the shape in the graphics window.
        :return: None
        """
        self._graphics_object.setWidth(1)
        self._graphics_object.setOutline('black')
        self._graphics_object.setFill(self._current_color)
        self._graphics_object.draw(self._win)

    def on(self):
        """
        Turns on this shape.  Turning on means changing the color from gray to the
        color this object was initialized to be.
        :return: None
        """
        self._graphics_object.undraw()
        self._current_color = self._color
        self.draw()

    def off(self):
        """
        Turns off this shape.  Turning off means changing the color to gray from the
        color this object was initialized to be.
        :return: None
        """
        self._graphics_object.undraw()
        # We do not turn off channel 0 (background stuff, etc.)
        if self._channel != 0:
            self._current_color = ChannelCollection.GRAY
        self.draw()


class Triangle(GShape):
    """
    A shape that is an equilateral triangle that points up.
    """
    def __init__(self, win: object, name: str, channel: int, x: int, y: int, color: str, height: int, width: int):
        """
        Initializes this Triangle GShape object.
        :param win: The graphics window.
        :param name: A string name of the thing this shape represents.
        :param channel: What channel on the Christmas lights controller this is associated with.
        :param x: The x coordinate of the top left of box containing the shape.
        :param y: The y coordinate of the top left of box containing the shape.
        :param color: The X11 name of the color as a string of the shape when it is on.
        :param height: The height of this Rectangle (from the base to the vertex between the
        equal-length sides at the top.
        :param width: The width of the base of this Triangle.
        """
        super().__init__(win, name, channel, x, y, color)
        self._height = height
        self._width = width
        bottom_left = graphics.Point(self._x, self._y + self._height)
        top_center = graphics.Point(self._x + self._width/2, self._y)
        bottom_right = graphics.Point(self._x + self._width, self._y + self._height)
        self._graphics_object = graphics.Polygon(bottom_left, top_center, bottom_right)
        if DEBUG: print('Triangle created (%s)' % (name))


class Circle(GShape):
    """
    A shape that is a circle.
    """
    def __init__(self, win: object, name: str, channel: int, x: int, y: int, color: str, radius: int):
        """
        Initializes this Circle GShape object.
        :param win: The graphics window.
        :param name: A string name of the thing this shape represents.
        :param channel: What channel on the Christmas lights controller this is associated with.
        :param x: The x coordinate of the top left of box containing the shape.
        :param y: The y coordinate of the top left of box containing the shape.
        :param color: The X11 name of the color as a string of the shape when it is on.
        :param radius: The radius of this Circle.
        """
        super().__init__(win, name, channel, x, y, color)
        self._radius = radius
        center_point = graphics.Point(self._x + self._radius/2, self._y + self._radius/2)
        self._graphics_object = graphics.Circle(center_point, self._radius)
        if DEBUG: print('Circle created (%s)' % (name))


class Rectangle(GShape):
    """
    A shape that is a rectangle.
    """
    def __init__(self, win: object, name: str, channel: int, x: int, y: int, color: str, height: int, width: int):
        """
        Initializes this Rectangle GShape object.
        :param win: The graphics window.
        :param name: A string name of the thing this shape represents.
        :param channel: What channel on the Christmas lights controller this is associated with.
        :param x: The x coordinate of the top left of box containing the shape.
        :param y: The y coordinate of the top left of box containing the shape.
        :param color: The X11 name of the color as a string of the shape when it is on.
        :param height: The height of this Rectangle.
        :param width: The width of this Rectangle.
        """
        super().__init__(win, name, channel, x, y, color)
        self._height = height
        self._width = width
        top_left = graphics.Point(self._x , self._y)
        bottom_right = graphics.Point(self._x + self._width, self._y + self._height)
        self._graphics_object = graphics.Rectangle(top_left, bottom_right)
        if DEBUG: print('Rectangle created (%s)' % (name))


class Line(GShape):
    """
    A shape that is a line segment.
    """
    def __init__(self, win: object, name: str, channel: int, x: int, y: int, color: str, x2: int, y2: int):
        """
        Initializes this Line GShape object.
        :param win: The graphics window.
        :param name: A string name of the thing this shape represents.
        :param channel: What channel on the Christmas lights controller this is associated with.
        :param x: The x coordinate of one end of the line.
        :param y: The y coordinate of one end of the line.
        :param color: The X11 name of the color as a string of the shape when it is on.
        :param x2: The x coordinate of the other end of the line.
        :param y2: The y coordinate of the other end of the line.
        """
        super().__init__(win, name, channel, x, y, color)
        self._x2 = x2
        self._y2 = y2
        point1 = graphics.Point(self._x, self._y)
        point2 = graphics.Point(self._x2, self._y2)
        self._graphics_object = graphics.Line(point1, point2)
        if DEBUG: print('Line created (%s)' % (name))


class ChannelCollection:
    """
    A collection of channel objects.
    """
    # The color of a GShape that is turned off.
    GRAY = "Gray41"

    def __init__(self):
        """
        Initializes the ChannelCollection with 17 channels.  Channel 0 is for anything
        that does not turn off and on.  Channel 0 is always on.  There can be multiple
        GShape objects in each channel.
        """
        self._channels = []
        self._iter_index = 1
        # We will have channels 0 - 16.  0 does not blink.
        for i in range(0, 17):
            self._channels.append([])

    def add(self, shape_object: object):
        """
        Adds a GShape object to the Channel collection into the channel associated with
        the GShape object when the GShape was initialized.
        :param shape_object: The GShape object to add.
        :return: None
        """
        self._channels[shape_object._channel].append(shape_object)

    def on(self, channel_number: int):
        """
        Turns on every GShape object in the requested channel number.
        :param channel_number: The channel number to turn on.
        :return: None
        """
        for a_shape in self._channels[channel_number]:
            a_shape.on()

    def off(self, channel_number: int):
        """
        Turns off every GShape object in the requested channel number.
        :param channel_number: The channel number to turn off.
        :return: None
        """
        for a_shape in self._channels[channel_number]:
            a_shape.off()

    def __iter__(self):
        """
        This makes this object iterable.  This resets the object's iter "pointer"
        every time a new iterator is created.  This probably should never be used in
        a nested for loop where both for loops are iterating over this object.
        :return: A reference to this iterable object.
        """
        self._iter_index = 1
        return self

    def __next__(self):
        """
        Returns the next channel in this iterable ChannelCollection object.
        :return: A reference to the list of GShape objects for the next channel.
        (One channel in the ChannelCollection contains a list of GShape objects that should
        all turn on or off when a channel is turned on or off.)
        """
        list = self._channels[self._iter_index]
        self._iter_index += 1
        return list



class GraphicsJson:
    """
    A class that creates a Graphical visualization based on the data in a JSON file.
    """
    def __init__(self, filename: str, channel_collection: object):
        """
        Reads in a JSON file and creates a graphical visualization from the data.
        :param filename: The filename of the JSON file to read in.
        :param channel_collection: The ChannelCollection object to populate.
        """
        json_file = open(filename, 'r')
        self._json_data = json.load(json_file)
        json_file.close()
        self._width = self._json_data["window_width"]
        self._height = self._json_data["window_height"]
        self._win = graphics.GraphWin("Map", self._width, self._height)
        self._win.setBackground(self._json_data['bg_color'])
        self._channel_collection = channel_collection
        if DEBUG: print(f'Using Map: { self._json_data["name"] }')
        channels = self._json_data['channels']
        for one_channel in channels:
            # Create a GShape based on the dictionary for this one "channel".
            shape = self.shape_factory(one_channel)
            self._channel_collection.add(shape)
            shape.draw()
        self._channel_collection.on(0)

    def __del__(self):
        """
        Destructor for this object that closes the graphics environment.
        :return: None
        """
        self._win.close()

    def close(self):
        """
        Closes the graphics environment.
        :return: None
        """
        self._win.close()

    def shape_factory(self, channel_entry: dict):
        """
        Takes in a dictionary member from the "channels" array in the JSON file and
        creates a GShape object.
        :param channel_entry: A dictionary member from the "channels" array in the JSON file.
        :return: A GShape object based on the input JSON data.
        """
        name = channel_entry['name']
        channel = channel_entry['channel']
        if channel > 16:
            channel = 0
        elif channel < 0:
            channel = 0
        shape = channel_entry['shape']
        x = channel_entry['x']
        y = channel_entry['y']
        color = channel_entry['color']
        if shape.lower() == 'triangle':
            height = channel_entry['height']
            width = channel_entry['width']
            return Triangle(self._win, name, channel, x, y, color, height, width)
        elif shape.lower() == 'circle':
            radius = channel_entry['radius']
            return Circle(self._win, name, channel, x, y, color, radius)
        elif shape.lower() == 'rectangle':
            height = channel_entry['height']
            width = channel_entry['width']
            return Rectangle(self._win, name, channel, x, y, color, height, width)
        elif shape.lower() == 'line':
            x2 = channel_entry['x2']
            y2 = channel_entry['y2']
            return Line(self._win, name, channel, x, y, color, x2, y2)

    def all_on(self):
        """
        Turns on all of the channels in the ChannelCollection.
        :return: None
        """
        for i in range(1, 17):
            self._channel_collection.on(i)

    def all_off(self):
        """
        Turns off all of the channels in the ChannelCollection.
        :return: None
        """
        for i in range(1, 17):
            self._channel_collection.off(i)


if __name__ == '__main__':
    # Tests GraphicsJson without using any of the rest of the ChristmasLights code.
    channel_collection = ChannelCollection()
    graphics_json = GraphicsJson('MapData.json', channel_collection)
    for i in range(1, 17):
        for j in range(1, 17):
            if i == j:
                channel_collection.on(j)
            else:
                channel_collection.off(j)
        time.sleep(.5)
    graphics_json.all_off()
    graphics_json._win.getMouse()
