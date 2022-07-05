from camera import *
from cv2 import *

def generate_camera(camera):
    while True:
        frame = camera.get_frame()