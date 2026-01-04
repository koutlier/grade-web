from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_grade(korean, english, math, social, science, history):
    total = (
        korean * 4 +
        english * 4 +
        math * 4 +
        social * 3 +
        science * 4 +
        history * 3
    )
    return round(total / 22, 3)  # 소수 셋째 자리까지

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        korean = float(request.form["korean"])
        english = float(request.form["english"])
        math = float(request.form["math"])
        social = float(request.form["social"])
        science = float(request.form["science"])
        history = float(request.form["history"])

        result = calculate_grade(
            korean, english, math, social, science, history
        )

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)