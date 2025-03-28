from flask import render_template
from app import app

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/user/<username>")
def user_profile(username):
    return f"This is the profile page for user: {username}"