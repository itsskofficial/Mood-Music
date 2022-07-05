from camera import *
from cv2 import *
from time import *
from datetime import *


def generate_camera(camera):
    end_time = datetime.now() + timedelta(seconds=5)
    while datetime.now() < end_time:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type:image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")
    dominant_emotion=recognize_emotions(frame)
    yield(b"--text\r\n" b"Content-Type:text\r\n\r\n" + dominant_emotion + b"\r\n\r\n") 

def recognize_emotions(frame):
    emo_detector=fer.FER(mtcnn=True)
    dominant_emotion,emotion_score=emo_detector.top_emotion(frame)
    return dominant_emotion

def playlist(dominant_emotion):
    if dominant_emotion=="Anger":

        