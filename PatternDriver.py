import importlib
import os
import time

import Lights

FIVE_MINUTES_IN_SECONDS = 300

PATTERN_KIT = 'PatternKit'

class PatternDriver():
    """
    A class that loads numerous "PatternKit"s and runs them until a timeout.
    """
    def __init__(self):
        """
        Sets up the PatternDriver by creating the Lights objects and loading
        the PatternKit files.
        """
        self.lights = Lights.Lights()
        # A list of PatternKit objects that derive from Pattern objects.
        self.pattern_objects = {}
        self.load_pattern_kits()
        if len(self.pattern_objects) == 0:
            raise Exception('No patterns found.  There must be one module in the current directory with "%s" in its name.'%(PATTERN_KIT))

    def load_pattern_kits(self):
        """
        Imports PatternKit files and stores them in a list to be executed.
        :return: None
        """
        all_files = os.listdir('.')
        for item in all_files:
            # Add files that contain the word 'PatternKit' in their name to the list of Patterns.
            if os.path.isfile(item) and (PATTERN_KIT in item):
                # Get the filename without the extension.
                module_name = os.path.splitext(item)[0]
                pattern_kit = importlib.import_module(module_name)
                pattern_object = pattern_kit.PatternKit(self.lights)
                self.pattern_objects[module_name] = pattern_object

    def run(self, timeout_sec : int = FIVE_MINUTES_IN_SECONDS):
        """
        Loops forever, running each of the PatternKits in succession for
        timeout_sec seconds each.
        :param timeout_sec: Number of seconds to run a PatternKit before
        starting another PatternKit
        :return: None (Never returns)
        """
        while True:
            for pattern_object in self.pattern_objects.keys():
                # Loop running this pattern_kit until the requested timeout expires.
                # The pattern_kit will complete, it will not be interrupted at timeout.
                self.lights.reset()
                end_time = time.time() + timeout_sec
                while end_time > time.time():
                    self.pattern_objects[pattern_object].play()