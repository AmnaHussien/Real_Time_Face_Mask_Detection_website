import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('app/mask_detector_model.h5')

#   should be the same labels used during training
LABELS = ['mask', 'no_mask']
#img_array is processed img data that model can understand
def model_predict(img_array):
    """Run inference using trained model and labels."""
    preds = model.predict(img_array)
    #finds the index of highest probability 
    label_index = int(np.argmax(preds))
    #map index to the lables
    label = LABELS[label_index]
    #retrieve probability of predicted class
    confidence = float(np.max(preds))
    return {'label': label, 'confidence': confidence}