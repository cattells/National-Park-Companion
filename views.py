from flask import Blueprint, render_template, jsonify, request, redirect, url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    # varEx - variables can be passed to template
    return render_template("index.html", varEx="Hot Springs please")

@views.route("/profile/<userName>")
def profile(userName):
    return render_template("index.html", varEx="Who likes BJJ??", name=userName)

@views.route("/json")
def get_json():
    return jsonify({'wash' : 'brandon', 'tex' : 'gord'})

# when sending data to the below end point route
# @views.route("/data")
# def get_data():
#     data = request.json
#     return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))