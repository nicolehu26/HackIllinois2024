from src import camera as camera_module
import time
from red import red
from blue import blue
from yellow import yellow
import cv2



if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 10
    fps = 30

    camera = camera_module.Camera({
        "show_preview": True
    })

    video_writer = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (camera.width, camera.height))

    start_time = time.time()

      # Get width and height from the camera object
    width, height = camera.get_resolution()

    while time.time() - start_time < total_seconds:
        camera.capture()
        # print(camera.image_array)
        red(camera)
        yellow(camera)
        blue(camera)
        frame = camera.capture()  # Capture a frame
        video_writer.write(frame)
        time.sleep(max(0, 1/sample_hz -
                       (time.time() - start_time)))

    video_writer.write(frame)
