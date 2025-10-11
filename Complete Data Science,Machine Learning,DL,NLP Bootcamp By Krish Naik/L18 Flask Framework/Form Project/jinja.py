from flask import Flask, render_template, request

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello {name}!'

@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is," + str(score)

@app.route('/success/<int:score>/result')
def result(score):
    res=''
    if score >=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html', results=res)


if __name__ == "__main__":
    app.run(debug=True)
