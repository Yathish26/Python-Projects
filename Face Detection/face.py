import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import os

# Load MobileNet model
model = MobileNet(weights='imagenet')

def identify_objects(image_name):
    # Read the image using OpenCV
    image_cv = cv2.imread(image_name)

    # Check if the image was loaded successfully
    if image_cv is None:
        print(f"Error: Could not read the image '{image_name}'. Please make sure the file exists.")
        return

    # Convert image from BGR (OpenCV format) to RGB (needed for TensorFlow)
    image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

    # Resize the image to the input size MobileNet expects (224x224)
    image_resized = cv2.resize(image_rgb, (224, 224))

    # Convert the image to a numpy array and preprocess it for MobileNet
    img_array = image.img_to_array(image_resized)
    img_array = np.expand_dims(img_array, axis=0)  # MobileNet expects a batch of images
    img_array = preprocess_input(img_array)

    # Make a prediction using the pre-trained MobileNet model
    predictions = model.predict(img_array)

    # Decode the results into a list of tuples (class, description, probability)
    decoded_predictions = decode_predictions(predictions, top=3)[0]  # Get top 3 predictions

    # Display the results
    print(f"Predictions for '{image_name}':")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} with probability {score:.2%}")

if __name__ == "__main__":
    # Get the image file name from the user
    image_name = input("Enter the image file name (e.g., image.jpg): ")
    
    # Check if the file exists in the current directory
    if not os.path.isfile(image_name):
        print(f"Error: The file '{image_name}' does not exist in the current directory.")
    else:
        identify_objects(image_name)
