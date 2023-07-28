# API-for-Tomato-Leaf-Disease-Prediction-Model Using Image Analysis

## About
Every year 14.1% proportion of Crops are destroyed due to plant diseases worldwide.
This impacts $220 Billion worth of Economy.

The idea to Early detect the disease in a Crop using Image Analysis by ML Model.

This API takes Image of a Tomato leaf plant and predicts the probabilty of a disease it may have.

The prediction model is based on CNN.


### How to run?

> Install the dependencies from requirements.txt
> 
> Start the flask server by running main.py
>
> Once the server is started at Port:5000
> 
> Make a POST request at http://127.0.0.1:5000/predict_disease
> 
> From there fetch the json message containing the disease and probability of it happening


### How it works?

> Flask is a python framework which allows us to start a server at a port.
>
> This allows us to work as an API to POST and fetch data.
>
> At that port I've set the route /predict-disease to receive a POST method. 
> 
> Once it receives an image in binary, the make_prediction() function from make_prediction.py module is called.
> 
> A Machine Learning model has been pre-trained where it makes prediction about the disease in tomato leaf
>
> The API then generates a response containing a json data and sends it to the opened server