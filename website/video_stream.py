import cv2, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import numpy as np
from tensorflow.keras.models import load_model
from Face_Mask_Detection.detect_mask_video import detect_and_predict_mask

# Load the serialized face detector model
faceNet = cv2.dnn.readNet(
    "C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Face_Mask_Detection/Face-Mask-Detection/face_detector/deploy.prototxt" ,
    "C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Face_Mask_Detection/Face-Mask-Detection/face_detector/res10_300x300_ssd_iter_140000.caffemodel"
)

# Load the face mask detector model
maskNet = load_model("Face_Mask_Detection/mask_detector.model")

# Start webcam
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Detect faces + masks
        (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

        for (box, pred) in zip(locs, preds):
            (startX, startY, endX, endY) = box
            (mask, withoutMask) = pred

            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            label = f"{label}: {max(mask, withoutMask) * 100:.2f}%"

            cv2.putText(frame, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

        # Encode as JPEG and yield for streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')