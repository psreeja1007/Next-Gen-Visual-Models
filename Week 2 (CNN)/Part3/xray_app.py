import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model('./pneumonia_model.keras')
class_names = ['NORMAL', 'PNEUMONIA']

# Prediction function
def predict_multiple_xrays(files):
    results = {}
    for idx, file in enumerate(files):
        # Load image from file path using PIL
        img = Image.open(file.name).convert("RGB")  # Convert to RGB just in case
        img = img.resize((128, 128))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = model.predict(img_array)
        predicted_class = tf.argmax(predictions, axis=1).numpy().item()
        confidence = float(np.max(predictions))

        results[file.name.split("/")[-1]] = {
            class_names[predicted_class]: confidence
        }

    return results

# Gradio app
demo = gr.Interface(
    fn=predict_multiple_xrays,
    inputs=gr.File(file_types=["image"], file_count="multiple", label="Upload Chest X-rays"),
    outputs=gr.JSON(label="Predictions"),
    title="🩺 Chest X-Ray Pneumonia Classifier (Multiple Images)",
    description="Drag and drop multiple chest X-rays (JPEG/PNG) to predict if they are **Normal** or show **Pneumonia**.",
    theme="default"
)

if __name__ == "__main__":
    demo.launch()
