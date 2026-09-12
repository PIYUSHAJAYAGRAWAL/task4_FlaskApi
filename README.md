# Task4_Flask_CIFAR10

A Flask REST API that serves a trained CNN model for CIFAR-10 image classification. Upload an image and get back the predicted class along with a confidence score.

## Features

- Flask-based REST API
- Pre-trained CNN model (`cnn_cifar10_model.keras`) built with TensorFlow/Keras
- Classifies images into 10 CIFAR-10 categories
- Simple JSON response with predicted class and confidence
- Image preprocessing (resize, normalize) handled automatically via Pillow

## CIFAR-10 Classes

The model predicts one of the following 10 classes:

- airplane
- automobile
- bird
- cat
- deer
- dog
- frog
- horse
- ship
- truck

## Project Structure

```
Task4_Flask_CIFAR10/
│
├── venv/                      # Python virtual environment
├── app.py                     # Flask application
├── cnn_cifar10_model.keras    # Trained CIFAR-10 CNN model
├── frog.png                   # Sample test image
├── requirements.txt           # Python dependencies
└── README.md
```

## Requirements

- Python 3.11
- Flask
- TensorFlow / Keras
- NumPy
- Pillow (PIL)

## Setup Instructions

1. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate.bat   # Windows
   ```

2. **Upgrade pip**

   ```bash
   python -m pip install --upgrade pip
   ```

3. **Install dependencies**

   ```bash
   python -m pip install -r requirements.txt
   ```

   (Alternatively, install individually: `flask`, `tensorflow`, `pillow`)

4. **Run the Flask app**

   ```bash
   python app.py
   ```

   By default, the app runs at:

   ```
   http://127.0.0.1:5000
   ```

## API Endpoints

### `GET /`

Health check endpoint to confirm the API is running.

**Response:**

```json
{
  "message": "CIFAR-10 Deep Learning Prediction API is running",
  "endpoint": "/predict"
}
```

### `POST /predict`

Upload an image file to get a prediction.

**Request:**

- Method: `POST`
- Form field: `image` (file)

**Example (using cURL):**

```bash
curl -X POST -F "image=@frog.png" http://127.0.0.1:5000/predict
```

**Success Response:**

```json
{
  "confidence": 0.3741,
  "predicted_class": "deer"
}
```

**Error Response (no image provided):**

```json
{
  "error": "No image provided. Please upload an image."
}
```

## How It Works

1. The client sends an image via a `POST` request to `/predict`.
2. The image is opened and converted to RGB using Pillow.
3. It is resized to `32x32` (the input size expected by the CIFAR-10 model).
4. Pixel values are normalized (divided by 255.0).
5. A batch dimension is added to match the model's expected input shape.
6. The model predicts class probabilities, and the class with the highest probability is returned along with its confidence score.

## Model Details

- Input shape: `(None, 32, 32, 3)`
- Output shape: `(None, 10)`
- Loaded using: `tensorflow.keras.models.load_model("cnn_cifar10_model.keras")`

## Notes

- GPU acceleration is **not** used on native Windows for TensorFlow >= 2.11. To enable GPU support, use WSL2 or the TensorFlow-DirectML plugin.
- The Flask development server is used here for testing/demo purposes only. For production, use a WSGI server (e.g., Gunicorn or Waitress).
- Debug mode is enabled by default (`app.run(debug=True)`), which auto-reloads the server on code changes.

## Testing

Test the health check:

```bash
curl http://127.0.0.1:5000/
```

Test prediction with the sample image included in the repo:

```bash
curl -X POST -F "image=@frog.png" http://127.0.0.1:5000/predict
```

Test with no image (should return an error):

```bash
curl -X POST http://127.0.0.1:5000/predict
```
## Virtual Environment
Download pre-configured venv here: [Google Drive Link](https://drive.google.com/file/d/1gVHGR4JckCsAzZ25cqOntNvnzZl0pa2C/view?usp=drive_link)
