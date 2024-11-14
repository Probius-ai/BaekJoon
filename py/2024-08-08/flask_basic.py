# pip install flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"

# $env:FLASK_APP="2024-08-08/flask_basic"  

# flask run