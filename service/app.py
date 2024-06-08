from flask import Flask
import os

App = Flask(__name__)

@App.route('/')
def sample():
    return "This is the {} application.".format(os.environ["APP"])


if __name__ == '__main__':
    App.run(debug=True, host='0.0.0.0')