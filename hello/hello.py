from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, I'm Flask. And you? What's your name?"
@app.route('/goodbye')
def other():
    return "Goodbye mate!"