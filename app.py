from flask import Flask, render_template, request

app = Flask(__name__)

# 🔹 기존 내신 계산 함수
def calculate_grade(scores):
    total = sum(scores)
    return total / len(scores)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        scores = [
            int(request.form["score1"]),
            int(request.form["score2"]),
            int(request.form["score3"])
        ]
        result = calculate_grade(scores)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)