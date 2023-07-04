# license-plate-detection
License plate detector app using Yolov8 on Streamlit

Roboflow was used to tag the license plate areas for machine learning

## Process:
When an image is uploaded into the Streamlit app, the image will be converted and fed into the model. Matplotlib will be used to trace the surrounding area of the detected license plate.
This area is then cropped and Easyocr is used to print out the license number from the cropped image.

## Result:
![alt text](https://github.com/jonbttt/license-plate-detection/blob/main/test-result.png?raw=true)
