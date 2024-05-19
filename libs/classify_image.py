import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

model = MobileNetV2(weights='imagenet')

def classify_image(image_path):

    img = cv2.imread(image_path)

    img_resized = cv2.resize(img, (224, 224))
    img_array = np.expand_dims(img_resized, axis=0)
    img_array = preprocess_input(img_array)
    
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    
    top_prediction = decoded_predictions[0]

    for prediction in decoded_predictions:
        print(f'Prediction: {prediction[1]} with confidence {prediction[2]:.2f}')

    print(f'Highest prediction: {top_prediction[1]} with confidence {top_prediction[2]:.2f}')

    result = (top_prediction[1], top_prediction[2])
    
    return top_prediction
