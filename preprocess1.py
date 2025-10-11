import os
import tensorflow as tf


BATCH_SIZE = 32
IMG_SIZE = (224,224)
#sefine dataset directory by access os
data_dir = os.path.join(os.getcwd(), "Face Mask Dataset")

#Load test dataset
test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
os.path.join(data_dir,"Test"),image_size= IMG_SIZE, batch_size=BATCH_SIZE, color_mode="rgb", shuffle = True)
#load train dataset
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
os.path.join(data_dir, "Train"),image_size= IMG_SIZE, batch_size=BATCH_SIZE, color_mode="rgb", shuffle = True)

#load validation dataset
validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
os.path.join(data_dir, "Validation"),image_size= IMG_SIZE, batch_size=BATCH_SIZE, color_mode="rgb", shuffle = True)

# Normalize pixel values to [0,1]
normalization_layer = tf.keras.layers.Rescaling(1./255)
#normalize batch of images in x , and keep y labels unchanged
train_dataset = train_dataset.map(lambda x, y: (normalization_layer(x), y))
validation_dataset = validation_dataset.map(lambda x, y: (normalization_layer(x), y))
test_dataset = test_dataset.map(lambda x, y: (normalization_layer(x), y))

print("Dataset Loaded and Preprocessed Successfully!")
print(" Train batches:", len(train_dataset))
print(" Validation batches:", len(validation_dataset))
print(" Test batches:", len(test_dataset))
