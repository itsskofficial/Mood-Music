import cv2
import fer

class VideoCamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)

    def __del__(self):
        self.video.releast()

    def get_frame(self):
        ret,self.frame=self.video.read()
        ret,self.jpeg=cv2.imencode('.jpg',self.frame)
        return self.jpeg.tobytes()

    def recognize_emotions(self):
        emo_detector=fer.FER(mtcnn=True)
        captured_emotions=emo_detector.detect_emotions(self.jpeg)
        dominant_emotion,emotion_score=emo_detector.top_emotion(self.jpeg)
        return dominant_emotion

    
        