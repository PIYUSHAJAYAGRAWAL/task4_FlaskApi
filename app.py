from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the trained CIFAR-10 model
model = load_model("cnn_cifar10_model.keras")

# CIFAR-10 class names
class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CIFAR-10 Deep Learning Prediction API is running",
        "endpoint": "/predict"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check whether an image was provided
        if "image" not in request.files:
            return jsonify({
                "error": "No image provided. Please upload an image."
            }), 400

        file = request.files["image"]

        # Open and convert image to RGB
        image = Image.open(file).convert("RGB")

        # CIFAR-10 images are 32x32
        image = image.resize((32, 32))

        # Convert image to NumPy array
        image_array = np.array(image, dtype=np.float32)

        # Normalize pixel values
        image_array = image_array / 255.0

        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)

        # Make prediction
        predictions = model.predict(image_array, verbose=0)

        # Get predicted class
        predicted_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_index]

        # Get confidence
        confidence = float(predictions[0][predicted_index])

        return jsonify({
            "predicted_class": predicted_class,
            "confidence": round(confidence, 4)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)