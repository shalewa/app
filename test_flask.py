from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('home.html', name=name)

if __name__ == "__main__":
    app.run()
