from cv2 import *
from flask import *
from matplotlib import *

app= Flask (__name__)

@app.route('/')
def hello_world():
    print("Hello World")

if __name__=="__main__":
    app.run(debug=True)