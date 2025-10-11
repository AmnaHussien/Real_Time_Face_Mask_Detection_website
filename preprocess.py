import os
import numpy as np
import cv2
from sklearn.utils import shuffle
#import tensorflow as tf
# from tf.keras.utils import to_categorical

dataset_dir = "Face Mask Dataset" #path to folder that contain dataset
output_dir = "preprocessed" #where .npa file would be written
target_size = (224,224) #model input size(width, height)
class_map = {"without_mask":0, "with_mask":1}
splits = {"Test","Train", "Validation"} #define subfolders

#create folder to save preprocesssed data
os.makedirs(output_dir, exist_ok=True)

def load_split(split_name):
    """
    Load all the images and labels from dataset split
    """
    x = [] #features -> images
    y = [] #dependent -> labels of images

    #combine split folder with dataset path to get full folder location
    split_dir = os.path.join("Face Mask Dataset", Test)

    #iterate over each folders(without mask, with mask) in th the split
    for class_name, label in class_map.items:
        class_dir = os.path.join(split_dir, class_name)
        #if you dont found the folder continue
        if not os.path.exists(class_dir):
            continue
        #iterate over images in each folder(with mask, without mask)
        for f_name in os.listdir(class_dir):
            #lower to convert filename string to lower case
            if f_name.lower().endswith(".jpg", ".png",".jpeg"):
                f_path = os.path.join(class_dir, f_name)

                img = cv2.imread(f_path) #read the image 
                if img is None:
                    continue
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.resize(target_size) # resize image into target size (224,224)

                x = x.append(img) #append features column with edited data of img
                y = y.append(label) #append dependnt list with img label
    #convert x, y to array
    x = np.array(x)
    y = np.array(y)

    print(f"Loaded {len(x)} images from {split_name} split.")
    return x, y
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

