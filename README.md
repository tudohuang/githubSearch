# GitHub Repository Search 🔍

🚀 **GitHub Repository Search** is a web-based application built with **Flask + JavaScript** that allows users to **search for GitHub repositories by username** or **fetch detailed information about a specific repository** using the **GitHub API**.

## **📌 Features**
- **🔎 Search for all repositories of a GitHub user**
- **📂 Retrieve detailed information about a specific GitHub repository**
- **⭐ Display repository stars, forks, and programming language**
- **📜 Show repository license and open issue count**
- **💡 User-friendly UI with SweetAlert for error messages**
- **🚀 Pagination support for a smooth browsing experience**

---

## **📥 Installation & Setup**
This project requires **Python 3.x** and **Flask**. Follow these steps to install and run the application:

### **1️⃣ Install Python Dependencies**
```bash
pip install flask requests
```

### **2️⃣ Run the Flask Server**
```bash
python app.py
```
The Flask server will start at **http://127.0.0.1:5000/**.

---

## **🔧 API Endpoints**
This application provides the following API endpoints to fetch GitHub repository data:

### **1️⃣ Get GitHub User's Repositories**
📌 **Endpoint**:  
```http
GET /search?username={GitHub_Username}
```
📌 **Example Request**:
```http
GET /search?username=octocat
```
📌 **Example Response** (JSON):
```json
[
    {
        "name": "Hello-World",
        "html_url": "https://github.com/octocat/Hello-World",
        "description": "My first repository on GitHub!",
        "stargazers_count": 42,
        "forks_count": 10,
        "language": "Python"
    }
]
```

---

### **2️⃣ Get Specific GitHub Repository Information**
📌 **Endpoint**:  
```http
GET /repo?repo={username}/{repository}
```
📌 **Example Request**:
```http
GET /repo?repo=octocat/Hello-World
```
📌 **Example Response** (JSON):
```json
{
    "name": "Hello-World",
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "My first repository on GitHub!",
    "stargazers_count": 42,
    "forks_count": 10,
    "language": "Python",
    "license": "MIT License",
    "open_issues": 3,
    "watchers": 15
}
```

---

## **🖥️ Technology Stack**
This application is built using **Flask (Python) + JavaScript (Frontend)**:

- **🌍 Backend (Flask)**
  - Uses `requests` module to fetch data from the **GitHub API**
  - Uses `render_template()` to serve **HTML pages**
  - Provides `/search` and `/repo` API endpoints

- **🎨 Frontend (HTML + JavaScript)**
  - Uses **AJAX** to communicate with the backend API
  - Implements **SweetAlert** for enhanced error handling
  - Uses **FontAwesome** icons for better UI
  - Styled with **CSS** for a clean and modern look

---


🚀 **GitHub Repository Search** – Your go-to tool for finding and analyzing GitHub repositories!


