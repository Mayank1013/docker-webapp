import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/whatisthis')
def hello():
    return 'This is simple python application running on flask on docker image'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
