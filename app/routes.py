from flask import redirect, render_template, request, flash, url_for
from app import app
import json
from app.email_utils import send_contact_email  # Assuming you put the function in email_utils.py

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    with open("projects.json") as f:
        projects = json.load(f)
    return render_template("projects.html", projects=projects)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # Send email
        send_contact_email(name, email, subject, message)

        # Show success message
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")
