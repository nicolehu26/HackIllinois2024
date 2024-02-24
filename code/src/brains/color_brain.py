import select
import tty
import termios
import sys
from . import base
from red import red
from yellow import yellow
from blue import blue
import time


class Config(base.Config):
    pass


class Brain(base.Brain):

    """Color and distance based brain object"""

    def __init__(self, config: Config, *arg):
        super().__init__(config, *arg)

    def logic(self):
        stop = False

        while not stop:
            if red(self.camera):
                self.vehicle.stop()
                self.leds[0].on()
                self.leds[1].on()
                self.leds[0].off()
                self.leds[1].off()
                stop = True
                print("stopping...")
                break
            
            if yellow(self.camera):
                self.vehicle.stop()
                self.leds[0].on()
                self.leds[0].off()
                time.sleep(0.25)
                self.leds[0].on()
                self.leds[0].off()
                self.vehicle.drive_forward(0.5)

            if blue(self.camera):
                self.vehicle.stop()
                self.leds[1].on()
                self.leds[1].off()
                time.sleep(0.5)
                self.leds[1].on()
                self.leds[1].off()
                self.vehicle.drive_forward(0.5)

            if self.distance_sensors[0].distance < 0.25:
                    self.vehicle.stop()
                    self.vehicle.pivot_left(1)

            self.vehicle.drive_forward(0.5)

    print("done")