import os
from dotenv import load_dotenv

from flask import Flask


load_dotenv()
App = Flask(__name__)


@App.route('/')
def sample():
    return f'This is the {os.environ["APP"]} application.'

if __name__ == '__main__':
    App.run(debug=True, host='0.0.0.0', port=5001)