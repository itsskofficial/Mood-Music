from cv2 import *
from flask import *
from matplotlib import *
from functions import *

app= Flask (__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/capture')
def recognize_emotion():
    # initialize the camera
    # If you have multiple camera connected with 
    # current device, assign a value in cam_port 
    # variable according to that
    cam_port = 0
    cam = VideoCapture(cam_port)
    
    # reading the input using the camera
    result, image = cam.read()
    
    # If image will detected without any error, 
    # show result
    if result:
    
        # showing result, it takes frame name and image 
        # output
        imshow("GeeksForGeeks", image)
    
    
        # If keyboard interrupt occurs, destroy image 
        # window
        waitKey(0)
        destroyWindow("GeeksForGeeks")
    
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

if __name__=="__main__":
    app.run(debug=True, port=5000)