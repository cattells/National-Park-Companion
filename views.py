from flask import Blueprint, render_template

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    # varEx - variables can be passed to template
    return render_template("index.html", varEx="Hot Springs please")

@views.route("/profile/<userName>")
def profile(userName):
    return render_template("index.html", varEx="Who likes BJJ??", name=userName)