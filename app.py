from dotenv.main import load_dotenv
import os
import openai
import json

load_dotenv()

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    filename = request.get_data()
    json_object = json.loads(filename.decode())
    data = json_object["message"]

    openai.api_key = os.environ["APIKEY"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        max_tokens=1000,
        messages=[{"role": "user", "content": data}],
    )

    answer = response["choices"][0]["message"]["content"]

    return answer
