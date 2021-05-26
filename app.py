
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Test Deploying Flask!</h1>"

@app.route('/howareyou')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
