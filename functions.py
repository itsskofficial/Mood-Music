from camera import *
from cv2 import *
from time import *
from datetime import *


def generate_camera(camera):
    end_time = datetime.now() + timedelta(seconds=5)
    while datetime.now() < end_time:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type:image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")
