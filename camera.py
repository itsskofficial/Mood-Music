from cv2 import *

class VideoCamera(object):
    def __init__(self):
        self.video=VideoCapture(0)

    def __del__(self):
        self.video.releast(0)

    def get_frame(self):
        ret,frame=self.video.read()
        ret,jpeg=imencode('.jpg',frame)
        return jpeg.tobytes()

    
        