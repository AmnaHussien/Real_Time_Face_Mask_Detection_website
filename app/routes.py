from flask import Flask, render_template, request, Response, Blueprint
from video_stream import generate_frames

#parameters(main== blueprint name, __name__ = import name)
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
#route to stream video
@main.route('/video_feed')
def video_feed():
    #integrate generator from video_stream.py file
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

#recive image from browser  and perform some operation then return 
@main.route('/detect')
def predict():
    return  render_template('detect.html')
@main.route('/results')
def results():
    return render_template('results.html')
@main.route('/about')
def about():
    return render_template('about.html')
