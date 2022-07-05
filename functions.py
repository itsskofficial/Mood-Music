from camera import *
from cv2 import *

def generate_camera(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n' b'Content-Type:image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
