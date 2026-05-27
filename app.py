from flask import Flask, render_template, request

app = Flask(__name__)

questions = {

    "core_devops": [
        {
            "q": "What best describes DevOps?",
            "options": [
                "A programming language",
                "A culture combining development and operations",
                "A testing framework",
                "A database system"
            ],
            "ans": "A culture combining development and operations"
        },
        {
            "q": "Key difference between Traditional IT and DevOps?",
            "options": [
                "Manual deployments vs Automated CI/CD",
                "Cloud vs On-prem",
                "Frontend vs Backend",
                "None"
            ],
            "ans": "Manual deployments vs Automated CI/CD"
        },
        {
            "q": "First step in CI/CD pipeline?",
            "options": [
                "Deploy",
                "Build",
                "Code push to Git",
                "Monitoring"
            ],
            "ans": "Code push to Git"
        },
        {
            "q": "What is Infrastructure as Code?",
            "options": [
                "Manual server setup",
                "Provisioning infra using code",
                "Monitoring system",
                "Logging tool"
            ],
            "ans": "Provisioning infra using code"
        }
    ],

    "aws": [
        {
            "q": "EC2 is used for?",
            "options": ["Virtual Machines", "Storage", "Networking", "Monitoring"],
            "ans": "Virtual Machines"
        },
        {
            "q": "EKS is?",
            "options": [
                "VM service",
                "Kubernetes managed service",
                "Database",
                "Storage"
            ],
            "ans": "Kubernetes managed service"
        },
        {
            "q": "Auto Scaling uses which service?",
            "options": ["CloudWatch", "IAM", "S3", "Lambda"],
            "ans": "CloudWatch"
        },
        {
            "q": "IAM Role is?",
            "options": [
                "Permanent user",
                "Temporary access for services",
                "Storage service",
                "Network layer"
            ],
            "ans": "Temporary access for services"
        },
        {
            "q": "VPC stands for?",
            "options": [
                "Virtual Private Cloud",
                "Virtual Public Cloud",
                "Variable Private Cloud",
                "None"
            ],
            "ans": "Virtual Private Cloud"
        }
    ],

    "terraform": [
        {
            "q": "Terraform state is used for?",
            "options": [
                "Store infra mapping",
                "Store logs",
                "Deploy code",
                "Monitoring"
            ],
            "ans": "Store infra mapping"
        },
        {
            "q": "Correct Terraform lifecycle?",
            "options": [
                "init → plan → apply",
                "build → deploy",
                "test → run",
                "commit → push"
            ],
            "ans": "init → plan → apply"
        },
        {
            "q": "for_each vs count?",
            "options": [
                "count is index-based, for_each is key-based",
                "Both same",
                "for_each is faster",
                "count is deprecated"
            ],
            "ans": "count is index-based, for_each is key-based"
        }
    ],

    "github_actions": [
        {
            "q": "GitHub Actions is used for?",
            "options": [
                "CI/CD automation",
                "Database",
                "Monitoring",
                "Networking"
            ],
            "ans": "CI/CD automation"
        },
        {
            "q": "Secrets in GitHub Actions are accessed using?",
            "options": [
                "${{ secrets.NAME }}",
                "env.NAME",
                "$NAME",
                "secret.NAME"
            ],
            "ans": "${{ secrets.NAME }}"
        },
        {
            "q": "Self-hosted runner advantage?",
            "options": [
                "More control",
                "Less cost always",
                "No config needed",
                "Slower builds"
            ],
            "ans": "More control"
        }
    ],

    "docker": [
        {
            "q": "Docker image is?",
            "options": [
                "Running container",
                "Blueprint",
                "Server",
                "Cluster"
            ],
            "ans": "Blueprint"
        },
        {
            "q": "Container is?",
            "options": [
                "Running instance",
                "Template",
                "Storage",
                "None"
            ],
            "ans": "Running instance"
        },
        {
            "q": "CMD vs ENTRYPOINT?",
            "options": [
                "CMD default, ENTRYPOINT fixed",
                "Both same",
                "ENTRYPOINT optional",
                "CMD mandatory"
            ],
            "ans": "CMD default, ENTRYPOINT fixed"
        }
    ],

    "ansible": [
        {
            "q": "Ansible is?",
            "options": [
                "Agentless automation tool",
                "Database",
                "Container runtime",
                "Cloud provider"
            ],
            "ans": "Agentless automation tool"
        },
        {
            "q": "Playbooks are?",
            "options": [
                "YAML task files",
                "Logs",
                "Scripts",
                "Containers"
            ],
            "ans": "YAML task files"
        }
    ],

    "helm": [
        {
            "q": "Helm is?",
            "options": [
                "Kubernetes package manager",
                "CI tool",
                "Cloud provider",
                "Monitoring tool"
            ],
            "ans": "Kubernetes package manager"
        },
        {
            "q": "values.yaml is used for?",
            "options": [
                "Override configs",
                "Logs",
                "Secrets",
                "Networking"
            ],
            "ans": "Override configs"
        }
    ],

    "git": [
        {
            "q": "Rebase vs Merge?",
            "options": [
                "Merge keeps history, rebase linear",
                "Same",
                "Rebase slower",
                "Merge deprecated"
            ],
            "ans": "Merge keeps history, rebase linear"
        },
        {
            "q": "Cherry-pick is?",
            "options": [
                "Apply specific commit",
                "Delete commit",
                "Merge branch",
                "Reset repo"
            ],
            "ans": "Apply specific commit"
        }
    ],

    "integration": [
        {
            "q": "Slack integration in CI/CD?",
            "options": [
                "Webhook notifications",
                "Database",
                "Logging",
                "None"
            ],
            "ans": "Webhook notifications"
        },
        {
            "q": "Jira integration is used for?",
            "options": [
                "Track failures/issues",
                "Deploy code",
                "Run containers",
                "Store logs"
            ],
            "ans": "Track failures/issues"
        }
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
