from flask import Flask
from views import views

app = Flask(__name__)

# views file will hold routes
# @app.route("/")
# def home():
#     return "1st Place current status"

# /views not necessary, can also be "/" etc
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=5000)