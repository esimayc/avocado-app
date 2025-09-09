# app/main.py
from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
import cv2

app = FastAPI()


model = tf.keras.models.load_model(r"C:\Users\user\Desktop\avocado-app\avocado_model.keras")




@app.get("/")
def read_root():
    return {"message": "Avocado API is working"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]
    prediction = float(max(0, round(prediction, 2)))  # negatif olmasın
    return {"days_left": prediction}
