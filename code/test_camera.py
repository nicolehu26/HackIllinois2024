from src import camera as camera_module
import time
from red import red
from blue import blue
from yellow import yellow

if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 10

    camera = camera_module.Camera({
        "show_preview": False
    })
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        camera.capture()
        # print(camera.image_array)
        red(camera)
        yellow(camera)
        blue(camera)
        time.sleep(max(0, 1/sample_hz -
                       (time.time() - start_time)))
