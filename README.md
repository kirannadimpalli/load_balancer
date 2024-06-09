# Load Balancer

## Overview
This project demonstrates how to build an HTTP load balancer using Flask.

## Setup

### Create and Activate Virtual Environment
To create a virtual environment and activate it:

```sh
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate # On Unix or MacOS
```
### install poetry
install poetry and install all project dependency

```sh
pip install poetry
poetry update
poetry install
```

### Build Docker Image
install docker in your machine and create image

```sh
docker build -t server .
docker-compose up -d
docker-compose down
```
### Running Tests
For executing test cases, run below commands

```sh
python -m pytest test_files
make run_tests
```

