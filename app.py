from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
from flask import session

import random

app = Flask(__name__)

app.secret_key = "secret123"

PASSWORD = "0508"

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        password = request.form["password"]

        if password == PASSWORD:

            session["login"] = True

            return redirect("/heart-view")

    return render_template("login.html")


@app.route("/heart-view")
def heart_view():

    if not session.get("login"):

        return redirect("/")

    return render_template("index.html")


@app.route("/heart")
def heart():

    if not session.get("login"):

        return jsonify({
            "error": "login required"
        })

    bpm = random.randint(70, 90)

    return jsonify({
        "bpm": bpm
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
