from flask import Flask, request, jsonify
from PIL import Image
from make_prediction import make_prediction

app = Flask(__name__)

@app.route("/predict_disease", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)

    return jsonify({'msg': make_prediction(img)})


if __name__ == "__main__":
    app.run(debug=True)

