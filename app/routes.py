from flask import Flask
from flask import render_template
from flask import Blueprint

#parameters(main== blueprint name, __name__ = import name)
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/video_feed')
def video_feed():
    return None

#recive image from browser  and perform some operation then return 
@main.route('/predict')
def predict():
    return None