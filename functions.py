from calendar import EPOCH
from camera import *
from cv2 import *
from time import *


def generate_camera(camera):
    frame = camera.get_frame()
    yield(b'--frame\r\n' b'Content-Type:image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

