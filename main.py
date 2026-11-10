from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        fahrenheit = float(request.form["fahrenheit"])
        result = (fahrenheit - 32) * 5 / 9

    return render_template("index.html", result=result)

app.run(debug=True)