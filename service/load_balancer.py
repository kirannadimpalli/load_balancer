from dotenv import load_dotenv
import random
import requests
from flask import Flask, request
import yaml


load_dotenv()
load_balancer = Flask(__name__)

def load_configuration(path):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

config = load_configuration('contract/loadbalancer.yaml')

@load_balancer.route('/')
def router():
    host_header = request.headers['Host']
    for entry in config['hosts']:
        if host_header == entry['host']:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404
    
@load_balancer.route('/<path>')
def path_router(path):
    for entry in config['paths']:
        if ('/' + path) == entry['path']:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404



