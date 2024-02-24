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

        if red(self.camera):
            self.vehicle.stop()
            self.leds[0].on()
            self.leds[1].on()
            time.sleep(0.5)
            self.leds[0].off()
            self.leds[1].off()
            stop = True
            print("stopping...")
            self.running = False

        # if yellow(self.camera):
        #     self.vehicle.stop()
        #     self.leds[0].on()
        #     self.leds[0].off()
        #     time.sleep(0.25)
        #     self.leds[0].on()
        #     self.leds[0].off()
        #     self.vehicle.drive_forward(0.25)
        
        if blue(self.camera):
                self.vehicle.stop()
                print("moving forward")
                self.leds[1].on()
                self.leds[1].off()
                time.sleep(0.1)
                self.leds[1].on()
                self.leds[1].off()
                self.vehicle.drive_forward(0.75)

        if self.distance_sensors[0].distance < 0.25 or self.distance_sensors[1].distance < 0.25:
                print("detected an object")
                # self.vehicle.stop()
                while self.distance_sensors[0].distance == 1 or self.distance_sensors[1] == 1:
                    print("pivoting")
                    self.vehicle.pivot_left(0.75)
                # self.vehicle.pivot_left(0.75)
                # self.vehicle.pivot_left(0.75)
                # self.vehicle.pivot_left(0.75)
                # self.vehicle.pivot_left(0.5)
                # time.sleep(0.1)
                print("done pivoting")
                self.vehicle.drive_forward(0.75)

        if not stop:
            self.vehicle.drive_forward(0.75)