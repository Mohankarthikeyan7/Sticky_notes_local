📒 Flask Notes App
A simple, containerized web application to store and manage personal learning notes — built with Flask, Docker, and GitHub for everyday productivity.

🔍 Project Overview
Managing daily notes while learning can get overwhelming — especially when scattered across devices or stored locally. This project was built to solve that.

The Flask Notes App allows users to:

Submit and store notes via a web form or API

Save structured notes in notes.json

Automatically back up daily notes to notes.md (Markdown format)

Run reliably inside a Docker container

Push and store data safely in GitHub

🚀 Features
📋 Web form to quickly write and save notes

🧠 JSON and Markdown-based storage for readability and structure

⚙️ API endpoint (/api/notes) for programmatic access

🐳 Dockerized for easy deployment

💻 Lightweight and easy to self-host

🔐 Avoids reliance on local-only storage

🧰 Tech Stack
Backend: Python, Flask

Storage: JSON & Markdown files

Containerization: Docker

Version Control & Hosting: GitHub

Editor: VS Code

⚙️ Setup Instructions
🔨 Prerequisites
Docker installed

Git installed (for cloning the repo)

🐳 Run with Docker
bash
Copy
Edit
git clone https://github.com/yourusername/flask-notes-app.git
cd flask-notes-app
docker build -t flask-notes .
docker run -p 5000:5000 flask-notes
Then visit: http://localhost:5000

📂 Project Structure
bash
Copy
Edit
flask-notes-app/
├── app.py             # Main Flask app
├── data/
│   ├── notes.json     # JSON note storage
│   └── notes.md       # Markdown backup
├── templates/
│   └── index.html     # Web form interface
├── Dockerfile
└── README.md
🔗 API Endpoint
Add a note:
http
Copy
Edit
POST /api/notes
Content-Type: application/json

{
  "text": "Today I learned about Flask routing."
}
✅ Use Cases
Note-taking while learning DevOps, cloud, or development topics

Managing personal knowledge in a structured way

Practicing Flask, Docker, and API design

Building a portfolio-ready DevOps/Python project

🙌 Contributions
Open to improvements and feature suggestions. Fork it, build it, and feel free to open a PR.