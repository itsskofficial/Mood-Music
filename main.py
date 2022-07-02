from cv2 import *

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