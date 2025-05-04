from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# 店情報を読み込む関数
def load_restaurants():
    with open("restaurants.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route("/")
def index():
    restaurants = load_restaurants()
    return render_template("index.html", restaurants=restaurants)

if __name__ == "__main__":
    app.run(debug=True)