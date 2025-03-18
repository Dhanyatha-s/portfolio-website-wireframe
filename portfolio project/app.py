from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy Data for Projects
projects = [
    {"id": 1, "name": "Comic Blog", "description": "A fun blog with a comic-style UI.", "image": "project1.png"},
    {"id": 2, "name": "Superhero Portfolio", "description": "A portfolio inspired by comic books.", "image": "project2.png"},
    {"id": 3, "name": "Cartoon AI", "description": "AI that generates cartoon-style images.", "image": "project3.png"},
    {"id": 4, "name": "Speech Bubble Chatbot", "description": "A chatbot that speaks in comic speech bubbles.", "image": "project4.png"},
    {"id": 5, "name": "Meme Generator", "description": "A Flask app that generates memes.", "image": "project5.png"},
    {"id": 6, "name": "Interactive Comic", "description": "A web-based interactive comic.", "image": "project6.png"},
    {"id": 7, "name": "Animated Resume", "description": "A comic-style resume.", "image": "project7.png"},
    {"id": 8, "name": "Comic Wiki", "description": "A Wikipedia-like page for comics.", "image": "project8.png"}
]

skills_data = {
    'Frontend': ["HTML", "CSS", "JavaScript", "React"],
    'Backend': ["Python", "Node.js", "Flask", "FastAPI"],
    'Database': ["SQL", "MySQL", "PostgreSQL", "MongoDB"]
}

@app.route('/')
def home():
    return render_template("index.html", projects=projects)

@app.route("/projects")
def projects_page():
    return render_template("project.html", projects=projects)

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        return render_template("project_details.html", project=project)
    return "Project Not Found", 404

@app.route('/skills', methods=['GET', 'POST'])  # Fixed method
def skills():
    return render_template("skills.html", skills=skills_data)

@app.route('/contact', methods=['GET', 'POST'])  # Fixed method
def contact_page():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)  # Fixed incorrect syntax
