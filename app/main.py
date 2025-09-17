# api/main.py
from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
import cv2

api = FastAPI()

# Multi-output modelini yükle
model = tf.keras.models.load_model(
    r"C:\Users\user\Desktop\avocado-app\avocado_model.keras"
)

@api.get("/")
def read_root():
    return {"message": "Avocado API is working"}

@api.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        img = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (224, 224))
        img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
        img = np.expand_dims(img, axis=0)

        predictions = model.predict(img, verbose=0)

        # Sınıflandırma
        class_probs = predictions[0][0]  # shape (5,)
        class_idx = int(np.argmax(class_probs)) + 1  # 1-5 arasında stage
        confidence = float(np.max(class_probs) * 100)

        # Regresyon
        days_left = float(max(0, predictions[1][0][0]))  # negatif olmasın

        return {
            "predicted_stage": class_idx,
            "confidence": round(confidence, 2),
            "days_to_ripeness": round(days_left, 1)
        }
    except Exception as e:
        return {"error": str(e)}
