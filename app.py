from cv2 import *
from flask import *
from matplotlib import *

app= Flask (__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True, port=5000)