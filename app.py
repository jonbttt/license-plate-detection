import cv2
import ultralytics
import torch
import pytesseract
import easyocr
import numpy as np
import streamlit as st
import tensorflow as tf
from platedetection import predict
from platedetection import coordinate
from platedetection import convert
from ultralytics import YOLO
from PIL import Image

reader = easyocr.Reader(['en'])
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
st.title('Plate Detection')
file = st.file_uploader("Choose a picture file", type=["jpg", "png", "jpeg"])

if file:
    try:
        coor = str(coordinate(file))
    except IndexError:
        pass

    col1, col2 = st.columns(2)
    with col1:
        st.image(file, caption='Uploaded image')
    with col2:
        result_image = predict(file)
        st.image(result_image, caption='Annotated image')

    try:
        coor1 = str.replace(coor,"tensor([[","")
        coor2 = str.replace(coor1,"]])","")
        coormain = convert(coor2)

        x1 = int(float(coormain[0]))
        y1 = int(float(coormain[1]))
        x2 = int(float(coormain[2]))
        y2 = int(float(coormain[3]))

        box = (x1,y1,x2,y2)
        img = Image.open(file)
        cropimg = img.crop(box)
        st.subheader("Cropped image:")
        st.image(cropimg, width=600)
        st.subheader("Plate number:")
        file_bytes = np.asarray(bytearray(cropimg), dtype=np.uint8)
        image_bgr = cv2.imdecode(file_bytes, 1)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        #add OCR here
        #ocr = pytesseract.image_to_string(cropimg)
        ocr = reader.readtext(cropimg)
        print(ocr)
    
        #st.caption(pNumber)
        #st.caption(ocr)
    except (NameError, IndexError):
        st.caption("No license plate detected")