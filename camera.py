import cv2
import fer
import pandas
import numpy
import matplotlib

class VideoCamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)

    def __del__(self):
        self.video.releast()

    def get_frame(self):
        ret,frame=self.video.read()
        ret,jpeg=cv2.imencode('.jpg',frame)
        return jpeg.tobytes()

    def recognize_emotions(self):
        

    
        