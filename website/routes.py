from flask import Flask, render_template, request, Response, Blueprint
#generate_frames in video_stream
#ofrom website import generate_frames
#import label var from model file
#ofrom ..preprocessed import model_predict, Labels
import json
from website.video_stream import generate_frames
#parameters(main== blueprint name, __name__ = import name)
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
    #recive image from browser
    # data = request.get_json()
    # image_base64 = data['image']

    # Decode image from base64
    #convert base64 to binary image data
    # image_bytes = base64.b64decode(image_base64.split(',')[1])
    #open it as image and ensure color mode is correct
    # img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    #rezie the image
    # img = img.resize((224, 224))
    #convert it to np array scale pixel values to 0,1 adds batch dim to be ready for prediction
    # img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    # Run prediction
    # result = model_predict(img_array)
    # label = result['label']
    # confidence = result['confidence']

    # return jsonify({
    #     'label': label,
    #     'confidence': confidence,
    #     'status': 'known' if label in LABELS else 'unknown'
    # })
    return render_template('detect.html')
@main.route('/results')
def results():
    return render_template('results.html')
@main.route('/about')
def about():
    return render_template('about.html')
