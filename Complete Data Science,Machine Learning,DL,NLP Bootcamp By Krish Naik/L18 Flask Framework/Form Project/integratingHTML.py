from flask import Flask, render_template

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "" \
    "<html>" \
        "<h1>Hey There! I have learned to integrate HTML in Flask!</h1>" \
        "<a href='http://127.0.0.1:5000/index'>INDEX</a>" \
        "<a href='http://127.0.0.1:5000/about'>ABOUT</a>" \
    "</html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
