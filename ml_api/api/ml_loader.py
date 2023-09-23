import os
from tensorflow import keras
import cv2 as cv
import numpy as np
brain_model=None
brain_labels=['yes','no']

def load():
    global brain_model
    brain_model=keras.models.load_model('.\\models\\brain_tumor_model.keras')

def predict(img_path):
    global brain_labels
    img=cv.imread(img_path)
    img=cv.resize(img,(256,256))
    img=img/255
    y_pre=brain_model.predict(
        np.expand_dims(img,0)
        )
    label=brain_labels[np.argmax(y_pre[0])]
    return label,y_pre[0]

    