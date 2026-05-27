from flask import Flask, render_template, request

app = Flask(__name__)

questions = {
    "devops": [
        {"q": "What is DevOps?", "options": ["Culture", "Tool", "Language"], "ans": "Culture"},
        {"q": "CI/CD stands for?", "options": ["Continuous Integration & Continuous Deployment", "Other"], "ans": "Continuous Integration & Continuous Deployment"}
    ],
    "aws": [
        {"q": "What is EC2?", "options": ["Virtual Server", "Database"], "ans": "Virtual Server"},
        {"q": "S3 is used for?", "options": ["Storage", "Compute"], "ans": "Storage"}
    ],
    "docker": [
        {"q": "Docker is used for?", "options": ["Containerization", "Virtualization"], "ans": "Containerization"}
    ],
    "k8s": [
        {"q": "Pod is?", "options": ["Smallest unit", "Cluster"], "ans": "Smallest unit"}
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        score = 0
        total = 0

        for chapter in questions:
            for i, q in enumerate(questions[chapter]):
                total += 1
                user_ans = request.form.get(f"{chapter}_{i}")
                if user_ans == q["ans"]:
                    score += 1

        return render_template("result.html", score=score, total=total)

    return render_template("index.html", questions=questions)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)