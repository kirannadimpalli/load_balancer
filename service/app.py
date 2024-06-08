from flask import Flask


App = Flask(__name__)


@App.route('/')
def router():
    return 'hello'

if __name__ == '__main__':
    App.run(debug=True)