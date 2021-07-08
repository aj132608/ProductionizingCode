from flask import Flask, request
from tensorflow.keras.models import load_model
import sys
import json

app = Flask(__name__)
model = load_model(sys.argv[1])


@app.route("/", methods=["POST"])
def predict():
    inputs = json.loads(request.data)["instances"]
    preds = model.predict(inputs).tolist()
    return {
            "predictions": preds
    }


app.run(host="0.0.0.0", port=5000)