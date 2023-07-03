# license-plate-detection
License plate detector app using Yolov8 on Streamlit

Roboflow was used to tag the license plate areas for machine learning

When an image is inputted into the Streamlit app, the image will be fed into the model and matplotlib will be used to trace the surrounding area of the detected license plate
This area is then cropped and Easyocr is used to print out the license number
