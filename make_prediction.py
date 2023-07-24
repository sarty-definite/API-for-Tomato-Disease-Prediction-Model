import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image
import numpy as np

lbls = ['Bacterial_spot227',
        'Early_blight227',
        'Late_blight227',
        'Leaf_Mold227',
        'Septoria_leaf_spot227',
        'Target_Spot227',
        'Tomato_Yellow_Leaf_Curl_Virus227',
        'Tomato_mosaic_virus227',
        'Two-spotted_spider_mite227',
        'healthy227']

model = tf.keras.models.load_model('90plus.h5', compile=False)

def make_prediction(img):
    img = img.resize((227, 227))
    img = img.convert("RGB")
    img_array = keras_image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    prediction_label = np.argmax(prediction)
    prediction_val = prediction[0][prediction_label]
    #     print(prediction)
    x = []
    for i in range(len(lbls)):
        if prediction[0][i]+0.1 >= max(prediction_val, 0.2): #returns all values above 10% and within 10% of the highest probability
            x.append(lbls[i] + ":" + str(round(prediction[0][i]*100, 2)) + "%")
    return '\n'.join(x)