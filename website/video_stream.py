import cv2, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import numpy as np
from tensorflow.keras.models import load_model
from Face_Mask_Detection.detect_mask_video import mask_prediction, initialize_models


face_detector, mask_model = initialize_models()
# Load the serialized face detector model
# faceNet = cv2.dnn.readNet(
#     "C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Face_Mask_Detection/Face-Mask-Detection/face_detector/deploy.prototxt" ,
#     "C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Face_Mask_Detection/Face-Mask-Detection/face_detector/res10_300x300_ssd_iter_140000.caffemodel"
# )

# Load the face mask detector model
# maskNet = load_model("Face_Mask_Detection/mask_detector.model")
# Start webcam
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, image_frame = camera.read()
        if not success:
            break

        # Detect faces and predict mask usage
        face_boxes, predictions = mask_prediction(image_frame, face_detector, mask_model)

        # Loop through all detected faces and their predictions
        for (box, pred) in zip(face_boxes, predictions):
            (x1, y1, x2, y2) = box
            (mask, without_mask) = pred  # probabilities for each class

            # Determine the label and color to display
            label = "Wearing Mask" if mask > without_mask else "Without Mask"
            color = (0, 255, 0) if label == "Wearing Mask" else (0, 0, 255)

            # Draw label and rectangle around the face
            cv2.putText(image_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(image_frame, (x1, y1), (x2, y2), color, 2)


        # Encode as JPEG and yield for streaming
        ret, buffer = cv2.imencode('.jpg', image_frame)
        image_frame = buffer.tobytes()

        yield (b'--image_frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image_frame + b'\r\n')