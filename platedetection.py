import cv2 # opencv
import ultralytics
import numpy as np
from ultralytics import YOLO
from PIL import Image

def predict(file):
    model = YOLO("model/best1.pt")
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image_bgr = cv2.imdecode(file_bytes, 1)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    results = model.predict(
        source=image_rgb, 
        conf=0.6,
        save=True)
    print(results)
    img_result = results[0].plot()
    
    return img_result

def coordinate(file):
    model = YOLO("model/best1.pt")
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image_bgr = cv2.imdecode(file_bytes, 1)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    results = model.predict(
        source=image_rgb, 
        conf=0.6,
        save=True)
    img_result = results[0].boxes
    box = img_result[0]  # returns one box
    return box.xyxy

def convert(string):
    li = list(string.split(", "))
    return li
