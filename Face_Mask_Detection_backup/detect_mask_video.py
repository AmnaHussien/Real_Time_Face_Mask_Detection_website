# Import required libraries
# keras: for loading and preprocessing the mask detection model
# imutils: for easier camera and frame handling
# cv2: OpenCV library for image and video processing
# numpy: for mathematical operations and arrays
# os, time: for file paths and timing
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import cv2
import time
import os

# Function to load the face detector and mask classifier models

def initialize_models():
    # Path to the face detection model files
    face_model_path = r"C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Real_Time_Face_Mask_Detection_website/Face_Mask_Detection_backup/face_detector"

    # Prototxt file defines the model architecture
    # Caffe model file contains the pre-trained weights
    prototxt = os.path.join(face_model_path, "deploy.prototxt")
    weights = os.path.join(face_model_path, "res10_300x300_ssd_iter_140000.caffemodel")
    # Path to the face detection model files

    # Load the face detection model from disk
    face_detector = cv2.dnn.readNet(prototxt, weights)
    base_path = r"C:/Users/User/Desktop/Amna/Python/Flaskintroduction/Real_Time_Face_Mask_Detection_website/"

    mask_model_path=os.path.join(base_path, "Face_Mask_Detection_backup", "mask_detector.model")
    # Load the pre-trained face mask detection model
    mask_model = load_model(mask_model_path)

    # Return both models
    return face_detector, mask_model


# Function to detect faces and predict mask usage

def mask_prediction(image_frame, face_detector, mask_model):
    # Get frame dimensions (height and width)
    (h, w) = image_frame.shape[:2]

    # Create a blob from the frame for the face detector
    # Mean values (104,177,123) are standard for this model
    blob = cv2.dnn.blobFromImage(image_frame, 1.0, (224, 224),
                                 (104.0, 177.0, 123.0))

    # Pass the blob through the network to detect faces
    face_detector.setInput(blob)
    detections = face_detector.forward()
    print(detections.shape)
    # Lists to store cropped face images, bounding boxes, and predictions
    face_imgs = []
    face_boxes = []
    predictions = []

    # Loop over all detected faces
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]  # detection confidence score

        # Only consider detections above a certain confidence threshold
        if confidence > 0.5:
            # Compute the (x, y)-coordinates of the bounding box
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")

            # Ensure the coordinates are within the frame
            (x1, y1) = (max(0, x1), max(0, y1))
            (x2, y2) = (min(w - 1, x2), min(h - 1, y2))

            # Extract the face ROI (Region of Interest)
            face = image_frame[y1:y2, x1:x2]
            if face.size == 0:
                continue  # skip invalid or empty faces

            # Convert from BGR to RGB color format
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

            # Resize to 224x224 pixels (required by the mask model)
            face = cv2.resize(face, (224, 224))

            # Convert to array and preprocess the face
            face = img_to_array(face)
            face = preprocess_input(face)

            # Add the processed face and its bounding box to the lists
            face_imgs.append(face)
            face_boxes.append((x1, y1, x2, y2))

    # Only make predictions if at least one face was found
    if len(face_imgs) > 0:
        face_imgs = np.array(face_imgs, dtype="float32")
        # Predict mask / no-mask for all detected faces
        predictions = mask_model.predict(face_imgs, batch_size=16)

    # Return both bounding boxes and predictions
    return face_boxes, predictions