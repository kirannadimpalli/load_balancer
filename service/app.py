from flask import Flask, jsonify, request
import os

App = Flask(__name__)

@App.route('/')
def sample():
    return jsonify(
        message=f'This is the {os.environ["APP"]} application.',
        server=request.base_url,
        custom_header=request.headers.get('MyCustomHeader', None),
        host_header=request.headers.get('Host', request.base_url),
        custom_params=request.args.get('MyCustomParam', None),
        query_strings=request.query_string.decode('utf-8'),
    )

@App.route('/healthcheck')
def healthcheck():
    return 'OK'

@App.route('/v1')
def v1():
    return "This is V1"


@App.route('/v2')
def v2():
    return "This is V2"

if __name__ == '__main__':
    App.run(debug=True, host='0.0.0.0')