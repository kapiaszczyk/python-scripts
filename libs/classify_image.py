import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

model = MobileNetV2(weights='imagenet')


def classify_image(image_path):
    """
    Classify an image using the MobileNetV2 model.

    This function reads an image from the specified path, resizes it to the
    size expected by the MobileNetV2 model (224x224), and preprocesses it
    using the preprocessing function provided by the model. It then uses the
    model to predict the top 3 classes for the image and prints these
    predictions along with their confidence scores. The function returns the
    top prediction as a tuple containing the class name and the confidence score.

    Args:
        image_path (str): The path to the image file.

    Returns:
        tuple: The top prediction as a tuple containing the class name and the confidence score.

    Raises:
        FileNotFoundError: If the image file does not exist.
        Exception: If there is an error reading the image file or making the prediction.
    """
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

    return result
