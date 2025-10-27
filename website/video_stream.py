# from model.mask_model import detect_mask
# Handle real-time video capture with OpenCV

# def generate_frames():
#     frame = detect_mask(frame)

#     return None
def detect_mask(frame):
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    cv2.putText(frame, "Mask Detected", (110, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return frame