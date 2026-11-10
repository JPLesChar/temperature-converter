from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result_text = None

    if request.method == "POST":
        try:
            fahrenheit = float(request.form.get("fahrenheit", ""))
            celsius = (fahrenheit - 32) * 5 / 9
            result_text = f"Celsius: {celsius:.2f}"
        except (TypeError, ValueError):
            result_text = "Please enter a valid number."

    return render_template("index.html", result_text=result_text)


if __name__ == "__main__":
    app.run(debug=True)
