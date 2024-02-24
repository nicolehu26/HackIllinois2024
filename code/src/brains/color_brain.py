import select
import tty
import termios
import sys
from . import base
from ...red import red
from ...yellow import yellow
import time


class Config(base.Config):
    pass


class Brain(base.Brain):

    """Color and distance based brain object"""

    def __init__(self, config: Config, *arg):
        super().__init__(config, *arg)

    def logic(self):
        stop = False
        if red(self.camera):
            self.vehicle.stop()

            if red(self.camera):
                self.vehicle.stop()
                self.leds[1].on()
                time.sleep(10)
                self.vehicle.drive_forward(1)
            
            if yellow(self.camera):
                self.vehicle.stop()
                stop = True

        if self.distance_sensor[0].distance < 0.25:
                self.vehicle.pivot_left(1)

        if not stop:
            self.vehicle.drive_forward()
