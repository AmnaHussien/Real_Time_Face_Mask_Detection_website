from flask import Flask, render_template, request, Response, Blueprint
import os
import json
from website.video_stream import generate_frames
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
#route to stream video
@main.route('/video_feed')
def video_feed():
    #integrate generator from video_stream.py file
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=image_frame')

#recive image from browser  and perform some operation then return 
@main.route('/detect')
def detect():
    """Handle real-time detection requests from the browser."""
    return render_template('detect.html')
@main.route('/results')
def results():
    with_mask = len(os.listdir("C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Real_Time_Face_Mask_Detection_website/Face_Mask_Detection_backup/dataset/with_mask"))
    without_mask = len(os.listdir("C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Real_Time_Face_Mask_Detection_website/Face_Mask_Detection_backup/dataset/without_mask"))

    total = with_mask + without_mask

    return render_template(
        "results.html",
        total_images=total,
        with_mask=with_mask,
        without_mask=without_mask
    )
@main.route('/about')
def about():
    return render_template('about.html')
