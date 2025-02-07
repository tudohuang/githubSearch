from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

GITHUB_USER_REPOS_URL = "https://api.github.com/users/{}/repos"
GITHUB_REPO_URL = "https://api.github.com/repos/{}/{}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        response = requests.get(GITHUB_USER_REPOS_URL.format(username), headers={"Accept": "application/vnd.github.v3+json"})
        
        if response.status_code == 404:
            return jsonify({"error": "GitHub user not found"}), 404
        if response.status_code != 200:
            return jsonify({"error": "GitHub API error"}), response.status_code

        repos = response.json()
        repo_list = [{
            "name": repo["name"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "stargazers_count": repo["stargazers_count"],
            "forks_count": repo["forks_count"],
            "language": repo["language"]
        } for repo in repos]

        return jsonify(repo_list)

    except requests.RequestException:
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/repo")
def repo_info():
    full_repo_name = request.args.get("repo")  # 格式應該是 "username/repository"
    if not full_repo_name or "/" not in full_repo_name:
        return jsonify({"error": "Valid 'username/repo_name' is required"}), 400

    username, repo_name = full_repo_name.split("/", 1)

    try:
        response = requests.get(GITHUB_REPO_URL.format(username, repo_name), headers={"Accept": "application/vnd.github.v3+json"})
        
        if response.status_code == 404:
            return jsonify({"error": "Repository not found"}), 404
        if response.status_code != 200:
            return jsonify({"error": "GitHub API error"}), response.status_code

        repo = response.json()
        repo_details = {
            "name": repo["name"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "stargazers_count": repo["stargazers_count"],
            "forks_count": repo["forks_count"],
            "language": repo["language"],
            "license": repo["license"]["name"] if repo["license"] else "No License",
            "open_issues": repo["open_issues_count"],
            "watchers": repo["watchers_count"]
        }

        return jsonify(repo_details)

    except requests.RequestException:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
