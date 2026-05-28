from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/heart")
def heart():
    bpm = random.randint(70, 90)

    return jsonify({
        "bpm": bpm
    })

if __name__ == "__main__":
    app.run(debug=True)