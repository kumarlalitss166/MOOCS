from flask import Flask

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is my first Flask App :) Lets make something cool! We are gonna build very amazing projects now on"

@app.route("/index")
def index():
    return "this is my index page."


if __name__ == "__main__":
    app.run(debug=True)
