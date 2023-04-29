# Importing Libraries
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from keras.models import load_model
from keras.utils import load_img, img_to_array

def clasiffier_CNN_predict(file):
    class_dict = {'Imágen Borrosa': 0, 'Imágen Borrosa y Agrietada': 1, 'Imágen Agrietada': 2}
    classes = []
    for key in class_dict.keys():
        classes.append(key)

    model_h5_path = 'model_inception.h5'
    model_new = load_model(model_h5_path, compile=False)

    #img_ = load_img(file, target_size=(512, 512))
    img_array = img_to_array(file)
    img_processed = np.expand_dims(img_array, axis=0)
    img_processed /= 255.

    prediction = model_new.predict(img_processed)

    index = np.argmax(prediction)

    return str(classes[index])
