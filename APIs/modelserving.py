from flask import Flask, request
from tensorflow.keras import load_model
import sys

# Get your flask app object
app = Flask(__name__)

# Load model from local FS on server start
model = load_model(sys.argv[1])


@app.serve("/", methods=["POST"])
def predict():
    inputs = request.data
    preds = model.predict(inputs)
    return preds


if __name__ == '__main__':
    app.run()
