from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", active_page="home")

@app.route("/projects")
def projects():
    return render_template("projects.html", active_page="projects")

@app.route("/resume")
def resume():
    return render_template("resume.html", active_page="resume")

@app.route("/sandbox")
def sandbox():
    return render_template("sandbox.html", active_page="sandbox")

if __name__ == "__main__":
    app.run(debug=True)
